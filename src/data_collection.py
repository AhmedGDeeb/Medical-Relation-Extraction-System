import requests
from bs4 import BeautifulSoup
import csv
import pandas as pd
import os
import time
import logging
from urllib.parse import urljoin
from typing import List, Dict, Optional

class DataCollector:
    def __init__(self, base_dir: str = "data"):
        self.base_dir = base_dir
        self.setup_directories()
        self.setup_logging()

    def setup_directories(self):
        """Create required directories"""
        os.makedirs(f"{self.base_dir}/raw", exist_ok=True)
        os.makedirs(f"{self.base_dir}/processed", exist_ok=True)
        os.makedirs(f"{self.base_dir}/evaluation", exist_ok=True)

    def setup_logging(self):
        """Setup logging system"""
        logging.basicConfig(
            level=logging.INFO,
            format='%(asctime)s - %(levelname)s - %(message)s',
            handlers=[
                logging.FileHandler(f'{self.base_dir}/data_collection.log'),
                logging.StreamHandler()
            ]
        )
        self.logger = logging.getLogger(__name__)

    def get_existing_links(self, links_file: str) -> set:
        """Get previously collected links"""
        existing_links = set()
        if os.path.exists(links_file):
            try:
                with open(links_file, 'r', encoding='utf-8') as f:
                    for line in f:
                        parts = line.strip().split(', ')
                        if len(parts) >= 5:
                            existing_links.add(parts[-1])
            except Exception as e:
                self.logger.warning(f"Error reading existing links: {e}")
        return existing_links

    def get_existing_corpus_data(self, corpus_file: str) -> set:
        """Get previously collected data"""
        existing_data = set()
        if os.path.exists(corpus_file):
            try:
                df = pd.read_csv(corpus_file)
                existing_data = set(df['link'].dropna().tolist())
            except Exception as e:
                self.logger.warning(f"Error reading existing corpus: {e}")
        return existing_data

    def collect_links_from_altibbi(self, site_type: str, max_pages: int = 1000,
                                 links_file: str = "nlp-links.txt") -> List[str]:
        """
        Collect links from Altibbi website

        Args:
            site_type: Type of site ('news' or 'articles')
            max_pages: Maximum number of pages to crawl
            links_file: File to save links

        Returns:
            List of collected links
        """
        main_url = "https://altibbi.com"

        if site_type == "news":
            page_url = main_url + "/%D8%A7%D8%AE%D8%A8%D8%A7%D8%B1-%D8%B7%D8%A8%D9%8A%D8%A9?page="
        elif site_type == "articles":
            page_url = main_url + "/%D9%85%D9%82%D8%A7%D9%84%D8%A7%D8%AA-%D8%B7%D8%A8%D9%8A%D8%A9?page="
        else:
            raise ValueError("site_type must be 'news' or 'articles'")

        links_file_path = f"{self.base_dir}/raw/{links_file}"
        existing_links = self.get_existing_links(links_file_path)
        all_links = list(existing_links)

        self.logger.info(f"Starting link collection from {site_type}. Existing links: {len(existing_links)}")

        for page in range(1, max_pages + 1):
            try:
                self.logger.info(f"Parsing page: {page}")

                response = requests.get(page_url + str(page), timeout=30)
                if response.status_code != 200:
                    self.logger.info(f"Finished collection. Status code: {response.status_code}")
                    break

                response.encoding = 'utf-8'
                soup = BeautifulSoup(response.text, 'html.parser')
                articles = soup.find_all('article', class_='news-article-item-container')

                if not articles:
                    self.logger.info("No articles found on this page")
                    break

                page_links = []
                for article in articles:
                    title_link = article.find('a')
                    if title_link and title_link.get('href'):
                        relative_url = title_link.get('href')
                        full_url = urljoin(main_url, relative_url)

                        if full_url not in existing_links:
                            page_links.append(full_url)

                # Save new links
                with open(links_file_path, 'a', encoding='utf-8') as f:
                    for i, link in enumerate(page_links):
                        f.write(f"altibbi.com, {site_type}, {page}, {i}, {link}\n")
                        all_links.append(link)

                self.logger.info(f"Page {page}: Collected {len(page_links)} new links")

                # Delay between requests
                time.sleep(1)

            except requests.RequestException as e:
                self.logger.error(f"Network error on page {page}: {e}")
                continue
            except Exception as e:
                self.logger.error(f"Unexpected error on page {page}: {e}")
                continue

        self.logger.info(f"Link collection completed. Total: {len(all_links)} links")
        return all_links

    def download_articles_content(self, links_file: str, corpus_file: str = "corpus.csv") -> pd.DataFrame:
        """
        Download article content from links

        Args:
            links_file: File containing links
            corpus_file: File to save content

        Returns:
            DataFrame containing collected data
        """
        links_file_path = f"{self.base_dir}/raw/{links_file}"
        corpus_file_path = f"{self.base_dir}/raw/{corpus_file}"

        # Get existing data
        existing_data = self.get_existing_corpus_data(corpus_file_path)

        # Read links
        links_to_process = []
        try:
            with open(links_file_path, 'r', encoding='utf-8') as f:
                for line in f:
                    parts = line.strip().split(', ')
                    if len(parts) >= 5:
                        link = parts[-1]
                        if link not in existing_data:
                            links_to_process.append(link)
        except Exception as e:
            self.logger.error(f"Error reading links file: {e}")
            return pd.DataFrame()

        self.logger.info(f"Links to process: {len(links_to_process)}")

        # Open CSV file for writing
        file_exists = os.path.exists(corpus_file_path)
        with open(corpus_file_path, 'a', newline='', encoding='utf-8') as csvfile:
            fieldnames = ['link', 'headline', 'articleBody']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

            if not file_exists:
                writer.writeheader()

            processed_count = 0
            error_count = 0

            for link in links_to_process:
                try:
                    self.logger.info(f"Processing: {link}")

                    response = requests.get(link, timeout=30)
                    if response.status_code != 200:
                        self.logger.warning(f"Error loading page: {response.status_code}")
                        error_count += 1
                        continue

                    response.encoding = 'utf-8'
                    soup = BeautifulSoup(response.text, 'html.parser')

                    # Extract headline
                    heading_element = soup.find(itemprop="headline")
                    heading = heading_element.get_text(strip=True) if heading_element else ""

                    # Extract article content
                    article_body_element = soup.find(itemprop="articleBody")
                    if article_body_element:
                        article_body = article_body_element.get_text(separator=' ', strip=True)
                    else:
                        article_body = ""

                    # Write data
                    writer.writerow({
                        'link': link,
                        'headline': heading,
                        'articleBody': article_body
                    })

                    processed_count += 1
                    self.logger.info(f"Processed {processed_count} articles")

                    # Delay between requests
                    time.sleep(2)

                except requests.RequestException as e:
                    self.logger.error(f"Network error: {link} - {e}")
                    error_count += 1
                    continue
                except Exception as e:
                    self.logger.error(f"Unexpected error: {link} - {e}")
                    error_count += 1
                    continue

        self.logger.info(f"Download completed. Processed: {processed_count}, Errors: {error_count}")

        # Read collected data
        try:
            return pd.read_csv(corpus_file_path)
        except Exception as e:
            self.logger.error(f"Error reading data file: {e}")
            return pd.DataFrame()

    def get_corpus_stats(self, corpus_file: str = "corpus.csv") -> Dict:
        """
        Get statistics about collected data

        Args:
            corpus_file: Data file

        Returns:
            Dictionary with statistics
        """
        corpus_file_path = f"{self.base_dir}/raw/{corpus_file}"

        try:
            df = pd.read_csv(corpus_file_path)

            stats = {
                'total_articles': len(df),
                'articles_with_headline': df['headline'].notna().sum(),
                'articles_with_content': df['articleBody'].notna().sum(),
                'total_words': df['articleBody'].str.split().str.len().sum() if 'articleBody' in df.columns else 0,
                'average_article_length': df['articleBody'].str.len().mean() if 'articleBody' in df.columns else 0
            }

            return stats

        except Exception as e:
            self.logger.error(f"Error calculating statistics: {e}")
            return {}
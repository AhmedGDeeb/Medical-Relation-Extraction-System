import pandas as pd
import re
import string

# Arabic character ranges including Tashkeel (diacritics)
ARABIC_LETTERS = r'[\u0600-\u06FF\u0750-\u077F\u08A0-\u08FF\uFB50-\uFDFF\uFE70-\uFEFF0-9]'
ARABIC_TASHKEEL = r'[\u0610-\u061A\u064B-\u065F\u0670\u06D6-\u06DC\u06DF-\u06E4\u06E7\u06E8\u06EA-\u06ED]'

def remove_non_arabic_letters(text):
    """Remove non-Arabic characters while preserving Arabic text, numbers, and basic punctuation"""
    if pd.isna(text):
        return ""
    return re.sub(r'[^\u0600-\u06FF\u0750-\u077F\u08A0-\u08FF\uFB50-\uFDFF\uFE70-\uFEFF0-9.,\s]', ' ', str(text))

def remove_punctuation(text):
    """Remove punctuation marks from text"""
    if pd.isna(text):
        return ""
    return re.sub(
        r'[!"#$%&\'()*+\-/:;<=>?@[\\\]^_`{|}~ـ؛؟،]',
        ' ',
        str(text)
    )

def unit_white_spaces(text):
    """Normalize whitespace characters"""
    if pd.isna(text):
        return ""
    return re.sub(r'[\n\r\t]+', ' ', str(text))

def remove_duplicated_spaces(text):
    """Remove extra spaces and trim"""
    if pd.isna(text):
        return ""
    return re.sub(r'\s+', ' ', str(text)).strip()

def clean_text_pipeline(text):
    """Apply all cleaning steps in sequence"""
    if pd.isna(text):
        return ""
    
    text = str(text)
    text = remove_non_arabic_letters(text)
    text = remove_punctuation(text)
    text = unit_white_spaces(text)
    text = remove_duplicated_spaces(text)
    
    return text

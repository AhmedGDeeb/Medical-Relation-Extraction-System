DATA_COLLECTION_CONFIG = {
    'base_dir': 'data',
    'request_timeout': 30,
    'delay_between_requests': 2,
    'max_retries': 3,
    'user_agent': 'MedicalDataCollector/1.0'
}

EXTRACTION_CONFIG = {
    'min_confidence': 0.3,
    'max_text_length': 5000,
    'patterns_per_relation': 20,
    'save_intermediate_results': True,
    'chunk_size': 1000
}
VALID_LANGUAGES = [
    'python',
]

def is_valid_language(language: str) -> bool:
    return language in VALID_LANGUAGES

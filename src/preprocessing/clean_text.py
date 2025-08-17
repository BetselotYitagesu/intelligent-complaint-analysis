"""
clean_text.py

This module contains text cleaning functions for complaint narratives.
"""

import re


def lowercase_text(text: str) -> str:
    """Convert text to lowercase."""
    return text.lower()


def remove_special_characters(text: str) -> str:
    """Remove non-alphanumeric characters except spaces."""
    return re.sub(r'[^a-zA-Z0-9\s]', '', text)


def remove_boilerplate(text: str) -> str:
    """Remove common boilerplate phrases from complaint narratives."""
    boilerplate_patterns = [
        r'i am writing to file a complaint', 
        r'this is to complain about', 
        r'please investigate'
    ]
    for pattern in boilerplate_patterns:
        text = re.sub(pattern, '', text, flags=re.IGNORECASE)
    return text


def clean_text_pipeline(text: str) -> str:
    """
    Full cleaning pipeline:
    1. Lowercase
    2. Remove special characters
    3. Remove boilerplate
    """
    text = lowercase_text(text)
    text = remove_special_characters(text)
    text = remove_boilerplate(text)
    return text

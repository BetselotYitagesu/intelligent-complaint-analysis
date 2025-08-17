"""
data_filter.py

Filter CFPB complaints for specific products and remove empty narratives.
"""

from typing import Optional
import pandas as pd
from preprocessing.clean_text import clean_text_pipeline

ALLOWED_PRODUCTS = [
    "Credit card",
    "Personal loan",
    "Buy Now, Pay Later",
    "Savings account",
    "Money transfers"
]


def filter_by_product(
    df: pd.DataFrame,
    products: Optional[list[str]] = None
) -> pd.DataFrame:
    """
    Keep only rows matching the specified products.
    
    Args:
        df: DataFrame containing complaint data.
        products: List of allowed product names. If None, 
        defaults to ALLOWED_PRODUCTS.
        
    Returns:
        Filtered DataFrame.
    """
    if products is None:
        products = ALLOWED_PRODUCTS
    return df[df['Product'].isin(products)].copy()


def drop_empty_narratives(df: pd.DataFrame) -> pd.DataFrame:
    """Remove rows where the consumer complaint narrative is empty."""
    return df[df['Consumer complaint narrative'].notnull()].copy()


def apply_text_cleaning(
    df: pd.DataFrame,
    column: str = 'Consumer complaint narrative'
) -> pd.DataFrame:
    """Apply the text cleaning pipeline to the specified column."""
    df[column] = df[column].apply(clean_text_pipeline)
    return df

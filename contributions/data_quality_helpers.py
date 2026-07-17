"""Shared helpers for validating cleaned Platform Technologies datasets."""

from typing import List, Optional

import pandas as pd


def summarize_dataset(df: pd.DataFrame, name: str) -> dict:
    """Return basic row, column, and null counts for a dataframe."""
    return {
        "name": name,
        "rows": len(df),
        "columns": list(df.columns),
        "null_counts": df.isna().sum().to_dict(),
    }


def drop_duplicate_rows(df: pd.DataFrame, subset: Optional[List[str]] = None) -> pd.DataFrame:
    """Remove duplicate rows, optionally checking only specific columns."""
    return df.drop_duplicates(subset=subset).reset_index(drop=True)


def fill_numeric_nulls(df: pd.DataFrame, columns: List[str], value: float = 0.0) -> pd.DataFrame:
    """Fill missing numeric values in selected columns."""
    cleaned = df.copy()
    for column in columns:
        if column in cleaned.columns:
            cleaned[column] = cleaned[column].fillna(value)
    return cleaned


def quick_health_check(df: pd.DataFrame, name: str) -> None:
    """Print a short quality report for pipeline debugging."""
    summary = summarize_dataset(df, name)
    print(f"[{summary['name']}] rows={summary['rows']}, columns={len(summary['columns'])}")
    for column, null_count in summary["null_counts"].items():
        if null_count > 0:
            print(f"  - {column}: {null_count} null values")

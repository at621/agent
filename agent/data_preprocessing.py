import pandas as pd
import numpy as np

def preprocess_data(df: pd.DataFrame, problem_type: str) -> pd.DataFrame:
    """
    Simple cleaning, e.g. fill numeric NaN with mean, etc.
    """
    df = df.copy()
    for col in df.select_dtypes(include=[np.number]).columns:
        df[col].fillna(df[col].mean(), inplace=True)

    # Additional transformations or one-hot encoding, etc.
    return df
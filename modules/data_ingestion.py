import pandas as pd
from config import DATA_PATH

def ingest_data():
    """
    Load sample CSV (placeholder).
    """
    df = pd.read_csv(DATA_PATH)
    return df
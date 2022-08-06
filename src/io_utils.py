import pandas as pd

def load_dataframe(filename: str, dir_path: str) -> pd.DataFrame:
    """
    Loads a CSV given a filename from Google Cloud Storage as a pandas DataFrame
    
    Args:
        filename (str): Name of CSV file.
        dir_path (str): Directory of the file.
    
    Returns:
        pd.DataFrame: Dataset loaded as a pandas DataFrame.
    """
    
    return pd.read_csv(f"{dir_path}/{filename}", index_col=0)
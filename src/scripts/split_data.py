import os
import pandas as pd
from ogb.lsc import PCQM4Mv2Dataset
from typing import List

import dotenv
dotenv.load_dotenv()

DATA_PATH = os.environ["DATA_PATH"]

def sample_and_save(dataframe: pd.DataFrame, indices: List[int], name: str) -> None:
    """
    Get a list of indices to sample a dataframe.
    Save this sample to `data` dir as a CSV file with a custom name.

    Args:
    df (pd.DataFrame): Dataframe containing the full dataset.
    indices (List[int]): Indices to sample from full dataset.
    name (str): Filename to save as.
    """
    dataframe.loc[
        dataframe["idx"].isin(indices)
    ].to_csv(f"{DATA_PATH}/{name}.csv", index=False)


if __name__ == "__main__":
    # Load PCQM4Mv2 Dataset Object
    pcqm4mv2_dataset = PCQM4Mv2Dataset(root=DATA_PATH, only_smiles=True)
    
    # Load full dataset as pd.DataFrame
    df = pd.read_csv(f"{DATA_PATH}/pcqm4m-v2/raw/data.csv.gz")

    split_dict = pcqm4mv2_dataset.get_idx_split()

    indices = {}
    for split_name in ["train", "valid", "test-dev", "test-challenge"]:
        print(f"Getting indices for '{split_name}' split...", end=None)
        indices[split_name] = split_dict[split_name].tolist()
        print(" Done!")

    for split_name, indices in indices.items():
        print(f"Saving '{split_name}' dataset...", end=None)
        sample_and_save(df, indices, split_name)
        print(" Done!")


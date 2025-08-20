import pandas as pd

class DataHandler:
    @staticmethod
    def load_csv(file_path: str) -> pd.DataFrame:
        return pd.read_csv(file_path, encoding="latin-1")

    @staticmethod
    def save_csv(dataframe: pd.DataFrame, save_path: str):
        dataframe.to_csv(save_path, index=False)

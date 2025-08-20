import pandas as pd

class DataCleaner:
    def __init__(self, dataframe: pd.DataFrame):
        self.df = dataframe

    def fill_missing(self, method: str) -> pd.DataFrame:
        if method not in ["Mean", "Median", "Mode"]:
            raise ValueError("Invalid fill method selected.")

        for column in self.df.columns:
            if self.df[column].isnull().sum() > 0:
                if self.df[column].dtype in ['int64', 'float64']:
                    if method == "Mean":
                        self.df[column].fillna(self.df[column].mean(), inplace=True)
                    elif method == "Median":
                        self.df[column].fillna(self.df[column].median(), inplace=True)
                    elif method == "Mode":
                        self.df[column].fillna(self.df[column].mode()[0], inplace=True)
                else:
                    self.df[column].fillna(self.df[column].mode()[0], inplace=True)
        return self.df

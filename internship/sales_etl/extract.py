
import pandas as pd

def extract_data(path):
    df = pd.read_csv(r"Desktop/files")
    print("Data extraCted successfully")
    return df

if __name__ == "__main__":
    df = extract_data("data/sales_data.csv")
    print(df.head())


import pandas as pd

def transform_data(df):
    # Clean numeric columns to remove any commas
      df["estimate_order_val"] = df["estimate_order_val"].str.replace(",", "").astype(float)
    df["cost"] = df["cost"].astype(float)
    # datE convrsion
    df["date"] = pd.to_datetime(df["date"])

    # n/a removing
      df["device_type"] = df["device_type"].fillna("Unknown")
    # Remove duplicates
    df = df.drop_duplicates()
    # Create profit column
      df["profit"] = df["estimate_order_val"] - df["cost"]
      print("Data transformed")
    return df

if __name__ == "__main__":
    df = pd.read_csv("data/sales_data.csv")
    df_clean = transform_data(df)
    print(df_clean.head())

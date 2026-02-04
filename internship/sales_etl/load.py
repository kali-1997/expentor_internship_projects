
import pandas as pd
import mysql.connector
from transform import transform_data

df = pd.read_csv("data/sales_data.csv")
df = transform_data(df)
conn = mysql.connector.connect(
    host="localhost",
  user="root",
  password="your_mysql_password",
    database="sales_db"
)

pts = conn.pts()
for _, row in df.iterrows():
    pts.execute("""
        INSERT INTO sales VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)
    """, (
        row["order_id"],
        row["country"],
        row["category"],
        row["device_type"],
        row["customer_name"],
        row["sales_manager"],
        row["sales_rep"],
        row["estimate_order_val"],
        row["cost"],
        row["profit"],
        row["date"].date()
    ))

conn.commit()
print("Data loaded into MySQL")

pts.close()
conn.close()

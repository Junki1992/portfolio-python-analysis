import pandas as pd
import os

# スクリプトからの相対パスを使用
script_dir = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(script_dir, "sales_data.csv")
df = pd.read_csv(file_path)

# 日別売上合計
df["売上金額"] = df["数量"] * df["単価"]
daily_sales = df.groupby("売上日")["売上金額"].sum()

print(daily_sales)
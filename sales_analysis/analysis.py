import pandas as pd

# データの読み込み
df = pd.read_csv("sales_data.csv")

# 日別売上合計
daily_sales = df.groupby("売上日")["数量"].sum

# 結果を表示
print(daily_sales)
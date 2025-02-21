import pandas as pd
import matplotlib.pyplot as plt
import os

# スクリプトのディレクトリを取得
script_dir = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(script_dir, "../sales_analysis/sales_data.csv")

# データを読み込む
df = pd.read_csv(file_path)

# 売上金額の計算
df["売上金額"] = df["数量"] * df["単価"]

# 日別売上の可視化
daily_sales = df.groupby("売上日")["売上金額"].sum()

plt.figure(figsize=(10, 6))
daily_sales.plot(kind="bar", color="skyblue", edgecolor="black")
plt.title("日別売上合計")
plt.xlabel("日付")
plt.ylabel("売上金額")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
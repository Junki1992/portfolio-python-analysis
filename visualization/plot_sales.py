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
# 日別売上のグラフを保存
plt.savefig(os.path.join(script_dir, "bar_chart_daily.png"))
plt.show()

# 商品ごとの売上金額を集計
sales_by_product = df.groupby("商品名")["売上金額"].sum()

# 最も売れた商品
best_product = sales_by_product.idxmax()
best_sales = sales_by_product.max()

# 商品別売上の可視化
plt.figure(figsize=(10, 6))
sales_by_product.sort_values().plot(kind="barh", color="lightcoral", edgecolor="black")
plt.axvline(best_sales, color="red", linestyle="dashed", linewidth=2, label=f"Best Seller: {best_product}")
plt.title("商品別売上合計")
plt.xlabel("売上金額")
plt.ylabel("商品名")
plt.legend()
plt.tight_layout()
# 商品別売上のグラフを保存
plt.savefig(os.path.join(script_dir, "bar_chart_products.png"))
plt.show()
import pandas as pd
import matplotlib.pyplot as plt
import os
import sys
# utils.pyをインポート
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from utils import load_data # 共通モジュールをインポート

def plot_daily_sales(df, output_path):
    df["売上日"] = pd.to_datetime(df["売上日"])
    df["売上金額"] = df["数量"] * df["単価"]
    daily_sales = df.groupby("売上日")["売上金額"].sum()

    plt.figure(figsize=(10, 6))
    daily_sales.plot(kind="bar", color="skyblue", edgecolor="black")
    plt.title("日別売上合計")
    plt.xlabel("日付")
    plt.ylabel("売上金額")
    plt.xticks(rotation=45)
    plt.tight_layout()

    plt.savefig(output_path)
    print(f"グラフを保存しました: {output_path}")
    plt.show()

if __name__ == "__main__":
    script_dir = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(script_dir, "../sales_analysis/sales_data.csv")
    output_path = os.path.join(script_dir, "bar_cart.png")

    df = load_data(file_path)
    if df is not None:
        plot_daily_sales(df, output_path)
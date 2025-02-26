import os
import sys

# パスを追加してからインポート
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from utils import load_data  # 共通モジュールをインポート


def generate_report(input_path, output_path):
    df = load_data(input_path)
    if df is None:
        return None

    df.to_excel(output_path, index=False)
    print(f"レポートを作成しました: {output_path}")


if __name__ == "__main__":
    script_dir = os.path.dirname(os.path.abspath(__file__))
    input_csv = os.path.join(script_dir, "../sales_analysis/sales_data.csv")
    output_excel = os.path.join(script_dir, "sales_report.xlsx")

    generate_report(input_csv, output_excel)

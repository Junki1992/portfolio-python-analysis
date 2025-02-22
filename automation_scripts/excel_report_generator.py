import pandas as pd
import os

# スクリプトのパスを取得
script_dir = os.path.dirname(os.path.abspath(__file__))
input_file = os.path.join(script_dir, "../sales_analysis/sales_data.csv")
output_file = os.path.join(script_dir, "sales_report.xlsx")

# CSVファイルを読み込む
df = pd.read_csv(input_file)

# EXCELに書き出す
df.to_excel(output_file, index=False)

print(f"EXCELレポートを作成しました: {output_file}")
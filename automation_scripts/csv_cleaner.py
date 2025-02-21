import pandas as pd
import os

def clean_csv(file_path, output_path=None, drop_columns=None):
    """
    指定されたCSVファイルをクリーンアップし、不要な列を削除します。

    Args:
        file_path (str): 入力CSVファイルのパス
        output_path (str, optional): 出力CSVファイルのパス。デフォルトはNone（上書き保存）。
        drop_columns (list, optional): 削除する列名のリスト。デフォルトはNone（すべての列を保持）
    """
    # CSVファイルを読み込む
    df = pd.read_csv(file_path)

    # 指定した列を削除
    if drop_columns:
        df = df.drop(columns=drop_columns, errors="ignore")

    # 欠損値を含む行を削除
    df = df.dropna()

    # 数値カラムを適切な型に変換
    for col in df.select_dtypes(include=["object"]):
        try:
            df[col] = pd.to_numeric(df[col])
        except ValueError:
            pass # 変換できない列はそのまま

    # クリーン済みデータの保存
    output_path = output_path if output_path else file_path
    df.to_csv(output_path, index=False)
    print(f"CSVをクリーンアップしました: {output_path}")

if __name__ == "__main__":
    script_dir = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(script_dir, "../sales_analysis/sales_data.csv")
    clean_csv(file_path, drop_columns=["不要な列1", "不要な列2"])
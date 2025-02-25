import pandas as pd
import os

def load_data(file_path):
    """CSVファイルを読み込む

    Args:
        file_path (str): CSVファイルのパス

    Returns:
        pd.DataFrame: 読み込んだデータフレーム
    """
    try:
        df = pd.read_csv(file_path, encoding="utf-8-sig")
        return df
    except UnicodeDecodeError:
        print("エンコーディングの問題が発生しました。Shift_JIS で試します...")
        try:
            df = pd.read_csv(file_path, encoding="shift_jis")
            return df
        except Exception as e:
            print(f"エラー: CSV の読み込みに失敗しました。\n{e}")
            return None
    except FileNotFoundError:
        print(f"エラー: {file_path}が見つかりませんでした。")
        return None

def generate_report(df, output_path):
    df["売上日"] = pd.to_datetime(df["売上日"])
    df["売上金額"] = df["数量"] * df["単価"]

    # 集計処理
    sales_by_date = df.groupby("売上日")["売上金額"].sum()
    sales_by_person = df.groupby("売上担当者")["売上金額"].sum()
    best_selling_product = df.groupby("商品名")["売上金額"].sum()

    # Excelに出力
    with pd.ExcelWriter(output_path, engine="openpyxl") as writer:
        sales_by_date.to_excel(writer, sheet_name="日別売上")
        sales_by_person.to_excel(writer, sheet_name="担当者別売上")
        pd.DataFrame({"最も売れた商品": (best_selling_product)}).to_excel(writer, sheet_name="売上トップ商品")

    print(f"レポートを作成しました: {output_path}")

if __name__ == "__main__":
    script_dir = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(script_dir, "../sales_analysis/sales_data.csv")
    output_path = os.path.join(script_dir, "sales_report.xlsx")

    df = load_data(file_path)
    if df is not None:
        generate_report(df, output_path)
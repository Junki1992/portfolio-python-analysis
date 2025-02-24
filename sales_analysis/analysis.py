import pandas as pd
import os

def load_data(file_name="sales_data.csv"):
    """
    売上データを読み込む関数
    """
    script_dir = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(script_dir, file_name)

    try:
        df = pd.read_csv(file_path)
        return df
    except FileNotFoundError:
        print(f"エラー: {file_name}が見つかりません。")
        return None

def calculate_sales(df: pd.DataFrame) -> pd.DataFrame:
    """売上金額を計算し、新しい列を追加"""
    df["売上金額"] = df["数量"] * df["単価"]
    return df

def filter_valid_sales(df: pd.DataFrame) -> pd.DataFrame:
    """売上金額を計算"""
    return df[(df["数量"] > 0) & (df["単価"] > 0)]


def sales_by_date(df):
    """日別売上の合計を計算"""
    return df.groupby("売上日")["売上金額"].sum().sort_index()

def main():
    df = load_data()
    if df is None:
        return

    df = calculate_sales(df)
    daily_sales = sales_by_date(df)

    print("\n 別売上合計:")
    print(daily_sales)

if __name__ == "__main__":
    main()
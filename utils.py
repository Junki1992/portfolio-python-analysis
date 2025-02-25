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

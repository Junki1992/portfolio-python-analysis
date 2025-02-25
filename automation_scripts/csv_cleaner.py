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
    try:
        df = pd.read_csv(file_path)
    except FileNotFoundError:
        print(f"エラー: {file_path}が見つかりません。")
        return
    except pd.errors.EmptyDataError:
        print(f"エラー: {file_path}が空です。")
        return
    except Exception as e:
        print(f"エラー: {file_path}の読み込みに失敗しました。\n{e}")
        return

    # 指定した列を削除
    if drop_columns:
        df = df.drop(columns=drop_columns, errors="ignore")

    # 欠損値の処理(全ての値がNaNの行を削除)
    df = df.dropna(how="all")

    # 数値変換の最適化
    df = df.apply(pd.to_numeric, errors="coerce")

    # 欠損値をゼロに置き換え（必要なら変更）
    df = df.fillna(0)

    # クリーン済みデータの保存
    output_path = output_path if output_path else file_path
    df.to_csv(output_path, index=False)
    print(f"CSVをクリーンアップしました: {output_path}")


if __name__ == "__main__":
    script_dir = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(script_dir, "../sales_analysis/sales_data.csv")
    clean_csv(file_path, drop_columns=["不要な列1", "不要な列2"])

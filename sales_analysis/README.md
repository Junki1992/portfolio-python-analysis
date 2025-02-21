# 📊 Sales Analysis (売上データ分析)

このディレクトリでは、売上データの分析を行うスクリプトと Jupyter Notebook を管理しています。  
売上データを可視化し、傾向を把握することでビジネスの意思決定を支援します。

## 📂 ファイル構成
- **`sales_data.csv`**：売上データのサンプル（CSV形式）
- **`analysis.py`**：Python スクリプトで売上データを分析
- **`report.ipynb`**：Jupyter Notebook 形式の分析レポート

## 🔧 使い方

### 1. データの前処理
まず、`sales_data.csv` を適切な形式で準備してください。

### 2. スクリプトを実行
以下のコマンドで Python スクリプトを実行できます：
```bash
python analysis.py
```

Jupyter Notebook を使う場合は：
```bash
jupyter notebook report.ipynb
```

## 📊 分析内容
- 売上金額の合計、平均、最大・最小値
- 売上担当者ごとの売上
- 売上日ごとの売上推移
- 最も売れた商品の特定
- 売上データの可視化（棒グラフ・ヒストグラム）

## 📦 依存ライブラリ
```bash
pip install pandas matplotlib jupyter
```

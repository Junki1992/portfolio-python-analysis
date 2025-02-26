import os
import sys

# プロジェクトのルートディレクトリをパスに追加
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import pytest
import pandas as pd
from sales_analysis.analysis import calculate_sales


# テストデータ
@pytest.fixture
def sample_data():
    return pd.DataFrame({"数量": [1, 2, 3], "単価": [100, 200, 300]})


# 売上金額のテスト
def test_calculate_sales(sample_data):
    df = calculate_sales(sample_data)
    assert df["売上金額"].tolist() == [100, 400, 900]

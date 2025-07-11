import pytest
import pandas as pd
from definition_800117cc09db4d1186f2d564873250c8 import calculate_risk_capacity_metrics

def test_calculate_risk_capacity_metrics_empty_df():
    df = pd.DataFrame()
    with pytest.raises(Exception):
        calculate_risk_capacity_metrics(df)

def test_calculate_risk_capacity_metrics_typical_case():
    data = {'Capital_Remaining': [100, 90, 80, 70],
            'Net_Earnings_Under_Stress': [10, -10, -10, -10],
            'Liquidity_Position': [50, 40, 30, 20]}
    df = pd.DataFrame(data)
    result = calculate_risk_capacity_metrics(df)
    assert isinstance(result, dict)

def test_calculate_risk_capacity_metrics_no_capital_drawdown():
    data = {'Capital_Remaining': [100, 110, 120, 130],
            'Net_Earnings_Under_Stress': [10, 10, 10, 10],
            'Liquidity_Position': [50, 60, 70, 80]}
    df = pd.DataFrame(data)
    result = calculate_risk_capacity_metrics(df)
    assert isinstance(result, dict)

def test_calculate_risk_capacity_metrics_liquidity_shortfall():
    data = {'Capital_Remaining': [100, 90, 80, 70],
            'Net_Earnings_Under_Stress': [10, -10, -10, -10],
            'Liquidity_Position': [50, 40, 30, -10]}
    df = pd.DataFrame(data)
    result = calculate_risk_capacity_metrics(df)
    assert isinstance(result, dict)

def test_calculate_risk_capacity_metrics_single_row():
    data = {'Capital_Remaining': [100],
            'Net_Earnings_Under_Stress': [10],
            'Liquidity_Position': [50]}
    df = pd.DataFrame(data)
    result = calculate_risk_capacity_metrics(df)
    assert isinstance(result, dict)

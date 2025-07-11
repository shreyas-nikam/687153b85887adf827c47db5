import pytest
import pandas as pd
from definition_6b13febc18d84de4977ac813e61a5311 import simulate_pricing_strategies

@pytest.fixture
def sample_transactions_df():
    data = {'Principal': [100000, 200000, 300000],
            'Interest Rate': [0.05, 0.06, 0.07],
            'Tenor': [1, 2, 3],
            'PD': [0.01, 0.02, 0.03],
            'LGD': [0.2, 0.3, 0.4],
            'Operational Cost Ratio': [0.01, 0.02, 0.03],
            'Cost of Funds': [0.02, 0.03, 0.04]}
    return pd.DataFrame(data)

def test_simulate_pricing_strategies_returns_dataframe(sample_transactions_df):
    result = simulate_pricing_strategies(sample_transactions_df)
    assert isinstance(result, pd.DataFrame)

def test_simulate_pricing_strategies_adds_columns(sample_transactions_df):
    result = simulate_pricing_strategies(sample_transactions_df)
    assert 'Interest Rate_Risk_Insensitive' in result.columns
    assert 'RARORAC_Risk_Insensitive' in result.columns
    assert 'Interest Rate_Risk_Sensitive' in result.columns
    assert 'RARORAC_Risk_Sensitive' in result.columns

def test_simulate_pricing_strategies_risk_insensitive_rate_unchanged(sample_transactions_df):
    result = simulate_pricing_strategies(sample_transactions_df)
    pd.testing.assert_series_equal(result['Interest Rate_Risk_Insensitive'], sample_transactions_df['Interest Rate'], check_names=False)

def test_simulate_pricing_strategies_empty_dataframe():
    empty_df = pd.DataFrame()
    result = simulate_pricing_strategies(empty_df)
    assert isinstance(result, pd.DataFrame)
    assert result.empty

def test_simulate_pricing_strategies_handles_nan(sample_transactions_df):
    sample_transactions_df.loc[0, 'Interest Rate'] = float('nan')
    result = simulate_pricing_strategies(sample_transactions_df)
    assert result['Interest Rate_Risk_Insensitive'].isnull().any()

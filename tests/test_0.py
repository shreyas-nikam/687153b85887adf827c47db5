import pytest
import pandas as pd
from definition_367b1de441f941f98609ef30fe02ab32 import generate_synthetic_transactions

def test_generate_synthetic_transactions_positive_num():
    num_transactions = 5
    df = generate_synthetic_transactions(num_transactions)
    assert isinstance(df, pd.DataFrame)
    assert len(df) == num_transactions
    assert all(col in df.columns for col in ['Principal', 'Interest Rate', 'Tenor', 'PD', 'LGD', 'Operational Cost Ratio', 'Cost of Funds'])

def test_generate_synthetic_transactions_zero_num():
    num_transactions = 0
    df = generate_synthetic_transactions(num_transactions)
    assert isinstance(df, pd.DataFrame)
    assert len(df) == 0
    assert all(col in df.columns for col in ['Principal', 'Interest Rate', 'Tenor', 'PD', 'LGD', 'Operational Cost Ratio', 'Cost of Funds'])

def test_generate_synthetic_transactions_large_num():
    num_transactions = 100
    df = generate_synthetic_transactions(num_transactions)
    assert isinstance(df, pd.DataFrame)
    assert len(df) == num_transactions
    assert all(col in df.columns for col in ['Principal', 'Interest Rate', 'Tenor', 'PD', 'LGD', 'Operational Cost Ratio', 'Cost of Funds'])

def test_generate_synthetic_transactions_negative_num():
    with pytest.raises(ValueError):
        generate_synthetic_transactions(-5)

def test_generate_synthetic_transactions_invalid_input_type():
    with pytest.raises(TypeError):
        generate_synthetic_transactions("abc")

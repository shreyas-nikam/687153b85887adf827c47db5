import pytest
import pandas as pd
from definition_77b7500728dd49398b9011280a561341 import generate_synthetic_data

@pytest.mark.parametrize("num_records, start_date, random_seed", [
    (10, '2023-01-01', 42),
    (0, '2023-01-01', 42),
    (5, '2024-02-29', 123) #Leap year
])
def test_generate_synthetic_data_valid_input(num_records, start_date, random_seed):
    df = generate_synthetic_data(num_records, start_date, random_seed)
    if num_records > 0:
        assert isinstance(df, pd.DataFrame)
        assert len(df) == num_records
        assert 'Date' in df.columns
        assert pd.api.types.is_datetime64_any_dtype(df['Date'])
    else:
        assert isinstance(df, pd.DataFrame)
        assert len(df) == 0


def test_generate_synthetic_data_invalid_num_records():
    with pytest.raises(TypeError):
        generate_synthetic_data('abc', '2023-01-01', 42)

def test_generate_synthetic_data_invalid_start_date():
    with pytest.raises(ValueError): #or TypeError depending on implementation
        generate_synthetic_data(5, 123, 42) #start_date needs to be parseable

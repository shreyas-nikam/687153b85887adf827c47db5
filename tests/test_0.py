import pytest
import pandas as pd
from definition_d93fd0786781474eb79f6eeff3d3b166 import load_and_validate_data

def test_load_and_validate_data_default():
    """Test loading with default filepath (synthetic data)."""
    df = load_and_validate_data()
    assert isinstance(df, pd.DataFrame)
    assert not df.empty

def test_load_and_validate_data_valid_filepath(tmp_path):
    """Test loading with a valid filepath."""
    d = tmp_path / "sub"
    d.mkdir()
    p = d / "test_data.csv"
    test_data = "Date,Base_Revenue,Base_Costs\n2024-01-01,100,50"
    p.write_text(test_data)
    df = load_and_validate_data(filepath=str(p))
    assert isinstance(df, pd.DataFrame)
    assert not df.empty
    assert "Base_Revenue" in df.columns

def test_load_and_validate_data_invalid_filepath():
    """Test handling of invalid filepath."""
    with pytest.raises(FileNotFoundError):
        load_and_validate_data(filepath="nonexistent_file.csv")

def test_load_and_validate_data_missing_columns(tmp_path):
    """Test handling of missing required columns."""
    d = tmp_path / "sub"
    d.mkdir()
    p = d / "test_data.csv"
    test_data = "Date,Revenue\n2024-01-01,100"
    p.write_text(test_data)
    with pytest.raises(KeyError):
        load_and_validate_data(filepath=str(p))

def test_load_and_validate_data_duplicate_dates(tmp_path):
    """Test handling of duplicate dates in the data."""
    d = tmp_path / "sub"
    d.mkdir()
    p = d / "test_data.csv"
    test_data = "Date,Base_Revenue,Base_Costs\n2024-01-01,100,50\n2024-01-01,110,60"
    p.write_text(test_data)
    with pytest.raises(ValueError):
        load_and_validate_data(filepath=str(p))

import pytest
from definition_31b7be878023457694bb980e30a7c66b import calculate_economic_capital

@pytest.mark.parametrize("principal, pd, lgd, ul_factor, expected", [
    (1000000, 0.01, 0.5, 0.05, 50000.0),  # Basic test case
    (500000, 0.02, 0.4, 0.1, 50000.0),  # Different values
    (1000000, 0.01, 0.5, 0, 0.0),  # Zero UL factor
    (0, 0.01, 0.5, 0.05, 0.0),  # Zero principal
    (-100000, 0.01, 0.5, 0.05, -5000.0), # Negative principal
])
def test_calculate_economic_capital(principal, pd, lgd, ul_factor, expected):
    assert calculate_economic_capital(principal, pd, lgd, ul_factor) == expected

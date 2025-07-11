import pytest
from definition_eb6f871ec1a54ca4bafbf7c3e3929bd9 import calculate_net_risk_adjusted_reward

@pytest.mark.parametrize("principal, interest_rate, tenor, funding_cost_rate, op_cost_ratio, expected_loss, expected", [
    (1000000, 0.05, 1, 0.02, 0.01, 10000, 20000.0),
    (500000, 0.10, 2, 0.03, 0.02, 5000, 74000.0),
    (2000000, 0.08, 3, 0.04, 0.03, 20000, 280000.0),
    (100000, 0.03, 0.5, 0.01, 0.005, 500, 950.0),
    (10000000, 0.07, 5, 0.025, 0.015, 50000, 2400000.0),
])
def test_calculate_net_risk_adjusted_reward(principal, interest_rate, tenor, funding_cost_rate, op_cost_ratio, expected_loss, expected):
    assert calculate_net_risk_adjusted_reward(principal, interest_rate, tenor, funding_cost_rate, op_cost_ratio, expected_loss) == expected

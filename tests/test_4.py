import pytest
from definition_58ced88d869c43b2b35182355e363e41 import calculate_rarorac

@pytest.mark.parametrize("net_risk_adjusted_reward, economic_capital, expected", [
    (1000, 10000, 0.1),
    (500, 5000, 0.1),
    (0, 1000, 0.0),
    (1000, 0, float('inf')),
    (-500, 1000, -0.5),
])
def test_calculate_rarorac(net_risk_adjusted_reward, economic_capital, expected):
    if expected == float('inf'):
        with pytest.raises(ZeroDivisionError):
            calculate_rarorac(net_risk_adjusted_reward, economic_capital)
    else:
        assert calculate_rarorac(net_risk_adjusted_reward, economic_capital) == expected

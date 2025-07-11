import pytest
from definition_663459f8a7c849cf828cd534bb696061 import calculate_expected_loss

@pytest.mark.parametrize("principal, pd, lgd, expected", [
    (1000000, 0.01, 0.5, 5000.0),
    (500000, 0.02, 0.25, 2500.0),
    (2000000, 0.005, 0.75, 7500.0),
    (100000, 0, 0.5, 0.0),
    (1000000, 0.01, 0, 0.0)
])
def test_calculate_expected_loss(principal, pd, lgd, expected):
    assert calculate_expected_loss(principal, pd, lgd) == expected
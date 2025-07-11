import pytest
import pandas as pd
from definition_fdc2601569a2453c801fe18ddad7bf56 import simulate_stress_impact

@pytest.fixture
def sample_data():
    data = pd.DataFrame({
        'Base_Revenue': [100, 110, 120],
        'Base_Costs': [50, 55, 60],
        'Base_Market_Losses': [10, 11, 12],
        'Base_Credit_Losses': [5, 6, 7],
    })
    return data

def test_simulate_stress_impact_sensitivity(sample_data):
    parameters = {'parameter_to_shock': 'Base_Revenue', 'shock_magnitude': 10}
    result = simulate_stress_impact(sample_data.copy(), 'Sensitivity', parameters)
    assert 'Adjusted_Revenue' in result.columns

def test_simulate_stress_impact_scenario(sample_data):
    parameters = {'scenario_name': 'TestScenario', 'scenario_severity_factor': 0.5}
    result = simulate_stress_impact(sample_data.copy(), 'Scenario', parameters)
    assert isinstance(result, pd.DataFrame)

def test_simulate_stress_impact_firm_wide(sample_data):
    parameters = {'systemic_crisis_scale': 0.2}
    result = simulate_stress_impact(sample_data.copy(), 'Firm-Wide', parameters)
    assert isinstance(result, pd.DataFrame)

def test_simulate_stress_impact_empty_data():
    data = pd.DataFrame()
    parameters = {'systemic_crisis_scale': 0.2}
    result = simulate_stress_impact(data.copy(), 'Firm-Wide', parameters)
    assert isinstance(result, pd.DataFrame)

def test_simulate_stress_impact_invalid_stress_type(sample_data):
    parameters = {'systemic_crisis_scale': 0.2}
    with pytest.raises(Exception):
        simulate_stress_impact(sample_data.copy(), 'InvalidType', parameters)

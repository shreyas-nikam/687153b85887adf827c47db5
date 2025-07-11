import pytest
from definition_08f3226da6dd4e65a168c967e1bef1d1 import generate_recommendations
import pandas as pd

@pytest.fixture
def sample_data():
    data = {
        'SelfRaisedIssues': [0.2, 0.8, 0.3, 0.9, 0.5],
        'RootCauseFixes': [0.1, 0.7, 0.2, 0.8, 0.4],
        'SuperficialFixes': [0.9, 0.3, 0.8, 0.2, 0.6],
        'EmployeePerceptionFairness': [2, 8, 3, 9, 5],
        'WillingnessToReportIssues': [1, 7, 2, 8, 4]
    }
    return pd.DataFrame(data)

@pytest.mark.parametrize("user_inputs, expected_recommendations", [
    (
        {'SimulatedSelfRaisedIssues': 0.2, 'SuperficialFixes': 0.8, 'EmployeePerceptionFairness': 5, 'WillingnessToReportIssues': 5},
        ["Focus on supervisor training for root cause analysis and reinforce accountability for thorough investigations."]
    ),
    (
        {'SimulatedSelfRaisedIssues': 0.8, 'SuperficialFixes': 0.2, 'EmployeePerceptionFairness': 2, 'WillingnessToReportIssues': 5},
        ["Review the fairness and transparency of the punishment regime and align incentives more holistically."]
    ),
    (
        {'SimulatedSelfRaisedIssues': 0.8, 'SuperficialFixes': 0.2, 'EmployeePerceptionFairness': 5, 'WillingnessToReportIssues': 2},
        ["Enhance leadership consistency in communicating risk values and promote a no-blame culture for self-reported errors (first-time mistakes)."]
    ),
    (
        {'SimulatedSelfRaisedIssues': 0.9, 'SuperficialFixes': 0.1, 'EmployeePerceptionFairness': 9, 'WillingnessToReportIssues': 9},
        ["Maintain current leadership, supervisory, and incentive strategies to sustain a strong risk culture."]
    ),
    (
        {'SimulatedSelfRaisedIssues': 0.5, 'SuperficialFixes': 0.5, 'EmployeePerceptionFairness': 5, 'WillingnessToReportIssues': 5},
        []
    )
])
def test_generate_recommendations(sample_data, user_inputs, expected_recommendations):
    # Mock the behavior of the indicator columns in the simulated data by adding them to the sample_data for testability
    for k, v in user_inputs.items():
        sample_data[k] = v

    recommendations = generate_recommendations(sample_data, user_inputs)
    assert recommendations == expected_recommendations

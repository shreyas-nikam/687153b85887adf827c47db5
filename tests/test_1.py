import pytest
from definition_9146d27e27a74ee88c76a218a54a35b1 import simulate_risk_culture_indicators
import pandas as pd

@pytest.fixture
def sample_dataframe():
    data = {
        'Date': pd.to_datetime(['2024-01-01', '2024-01-02', '2024-01-03']),
        'LeadershipConsistency': [70, 80, 90],
        'SupervisorTrainingAdherence': [60, 70, 80],
        'FairnessOfPunishmentRegime': ['Balanced', 'Strict', 'Lenient'],
        'IncentiveAlignment': ['Risk-aware', 'Balanced', 'Results-focused'],
        'AccountabilityClarity': ['Transparent', 'Clear', 'Vague'],
        'SelfRaisedIssues': [0.6, 0.7, 0.8],
        'RootCauseFixes': [0.7, 0.8, 0.9],
        'SuperficialFixes': [0.3, 0.2, 0.1],
        'EmployeePerceptionFairness': [6, 7, 8],
        'WillingnessToReportIssues': [7, 8, 9]
    }
    return pd.DataFrame(data)

def test_simulate_risk_culture_indicators_increases_self_raised_issues(sample_dataframe):
    df = simulate_risk_culture_indicators(sample_dataframe.copy(), 100, 100, 'Balanced', 'Risk-aware', 'Transparent')
    assert (df['SelfRaisedIssues'] >= sample_dataframe['SelfRaisedIssues']).all()

def test_simulate_risk_culture_indicators_decreases_willingness_to_report_issues(sample_dataframe):
    df = simulate_risk_culture_indicators(sample_dataframe.copy(), 0, 0, 'Strict', 'Results-focused', 'Vague')
    assert (df['WillingnessToReportIssues'] <= sample_dataframe['WillingnessToReportIssues']).all()

def test_simulate_risk_culture_indicators_balanced_punishment_regime(sample_dataframe):
    df = simulate_risk_culture_indicators(sample_dataframe.copy(), 50, 50, 'Balanced', 'Balanced', 'Clear')
    assert df is not None

def test_simulate_risk_culture_indicators_risk_aware_incentive_alignment(sample_dataframe):
    df = simulate_risk_culture_indicators(sample_dataframe.copy(), 50, 50, 'Balanced', 'Risk-aware', 'Clear')
    assert df is not None

def test_simulate_risk_culture_indicators_transparent_accountability(sample_dataframe):
    df = simulate_risk_culture_indicators(sample_dataframe.copy(), 50, 50, 'Balanced', 'Risk-aware', 'Transparent')
    assert df is not None
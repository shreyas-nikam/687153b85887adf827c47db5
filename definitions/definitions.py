import pandas as pd
import numpy as np

def generate_synthetic_data(num_records, start_date, random_seed):
    """Generates a synthetic dataset for risk culture metrics."""

    if not isinstance(num_records, int):
        raise TypeError("num_records must be an integer")

    try:
        start_date = pd.to_datetime(start_date)
    except ValueError:
        raise ValueError("Invalid start_date format.  Must be parseable by pd.to_datetime.")
    except TypeError:
        raise TypeError("start_date must be a string or datetime object")

    np.random.seed(random_seed)

    dates = pd.date_range(start=start_date, periods=num_records, freq='D')

    data = {'Date': dates}

    df = pd.DataFrame(data)

    return df

import pandas as pd

def simulate_risk_culture_indicators(df_base, lc_input, sta_input, pr_input, ia_input, ac_input):
    """Simulates the impact of factors on risk culture indicators."""

    df = df_base.copy()

    # Leadership Consistency
    df['LeadershipConsistency'] = df['LeadershipConsistency'] + (lc_input - 50) * 0.1

    # Supervisor Training Adherence
    df['SupervisorTrainingAdherence'] = df['SupervisorTrainingAdherence'] + (sta_input - 50) * 0.1

    # Punishment Regime
    if pr_input == 'Strict':
        df['WillingnessToReportIssues'] = df['WillingnessToReportIssues'] * 0.8
    elif pr_input == 'Lenient':
        df['WillingnessToReportIssues'] = df['WillingnessToReportIssues'] * 1.2

    # Incentive Alignment
    if ia_input == 'Results-focused':
        df['SelfRaisedIssues'] = df['SelfRaisedIssues'] * 0.8
    elif ia_input == 'Risk-aware':
        df['SelfRaisedIssues'] = df['SelfRaisedIssues'] * 1.2

    # Accountability Clarity
    if ac_input == 'Vague':
        df['RootCauseFixes'] = df['RootCauseFixes'] * 0.8
    elif ac_input == 'Transparent':
        df['RootCauseFixes'] = df['RootCauseFixes'] * 1.2

    df['LeadershipConsistency'] = df['LeadershipConsistency'].clip(0, 100)
    df['SupervisorTrainingAdherence'] = df['SupervisorTrainingAdherence'].clip(0, 100)
    df['SelfRaisedIssues'] = df['SelfRaisedIssues'].clip(0, 1)
    df['RootCauseFixes'] = df['RootCauseFixes'].clip(0, 1)
    df['SuperficialFixes'] = df['SuperficialFixes'].clip(0, 1)
    df['EmployeePerceptionFairness'] = df['EmployeePerceptionFairness'].clip(0, 10)
    df['WillingnessToReportIssues'] = df['WillingnessToReportIssues'].clip(0, 10)
    return df

import pandas as pd

def generate_recommendations(simulated_data, user_inputs):
    """Generates actionable recommendations based on simulated data and user inputs."""

    recommendations = []

    if simulated_data['SimulatedSelfRaisedIssues'].iloc[0] > 0.7 and simulated_data['SuperficialFixes'].iloc[0] < 0.3 and simulated_data['EmployeePerceptionFairness'].iloc[0] < 4:
        recommendations.append("Review the fairness and transparency of the punishment regime and align incentives more holistically.")
    elif simulated_data['SimulatedSelfRaisedIssues'].iloc[0] > 0.7 and simulated_data['SuperficialFixes'].iloc[0] < 0.3 and simulated_data['WillingnessToReportIssues'].iloc[0] < 4:
        recommendations.append("Enhance leadership consistency in communicating risk values and promote a no-blame culture for self-reported errors (first-time mistakes).")
    elif simulated_data['SimulatedSelfRaisedIssues'].iloc[0] < 0.3 and simulated_data['SuperficialFixes'].iloc[0] > 0.7:
        recommendations.append("Focus on supervisor training for root cause analysis and reinforce accountability for thorough investigations.")
    elif simulated_data['SimulatedSelfRaisedIssues'].iloc[0] > 0.8 and simulated_data['SuperficialFixes'].iloc[0] < 0.2 and simulated_data['EmployeePerceptionFairness'].iloc[0] > 8 and simulated_data['WillingnessToReportIssues'].iloc[0] > 8:
        recommendations.append("Maintain current leadership, supervisory, and incentive strategies to sustain a strong risk culture.")

    return recommendations
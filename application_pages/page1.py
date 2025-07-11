
import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px

@st.cache_data
def generate_synthetic_data(num_records, start_date, random_seed):
    """Generates a synthetic dataset for risk culture metrics."""
    if not isinstance(num_records, int):
        raise TypeError("num_records must be an integer")
    try:
        start_date = pd.to_datetime(start_date)
    except ValueError:
        raise ValueError("Invalid start_date format. Must be parseable by pd.to_datetime.")
    except TypeError:
        raise TypeError("start_date must be a string or datetime object")
    np.random.seed(random_seed)
    dates = pd.date_range(start=start_date, periods=num_records, freq='D')
    data = {'Date': dates,
            'LeadershipConsistency': np.random.uniform(50, 70, num_records), # Placeholder for a metric
            'SupervisorTrainingAdherence': np.random.uniform(60, 80, num_records), # Placeholder
            'SelfRaisedIssues': np.random.uniform(0.3, 0.6, num_records), # Proportion
            'RootCauseFixes': np.random.uniform(0.4, 0.7, num_records), # Proportion
            'SuperficialFixes': np.random.uniform(0.2, 0.5, num_records), # Proportion
            'EmployeePerceptionFairness': np.random.uniform(5, 8, num_records), # Scale 1-10
            'WillingnessToReportIssues': np.random.uniform(5, 8, num_records) # Scale 1-10
           }
    df = pd.DataFrame(data)
    return df

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

def generate_recommendations(simulated_data, user_inputs):
    """Generates actionable recommendations based on simulated data and user inputs."""
    recommendations = []
    sim_row = {}
    sim_row['SimulatedSelfRaisedIssues'] = simulated_data['SelfRaisedIssues'].mean()
    sim_row['SuperficialFixes'] = simulated_data['SuperficialFixes'].mean()
    sim_row['EmployeePerceptionFairness'] = simulated_data['EmployeePerceptionFairness'].mean()
    sim_row['WillingnessToReportIssues'] = simulated_data['WillingnessToReportIssues'].mean()

    # Business logic
    if sim_row['SimulatedSelfRaisedIssues'] > 0.7 and sim_row['SuperficialFixes'] < 0.3 and sim_row['EmployeePerceptionFairness'] < 4:
        recommendations.append("Review the fairness and transparency of the punishment regime and align incentives more holistically.")
    elif sim_row['SimulatedSelfRaisedIssues'] > 0.7 and sim_row['SuperficialFixes'] < 0.3 and sim_row['WillingnessToReportIssues'] < 4:
        recommendations.append("Enhance leadership consistency in communicating risk values and promote a no-blame culture for self-reported errors (first-time mistakes).")
    elif sim_row['SimulatedSelfRaisedIssues'] < 0.3 and sim_row['SuperficialFixes'] > 0.7:
        recommendations.append("Focus on supervisor training for root cause analysis and reinforce accountability for thorough investigations.")
    elif sim_row['SimulatedSelfRaisedIssues'] > 0.8 and sim_row['SuperficialFixes'] < 0.2 and sim_row['EmployeePerceptionFairness'] > 8 and sim_row['WillingnessToReportIssues'] > 8:
        recommendations.append("Maintain current leadership, supervisory, and incentive strategies to sustain a strong risk culture.")

    if not recommendations:
        recommendations.append("Keep monitoring key metrics while exploring incremental improvements in communication, reward systems, and accountability frameworks.")
    return recommendations

def run_page1():
    st.header("Simulation and Visualizations")

    # Input widgets
    lc_input = st.sidebar.slider("Leadership Consistency ($LC_{input}$):", 0, 100, 50, help="Represents the degree to which leadership actions and communications are consistent with risk management values. Higher consistency is expected to improve employee perception of fairness and willingness to report issues.")
    sta_input = st.sidebar.slider("Supervisor Training Adherence ($STA_{input}$):", 0, 100, 50, help="Reflects the extent to which supervisors adhere to established training protocols and best practices. Higher adherence is expected to improve root cause fixes and reduce superficial fixes.")
    pr_input = st.sidebar.selectbox("Fairness of Punishment Regime ($PR_{input}$):", ['Strict', 'Balanced', 'Lenient'], index=1, help="Influences employees' willingness to report issues. A 'Strict' regime might discourage reporting, while a 'Lenient' regime could encourage it.")
    ia_input = st.sidebar.selectbox("Incentive Alignment ($IA_{input}$):", ['Results-focused', 'Balanced', 'Risk-aware'], index=1, help="Affects the focus on self-raised issues versus hiding problems. A 'Results-focused' incentive might discourage self-reporting, whereas a 'Risk-aware' incentive could promote it.")
    ac_input = st.sidebar.selectbox("Accountability Clarity ($AC_{input}$):", ['Vague', 'Clear', 'Transparent'], index=1, help="Impacts the effectiveness of root cause fixes. 'Vague' accountability may lead to superficial fixes, while 'Transparent' accountability fosters thorough investigations.")

    # Data Generation
    num_records = 100
    start_date = '2023-01-01'
    random_seed = 42
    base_data = generate_synthetic_data(num_records, start_date, random_seed)

    st.latex(r'NewValue = OldValue + (Input - 50) \cdot 0.1')

    # Simulation
    simulated_data = simulate_risk_culture_indicators(base_data, lc_input, sta_input, pr_input, ia_input, ac_input)

    # Visualizations
    st.subheader("Trend Plot: Quantum of Self-Raised Issues")
    fig_trend = px.line(simulated_data, x='Date', y='SelfRaisedIssues', title="Trend of Self-Raised Issues")
    st.plotly_chart(fig_trend, use_container_width=True)

    st.subheader("Aggregated Comparison: Root Cause Fixes vs. Superficial Fixes")
    avg_root_cause_fixes = simulated_data['RootCauseFixes'].mean()
    avg_superficial_fixes = simulated_data['SuperficialFixes'].mean()
    comparison_data = pd.DataFrame({'Fix Type': ['Root Cause Fixes', 'Superficial Fixes'], 'Average': [avg_root_cause_fixes, avg_superficial_fixes]})
    fig_comparison = px.bar(comparison_data, x='Fix Type', y='Average', title="Comparison of Fix Types")
    st.plotly_chart(fig_comparison, use_container_width=True)

    st.subheader("Relationship Plot: Employee Perception of Fairness vs. Willingness to Report Issues")
    fig_relationship = px.scatter(simulated_data, x='EmployeePerceptionFairness', y='WillingnessToReportIssues', title="Relationship between Fairness and Reporting Willingness")
    st.plotly_chart(fig_relationship, use_container_width=True)

    # Recommendations
    st.subheader("Actionable Recommendations")
    user_inputs = {'lc_input': lc_input, 'sta_input': sta_input, 'pr_input': pr_input, 'ia_input': ia_input, 'ac_input': ac_input}
    recommendations = generate_recommendations(simulated_data, user_inputs)
    for recommendation in recommendations:
        st.markdown(f"- {recommendation}")


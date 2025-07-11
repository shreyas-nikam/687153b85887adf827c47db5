
import streamlit as st
import pandas as pd

@st.cache_data
def generate_synthetic_data(num_records, start_date, random_seed):
    """Generates a synthetic dataset for risk culture metrics."""
    import numpy as np
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

def run_page2():
    st.header("Raw Data Overview")

    # Input widgets (using defaults)
    lc_input = st.sidebar.slider("Leadership Consistency ($LC_{input}$):", 0, 100, 50, help="Represents the degree to which leadership actions and communications are consistent with risk management values.")
    sta_input = st.sidebar.slider("Supervisor Training Adherence ($STA_{input}$):", 0, 100, 50, help="Reflects the extent to which supervisors adhere to established training protocols and best practices.")
    pr_input = st.sidebar.selectbox("Fairness of Punishment Regime ($PR_{input}$):", ['Strict', 'Balanced', 'Lenient'], index=1, help="Influences employees' willingness to report issues.")
    ia_input = st.sidebar.selectbox("Incentive Alignment ($IA_{input}$):", ['Results-focused', 'Balanced', 'Risk-aware'], index=1, help="Affects the focus on self-raised issues versus hiding problems.")
    ac_input = st.sidebar.selectbox("Accountability Clarity ($AC_{input}$):", ['Vague', 'Clear', 'Transparent'], index=1, help="Impacts the effectiveness of root cause fixes.")

    # Data Generation
    num_records = 100
    start_date = '2023-01-01'
    random_seed = 42
    base_data = generate_synthetic_data(num_records, start_date, random_seed)

    # Simulation
    simulated_data = simulate_risk_culture_indicators(base_data, lc_input, sta_input, pr_input, ia_input, ac_input)

    # Display Initial Data
    st.subheader("Initial Data (First 5 Rows)")
    st.dataframe(base_data.head())
    st.subheader("Initial Data (Summary Statistics)")
    st.dataframe(base_data.describe())

    # Display Simulated Data
    st.subheader("Simulated Data (First 5 Rows)")
    st.dataframe(simulated_data.head())
    st.subheader("Simulated Data (Summary Statistics)")
    st.dataframe(simulated_data.describe())

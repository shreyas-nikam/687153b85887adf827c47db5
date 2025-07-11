import streamlit as st
import pandas as pd

def simulate_stress_impact(data, stress_type, parameters):
    """
    Applies stress test methodology to data.
    Args:
        data (pd.DataFrame): The base financial data.
        stress_type (str): Type of stress test ('Sensitivity', 'Scenario', 'Firm-Wide').
        parameters (dict): Dictionary of parameters specific to the stress type.
    Returns:
        pd.DataFrame: DataFrame with stressed financial data.
    """
    stressed_data = data.copy()
    if stress_type == 'Sensitivity':
        parameter_to_shock = parameters.get('parameter_to_shock')
        shock_magnitude = parameters.get('shock_magnitude')
        if parameter_to_shock not in stressed_data.columns:
            raise KeyError(f"Parameter '{{parameter_to_shock}}' not found in data for Sensitivity stress test.")
        stressed_data[f'Adjusted_{{parameter_to_shock.replace("Base_", "")}}'] = (
            stressed_data[parameter_to_shock] * (1 - shock_magnitude/100)
        )
    elif stress_type == 'Scenario':
        scenario_severity_factor = parameters.get('scenario_severity_factor')
        for col in stressed_data.columns:
            if 'Base' in col:
                stressed_data[col.replace('Base', 'Adjusted')] = stressed_data[col] * (1 - scenario_severity_factor)
    elif stress_type == 'Firm-Wide':
        systemic_crisis_scale = parameters.get('systemic_crisis_scale')
        for col in stressed_data.columns:
            if 'Base' in col:
                stressed_data[col.replace('Base', 'Adjusted')] = stressed_data[col] * (1 - systemic_crisis_scale)
    else:
        raise Exception("Invalid stress type.")
    return stressed_data

def run_page2():
    st.markdown(r"""
    ### 2. Interactive Stress Test Simulation

    This page lets you select a stress testing methodology and define its parameters to examine its simulated effect on your financial data.  
    You will see the underlying formulas for each methodology and how your input parameters change the results in real time.

    - **Sensitivity**: Shocks a single parameter.
    - **Scenario**: Applies a stress factor to all relevant parameters.
    - **Firm-Wide**: Simulates an extensive crisis across all financial data.

    The formulas used:
    - Sensitivity: $\text{Adjusted Parameter} = \text{Base Parameter} \times \left(1 - \frac{\text{Shock Magnitude}}{100}\right)$
    - Scenario: $\text{Adjusted Base Component} = \text{Base Component} \times (1 - \text{Scenario Severity Factor})$
    - Firm-Wide: $\text{Adjusted Base Component} = \text{Base Component} \times (1 - \text{Systemic Crisis Scale})$
    """)
    if 'base_data' not in st.session_state:
        st.error("No base data loaded. Please visit Page 1 and load your data.")
        st.stop()
    data = st.session_state['base_data']
    st.sidebar.markdown("#### Stress Test Settings")
    stress_type = st.sidebar.selectbox(
        "Choose the stress test methodology to apply. Each type affects parameters differently.",
        options=["Sensitivity", "Scenario", "Firm-Wide"]
    )

    parameters = {}
    if stress_type == "Sensitivity":
        st.sidebar.markdown(
            "*Sensitivity testing focuses on a single parameter. Select which parameter to shock.*"
        )
        parameter_to_shock = st.sidebar.selectbox(
            "Select the specific financial parameter to shock.",
            options=[col for col in data.columns if col.startswith("Base_")],
            help="Sensitivity testing focuses on a single variable."
        )
        shock_magnitude = st.sidebar.slider(
            "Define the percentage reduction to apply to the selected parameter ($0-100\%$).",
            0, 100, 10,
            help="For example, 10 for 10% reduction."
        )
        parameters['parameter_to_shock'] = parameter_to_shock
        parameters['shock_magnitude'] = shock_magnitude
    elif stress_type == "Scenario":
        st.sidebar.markdown(
            "*Scenario testing applies a broad factor across all base parameters.*"
        )
        scenario_severity_factor = st.sidebar.slider(
            "Adjust the severity of the economic scenario. (0.0 - 1.0)",
            min_value=0.0, max_value=1.0, value=0.2, step=0.01,
            help="For example, 0.2 = 20% reduction."
        )
        parameters['scenario_severity_factor'] = scenario_severity_factor
    elif stress_type == "Firm-Wide":
        st.sidebar.markdown("*Firm-wide simulates an extensive aggregate impact.*")
        systemic_crisis_scale = st.sidebar.slider(
            "Set the scale of the systemic crisis. (0.0 - 1.0)",
            min_value=0.0, max_value=1.0, value=0.4, step=0.01,
            help="A broad reduction across all."
        )
        parameters['systemic_crisis_scale'] = systemic_crisis_scale

    err = None
    stressed_data = None
    with st.spinner("Simulating stressed data..."):
        try:
            stressed_data = simulate_stress_impact(data, stress_type, parameters)
            st.success("Stress test applied. Preview the results below.")
        except Exception as e:
            err = str(e)
    if err:
        st.error(err)
        st.stop()
    st.markdown("#### Stressed Data Preview")
    st.dataframe(stressed_data)

    st.markdown(r"""
    **Business Logic:**
    - Select and customize stress events to observe their direct effect on key financials.
    - Each methodology addresses a different type of plausible risk, from targeted to systemic.
    - All downstream scenario visualizations and risk metrics will reflect these adjustments.
    """)
    # Save to session state for downstream pages
    st.session_state['stressed_data'] = stressed_data
    st.session_state['stress_type'] = stress_type
    st.session_state['stress_parameters'] = parameters

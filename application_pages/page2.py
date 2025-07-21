
import streamlit as st
import pandas as pd

def simulate_stress_impact(data, stress_type, parameters):
    """Applies stress test methodology to data.

    Args:
        data (pd.DataFrame): The base financial data.
        stress_type (str): Type of stress test ('Sensitivity', 'Scenario', 'Firm-Wide').
        parameters (dict): Dictionary of parameters specific to the stress type.

    Returns:
        pd.DataFrame: DataFrame with stressed financial data.

    Raises:
        KeyError: If a required parameter or column is missing for the specified stress type.
        Exception: If an invalid stress type is provided.
    """
    stressed_data = data.copy() # Work on a copy to avoid modifying original data

    if stress_type == 'Sensitivity':
        parameter_to_shock = parameters.get('parameter_to_shock')
        shock_magnitude = parameters.get('shock_magnitude')
        if parameter_to_shock not in stressed_data.columns:
            raise KeyError(f"Parameter '{parameter_to_shock}' not found in data for Sensitivity stress test.")
        stressed_data[f'Adjusted_{parameter_to_shock.replace("Base_", "")}'] = stressed_data[parameter_to_shock] * (1 - shock_magnitude/100)
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
    st.header("Stress Test Simulation")
    st.markdown("In this page, you can simulate stress test scenarios based on the data loaded in the previous page.")

    if 'base_data' not in st.session_state:
        st.warning("Please load data on the 'Data Loading & Selection' page first.")
        return

    base_data = st.session_state['base_data']

    stress_type = st.sidebar.selectbox(
        "Select Stress Test Type:",
        options=["Sensitivity", "Scenario", "Firm-Wide"],
        help="Choose the stress test methodology to apply. Each type affects parameters differently."
    )

    parameters = {}

    if stress_type == "Sensitivity":
        parameter_to_shock = st.sidebar.selectbox(
            "Parameter to Shock:",
            options=["Base_Revenue", "Base_Costs"],
            help="Select the specific financial parameter to shock. Sensitivity testing focuses on a single variable."
        )
        shock_magnitude = st.sidebar.slider(
            "Shock Magnitude (% Reduction):",
            min_value=0,
            max_value=100,
            value=10,
            help="Define the percentage reduction to apply to the selected parameter ($0-100\%$). For example, 10 for a 10% reduction."
        )
        parameters['parameter_to_shock'] = parameter_to_shock
        parameters['shock_magnitude'] = shock_magnitude
    elif stress_type == "Scenario":
        scenario_severity_factor = st.sidebar.slider(
            "Scenario Severity Factor:",
            min_value=0.0,
            max_value=1.0,
            value=0.2,
            help="Adjust the severity of the economic scenario. This factor ($0.0-1.0$) simulates a broad downturn impact (e.g., 0.2 for a 20% reduction)."
        )
        parameters['scenario_severity_factor'] = scenario_severity_factor
    elif stress_type == "Firm-Wide":
        systemic_crisis_scale = st.sidebar.slider(
            "Systemic Crisis Scale:",
            min_value=0.0,
            max_value=1.0,
            value=0.5,
            help="Set the scale of the systemic crisis. This factor ($0.0-1.0$) applies a broad reduction across all base financial components, simulating severe aggregate impact."
        )
        parameters['systemic_crisis_scale'] = systemic_crisis_scale

    try:
        stressed_data = simulate_stress_impact(base_data, stress_type, parameters)
        st.dataframe(stressed_data)
        st.session_state['stressed_data'] = stressed_data
    except KeyError as e:
        st.error(f"Error: {e}")
    except Exception as e:
        st.error(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    run_page2()

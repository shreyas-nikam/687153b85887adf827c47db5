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

    # Always initialize Adjusted columns with base values first
    if 'Base_Revenue' in stressed_data.columns:
        stressed_data['Adjusted_Revenue'] = stressed_data['Base_Revenue']
    if 'Base_Costs' in stressed_data.columns:
        stressed_data['Adjusted_Costs'] = stressed_data['Base_Costs']

    if stress_type == 'Sensitivity':
        parameter_to_shock = parameters.get('parameter_to_shock')
        shock_magnitude = parameters.get('shock_magnitude')
        if parameter_to_shock not in stressed_data.columns:
            raise KeyError(f"Parameter '{parameter_to_shock}' not found in data for Sensitivity stress test.")
        # Apply shock only to the selected parameter
        adjusted_col_name = f'Adjusted_{parameter_to_shock.replace("Base_", "")}'
        stressed_data[adjusted_col_name] = stressed_data[parameter_to_shock] * (1 - shock_magnitude/100)
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
    # Stress Test Simulation Engine
    
    ## Theoretical Foundation
    
    Stress testing is a critical risk management tool that evaluates how financial institutions perform under adverse 
    market conditions. Based on the **PRMIA Operational Risk Manager Handbook**, we implement three distinct 
    methodologies, each serving different analytical purposes in understanding risk exposure.
    """)

    if 'base_data' not in st.session_state:
        st.error("**No Base Data Found**")
        st.markdown("""
        Please complete the following steps:
        1. Navigate to **'Data Loading & Selection'** page using the sidebar
        2. Load either synthetic data or upload your CSV file
        3. Return to this page to run stress simulations
        """)
        st.stop()

    base_data = st.session_state['base_data']
    
    # Display current data summary
    st.success("**Base Data Loaded Successfully**")
    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric("Data Points", len(base_data))
    with col2:
        st.metric("Avg Revenue", f"${base_data['Base_Revenue'].mean():.2f}")
    with col3:
        st.metric("Avg Costs", f"${base_data['Base_Costs'].mean():.2f}")

    st.markdown("---")

    # Stress test type selection with detailed explanations
    st.subheader("Stress Test Methodology Selection")
    
    stress_type = st.sidebar.selectbox(
        "Select Stress Test Type:",
        options=["Sensitivity", "Scenario", "Firm-Wide"],
        help="Choose the stress test methodology based on your analysis objectives."
    )

    # Detailed explanation for each stress type
    if stress_type == "Sensitivity":
        st.markdown(r"""
        ### Sensitivity Stress Testing
        
        **Definition**: Focuses on the impact of changing **a single parameter** or one component of a portfolio.
        
        **Mathematical Formula**:
        $$\text{Adjusted Parameter} = \text{Base Parameter} \times \left(1 - \frac{\text{Shock Magnitude}}{100}\right)$$
        
        **Business Applications**:
        - **Interest Rate Risk**: How does a 2% interest rate increase affect loan portfolios?
        - **Credit Risk**: What happens if default rates on a specific product line double?
        - **Market Risk**: Impact of a 20% decline in a particular asset class
        
        **Regulatory Context**: 
        Required under Basel III for banks to assess individual risk factor sensitivities.
        
        **Key Benefits**:
        - Identifies which single factors pose the greatest risk
        - Simple to implement and understand
        - Useful for hedging strategy development

        **Limitations**:
        - Doesn't capture correlation effects between risk factors
        - May underestimate systemic risk scenarios
        """)
        
    elif stress_type == "Scenario":
        st.markdown(r"""
        ### Scenario Stress Testing
        
        **Definition**: Evaluates the impact of **specific hypothetical events** affecting multiple financial components simultaneously.
        
        **Mathematical Formula**:
        $$\text{Adjusted Component} = \text{Base Component} \times (1 - \text{Scenario Severity Factor})$$
        
        **Common Scenario Examples**:
        - **Economic Recession**: GDP decline, unemployment rise, market volatility
        - **Commodity Price Shock**: Oil price surge affecting transportation costs
        - **Geopolitical Events**: Trade wars, sanctions, political instability
        - **Natural Disasters**: Hurricane impact on regional operations
        
        **Regulatory Examples**:
        - **CCAR (US)**: Severely adverse economic scenarios
        - **EBA (EU)**: Adverse macroeconomic scenarios
        - **APRA (Australia)**: Housing market stress scenarios
        
        **Key Benefits**:
        - Captures realistic market correlations
        - Tests multiple risk factors simultaneously
        - Provides plausible stress narratives

        **Implementation Considerations**:
        - Based on historical events or expert judgment
        - Should reflect institution's specific risk profile
        """)
        
    else:  # Firm-Wide
        st.markdown(r"""
        ### Firm-Wide Stress Testing
        
        **Definition**: Assesses the **aggregate impact of severe systemic crises** across all portfolios and business processes.
        
        **Mathematical Formula**:
        $$\text{Adjusted Component} = \text{Base Component} \times (1 - \text{Systemic Crisis Scale})$$
        
        **Systemic Crisis Examples**:
        - **2008 Financial Crisis**: Global banking system collapse
        - **COVID-19 Pandemic**: Worldwide economic shutdown
        - **Sovereign Debt Crisis**: Government defaults affecting entire economies
        - **Cyber Attack**: System-wide technology infrastructure failure
        
        **Comprehensive Impact Assessment**:
        - **Income**: Revenue declines across all business lines
        - **Costs**: Increased operational and funding costs
        - **Market Risk**: Portfolio losses across all asset classes
        - **Counterparty Risk**: Increased default probabilities
        - **Liquidity**: Funding market stress and deposit outflows

        **Regulatory Requirements**:
        - **Dodd-Frank**: Annual stress tests for large US banks
        - **Basel III**: Capital adequacy under severe stress
        - **ICAAP**: Internal capital adequacy assessment processes
        
        **Key Benefits**:
        - Tests overall institutional resilience
        - Identifies systemic vulnerabilities
        - Supports capital planning decisions

        **Critical Considerations**:
        - Must reflect "tail risk" scenarios (low probability, high impact)
        - Should incorporate correlations across all risk types
        """)

    st.markdown("---")
    st.subheader("Parameter Configuration")

    parameters = {}

    if stress_type == "Sensitivity":
        col1, col2 = st.columns(2)
        
        with col1:
            parameter_to_shock = st.selectbox(
                "Parameter to Shock:",
                options=["Base_Revenue", "Base_Costs"],
                help="Select which financial component to stress test"
            )
            
        with col2:
            shock_magnitude = st.slider(
                "Shock Magnitude (% Reduction):",
                min_value=0,
                max_value=100,
                value=10,
                help="Percentage reduction to apply (0% = no impact, 100% = total loss)"
            )
        
        # Real-time calculation preview
        if parameter_to_shock == "Base_Revenue":
            original_value = base_data['Base_Revenue'].mean()
            shocked_value = original_value * (1 - shock_magnitude/100)
            st.info(f"**Preview**: Average {parameter_to_shock} would change from {original_value:.2f} to {shocked_value:.2f}")
        else:
            original_value = base_data['Base_Costs'].mean()
            shocked_value = original_value * (1 - shock_magnitude/100)
            st.info(f"**Preview**: Average {parameter_to_shock} would change from {original_value:.2f} to {shocked_value:.2f}")

        parameters['parameter_to_shock'] = parameter_to_shock
        parameters['shock_magnitude'] = shock_magnitude
        
    elif stress_type == "Scenario":
        scenario_severity_factor = st.slider(
            "Scenario Severity Factor:",
            min_value=0.0,
            max_value=1.0,
            value=0.2,
            step=0.05,
            help="Overall economic downturn severity (0.0 = no impact, 1.0 = complete collapse)"
        )
        
        # Scenario interpretation
        if scenario_severity_factor <= 0.1:
            scenario_desc = "**Mild Economic Slowdown** - Minor market corrections"
        elif scenario_severity_factor <= 0.3:
            scenario_desc = "**Moderate Recession** - Significant but manageable downturn"
        elif scenario_severity_factor <= 0.5:
            scenario_desc = "**Severe Recession** - Major economic contraction"
        else:
            scenario_desc = "**Economic Depression** - Extreme systemic crisis"

        st.info(f"**Scenario Interpretation**: {scenario_desc}")
        
        # Impact preview
        revenue_impact = base_data['Base_Revenue'].sum() * scenario_severity_factor
        cost_impact = base_data['Base_Costs'].sum() * scenario_severity_factor
        st.warning(f"**Estimated Total Impact**: Revenue loss {revenue_impact:.2f}, Cost reduction {cost_impact:.2f}")

        parameters['scenario_severity_factor'] = scenario_severity_factor
        
    elif stress_type == "Firm-Wide":
        systemic_crisis_scale = st.slider(
            "Systemic Crisis Scale:",
            min_value=0.0,
            max_value=1.0,
            value=0.5,
            step=0.05,
            help="Scale of firm-wide systemic impact (0.0 = no crisis, 1.0 = total system failure)"
        )
        
        # Crisis scale interpretation
        if systemic_crisis_scale <= 0.2:
            crisis_desc = "**Limited Systemic Stress** - Isolated market disruptions"
        elif systemic_crisis_scale <= 0.4:
            crisis_desc = "**Moderate Systemic Crisis** - Regional economic instability"
        elif systemic_crisis_scale <= 0.6:
            crisis_desc = "**Severe Systemic Crisis** - National economic emergency"
        else:
            crisis_desc = "**Extreme Systemic Collapse** - Global financial system failure"

        st.error(f"**Crisis Level**: {crisis_desc}")

        # Comprehensive impact preview
        total_revenue = base_data['Base_Revenue'].sum()
        total_costs = base_data['Base_Costs'].sum()
        revenue_loss = total_revenue * systemic_crisis_scale
        net_impact = revenue_loss - (total_costs * systemic_crisis_scale)
        
        st.warning(f"""
        **Firm-Wide Impact Assessment**:
        - Revenue Loss: ${revenue_loss:.2f} ({systemic_crisis_scale*100:.1f}% of total)
        - Net Financial Impact: ${net_impact:.2f}
        - Business Continuity Risk: {'Critical' if systemic_crisis_scale > 0.7 else 'Elevated' if systemic_crisis_scale > 0.4 else 'Manageable'}
        """)
        
        parameters['systemic_crisis_scale'] = systemic_crisis_scale

    st.markdown("---")
    
    # Execute stress test
    if st.button("**Execute Stress Test**", type="primary", use_container_width=True):
        try:
            with st.spinner(f"Running {stress_type} stress test simulation..."):
                stressed_data = simulate_stress_impact(base_data, stress_type, parameters)
                
            # Store results in session state
            st.session_state['stressed_data'] = stressed_data
            st.session_state['stress_type'] = stress_type
            st.session_state['stress_parameters'] = parameters
            
            st.success(f"**{stress_type} Stress Test Completed Successfully!**")
            
            # Results summary
            st.subheader("Stress Test Results Summary")
            
            # Calculate immediate impact metrics
            if 'Adjusted_Revenue' in stressed_data.columns and 'Adjusted_Costs' in stressed_data.columns:
                original_revenue = base_data['Base_Revenue'].sum()
                stressed_revenue = stressed_data['Adjusted_Revenue'].sum()
                original_costs = base_data['Base_Costs'].sum()
                stressed_costs = stressed_data['Adjusted_Costs'].sum()
                
                revenue_change = stressed_revenue - original_revenue
                cost_change = stressed_costs - original_costs
                net_impact = revenue_change - cost_change
                
                col1, col2, col3, col4 = st.columns(4)
                
                with col1:
                    st.metric(
                        "Revenue Impact", 
                        f"${revenue_change:,.2f}",
                        delta=f"{(revenue_change/original_revenue)*100:.1f}%"
                    )
                with col2:
                    st.metric(
                        "Cost Impact", 
                        f"${cost_change:,.2f}",
                        delta=f"{(cost_change/original_costs)*100:.1f}%"
                    )
                with col3:
                    st.metric(
                        "Net Impact", 
                        f"${net_impact:,.2f}",
                        delta="Profit Change"
                    )
                with col4:
                    recovery_time = abs(net_impact) / (original_revenue * 0.1) if net_impact < 0 else 0
                    st.metric(
                        "Est. Recovery", 
                        f"{recovery_time:.1f} periods",
                        delta="Time to recover" if recovery_time > 0 else "No recovery needed"
                    )
            
            # Display stressed data
            st.subheader("Detailed Stressed Data")
            st.dataframe(stressed_data, use_container_width=True)
            
            # Next steps guidance
            st.info("""
            **Next Steps**:
            1. Navigate to **'Visualizations'** page to analyze detailed impact charts
            2. Review risk capacity metrics and financial resilience indicators
            3. Compare different stress scenarios by returning to adjust parameters
            """)
            
        except KeyError as e:
            st.error(f"**Configuration Error**: {e}")
            st.markdown("""
            **Troubleshooting Steps**:
            - Verify all required data columns are present
            - Check parameter selection matches available data
            - Ensure data was properly loaded in Page 1
            """)
        except Exception as e:
            st.error(f"**Simulation Error**: {e}")
            st.markdown("""
            **Common Solutions**:
            - Refresh the page and reload data
            - Verify parameter values are within valid ranges
            - Contact support if error persists
            """)

    st.markdown("""
    ---
    ### Stress Testing Best Practices
    
    **Parameter Selection Guidelines**:
    - **Conservative Approach**: Start with moderate stress levels (10-30%)
    - **Regulatory Alignment**: Use stress factors consistent with regulatory guidance
    - **Historical Validation**: Compare results with actual historical stress events
    - **Forward-Looking**: Consider emerging risks not captured in historical data
    
    **Model Validation**:
    - Back-test against historical crisis periods
    - Sensitivity analysis on key assumptions
    - Independent review of methodologies
    - Regular model performance monitoring
    """)

if __name__ == "__main__":
    run_page2()

import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

def calculate_risk_capacity_metrics(projected_data):
    """
    Computes key metrics to assess the firm's risk capacity under stress.

    Args:
        projected_data (pd.DataFrame): DataFrame with projected financial data,
                                       including 'Adjusted_Revenue', 'Adjusted_Costs'.

    Returns:
        dict: Dictionary of calculated risk capacity metrics.

    Raises:
        Exception: If the input DataFrame is empty.
    """
    if projected_data.empty:
        raise Exception("Input DataFrame cannot be empty.")

    if 'Adjusted_Revenue' not in projected_data.columns or 'Adjusted_Costs' not in projected_data.columns:
        # Check if 'Base_Revenue' and 'Base_Costs' exist for initial adjustment if not already done
        if 'Base_Revenue' in projected_data.columns and 'Base_Costs' in projected_data.columns:
            # If Adjusted_Revenue/Costs are not created (e.g., if page2 was skipped),
            # assume no stress applied and use base values
            missing_cols = []
            if 'Adjusted_Revenue' not in projected_data.columns:
                missing_cols.append('Adjusted_Revenue')
                projected_data['Adjusted_Revenue'] = projected_data['Base_Revenue']
            if 'Adjusted_Costs' not in projected_data.columns:
                missing_cols.append('Adjusted_Costs')
                projected_data['Adjusted_Costs'] = projected_data['Base_Costs']
            
            st.info(f"⚠️ **Stress Test Data Completed**: {', '.join(missing_cols)} were missing but have been filled with base values. This usually happens when:\n"
                   "- You haven't run the stress test simulation on Page 2 yet\n"
                   "- The stress test was applied but only to one parameter\n\n"
                   "**Solution**: The missing columns have been automatically filled with base values (no stress applied to those parameters).")
        else:
            raise KeyError("Missing 'Adjusted_Revenue'/'Adjusted_Costs' and 'Base_Revenue'/'Base_Costs' for metric derivation. Please ensure you load data on Page 1 and apply stress test on Page 2.")

    projected_data['Net_Earnings_Under_Stress'] = projected_data['Adjusted_Revenue'] - projected_data['Adjusted_Costs']

    initial_capital_value = 1000
    initial_liquidity_value = 500

    # These impacts are illustrative as per the prompt's reference
    if 'Base_Revenue' in projected_data.columns and 'Base_Costs' in projected_data.columns:
        projected_data['Capital_Impact'] = (projected_data['Base_Revenue'] - projected_data['Adjusted_Revenue']) + \
                                          (projected_data['Adjusted_Costs'] - projected_data['Base_Costs'])
        projected_data['Capital_Remaining'] = initial_capital_value - projected_data['Capital_Impact'].cumsum()
        projected_data['Liquidity_Impact'] = (projected_data['Base_Revenue'] - projected_data['Adjusted_Revenue']) * 0.5
        projected_data['Liquidity_Position'] = initial_liquidity_value - projected_data['Liquidity_Impact'].cumsum()
    else:
        st.warning("Base_Revenue or Base_Costs not available for full impact calculation. Capital and Liquidity impacts might be inaccurate or estimated.")
        # Fallback if base columns are missing (though page1 should ensure them)
        projected_data['Capital_Impact'] = 0 # Or some default impact
        projected_data['Capital_Remaining'] = initial_capital_value - projected_data['Net_Earnings_Under_Stress'].cumsum() # Simplified fallback
        projected_data['Liquidity_Impact'] = 0 # Or some default
        projected_data['Liquidity_Position'] = initial_liquidity_value - projected_data['Net_Earnings_Under_Stress'].cumsum() * 0.5 # Simplified fallback

    capital_remaining = projected_data['Capital_Remaining']
    liquidity_position = projected_data['Liquidity_Position']

    initial_capital = initial_capital_value # Use the defined initial value
    min_capital = capital_remaining.min()
    capital_drawdown = initial_capital - min_capital
    capital_drawdown_percentage = (capital_drawdown / initial_capital) * 100 if initial_capital != 0 else 0

    min_liquidity = liquidity_position.min()
    liquidity_shortfall = abs(min_liquidity) if min_liquidity < 0 else 0

    metrics = {
        'Initial_Capital': initial_capital,
        'Minimum_Capital_Remaining': min_capital,
        'Capital_Drawdown': capital_drawdown,
        'Capital_Drawdown_Percentage': capital_drawdown_percentage,
        'Minimum_Liquidity_Position': min_liquidity,
        'Liquidity_Shortfall': liquidity_shortfall
    }
    return metrics, projected_data # Also return the augmented data for plotting

def generate_visualizations(data, plot_type, config={}):
    """Generates and displays visualizations based on plot_type using Plotly."""
    if data.empty:
        st.warning("Dataframe is empty, cannot generate visualizations.")
        return

    if 'Date' not in data.columns or not pd.api.types.is_datetime64_any_dtype(data['Date']):
        st.error("The 'Date' column is missing or not in datetime format. Please ensure your data has a 'Date' column properly formatted.")
        return

    if plot_type == 'trend':
        st.subheader("Trend Plots")
        trend_cols = ['Base_Revenue', 'Base_Costs', 'Adjusted_Revenue', 'Adjusted_Costs',
                      'Net_Earnings_Under_Stress', 'Capital_Remaining', 'Liquidity_Position']

        for column in trend_cols:
            if column in data.columns and pd.api.types.is_numeric_dtype(data[column]):
                fig = px.line(data, x='Date', y=column,
                              title=f'{column} Trend Over Time',
                              labels={'Date': 'Date', column: 'Value'})
                fig.update_layout(hovermode="x unified", title_x=0.5)
                st.plotly_chart(fig, use_container_width=True)

    elif plot_type == 'relationship':
        st.subheader("Relationship Plots (Scatter Plots)")
        numeric_columns = data.select_dtypes(include=['number']).columns.tolist()
        cols_to_exclude = ['Date']
        numeric_columns = [col for col in numeric_columns if col not in cols_to_exclude]

        if len(numeric_columns) < 2:
            st.warning("Not enough numeric columns for relationship plots.")
            return

        selected_x = st.sidebar.selectbox("Select X-axis for Relationship Plot", options=numeric_columns)
        selected_y = st.sidebar.selectbox("Select Y-axis for Relationship Plot", options=[col for col in numeric_columns if col != selected_x])

        if selected_x and selected_y:
            fig = px.scatter(data, x=selected_x, y=selected_y,
                             title=f'Relationship: {selected_x} vs {selected_y}',
                             labels={selected_x: selected_x, selected_y: selected_y})
            fig.update_layout(title_x=0.5)
            st.plotly_chart(fig, use_container_width=True)
        else:
            st.info("Select two numeric columns to display a relationship plot.")

    elif plot_type == 'comparison':
        st.subheader("Comparison Plots (Bar Charts)")
        numeric_columns = data.select_dtypes(include=['number']).columns.tolist()
        cols_to_exclude_for_comparison = ['Date', 'Capital_Impact', 'Liquidity_Impact'] # Exclude cumulative impacts or temporary
        numeric_columns = [col for col in numeric_columns if col not in cols_to_exclude_for_comparison]

        if len(numeric_columns) < 2:
            st.warning("Not enough numeric columns for comparison plots.")
            return

        col1_name = st.sidebar.selectbox("Select First Column for Comparison", options=numeric_columns)
        col2_name = st.sidebar.selectbox("Select Second Column for Comparison", options=[col for col in numeric_columns if col != col1_name])

        if col1_name and col2_name:
            fig = go.Figure(data=[
                go.Bar(name=col1_name, x=data['Date'], y=data[col1_name]),
                go.Bar(name=col2_name, x=data['Date'], y=data[col2_name])
            ])
            fig.update_layout(barmode='group', title=f'Comparison: {col1_name} vs {col2_name}', title_x=0.5)
            st.plotly_chart(fig, use_container_width=True)
        else:
            st.info("Select two numeric columns to display a comparison plot.")

    else:
        st.error("Invalid plot_type. Choose from 'trend', 'relationship', or 'comparison'.")

def run_page3():
    st.markdown(r"""
    ### 3. Risk Capacity Metrics & Visualizations

    This page presents the key financial risk metrics derived from the stressed data and interactive visualizations.
    Understanding these metrics and trends helps assess the firm's resilience under adverse conditions.

    **Key Metrics Formulas:**
    - **Capital Drawdown**: $\text{Capital Drawdown} = \text{Initial Capital} - \text{Minimum Capital Remaining}$
    - **Capital Drawdown Percentage**: $\text{Capital Drawdown Percentage} = \left( \frac{\text{Capital Drawdown}}{\text{Initial Capital}} \right) \times 100$
    - **Liquidity Shortfall**:
      $$ \text{Liquidity Shortfall} = \begin{cases} |\text{Minimum Liquidity Position}| & \text{if } \text{Minimum Liquidity Position} < 0 \\ 0 & \text{otherwise} \end{cases} $$
    """)

    if 'stressed_data' not in st.session_state:
        st.error("No stressed data available. Please go to Page 1 to load data and Page 2 to apply stress.")
        st.stop()

    stressed_data = st.session_state['stressed_data']
    
    # Debug information to help understand what's in the data
    with st.expander("🔍 **Debug Info**: Available Data Columns"):
        st.write("**Columns in stressed_data:**", list(stressed_data.columns))
        st.write("**Session state keys:**", list(st.session_state.keys()))
        if 'stress_type' in st.session_state:
            st.write("**Last stress test applied:**", st.session_state['stress_type'])
            if 'stress_parameters' in st.session_state:
                st.write("**Stress test parameters:**", st.session_state['stress_parameters'])
        else:
            st.write("**Last stress test applied:** None")
        st.write("**Data shape:**", stressed_data.shape)
        if len(stressed_data) > 0:
            st.write("**Sample data:**")
            st.dataframe(stressed_data.head(3))

    risk_metrics, augmented_data = {}, pd.DataFrame()
    err = None
    with st.spinner("Calculating risk metrics..."):
        try:
            risk_metrics, augmented_data = calculate_risk_capacity_metrics(stressed_data.copy())
            st.success("Risk metrics calculated.")
        except Exception as e:
            err = str(e)
    if err:
        st.error(err)
        st.stop()

    st.markdown("#### Risk Capacity Metrics")
    col1, col2, col3 = st.columns(3)
    metrics_display = {
        "Initial Capital": risk_metrics['Initial_Capital'],
        "Minimum Capital Remaining": risk_metrics['Minimum_Capital_Remaining'],
        "Capital Drawdown": risk_metrics['Capital_Drawdown'],
        "Capital Drawdown Percentage": f"{risk_metrics['Capital_Drawdown_Percentage']:.2f}%",
        "Minimum Liquidity Position": risk_metrics['Minimum_Liquidity_Position'],
        "Liquidity Shortfall": risk_metrics['Liquidity_Shortfall']
    }

    cols = [col1, col2, col3]
    for i, (label, value) in enumerate(metrics_display.items()):
        cols[i % 3].metric(label=label, value=f"{value:.2f}" if isinstance(value, (int, float)) else value)

    st.markdown("---")

    st.sidebar.markdown("#### Visualization Settings")
    plot_selection = st.sidebar.radio(
        "Select plot type:",
        ("Trend", "Relationship", "Comparison")
    )

    with st.spinner("Generating visualizations..."):
        if plot_selection == "Trend":
            generate_visualizations(augmented_data, 'trend')
        elif plot_selection == "Relationship":
            generate_visualizations(augmented_data, 'relationship')
        elif plot_selection == "Comparison":
            generate_visualizations(augmented_data, 'comparison')
    
    st.markdown(r"""
    **Business Logic:**
    - Visualizations provide a clear, intuitive understanding of financial performance under stress.
    - Trend plots show the evolution of key metrics over time.
    - Relationship plots reveal correlations between different impact metrics.
    - Comparison plots highlight the relative changes between selected financial components.
    """)

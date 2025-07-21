
import streamlit as st
import pandas as pd
import plotly.express as px

def calculate_risk_capacity_metrics(projected_data):
    """Computes key metrics to assess the firm's risk capacity under stress.

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

    # Derivations for demonstration purposes, as in the notebook.
    # In a real application, these might come from more complex models or be pre-existing.
    if 'Adjusted_Revenue' not in projected_data.columns or 'Adjusted_Costs' not in projected_data.columns:
        raise KeyError("Missing 'Adjusted_Revenue' or 'Adjusted_Costs' for metric derivation.")

    projected_data['Net_Earnings_Under_Stress'] = projected_data['Adjusted_Revenue'] - projected_data['Adjusted_Costs']
    
    # Simplified capital and liquidity impact calculation for demonstration
    initial_capital_value = 1000
    initial_liquidity_value = 500
    projected_data['Capital_Impact'] = (projected_data['Base_Revenue'] - projected_data['Adjusted_Revenue']) + \
                                      (projected_data['Adjusted_Costs'] - projected_data['Base_Costs'])
    projected_data['Capital_Remaining'] = initial_capital_value - projected_data['Capital_Impact'].cumsum()
    
    projected_data['Liquidity_Impact'] = (projected_data['Base_Revenue'] - projected_data['Adjusted_Revenue']) * 0.5
    projected_data['Liquidity_Position'] = initial_liquidity_value - projected_data['Liquidity_Impact'].cumsum()

    capital_remaining = projected_data['Capital_Remaining']
    liquidity_position = projected_data['Liquidity_Position']

    initial_capital = capital_remaining.iloc[0] if not capital_remaining.empty else initial_capital_value
    min_capital = capital_remaining.min() if not capital_remaining.empty else initial_capital_value
    capital_drawdown = initial_capital - min_capital
    if initial_capital != 0:
        capital_drawdown_percentage = (capital_drawdown / initial_capital) * 100
    else:
        capital_drawdown_percentage = 0

    min_liquidity = liquidity_position.min() if not liquidity_position.empty else initial_liquidity_value
    liquidity_shortfall = 0
    if min_liquidity < 0:
        liquidity_shortfall = abs(min_liquidity)

    metrics = {
        'Initial_Capital': initial_capital,
        'Minimum_Capital_Remaining': min_capital,
        'Capital_Drawdown': capital_drawdown,
        'Capital_Drawdown_Percentage': capital_drawdown_percentage,
        'Minimum_Liquidity_Position': min_liquidity,
        'Liquidity_Shortfall': liquidity_shortfall
    }

    return metrics

def generate_visualizations(data, plot_type, col1=None, col2=None):
    """Generates and displays visualizations based on plot_type using Plotly.

    Args:
        data (pd.DataFrame): DataFrame with data to visualize.
        plot_type (str): Type of plot ('trend', 'relationship', 'comparison').
        col1 (str, optional): First column for comparison plot.
        col2 (str, optional): Second column for comparison plot.

    Raises:
        ValueError: If plot_type is invalid or data is insufficient.
    """

    if data.empty:
        st.warning("Dataframe is empty, cannot generate visualizations.")
        return

    if 'Date' not in data.columns:
        data['Date'] = range(len(data))

    if plot_type == 'trend':
        st.subheader("Trend Plots")
        trend_cols = ['Base_Revenue', 'Base_Costs', 'Adjusted_Revenue', 'Adjusted_Costs', 'Net_Earnings_Under_Stress', 'Capital_Remaining', 'Liquidity_Position']
        for column in trend_cols:
            if column in data.columns:
                fig = px.line(data, x='Date', y=column, title=f'{column} Trend Over Time')
                st.plotly_chart(fig, use_container_width=True)

    elif plot_type == 'relationship':
        st.subheader("Relationship Plots (Scatter Plots)")
        numeric_columns = data.select_dtypes(include=['number']).columns.tolist()
        for i in range(len(numeric_columns)):
            for j in range(i + 1, len(numeric_columns)):
                col1 = numeric_columns[i]
                col2 = numeric_columns[j]
                fig = px.scatter(data, x=col1, y=col2, title=f'Relationship: {col1} vs {col2}')
                st.plotly_chart(fig, use_container_width=True)

    elif plot_type == 'comparison':
        st.subheader("Comparison Plots (Bar Charts)")
        if col1 and col2:
            fig = px.bar(data, x='Date', y=[col1, col2], title=f'Comparison: {col1} vs {col2}')
            st.plotly_chart(fig, use_container_width=True)
        else:
            st.warning("Please select two columns for comparison.")

def run_page3():
    st.header("Visualizations")
    st.markdown("In this page, you can visualize the results of the stress test simulation.")

    if 'stressed_data' not in st.session_state:
        st.warning("Please run the simulation on the 'Stress Test Simulation' page first.")
        return

    stressed_data = st.session_state['stressed_data']

    try:
        risk_metrics = calculate_risk_capacity_metrics(stressed_data.copy())

        st.subheader("Risk Capacity Metrics")
        for key, value in risk_metrics.items():
            st.metric(label=key, value=f"{value:.2f}")

        st.subheader("Visualizations")
        plot_type = st.selectbox("Select Plot Type:", options=['trend', 'relationship', 'comparison'])

        if plot_type == 'comparison':
            col1 = st.selectbox("Select first column for comparison:", options=stressed_data.columns)
            col2 = st.selectbox("Select second column for comparison:", options=stressed_data.columns)
            generate_visualizations(stressed_data, plot_type, col1=col1, col2=col2)
        else:
            generate_visualizations(stressed_data, plot_type)

    except Exception as e:
        st.error(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    run_page3()

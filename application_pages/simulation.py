
import pandas as pd
import numpy as np
import streamlit as st
import plotly.express as px
import plotly.graph_objects as go

def generate_synthetic_transactions(num_transactions):
    if not isinstance(num_transactions, int):
        raise TypeError("Number of transactions must be an integer.")
    if num_transactions < 0:
        raise ValueError("Number of transactions must be non-negative.")
    data = {
        'Principal': np.random.uniform(10000, 1000000, num_transactions),
        'Interest Rate': np.random.uniform(0.02, 0.15, num_transactions),
        'Tenor': np.random.randint(12, 120, num_transactions),
        'PD': np.random.uniform(0.001, 0.1, num_transactions),
        'LGD': np.random.uniform(0.4, 0.8, num_transactions),
        'Operational Cost Ratio': np.random.uniform(0.005, 0.02, num_transactions),
        'Cost of Funds': np.random.uniform(0.01, 0.05, num_transactions)
    }
    return pd.DataFrame(data)

def calculate_expected_loss(principal, pd, lgd):
    return principal * pd * lgd

def calculate_economic_capital(principal, pd, lgd, ul_factor):
    return principal * pd * lgd * ul_factor

def calculate_net_risk_adjusted_reward(principal, interest_rate, tenor, funding_cost_rate, op_cost_ratio, expected_loss):
    total_income = principal * interest_rate * tenor
    total_funding_cost = principal * funding_cost_rate * tenor
    total_operating_cost = principal * op_cost_ratio * tenor
    net_risk_adjusted_reward = total_income - total_funding_cost - total_operating_cost - expected_loss
    return net_risk_adjusted_reward

def calculate_rarorac_single_transaction(net_risk_adjusted_reward, economic_capital):
    if economic_capital == 0:
        return np.nan
    return net_risk_adjusted_reward / economic_capital

def calculate_all_rarorac_components_df(df, interest_rate_column, ul_factor):
    df_copy = df.copy()
    df_copy['Expected Loss'] = df_copy['Principal'] * df_copy['PD'] * df_copy['LGD']
    df_copy['Revenue'] = df_copy['Principal'] * df_copy[interest_rate_column] * df_copy['Tenor']
    df_copy['Operating Cost'] = df_copy['Principal'] * df_copy['Operational Cost Ratio'] * df_copy['Tenor']
    df_copy['Economic Capital'] = df_copy['Principal'] * df_copy['PD'] * df_copy['LGD'] * ul_factor
    df_copy['Net Risk Adjusted Return'] = df_copy['Revenue'] - df_copy['Expected Loss'] - df_copy['Operating Cost'] - (df_copy['Cost of Funds'] * df_copy['Principal'] * df_copy['Tenor'])
    df_copy['RARORAC'] = df_copy['Net Risk Adjusted Return'] / df_copy['Economic Capital']
    df_copy.loc[df_copy['Economic Capital'] == 0, 'RARORAC'] = np.nan
    df_copy.loc[~np.isfinite(df_copy['RARORAC']), 'RARORAC'] = np.nan
    return df_copy

def adjust_interest_rate(row, hurdle_rate, ul_factor):
    principal = row['Principal']
    pd = row['PD']
    lgd = row['LGD']
    tenor = row['Tenor']
    operational_cost_ratio = row['Operational Cost Ratio']
    cost_of_funds = row['Cost of Funds']

    expected_loss = principal * pd * lgd
    operating_cost = principal * operational_cost_ratio * tenor
    economic_capital = principal * pd * lgd * ul_factor

    if economic_capital == 0:
        return np.nan

    min_interest_rate = 0.001
    max_interest_rate = 2.0
    current_interest_rate = row['Interest Rate']

    for _ in range(100):
        revenue = principal * current_interest_rate * tenor
        net_risk_adjusted_return = revenue - expected_loss - operating_cost - (cost_of_funds * principal * tenor)
        rarorac = net_risk_adjusted_return / economic_capital

        if rarorac >= hurdle_rate:
            max_interest_rate = current_interest_rate
        else:
            min_interest_rate = current_interest_rate

        if abs(max_interest_rate - min_interest_rate) < 1e-7:
            break

        current_interest_rate = (min_interest_rate + max_interest_rate) / 2.0

    final_revenue = principal * current_interest_rate * tenor
    final_nrar = final_revenue - expected_loss - operating_cost - (cost_of_funds * principal * tenor)
    final_rarorac = final_nrar / economic_capital

    if final_rarorac < hurdle_rate and abs(current_interest_rate - (max_interest_rate + min_interest_rate)/2.0) < 1e-7 and (hurdle_rate - final_rarorac) > 0.001:
        return np.nan

    return current_interest_rate

def simulate_pricing_strategies(transactions_df, hurdle_rate, ul_factor):
    if transactions_df.empty:
        return pd.DataFrame()

    df = transactions_df.copy()

    df['Interest Rate_Risk_Insensitive'] = df['Interest Rate']
    df_ris = calculate_all_rarorac_components_df(df, 'Interest Rate_Risk_Insensitive', ul_factor)
    df['RARORAC_Risk_Insensitive'] = df_ris['RARORAC']
    df['Net Risk Adjusted Return_Risk_Insensitive'] = df_ris['Net Risk Adjusted Return']
    df['Economic Capital'] = df_ris['Economic Capital']

    df['Interest Rate_Risk_Sensitive'] = df.apply(lambda row: adjust_interest_rate(row, hurdle_rate=hurdle_rate, ul_factor=ul_factor), axis=1)
    df_rs = calculate_all_rarorac_components_df(df, 'Interest Rate_Risk_Sensitive', ul_factor)
    df['RARORAC_Risk_Sensitive'] = df_rs['RARORAC']
    df['Net Risk Adjusted Return_Risk_Sensitive'] = df_rs['Net Risk Adjusted Return']

    return df

def run_simulation():
    st.header("Simulation")
    st.markdown("Interactive lab.")

    num_transactions = st.session_state.get("num_transactions", 100)
    hurdle_rate = st.session_state.get("hurdle_rate", 0.10)
    ul_factor = st.session_state.get("ul_factor", 3.0)

    st.markdown("---")

    transactions_df = generate_synthetic_transactions(num_transactions)
    st.subheader("Transactions Data")
    st.dataframe(transactions_df.head())
    st.info(f"Generated {num_transactions} transactions.")

    st.markdown("---")

    with st.expander("EL"):
        st.markdown(r"EL is average loss.")
        st.latex(r"\text{EL} = P \times PD \times LGD")

    with st.expander("EC"):
        st.markdown(r"EC is capital required.")
        st.latex(r"\text{EC} = P \times PD \times LGD \times UL")

    with st.expander("NRAR"):
        st.markdown(r"NRAR is net income.")
        st.latex(r"\text{NRAR} = TI - TFC - TOC - EL")

    with st.expander("RARORAC"):
        st.markdown(r"RARORAC is return per unit of capital.")
        st.latex(r"\text{RARORAC} = \frac{NRAR}{EC}")

    st.markdown("---")

    simulation_results = simulate_pricing_strategies(transactions_df, hurdle_rate, ul_factor)
    st.success("Simulation complete!")

    st.subheader("Comparison")
    display_cols = ['Principal', 'Interest Rate', 'Interest Rate_Risk_Insensitive', 'RARORAC_Risk_Insensitive', 'Interest Rate_Risk_Sensitive', 'RARORAC_Risk_Sensitive', 'Net Risk Adjusted Return_Risk_Insensitive', 'Net Risk Adjusted Return_Risk_Sensitive', 'Economic Capital']
    st.dataframe(simulation_results[display_cols].head(10).style.format({'Principal': '${:,.0f}', 'Interest Rate': '{:.2%}', 'Interest Rate_Risk_Insensitive': '{:.2%}', 'RARORAC_Risk_Insensitive': '{:.2%}', 'Interest Rate_Risk_Sensitive': '{:.2%}', 'RARORAC_Risk_Sensitive': '{:.2%}', 'Net Risk Adjusted Return_Risk_Insensitive': '${:,.0f}', 'Net Risk Adjusted Return_Risk_Sensitive': '${:,.0f}', 'Economic Capital': '${:,.0f}'}))

    st.markdown("---")

    st.subheader("RARORAC Distribution")
    melted_rarorac = simulation_results.melt(id_vars=['Principal'], value_vars=['RARORAC_Risk_Insensitive', 'RARORAC_Risk_Sensitive'], var_name='Pricing Strategy', value_name='RARORAC')
    melted_rarorac = melted_rarorac.dropna(subset=['RARORAC'])

    fig = go.Figure()
    fig.add_trace(go.Histogram(x=melted_rarorac[melted_rarorac['Pricing Strategy'] == 'RARORAC_Risk_Insensitive']['RARORAC'], name='Risk-Insensitive Pricing', xbins=dict(size=0.01), marker_color='#4C72B0', opacity=0.6, histnorm='probability density'))
    fig.add_trace(go.Histogram(x=melted_rarorac[melted_rarorac['Pricing Strategy'] == 'RARORAC_Risk_Sensitive']['RARORAC'], name='Risk-Sensitive Pricing', xbins=dict(size=0.01), marker_color='#DD8452', opacity=0.6, histnorm='probability density'))

    fig.add_vline(x=hurdle_rate, line_dash="dash", line_color="red", annotation_text=f"Hurdle Rate: {hurdle_rate:.2%}", annotation_position="top right")

    fig.update_layout(title_text='RARORAC Distribution', xaxis_title='RARORAC', yaxis_title='Density', barmode='overlay', legend_title='Pricing Strategy', font=dict(size=12), hovermode="x unified")

    st.plotly_chart(fig, use_container_width=True)

    st.subheader("Interest Rate vs. Principal")
    plot_df = simulation_results.dropna(subset=['RARORAC_Risk_Sensitive', 'Interest Rate_Risk_Sensitive'])

    fig_scatter = px.scatter(plot_df, x='Principal', y='Interest Rate_Risk_Sensitive', color='RARORAC_Risk_Sensitive', size_max=10, color_continuous_scale=px.colors.sequential.Hot, labels={'Principal': 'Principal Amount', 'Interest Rate_Risk_Sensitive': 'Interest Rate (Risk-Sensitive)', 'RARORAC_Risk_Sensitive': 'RARORAC (Sensitive)'}, title='Risk-Sensitive Interest Rate vs. Principal', hover_data={'Principal': ':.0f', 'Interest Rate_Risk_Sensitive': ':.2%', 'RARORAC_Risk_Sensitive': ':.2%'})

    fig_scatter.update_layout(font=dict(size=12))
    fig_scatter.update_xaxes(tickformat="$,.0f")
    fig_scatter.update_yaxes(tickformat=".1%")

    st.plotly_chart(fig_scatter, use_container_width=True)

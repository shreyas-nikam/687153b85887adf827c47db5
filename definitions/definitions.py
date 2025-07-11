import pandas as pd
import numpy as np

def generate_synthetic_transactions(num_transactions):
    """Generates a DataFrame of synthetic loan transactions."""

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
    """Computes the Expected Loss for a given transaction."""
    return principal * pd * lgd

def calculate_economic_capital(principal, pd, lgd, ul_factor):
                """Computes Economic Capital."""
                return principal * ul_factor

def calculate_net_risk_adjusted_reward(principal, interest_rate, tenor, funding_cost_rate, op_cost_ratio, expected_loss):
    """Computes the Net Risk Adjusted Reward."""

    total_income = principal * interest_rate * tenor
    total_funding_cost = principal * funding_cost_rate * tenor
    total_operating_cost = principal * op_cost_ratio
    net_risk_adjusted_reward = total_income - total_funding_cost - total_operating_cost - expected_loss
    return net_risk_adjusted_reward

def calculate_rarorac(net_risk_adjusted_reward, economic_capital):
    """Computes the RARORAC for a transaction."""
    if economic_capital == 0:
        raise ZeroDivisionError("Economic Capital cannot be zero")
    return net_risk_adjusted_reward / economic_capital

import pandas as pd
import numpy as np

def simulate_pricing_strategies(transactions_df):
    """Applies risk-insensitive and risk-sensitive pricing strategies."""

    if transactions_df.empty:
        return pd.DataFrame()

    df = transactions_df.copy()

    # Risk-Insensitive Pricing
    df['Interest Rate_Risk_Insensitive'] = df['Interest Rate']
    df['RARORAC_Risk_Insensitive'] = calculate_rarorac(df, 'Interest Rate_Risk_Insensitive')

    # Risk-Sensitive Pricing
    df['Interest Rate_Risk_Sensitive'] = df.apply(lambda row: adjust_interest_rate(row, hurdle_rate=0.1), axis=1)
    df['RARORAC_Risk_Sensitive'] = calculate_rarorac(df, 'Interest Rate_Risk_Sensitive')

    return df


def calculate_rarorac(df, interest_rate_column):
    """Calculates RARORAC."""
    df['Expected Loss'] = df['Principal'] * df['PD'] * df['LGD']
    df['Revenue'] = df['Principal'] * df[interest_rate_column] * df['Tenor']
    df['Operating Cost'] = df['Principal'] * df['Operational Cost Ratio'] * df['Tenor']
    df['Economic Capital'] = df['Principal'] * df['PD'] * df['LGD'] * 3  # Example: 3 times Expected Loss
    df['Net Risk Adjusted Return'] = df['Revenue'] - df['Expected Loss'] - df['Operating Cost'] - (df['Cost of Funds'] * df['Principal'] * df['Tenor'])
    df['RARORAC'] = df['Net Risk Adjusted Return'] / df['Economic Capital']
    df.loc[~np.isfinite(df['RARORAC']), 'RARORAC'] = np.nan  # Handle division by zero
    return df['RARORAC']

def adjust_interest_rate(row, hurdle_rate):
    """Adjusts interest rate to meet or exceed hurdle rate."""
    principal = row['Principal']
    pd = row['PD']
    lgd = row['LGD']
    tenor = row['Tenor']
    operational_cost_ratio = row['Operational Cost Ratio']
    cost_of_funds = row['Cost of Funds']

    expected_loss = principal * pd * lgd
    operating_cost = principal * operational_cost_ratio * tenor
    economic_capital = principal * pd * lgd * 3
    net_risk_adjusted_return = -expected_loss - operating_cost - (cost_of_funds * principal * tenor)
    
    min_interest_rate = 0.0  # Minimum possible interest rate
    max_interest_rate = 1.0  # Maximum possible interest rate
    
    interest_rate = row['Interest Rate'] #Initial value

    # Binary search for the interest rate that meets the hurdle rate
    for _ in range(100):  # Limit iterations to avoid infinite loops
        revenue = principal * interest_rate * tenor
        net_risk_adjusted_return = revenue - expected_loss - operating_cost - (cost_of_funds * principal * tenor)
        rarorac = net_risk_adjusted_return / economic_capital
        
        if economic_capital == 0:
           rarorac = np.nan
        
        if np.isnan(rarorac):
            return np.nan #If rarocac cannot be calculated, returns nan value

        if rarorac >= hurdle_rate:
            max_interest_rate = interest_rate
        else:
            min_interest_rate = interest_rate
        
        interest_rate = (min_interest_rate + max_interest_rate) / 2.0 #Adjust interest rate

    return interest_rate
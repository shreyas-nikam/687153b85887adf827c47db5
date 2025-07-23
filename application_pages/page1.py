import streamlit as st
import pandas as pd

def load_and_validate_data(filepath=None):
    """Loads and validates financial data.

    Args:
        filepath (str, optional): Path to the CSV file. If None, a synthetic dataset is used.

    Returns:
        pd.DataFrame: Loaded and validated financial data.

    Raises:
        FileNotFoundError: If the specified file does not exist.
        KeyError: If required columns are missing.
        ValueError: If duplicate dates are found.
    """
    if filepath is None:
        # Synthetic dataset as default
        data = {'Date': ['2024-01-01', '2024-01-02', '2024-01-03', '2024-01-04', '2024-01-05'],
                'Base_Revenue': [100, 110, 105, 115, 120],
                'Base_Costs': [50, 60, 55, 65, 70]}
        df = pd.DataFrame(data)
        df['Date'] = pd.to_datetime(df['Date'])
    else:
        try:
            df = pd.read_csv(filepath)
        except FileNotFoundError:
            raise FileNotFoundError("File not found at specified path.")
    
    required_columns = ['Date', 'Base_Revenue', 'Base_Costs']
    for col in required_columns:
        if col not in df.columns:
            raise KeyError(f"Required column '{col}' is missing.")

    if df['Date'].duplicated().any():
        raise ValueError("Duplicate dates found in the data.")
    
    df['Date'] = pd.to_datetime(df['Date']) # Ensure Date column is datetime
    return df

def run_page1():
    st.markdown(r"""
    # Data Loading & Selection
    
    ## Business Context
    
    The foundation of any robust stress testing framework begins with **high-quality, validated financial data**. 
    This page serves as the critical first step in our Risk Management Framework, where we establish the baseline 
    financial position that will be subjected to various stress scenarios.
    
    ### Why Data Quality Matters in Stress Testing
    
    According to the PRMIA Operational Risk Manager Handbook, stress testing effectiveness is directly dependent on:
    - **Data Accuracy**: Incorrect baseline data leads to unreliable stress test results
    - **Data Completeness**: Missing financial components can underestimate risk exposure
    - **Data Consistency**: Duplicate or inconsistent time series data can skew temporal analysis
    
    ### Key Financial Components Required
    
    Our stress testing framework requires three fundamental data elements:
    
    1. **Date**: Temporal reference for time-series analysis and trend identification
    2. **Base_Revenue**: The firm's revenue under normal, unstressed market conditions
    3. **Base_Costs**: The firm's operational costs under normal business circumstances

    These components form the foundation for calculating:
    - Net earnings under stress
    - Capital impact assessments
    - Liquidity position changes
    - Risk capacity metrics
    """)

    st.markdown("---")

    st.subheader("Data Source Configuration")

    data_source = st.radio(
        "Select your preferred data source:",
        options=["Synthetic Data", "Upload CSV"],
        help="Choose between pre-generated sample data for quick testing or upload your own financial dataset.",
        horizontal=True
    )

    if data_source == "Upload CSV":
        st.markdown("""
        ### Custom Data Upload

        Upload your financial dataset in CSV format. Ensure your file contains the following columns:
        - `Date`: Timeline for your financial data (YYYY-MM-DD format recommended)
        - `Base_Revenue`: Revenue figures under normal conditions
        - `Base_Costs`: Cost figures under normal conditions
        
        **Data Validation Checks:**
        - Required columns presence verification
        - Duplicate date detection
        - Data type validation
        """)
        
        uploaded_file = st.file_uploader(
            "Choose your CSV file", 
            type=["csv"], 
            help="Maximum file size: 200MB. Supported format: CSV with UTF-8 encoding."
        )
        
        if uploaded_file is not None:
            try:
                with st.spinner("Loading and validating your data..."):
                    base_data = load_and_validate_data(uploaded_file)
                    
                st.success("Data loaded and validated successfully!")
                
                # Display data summary
                col1, col2, col3 = st.columns(3)
                with col1:
                    st.metric("Total Records", len(base_data))
                with col2:
                    st.metric("Date Range", f"{base_data['Date'].min().strftime('%Y-%m-%d')} to {base_data['Date'].max().strftime('%Y-%m-%d')}")
                with col3:
                    st.metric("Avg Revenue", f"{base_data['Base_Revenue'].mean():.2f}")

                st.subheader("Data Preview")
                st.dataframe(base_data, use_container_width=True)
                
                # Store in session state
                st.session_state['base_data'] = base_data
                
                st.info("**Data Saved**: Your data has been stored for use in stress testing simulations.")
                
            except FileNotFoundError as e:
                st.error(f"File Error: {e}")
            except KeyError as e:
                st.error(f"Data Structure Error: {e}")
                st.markdown("""
                **Common Solutions:**
                - Ensure your CSV has columns named exactly: `Date`, `Base_Revenue`, `Base_Costs`
                - Check for typos in column headers
                - Verify CSV format and encoding (UTF-8 recommended)
                """)
            except ValueError as e:
                st.error(f"Data Quality Error: {e}")
                st.markdown("""
                **Resolution Steps:**
                - Remove duplicate date entries
                - Ensure dates are in a consistent format
                - Verify no missing values in critical columns
                """)
            except Exception as e:
                st.error(f"Unexpected Error: {e}")

    else:  # Synthetic Data
        st.markdown("""
        ### Synthetic Dataset
        
        Using our pre-generated synthetic financial dataset for immediate exploration. This dataset demonstrates:
        
        **Dataset Characteristics:**
        - **Time Period**: 5-day sample period (2024-01-01 to 2024-01-05)
        - **Revenue Range**: $100-$120 (simulating normal business variability)
        - **Cost Range**: $50-$70 (representing operational expenses)
        - **Purpose**: Ideal for understanding stress testing concepts without data preparation
        
        **Business Scenario Simulation:**
        This synthetic data represents a small financial institution or business unit with:
        - Moderate revenue volatility typical of normal market conditions
        - Proportional cost structure relative to revenue
        - Baseline profitability suitable for stress scenario analysis
        """)
        
        try:
            with st.spinner("Generating synthetic dataset..."):
                base_data = load_and_validate_data()
                
            st.success("Synthetic data generated successfully!")
            
            # Display enhanced data summary
            col1, col2, col3, col4 = st.columns(4)
            with col1:
                st.metric("Records", len(base_data))
            with col2:
                st.metric("Total Revenue", f"${base_data['Base_Revenue'].sum():,.0f}")
            with col3:
                st.metric("Total Costs", f"${base_data['Base_Costs'].sum():,.0f}")
            with col4:
                profit_margin = ((base_data['Base_Revenue'].sum() - base_data['Base_Costs'].sum()) / base_data['Base_Revenue'].sum()) * 100
                st.metric("Profit Margin", f"{profit_margin:.1f}%")
            
            st.subheader("Synthetic Data Overview")
            st.dataframe(base_data, use_container_width=True)
            
            # Store in session state
            st.session_state['base_data'] = base_data

            st.info("**Data Ready**: Proceed to the Stress Test Simulation page to apply various stress scenarios.")

        except Exception as e:
            st.error(f"Error generating synthetic data: {e}")

    st.markdown("""
    ---
    ### Next Steps

    Once your data is loaded and validated:
    1. **Navigate to Page 2**: Use the sidebar to access "Stress Test Simulation"
    2. **Select Stress Type**: Choose from Sensitivity, Scenario, or Firm-Wide testing
    3. **Configure Parameters**: Adjust stress factors based on your risk scenarios
    4. **Analyze Results**: View comprehensive visualizations and risk metrics on Page 3
    
    **Pro Tip**: Start with synthetic data to understand the framework, then upload your own data for real-world analysis.
    """)

if __name__ == "__main__":
    run_page1()

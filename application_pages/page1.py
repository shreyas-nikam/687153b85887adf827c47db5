import streamlit as st
import pandas as pd

def load_and_validate_data(uploaded_file):
    """
    Loads and validates financial data from an uploaded file or returns synthetic data.

    Args:
        uploaded_file: Uploaded file object from Streamlit (or None for synthetic).

    Returns:
        df: Validated DataFrame
    Raises:
        FileNotFoundError, KeyError, ValueError as appropriate.
    """
    if uploaded_file is None:
        data = {
            'Date': ['2024-01-01', '2024-01-02', '2024-01-03', '2024-01-04', '2024-01-05'],
            'Base_Revenue': [100, 110, 105, 115, 120],
            'Base_Costs': [50, 60, 55, 65, 70]
        }
        df = pd.DataFrame(data)
    else:
        try:
            df = pd.read_csv(uploaded_file)
        except Exception:
            raise FileNotFoundError("Failed to load file. Please check file format.")

    required_cols = ['Date', 'Base_Revenue', 'Base_Costs']
    for col in required_cols:
        if col not in df.columns:
            raise KeyError(f"Required column '{{col}}' is missing from your data.")
    if df['Date'].duplicated().any():
        raise ValueError("Duplicate dates found in your data.")
    df['Date'] = pd.to_datetime(df['Date'])
    return df

def run_page1():
    st.markdown(r"""
    ### 1. Data Loading and Validation

    This page allows you to load your financial data for stress testing. You may use our **synthetic demo data** or upload your own CSV file. 
    Your uploaded file must have at least the following columns: `Date`, `Base_Revenue`, `Base_Costs`.

    *Example row:*

    | Date       | Base_Revenue | Base_Costs |
    |------------|--------------|------------|
    | 2024-01-01 |   100        |    50      |

    All columns are required. Date must be unique per row.
    """)
    st.sidebar.markdown("#### Data Source Selection")
    use_synthetic = st.sidebar.radio(
        "Select the data source for the stress test analysis.",
        options=["Use demo data", "Upload CSV"],
        index=0
    )

    uploaded_file = None
    if use_synthetic == "Upload CSV":
        uploaded_file = st.sidebar.file_uploader(
            "Upload a CSV file containing `Date`, `Base_Revenue`, and `Base_Costs` columns.",
            type="csv",
            help="Your file must include 'Date', 'Base_Revenue', and 'Base_Costs' columns. Dates must be unique."
        )

    base_data = None
    err = None
    with st.spinner("Loading data..."):
        try:
            base_data = load_and_validate_data(uploaded_file if use_synthetic=="Upload CSV" else None)
            st.success("Data loaded successfully.")
        except (FileNotFoundError, KeyError, ValueError) as e:
            err = str(e)
    if err:
        st.error(err)
        st.stop()

    st.markdown("#### Data Preview")
    st.dataframe(base_data)

    st.markdown(r"""
    **Business Logic:**
    - Accurate, validated data is required for reliable stress scenario analysis.
    - Uploaded data must be *free from duplicates* and contain the mandatory columns.
    - All subsequent analysis will use this data as the baseline.
    """)
    
    # Save to session state for use in other pages
    st.session_state['base_data'] = base_data

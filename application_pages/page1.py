
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
    st.header("Data Loading & Selection")
    st.markdown("In this page, you can load your financial data for stress test analysis.")

    data_source = st.radio(
        "Select Data Source:",
        options=["Synthetic Data", "Upload CSV"],
        help="Select the data source for the stress test analysis."
    )

    if data_source == "Upload CSV":
        uploaded_file = st.file_uploader("Upload a CSV file", type=["csv"], help="Upload a CSV file containing 'Date', 'Base_Revenue', and 'Base_Costs' columns.")
        if uploaded_file is not None:
            try:
                base_data = load_and_validate_data(uploaded_file)
                st.dataframe(base_data)
                st.session_state['base_data'] = base_data
            except FileNotFoundError as e:
                st.error(f"Error: {e}")
            except KeyError as e:
                st.error(f"Error: {e}")
            except ValueError as e:
                st.error(f"Error: {e}")
            except Exception as e:
                st.error(f"An unexpected error occurred: {e}")
    else:
        try:
            base_data = load_and_validate_data()
            st.dataframe(base_data)
            st.session_state['base_data'] = base_data
        except Exception as e:
            st.error(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    run_page1()

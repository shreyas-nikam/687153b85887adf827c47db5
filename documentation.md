id: 687153b85887adf827c47db5_documentation
summary: Risk Management Framework Lab 1 Documentation
feedback link: https://docs.google.com/forms/d/e/1FAIpQLSfWkOK-in_bMMoHSZfcIvAeO58PAH9wrDqcxnJABHaxiDqhSA/viewform?usp=sf_link
environments: Web
status: Published
# QuLab: Stress Test Scenario Visualization and Risk Management

## 1. Introduction to QuLab and Risk Management Framework
Duration: 00:05

Welcome to the QuLab codelab! In this lab, we will embark on an exciting journey to explore the **Risk Management Framework** through the lens of stress test scenario visualization. This application, **QuLab**, serves as an interactive platform designed to demystify and visualize the potential impact of various stress test scenarios on a firm's financial health.

For developers, understanding this application provides crucial insights into:
*   **Streamlit Application Development:** How to structure a multi-page Streamlit application, manage session state, and build interactive UIs.
*   **Financial Risk Management Concepts:** Gain practical understanding of stress testing methodologies (Sensitivity, Scenario, Firm-Wide).
*   **Data Handling and Validation:** Learn how to load, validate, and persist data across different parts of a web application.
*   **Data Visualization with Plotly:** Effectively present complex financial data trends and relationships.

The primary objective of QuLab is to enhance comprehension of how **correlated threats** can simultaneously affect multiple portfolios and processes within a financial institution. By simulating and visualizing the outcomes of different stress test types, we aim to:
*   Facilitate an understanding of the relationship between economic and market parameters and their ripple effects on financial metrics.
*   Clearly present estimated impacts on crucial financial components such as income, costs, market risk losses, counterparty losses, credit losses, liquidity, provisions, reserves, and operational losses.
*   Offer interactive visualizations that illustrate financial trajectories under stress, correlations between impact metrics, and aggregated comparisons of losses.

<aside class="positive">
<b>Stress testing</b> is a vital tool for financial institutions to assess their resilience to adverse economic conditions. It helps identify potential vulnerabilities and ensures adequate capital and liquidity buffers are maintained.
</aside>

### Application Architecture Overview

QuLab is structured as a multi-page Streamlit application, promoting modularity and maintainability. The core components and their interactions are depicted below:

```mermaid
graph TD
    A[app.py: Main Application Entry Point] --> B{Navigation Sidebar};
    B --> C[Page 1: Data Loading & Selection (page1.py)];
    B --> D[Page 2: Stress Test Simulation (page2.py)];
    B --> E[Page 3: Visualizations (page3.py)];

    C -- "Saves base_data to session_state" --> D;
    D -- "Loads base_data, saves stressed_data to session_state" --> E;
    E -- "Loads stressed_data, performs calculations & generates visualizations" --> F[User Interface];

    subgraph Data Flow
        F_a[Financial Data (CSV / Synthetic)] --> C;
        D --> F_b[Stressed Data Display];
        E --> F_c[Metrics & Visualizations Display];
    end
```

This flow ensures a clear progression: data is loaded, then processed under stress, and finally visualized. The `st.session_state` mechanism is critical for passing data between these distinct application pages.

## 2. Setting Up the Environment and Running the Application
Duration: 00:10

Before we dive into the code, let's set up your development environment.

### Prerequisites
*   **Python 3.8+**: Ensure you have a compatible Python version installed.
*   **pip**: Python's package installer, usually comes with Python.

### Step-by-Step Setup

1.  **Create Project Directories and Files**:
    Create a project directory named `QuLab_Codelab` and inside it, create the following files and directories:
    ```
    QuLab_Codelab/
    ├── app.py
    ├── requirements.txt
    └── application_pages/
        ├── __init__.py
        ├── page1.py
        ├── page2.py
        └── page3.py
    ```
    Place the provided code into their respective files.

2.  **Create `requirements.txt`**:
    This file lists all the necessary Python packages.
    ```
    streamlit
    pandas
    plotly
    ```

3.  **Create a Virtual Environment**:
    It's a best practice to use a virtual environment to manage dependencies for your project.
    Open your terminal or command prompt, navigate to the `QuLab_Codelab` directory, and run:

    ```bash
    python -m venv venv
    ```

4.  **Activate the Virtual Environment**:
    *   **On Windows:**
        ```bash
        .\venv\Scripts\activate
        ```
    *   **On macOS/Linux:**
        ```bash
        source venv/bin/activate
        ```

5.  **Install Dependencies**:
    With your virtual environment activated, install the required packages using pip:

    ```bash
    pip install -r requirements.txt
    ```

6.  **Run the Streamlit Application**:
    Once all dependencies are installed, you can launch the application:

    ```bash
    streamlit run app.py
    ```
    This command will open the QuLab application in your web browser, typically at `http://localhost:8501`.

## 3. Data Loading & Selection (Page 1)
Duration: 00:15

This is the first interaction point for users, where they provide the foundational financial data for stress testing.

### `app.py` integration for Page 1

Let's look at how `app.py` handles navigation to `page1.py`:

```python
# app.py relevant snippet
# Your code starts here
page = st.sidebar.selectbox(label="Navigation", options=["Data Loading & Selection", "Stress Test Simulation", "Visualizations"])
if page == "Data Loading & Selection":
    from application_pages.page1 import run_page1
    run_page1()
# Your code ends
```
When "Data Loading & Selection" is chosen from the sidebar, the `run_page1()` function from `application_pages/page1.py` is executed.

### `application_pages/page1.py` Breakdown

This file contains the logic for loading and validating the base financial data.

#### `load_and_validate_data` Function

```python
# application_pages/page1.py
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
```
This function is crucial for data integrity. It handles:
*   **Synthetic Data Generation**: If no filepath is provided, it creates a small default dataset with `Date`, `Base_Revenue`, and `Base_Costs`. This is great for quick demonstrations.
*   **CSV Upload**: If a `filepath` (from `st.file_uploader`) is provided, it attempts to read the CSV.
*   **Validation Checks**:
    *   **Required Columns**: Ensures 'Date', 'Base_Revenue', and 'Base_Costs' are present.
    *   **Duplicate Dates**: Prevents issues from non-unique time series data.
*   **Date Conversion**: Guarantees the 'Date' column is in datetime format, essential for time-series analysis and plotting.

#### `run_page1` Function

```python
# application_pages/page1.py
# (continued from above)

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
    else: # Synthetic Data
        try:
            base_data = load_and_validate_data()
            st.dataframe(base_data)
            st.session_state['base_data'] = base_data
        except Exception as e:
            st.error(f"An unexpected error occurred: {e}")
```

This function sets up the Streamlit UI for the first page:
*   **Data Source Selection**: Uses `st.radio` to let users choose between `Synthetic Data` or `Upload CSV`.
*   **File Uploader**: If `Upload CSV` is selected, `st.file_uploader` appears.
*   **Data Loading and Display**: Calls `load_and_validate_data` and displays the resulting DataFrame using `st.dataframe`.
*   **Error Handling**: Robust `try-except` blocks catch specific data validation errors (`FileNotFoundError`, `KeyError`, `ValueError`) and general unexpected errors, providing user-friendly messages.
*   **Session State**: Most importantly, `st.session_state['base_data'] = base_data` saves the loaded DataFrame. This makes `base_data` accessible to other pages (like Page 2 and Page 3) without having to reload it.

<aside class="positive">
Using `st.session_state` is critical for multi-page Streamlit applications. It allows data to persist across reruns and be shared between different components or pages, providing a seamless user experience.
</aside>

## 4. Stress Test Simulation (Page 2)
Duration: 00:20

This page is where the magic of stress testing happens. Based on the `base_data` loaded, users can apply different stress methodologies.

### `app.py` integration for Page 2

```python
# app.py relevant snippet
elif page == "Stress Test Simulation":
    from application_pages.page2 import run_page2
    run_page2()
```
When "Stress Test Simulation" is chosen, `run_page2()` is executed.

### `application_pages/page2.py` Breakdown

This file contains the core logic for simulating stress impacts.

#### `simulate_stress_impact` Function

```python
# application_pages/page2.py
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
        # Apply the shock: parameter_value * (1 - shock_magnitude/100)
        stressed_data[f'Adjusted_{parameter_to_shock.replace("Base_", "")}'] = stressed_data[parameter_to_shock] * (1 - shock_magnitude/100)
    elif stress_type == 'Scenario':
        scenario_severity_factor = parameters.get('scenario_severity_factor')
        # Apply scenario factor to all 'Base' columns
        for col in stressed_data.columns:
            if 'Base' in col:
                stressed_data[col.replace('Base', 'Adjusted')] = stressed_data[col] * (1 - scenario_severity_factor)
    elif stress_type == 'Firm-Wide':
        systemic_crisis_scale = parameters.get('systemic_crisis_scale')
        # Apply systemic crisis scale to all 'Base' columns
        for col in stressed_data.columns:
            if 'Base' in col:
                stressed_data[col.replace('Base', 'Adjusted')] = stressed_data[col] * (1 - systemic_crisis_scale)
    else:
        raise Exception("Invalid stress type.")

    return stressed_data
```

This function implements the core stress test logic, taking `base_data`, `stress_type`, and `parameters` to generate `stressed_data`.

#### Stress Test Types Explained:

1.  **Sensitivity Test**:
    *   **Concept**: Isolates and shocks a single financial parameter (e.g., revenue, costs) to see its individual impact. This helps understand the sensitivity of the firm's finances to specific variables.
    *   **Implementation**: A `parameter_to_shock` (e.g., `Base_Revenue`) is selected, and a `shock_magnitude` (percentage reduction) is applied.
    *   **Formula**:
        $$ \text{Adjusted Parameter} = \text{Base Parameter} \times \left(1 - \frac{\text{Shock Magnitude}}{100}\right) $$
    *   A new column like `Adjusted_Revenue` or `Adjusted_Costs` is created.

2.  **Scenario Test**:
    *   **Concept**: Simulates the impact of a predefined economic or market scenario (e.g., a mild recession, interest rate hike). This involves applying a broad impact factor across multiple relevant financial components.
    *   **Implementation**: A `scenario_severity_factor` (between 0.0 and 1.0) is applied to all columns containing 'Base' in their name.
    *   **Formula**:
        $$ \text{Adjusted Base Column} = \text{Base Column} \times (1 - \text{Scenario Severity Factor}) $$

3.  **Firm-Wide Test**:
    *   **Concept**: Represents a severe, systemic crisis affecting the entire financial system. This typically involves a more drastic, aggregated shock across all major financial components, simulating a highly adverse market condition.
    *   **Implementation**: A `systemic_crisis_scale` (between 0.0 and 1.0) is applied similarly to the scenario test, often representing a deeper, more widespread impact.
    *   **Formula**:
        $$ \text{Adjusted Base Column} = \text{Base Column} \times (1 - \text{Systemic Crisis Scale}) $$

<aside class="negative">
It is crucial to ensure that the parameters passed to `simulate_stress_impact` match the selected `stress_type`. Missing or incorrect parameters can lead to `KeyError` or unexpected behavior.
</aside>

#### `run_page2` Function

```python
# application_pages/page2.py
# (continued from above)

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
```

Key features of this UI:
*   **Data Dependency**: It first checks `st.session_state` for `base_data`. If not found, it prompts the user to load data first.
*   **Stress Type Selection**: `st.sidebar.selectbox` allows users to pick one of the three stress test types.
*   **Dynamic Parameter Inputs**: Based on the chosen `stress_type`, relevant sliders (`st.sidebar.slider`) and select boxes (`st.sidebar.selectbox`) appear in the sidebar for users to adjust parameters. This provides a highly interactive experience.
*   **Simulation Execution**: The `simulate_stress_impact` function is called with the current parameters.
*   **Display Stressed Data**: The resulting `stressed_data` DataFrame is displayed using `st.dataframe`.
*   **Session State Update**: `st.session_state['stressed_data'] = stressed_data` saves the output, making it available for the Visualization page.
*   **Error Handling**: Catches specific `KeyError` from `simulate_stress_impact` (e.g., if a shock parameter is invalid) and general exceptions.

## 5. Visualizing Stress Test Results (Page 3)
Duration: 00:25

This is where the impact of stress scenarios becomes evident through computed metrics and interactive visualizations.

### `app.py` integration for Page 3

```python
# app.py relevant snippet
elif page == "Visualizations":
    from application_pages.page3 import run_page3
    run_page3()
```
When "Visualizations" is chosen, `run_page3()` is executed.

### `application_pages/page3.py` Breakdown

This file focuses on calculating risk metrics and generating plots.

#### `calculate_risk_capacity_metrics` Function

```python
# application_pages/page3.py
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
```

This function performs calculations based on the `stressed_data` to derive key risk capacity metrics. Note that some calculations (like `Capital_Impact` and `Liquidity_Impact`) are simplified for demonstration.

#### Key Metric Derivations:

*   **Net Earnings Under Stress**:
    $$ \text{Net Earnings} = \text{Adjusted Revenue} - \text{Adjusted Costs} $$
*   **Capital Impact**:
    This is the change in capital due to the stress, reflecting lost revenue and increased costs.
    $$ \text{Capital Impact} = (\text{Base Revenue} - \text{Adjusted Revenue}) + (\text{Adjusted Costs} - \text{Base Costs}) $$
*   **Capital Remaining**:
    This tracks the firm's capital position over time, assuming a starting capital. `cumsum()` is used to accumulate impact over time.
    $$ \text{Capital Remaining}_t = \text{Initial Capital} - \sum_{i=1}^{t} \text{Capital Impact}_i $$
*   **Liquidity Impact**:
    A simplified impact on liquidity, often tied to revenue changes.
    $$ \text{Liquidity Impact} = (\text{Base Revenue} - \text{Adjusted Revenue}) \times 0.5 $$
*   **Liquidity Position**:
    Similar to capital, this tracks the liquidity over time.
    $$ \text{Liquidity Position}_t = \text{Initial Liquidity} - \sum_{i=1}^{t} \text{Liquidity Impact}_i $$
*   **Capital Drawdown**:
    The maximum reduction in capital from its initial value.
    $$ \text{Capital Drawdown} = \text{Initial Capital} - \text{Minimum Capital Remaining} $$
*   **Capital Drawdown Percentage**:
    $$ \text{Capital Drawdown Percentage} = \left(\frac{\text{Capital Drawdown}}{\text{Initial Capital}}\right) \times 100 $$
*   **Liquidity Shortfall**:
    Indicates if the liquidity position falls below zero, representing the deficit.
    $$ \text{Liquidity Shortfall} = \max(0, -\text{Minimum Liquidity Position}) $$

#### `generate_visualizations` Function

```python
# application_pages/page3.py
# (continued from above)

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
        data['Date'] = range(len(data)) # Fallback if 'Date' is somehow missing

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
        # Generates scatter plots for all pairs of numeric columns
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
```

This function leverages `plotly.express` to create various interactive charts:

*   **Trend Plots (`px.line`)**: Shows how key financial metrics (base and adjusted) evolve over time. This is critical for observing the trajectory under stress.
*   **Relationship Plots (`px.scatter`)**: Visualizes the correlation between different numeric columns. Useful for identifying how one metric changes in relation to another.
*   **Comparison Plots (`px.bar`)**: Allows users to select two specific columns and compare their values over time using a bar chart, ideal for direct comparisons of stressed vs. non-stressed metrics.

<aside class="positive">
Plotly Express makes it incredibly easy to generate complex, interactive visualizations with minimal code, greatly enhancing the user's ability to explore data.
</aside>

#### `run_page3` Function

```python
# application_pages/page3.py
# (continued from above)

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
```

This function orchestrates the display of results:
*   **Data Dependency**: It checks `st.session_state` for `stressed_data`, ensuring the simulation has been run.
*   **Metric Display**: It calls `calculate_risk_capacity_metrics` and then displays each metric using `st.metric`, which is excellent for showing key performance indicators.
*   **Plot Type Selection**: `st.selectbox` allows users to choose the type of visualization they want.
*   **Dynamic Column Selection**: For 'comparison' plots, additional `st.selectbox` widgets appear, letting users choose which columns to compare dynamically.
*   **Visualization Generation**: Calls `generate_visualizations` to render the selected plot.
*   **Error Handling**: Catches general exceptions that might occur during metric calculation or visualization.

## 6. Understanding the Code Structure and Best Practices
Duration: 00:10

Now that we've explored each page's functionality, let's reflect on the overall architecture and best practices demonstrated in QuLab.

### Modular Design (`application_pages` folder)

The application adheres to a modular design by separating concerns into distinct Python files within the `application_pages` directory.
*   `app.py`: Acts as the orchestrator, handling overall page layout, navigation, and loading of sub-modules. It's concise and easy to understand the application flow.
*   `page1.py`, `page2.py`, `page3.py`: Each file encapsulates the UI and business logic for a specific section of the application (data loading, simulation, visualization). This makes the code base more manageable, readable, and easier to debug or extend.

```console
QuLab_Codelab/
├── app.py                  # Main application
├── requirements.txt        # Python dependencies
└── application_pages/
    ├── __init__.py         # Makes 'application_pages' a Python package
    ├── page1.py            # Data loading logic
    ├── page2.py            # Stress simulation logic
    └── page3.py            # Visualization logic
```

### `st.session_state` for Inter-Page Communication

The consistent use of `st.session_state` is a cornerstone of this application's functionality.
*   `st.session_state['base_data']`: Stores the initially loaded data, making it available for the stress simulation page.
*   `st.session_state['stressed_data']`: Stores the results of the stress simulation, making it available for the visualization page.

This pattern avoids re-running expensive computations or re-uploading files when navigating between pages, improving performance and user experience.

### Robust Error Handling

Each page includes `try-except` blocks to gracefully handle potential errors, such as:
*   `FileNotFoundError`, `KeyError`, `ValueError` during data loading/validation.
*   `KeyError` if expected columns or parameters are missing during simulation.
*   General `Exception` catches for unexpected issues.

This prevents the application from crashing and provides informative messages to the user.

### Streamlit UI Best Practices

*   `st.set_page_config(layout="wide")`: Utilizes the full width of the browser, which is excellent for displaying large DataFrames and multiple plots.
*   `st.sidebar`: Organizes navigation and interactive controls (sliders, select boxes), keeping the main content area clean.
*   `st.markdown`, `st.header`, `st.subheader`: Structured text elements for clear information presentation.
*   `st.dataframe`, `st.metric`, `st.plotly_chart`: Effective widgets for displaying tabular data, key metrics, and interactive plots.
*   `help` arguments in widgets: Provides useful tooltips to guide users.

### Potential Improvements and Extensions

*   **More Sophisticated Models**: Integrate more complex financial models for capital, liquidity, and risk calculations instead of simplified derivations.
*   **Additional Stress Factors**: Allow users to input economic variables (e.g., GDP growth, unemployment rate, interest rates) and map them to financial impacts using predefined relationships.
*   **Scenario Library**: Enable saving and loading custom scenarios.
*   **User Authentication**: For a production environment, implement user login and data security.
*   **Export Options**: Allow users to download the stressed data or visualizations.
*   **Real-time Data Integration**: Connect to APIs for live market data.

## 7. Conclusion and Next Steps
Duration: 00:05

Congratulations! You have successfully explored the QuLab application, understanding its functionalities for stress test scenario visualization within a Risk Management Framework. You've gained insights into:

*   The importance of stress testing in financial institutions.
*   The three main types of stress tests: Sensitivity, Scenario, and Firm-Wide.
*   How to build a modular Streamlit application.
*   Effective data handling, validation, and persistence across pages using `st.session_state`.
*   Generating interactive data visualizations with Plotly.

This codelab provides a solid foundation for further exploration into financial risk analytics and Streamlit development.

### Next Steps

*   **Experiment with the Application**: Play around with different data inputs and stress parameters to observe their effects on the results and visualizations.
*   **Modify Existing Logic**: Try changing the calculation logic for `Capital_Impact` or `Liquidity_Impact` in `page3.py` to reflect more realistic financial models.
*   **Add New Features**: Implement one of the "Potential Improvements" suggested in the previous step. For example, add a new type of stress test, or enable users to upload more complex data with additional financial metrics.
*   **Explore Streamlit Documentation**: Dive deeper into the Streamlit documentation to discover more widgets and functionalities.
*   **Deployment**: Consider deploying your modified QuLab application to a cloud platform (e.g., Streamlit Community Cloud, Heroku, AWS) to share it with others.

<button>
  [Streamlit Documentation](https://docs.streamlit.io/)
</button>

<button>
  [Plotly Express Documentation](https://plotly.com/python/plotly-express/)
</button>

Thank you for completing this codelab. We hope it empowers you to build more insightful and powerful data applications!

id: 687153b85887adf827c47db5_documentation
summary: Risk Management Framework Lab 1 Documentation
feedback link: https://docs.google.com/forms/d/e/1FAIpQLSfWkOK-in_bMMoHSZfcIvAeO58PAH9wrDqcxnJABHaxiDqhSA/viewform?usp=sf_link
environments: Web
status: Published
# Build a Risk Culture & Accountability Dashboard with Streamlit

## Introduction and Setup
Duration: 0:10:00

Welcome to the QuLab: Risk Culture & Accountability Dashboard codelab! In this lab, you will explore a interactive Streamlit application designed to simulate and visualize the dynamics of **Risk Culture & Accountability** within an organization.

Understanding and fostering a strong risk culture is paramount for any organization's long-term sustainability and resilience. It goes beyond simple compliance and involves the shared attitudes, values, and behaviors that shape decision-making regarding risk. This application provides a tangible way to see how key factors like leadership actions, supervisory practices, incentive structures, and accountability clarity can influence core risk culture indicators such as the willingness of employees to report issues and the effectiveness of problem resolution.

By the end of this codelab, you will understand:
*   The structure of this multi-page Streamlit application.
*   How synthetic data is generated and simulated based on user inputs.
*   The role of various organizational levers (Leadership, Supervision, Incentives, Accountability) in shaping risk culture.
*   How to visualize trends and relationships in risk culture data.
*   How basic business logic can translate simulated outcomes into actionable recommendations.

The application is built using Python and the Streamlit framework for rapid web application development. It leverages libraries like pandas for data manipulation, numpy for numerical operations, and plotly for interactive visualizations.

**Technology Stack:**
*   Python
*   Streamlit
*   pandas
*   numpy
*   plotly

To follow along, you need to have Python installed (version 3.7 or higher recommended). You'll also need to install the required libraries:

```console
pip install streamlit pandas numpy plotly
```

The application code is split into several files:
*   `app.py`: The main entry point that sets up the page configuration, displays the initial introduction, and handles sidebar navigation.
*   `application_pages/page1.py`: Contains the logic for the "Simulation and Visualizations" page, including data generation, simulation, plotting, and recommendations.
*   `application_pages/page2.py`: Contains the logic for the "Raw Data Overview" page, displaying the underlying data.
*   `application_pages/page3.py`: Contains the content for the "About This Lab" page, explaining the concepts and simulation details.

Create the necessary directory structure (`application_pages`) and save the following code into the respective files:

`app.py`
```python
import streamlit as st
st.set_page_config(page_title="QuLab", layout="wide")
st.sidebar.image("https://www.quantuniversity.com/assets/img/logo5.jpg")
st.sidebar.divider()
st.title("QuLab: Risk Culture & Accountability Dashboard")
st.divider()
st.markdown("""
In this lab, we explore the intricate dynamics of **Risk Culture & Accountability** within an organization. This interactive dashboard simulates and visualizes how critical factors like leadership consistency, supervisory practices, and incentive structures influence an organization's risk culture indicators.

### Purpose and Objectives:
*   To enable users to understand key insights from the "Risk Culture" concept, drawing from the PRMIA Operational Risk Manager Handbook.
*   To facilitate understanding of the critical roles of leadership and supervisors in fostering a robust risk culture.
*   To analyze how different cultural interventions (e.g., reward systems, accountability frameworks) quantitatively influence organizational behavior and key risk culture indicators.
*   To identify simulated areas for improvement in an organization's risk culture and generate concrete recommendations.

Use the sidebar to navigate through the different sections of this application and interact with the simulation parameters.
""")
# Your code starts here
page = st.sidebar.selectbox(label="Navigation", options=["Simulation and Visualizations", "Raw Data Overview", "About This Lab"])
if page == "Simulation and Visualizations":
    from application_pages.page1 import run_page1
    run_page1()
elif page == "Raw Data Overview":
    from application_pages.page2 import run_page2
    run_page2()
elif page == "About This Lab":
    from application_pages.page3 import run_page3
    run_page3()
# Your code ends
```

`application_pages/page1.py`
```python
import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px

@st.cache_data
def generate_synthetic_data(num_records, start_date, random_seed):
    """Generates a synthetic dataset for risk culture metrics."""
    if not isinstance(num_records, int):
        raise TypeError("num_records must be an integer")
    try:
        start_date = pd.to_datetime(start_date)
    except ValueError:
        raise ValueError("Invalid start_date format. Must be parseable by pd.to_datetime.")
    except TypeError:
        raise TypeError("start_date must be a string or datetime object")
    np.random.seed(random_seed)
    dates = pd.date_range(start=start_date, periods=num_records, freq='D')
    data = {'Date': dates,
            'LeadershipConsistency': np.random.uniform(50, 70, num_records), # Placeholder for a metric
            'SupervisorTrainingAdherence': np.random.uniform(60, 80, num_records), # Placeholder
            'SelfRaisedIssues': np.random.uniform(0.3, 0.6, num_records), # Proportion
            'RootCauseFixes': np.random.uniform(0.4, 0.7, num_records), # Proportion
            'SuperficialFixes': np.random.uniform(0.2, 0.5, num_records), # Proportion
            'EmployeePerceptionFairness': np.random.uniform(5, 8, num_records), # Scale 1-10
            'WillingnessToReportIssues': np.random.uniform(5, 8, num_records) # Scale 1-10
           }
    df = pd.DataFrame(data)
    return df

def simulate_risk_culture_indicators(df_base, lc_input, sta_input, pr_input, ia_input, ac_input):
    """Simulates the impact of factors on risk culture indicators."""
    df = df_base.copy()
    # Leadership Consistency
    df['LeadershipConsistency'] = df['LeadershipConsistency'] + (lc_input - 50) * 0.1
    # Supervisor Training Adherence
    df['SupervisorTrainingAdherence'] = df['SupervisorTrainingAdherence'] + (sta_input - 50) * 0.1
    # Punishment Regime
    if pr_input == 'Strict':
        df['WillingnessToReportIssues'] = df['WillingnessToReportIssues'] * 0.8
    elif pr_input == 'Lenient':
        df['WillingnessToReportIssues'] = df['WillingnessToReportIssues'] * 1.2
    # Incentive Alignment
    if ia_input == 'Results-focused':
        df['SelfRaisedIssues'] = df['SelfRaisedIssues'] * 0.8
    elif ia_input == 'Risk-aware':
        df['SelfRaisedIssues'] = df['SelfRaisedIssues'] * 1.2
    # Accountability Clarity
    if ac_input == 'Vague':
        df['RootCauseFixes'] = df['RootCauseFixes'] * 0.8
    elif ac_input == 'Transparent':
        df['RootCauseFixes'] = df['RootCauseFixes'] * 1.2

    df['LeadershipConsistency'] = df['LeadershipConsistency'].clip(0, 100)
    df['SupervisorTrainingAdherence'] = df['SupervisorTrainingAdherence'].clip(0, 100)
    df['SelfRaisedIssues'] = df['SelfRaisedIssues'].clip(0, 1)
    df['RootCauseFixes'] = df['RootCauseFixes'].clip(0, 1)
    df['SuperficialFixes'] = df['SuperficialFixes'].clip(0, 1)
    df['EmployeePerceptionFairness'] = df['EmployeePerceptionFairness'].clip(0, 10)
    df['WillingnessToReportIssues'] = df['WillingnessToReportIssues'].clip(0, 10)
    return df

def generate_recommendations(simulated_data, user_inputs):
    """Generates actionable recommendations based on simulated data and user inputs."""
    recommendations = []
    sim_row = {}
    sim_row['SimulatedSelfRaisedIssues'] = simulated_data['SelfRaisedIssues'].mean()
    sim_row['SuperficialFixes'] = simulated_data['SuperficialFixes'].mean()
    sim_row['EmployeePerceptionFairness'] = simulated_data['EmployeePerceptionFairness'].mean()
    sim_row['WillingnessToReportIssues'] = simulated_data['WillingnessToReportIssues'].mean()

    # Business logic
    if sim_row['SimulatedSelfRaisedIssues'] > 0.7 and sim_row['SuperficialFixes'] < 0.3 and sim_row['EmployeePerceptionFairness'] < 4:
        recommendations.append("Review the fairness and transparency of the punishment regime and align incentives more holistically.")
    elif sim_row['SimulatedSelfRaisedIssues'] > 0.7 and sim_row['SuperficialFixes'] < 0.3 and sim_row['WillingnessToReportIssues'] < 4:
        recommendations.append("Enhance leadership consistency in communicating risk values and promote a no-blame culture for self-reported errors (first-time mistakes).")
    elif sim_row['SimulatedSelfRaisedIssues'] < 0.3 and sim_row['SuperficialFixes'] > 0.7:
        recommendations.append("Focus on supervisor training for root cause analysis and reinforce accountability for thorough investigations.")
    elif sim_row['SimulatedSelfRaisedIssues'] > 0.8 and sim_row['SuperficialFixes'] < 0.2 and sim_row['EmployeePerceptionFairness'] > 8 and sim_row['WillingnessToReportIssues'] > 8:
        recommendations.append("Maintain current leadership, supervisory, and incentive strategies to sustain a strong risk culture.")

    if not recommendations:
        recommendations.append("Keep monitoring key metrics while exploring incremental improvements in communication, reward systems, and accountability frameworks.")
    return recommendations


def run_page1():
    st.header("Simulation and Visualizations")

    # Input widgets
    lc_input = st.sidebar.slider("Leadership Consistency ($LC_{input}$):", 0, 100, 50, help="Represents the degree to which leadership actions and communications are consistent with risk management values. Higher consistency is expected to improve employee perception of fairness and willingness to report issues.")
    sta_input = st.sidebar.slider("Supervisor Training Adherence ($STA_{input}$):", 0, 100, 50, help="Reflects the extent to which supervisors adhere to established training protocols and best practices. Higher adherence is expected to improve root cause fixes and reduce superficial fixes.")
    pr_input = st.sidebar.selectbox("Fairness of Punishment Regime ($PR_{input}$):", ['Strict', 'Balanced', 'Lenient'], index=1, help="Influences employees' willingness to report issues. A 'Strict' regime might discourage reporting, while a 'Lenient' regime could encourage it.")
    ia_input = st.sidebar.selectbox("Incentive Alignment ($IA_{input}$):", ['Results-focused', 'Balanced', 'Risk-aware'], index=1, help="Affects the focus on self-raised issues versus hiding problems. A 'Results-focused' incentive might discourage self-reporting, whereas a 'Risk-aware' incentive could promote it.")
    ac_input = st.sidebar.selectbox("Accountability Clarity ($AC_{input}$):", ['Vague', 'Clear', 'Transparent'], index=1, help="Impacts the effectiveness of root cause fixes. 'Vague' accountability may lead to superficial fixes, while 'Transparent' accountability fosters thorough investigations.")

    # Data Generation
    num_records = 100
    start_date = '2023-01-01'
    random_seed = 42
    base_data = generate_synthetic_data(num_records, start_date, random_seed)

    st.latex(r'NewValue = OldValue + (Input - 50) \cdot 0.1')

    # Simulation
    simulated_data = simulate_risk_culture_indicators(base_data, lc_input, sta_input, pr_input, ia_input, ac_input)

    # Visualizations
    st.subheader("Trend Plot: Quantum of Self-Raised Issues")
    fig_trend = px.line(simulated_data, x='Date', y='SelfRaisedIssues', title="Trend of Self-Raised Issues")
    st.plotly_chart(fig_trend, use_container_width=True)

    st.subheader("Aggregated Comparison: Root Cause Fixes vs. Superficial Fixes")
    avg_root_cause_fixes = simulated_data['RootCauseFixes'].mean()
    avg_superficial_fixes = simulated_data['SuperficialFixes'].mean()
    comparison_data = pd.DataFrame({'Fix Type': ['Root Cause Fixes', 'Superficial Fixes'], 'Average': [avg_root_cause_fixes, avg_superficial_fixes]})
    fig_comparison = px.bar(comparison_data, x='Fix Type', y='Average', title="Comparison of Fix Types")
    st.plotly_chart(fig_comparison, use_container_width=True)

    st.subheader("Relationship Plot: Employee Perception of Fairness vs. Willingness to Report Issues")
    fig_relationship = px.scatter(simulated_data, x='EmployeePerceptionFairness', y='WillingnessToReportIssues', title="Relationship between Fairness and Reporting Willingness")
    st.plotly_chart(fig_relationship, use_container_width=True)

    # Recommendations
    st.subheader("Actionable Recommendations")
    user_inputs = {'lc_input': lc_input, 'sta_input': sta_input, 'pr_input': pr_input, 'ia_input': ia_input, 'ac_input': ac_input}
    recommendations = generate_recommendations(simulated_data, user_inputs)
    for recommendation in recommendations:
        st.markdown(f"- {recommendation}")
```

`application_pages/page2.py`
```python
import streamlit as st
import pandas as pd

@st.cache_data
def generate_synthetic_data(num_records, start_date, random_seed):
    """Generates a synthetic dataset for risk culture metrics."""
    import numpy as np
    if not isinstance(num_records, int):
        raise TypeError("num_records must be an integer")
    try:
        start_date = pd.to_datetime(start_date)
    except ValueError:
        raise ValueError("Invalid start_date format. Must be parseable by pd.to_datetime.")
    except TypeError:
        raise TypeError("start_date must be a string or datetime object")
    np.random.seed(random_seed)
    dates = pd.date_range(start=start_date, periods=num_records, freq='D')
    data = {'Date': dates,
            'LeadershipConsistency': np.random.uniform(50, 70, num_records), # Placeholder for a metric
            'SupervisorTrainingAdherence': np.random.uniform(60, 80, num_records), # Placeholder
            'SelfRaisedIssues': np.random.uniform(0.3, 0.6, num_records), # Proportion
            'RootCauseFixes': np.random.uniform(0.4, 0.7, num_records), # Proportion
            'SuperficialFixes': np.random.uniform(0.2, 0.5, num_records), # Proportion
            'EmployeePerceptionFairness': np.random.uniform(5, 8, num_records), # Scale 1-10
            'WillingnessToReportIssues': np.random.uniform(5, 8, num_records) # Scale 1-10
           }
    df = pd.DataFrame(data)
    return df

def simulate_risk_culture_indicators(df_base, lc_input, sta_input, pr_input, ia_input, ac_input):
    """Simulates the impact of factors on risk culture indicators."""
    df = df_base.copy()
    # Leadership Consistency
    df['LeadershipConsistency'] = df['LeadershipConsistency'] + (lc_input - 50) * 0.1
    # Supervisor Training Adherence
    df['SupervisorTrainingAdherence'] = df['SupervisorTrainingAdherence'] + (sta_input - 50) * 0.1
    # Punishment Regime
    if pr_input == 'Strict':
        df['WillingnessToReportIssues'] = df['WillingnessToReportIssues'] * 0.8
    elif pr_input == 'Lenient':
        df['WillingnessToReportIssues'] = df['WillingnessToReportIssues'] * 1.2
    # Incentive Alignment
    if ia_input == 'Results-focused':
        df['SelfRaisedIssues'] = df['SelfRaisedIssues'] * 0.8
    elif ia_input == 'Risk-aware':
        df['SelfRaisedIssues'] = df['SelfRaisedIssues'] * 1.2
    # Accountability Clarity
    if ac_input == 'Vague':
        df['RootCauseFixes'] = df['RootCauseFixes'] * 0.8
    elif ac_input == 'Transparent':
        df['RootCauseFixes'] = df['RootCauseFixes'] * 1.2

    df['LeadershipConsistency'] = df['LeadershipConsistency'].clip(0, 100)
    df['SupervisorTrainingAdherence'] = df['SupervisorTrainingAdherence'].clip(0, 100)
    df['SelfRaisedIssues'] = df['SelfRaisedIssues'].clip(0, 1)
    df['RootCauseFixes'] = df['RootCauseFixes'].clip(0, 1)
    df['SuperficialFixes'] = df['SuperficialFixes'].clip(0, 1)
    df['EmployeePerceptionFairness'] = df['EmployeePerceptionFairness'].clip(0, 10)
    df['WillingnessToReportIssues'] = df['WillingnessToReportIssues'].clip(0, 10)
    return df

def run_page2():
    st.header("Raw Data Overview")

    # Input widgets (using defaults)
    lc_input = st.sidebar.slider("Leadership Consistency ($LC_{input}$):", 0, 100, 50, help="Represents the degree to which leadership actions and communications are consistent with risk management values.")
    sta_input = st.sidebar.slider("Supervisor Training Adherence ($STA_{input}$):", 0, 100, 50, help="Reflects the extent to which supervisors adhere to established training protocols and best practices.")
    pr_input = st.sidebar.selectbox("Fairness of Punishment Regime ($PR_{input}$):", ['Strict', 'Balanced', 'Lenient'], index=1, help="Influences employees' willingness to report issues.")
    ia_input = st.sidebar.selectbox("Incentive Alignment ($IA_{input}$):", ['Results-focused', 'Balanced', 'Risk-aware'], index=1, help="Affects the focus on self-raised issues versus hiding problems.")
    ac_input = st.sidebar.selectbox("Accountability Clarity ($AC_{input}$):", ['Vague', 'Clear', 'Transparent'], index=1, help="Impacts the effectiveness of root cause fixes.")

    # Data Generation
    num_records = 100
    start_date = '2023-01-01'
    random_seed = 42
    base_data = generate_synthetic_data(num_records, start_date, random_seed)

    # Simulation
    simulated_data = simulate_risk_culture_indicators(base_data, lc_input, sta_input, pr_input, ia_input, ac_input)

    # Display Initial Data
    st.subheader("Initial Data (First 5 Rows)")
    st.dataframe(base_data.head())
    st.subheader("Initial Data (Summary Statistics)")
    st.dataframe(base_data.describe())

    # Display Simulated Data
    st.subheader("Simulated Data (First 5 Rows)")
    st.dataframe(simulated_data.head())
    st.subheader("Simulated Data (Summary Statistics)")
    st.dataframe(simulated_data.describe())
```

`application_pages/page3.py`
```python
import streamlit as st

def run_page3():
    st.header("About This Lab")
    st.markdown("""
    This "Risk Management Framework Lab 1" provides an interactive platform to understand the qualitative and quantitative aspects of **Risk Culture & Accountability**. The application simulates how various organizational interventions can influence key risk culture indicators.

    ### Key Concepts Covered:
    *   **Risk Culture:** The norms, attitudes, and behaviors concerning risk-taking within an organization.
    *   **Leadership Consistency:** The alignment of leadership's words and actions with stated risk management values.
    *   **Supervisor Training Adherence:** The degree to which immediate managers follow best practices in risk identification and mitigation.
    *   **Punishment Regime:** The perceived fairness and severity of consequences for risk-related missteps.
    *   **Incentive Alignment:** How reward systems encourage or discourage desired risk behaviors, such as self-reporting issues.
    *   **Accountability Clarity:** The transparency and understanding of who is responsible for what in risk management.

    ### Data Simulation:
    The data used in this application is synthetically generated to mimic real-world scenarios. It includes metrics like 'Self-Raised Issues', 'Root Cause Fixes', 'Superficial Fixes', 'Employee Perception of Fairness', and 'Willingness to Report Issues'. These metrics are dynamically adjusted based on the user's input parameters in the "Simulation and Visualizations" page.

    The simulation models the influence of leadership actions, supervisory practices, and incentive structures on these indicators. The formula used for adjusting continuous variables like Leadership Consistency and Supervisor Training Adherence is:
    $$
    NewValue = OldValue + (Input - 50) \cdot 0.1
    $$
    Where 'Input' is the slider value (0-100). This formula applies a proportional adjustment, increasing the metric if the input is above 50 and decreasing it if below 50.

    Categorical inputs (Punishment Regime, Incentive Alignment, Accountability Clarity) apply multiplicative factors to relevant metrics, reflecting their direct impact on employee behavior and outcomes.

    ### How to Use:
    Navigate to the "Simulation and Visualizations" page using the sidebar. Adjust the sliders and dropdowns in the sidebar to observe the real-time changes in the simulated data and visualizations. The "Raw Data Overview" page provides a deeper look into the generated and simulated datasets.

    ### References:
    *   PRMIA (Professional Risk Managers' International Association) Operational Risk Manager Handbook.
    *   Various academic papers on organizational behavior and risk culture.
    """)
```

To run the application, open your terminal or command prompt, navigate to the directory where you saved `app.py`, and run the command:

```console
streamlit run app.py
```

Your web browser should open automatically to display the application.

## Understanding the Application Structure and Navigation
Duration: 0:05:00

The application utilizes a common structure for multi-page Streamlit apps, although it implements it slightly differently than the built-in multi-page feature.

The main file, `app.py`, handles the initial setup and routing:
1.  It sets the page configuration using `st.set_page_config`.
2.  It adds an image and a divider to the sidebar.
3.  It sets the main title of the application.
4.  It displays an introductory markdown section explaining the lab's purpose and objectives.
5.  Crucially, it creates a `st.sidebar.selectbox` titled "Navigation".

```python
page = st.sidebar.selectbox(label="Navigation", options=["Simulation and Visualizations", "Raw Data Overview", "About This Lab"])
if page == "Simulation and Visualizations":
    from application_pages.page1 import run_page1
    run_page1()
elif page == "Raw Data Overview":
    from application_pages.page2 import run_page2
    run_page2()
elif page == "About This Lab":
    from application_pages.page3 import run_page3
    run_page3()
```

This `selectbox` controls which "page" is displayed in the main content area. Based on the user's selection, it imports the corresponding function (`run_page1`, `run_page2`, or `run_page3`) from the respective file in the `application_pages` directory and calls that function.

Each `run_pageX` function is responsible for rendering the entire content and handling interactions for that specific page. This modular design keeps the code organized and makes it easier to manage different sections of the application.

The navigation options in the sidebar allow users to switch between:
*   **Simulation and Visualizations:** The core interactive part where users manipulate inputs and see simulation results visually.
*   **Raw Data Overview:** A page to inspect the underlying base and simulated data tables.
*   **About This Lab:** Information about the concepts, simulation model, and how to use the app.

Notice that the input widgets for the simulation (`lc_input`, `sta_input`, `pr_input`, etc.) are defined within the `run_page1` and `run_page2` functions, but they are placed in the sidebar using `st.sidebar.`. This means these widgets are always visible in the sidebar regardless of which page is selected, allowing parameters to potentially influence content on multiple pages (though in this specific app, they primarily drive the simulation results displayed on Page 1 and the data shown on Page 2).

## Exploring the "Simulation and Visualizations" Page
Duration: 0:15:00

This is the main interactive section of the application, handled by the `run_page1` function in `application_pages/page1.py`. It allows users to manipulate simulation parameters and observe their impact on key risk culture indicators through visualizations.

The `run_page1` function first defines the input widgets placed in the sidebar:
*   `st.sidebar.slider`: Used for continuous inputs like Leadership Consistency and Supervisor Training Adherence, ranging from 0 to 100.
*   `st.sidebar.selectbox`: Used for categorical inputs like Punishment Regime, Incentive Alignment, and Accountability Clarity.

```python
# Input widgets
lc_input = st.sidebar.slider("Leadership Consistency ($LC_{input}$):", 0, 100, 50, help="...")
sta_input = st.sidebar.slider("Supervisor Training Adherence ($STA_{input}$):", 0, 100, 50, help="...")
pr_input = st.sidebar.selectbox("Fairness of Punishment Regime ($PR_{input}$):", ['Strict', 'Balanced', 'Lenient'], index=1, help="...")
ia_input = st.sidebar.selectbox("Incentive Alignment ($IA_{input}$):", ['Results-focused', 'Balanced', 'Risk-aware'], index=1, help="...")
ac_input = st.sidebar.selectbox("Accountability Clarity ($AC_{input}$):", ['Vague', 'Clear', 'Transparent'], index=1, help="...")
```
These input values are captured whenever the user interacts with the widgets, triggering a re-run of the Streamlit script.

Next, the application generates the base synthetic data using the `generate_synthetic_data` function:
```python
@st.cache_data
def generate_synthetic_data(num_records, start_date, random_seed):
    """Generates a synthetic dataset for risk culture metrics."""
    # ... data generation logic ...
    return df

# Data Generation
num_records = 100
start_date = '2023-01-01'
random_seed = 42
base_data = generate_synthetic_data(num_records, start_date, random_seed)
```
The `@st.cache_data` decorator is used here. This is a performance optimization in Streamlit. It tells Streamlit to run this function and cache the result. If the function is called again with the same parameters (`num_records`, `start_date`, `random_seed`), Streamlit will return the cached result instead of re-running the function. This is efficient because the base data only needs to be generated once unless these specific parameters change (which they don't in this app, as they are hardcoded).

The core simulation logic is encapsulated in the `simulate_risk_culture_indicators` function:
```python
def simulate_risk_culture_indicators(df_base, lc_input, sta_input, pr_input, ia_input, ac_input):
    """Simulates the impact of factors on risk culture indicators."""
    df = df_base.copy()
    # Leadership Consistency & Supervisor Training Adherence: Proportional adjustment
    df['LeadershipConsistency'] = df['LeadershipConsistency'] + (lc_input - 50) * 0.1
    df['SupervisorTrainingAdherence'] = df['SupervisorTrainingAdherence'] + (sta_input - 50) * 0.1
    # Categorical inputs: Multiplicative adjustments
    if pr_input == 'Strict':
        df['WillingnessToReportIssues'] = df['WillingnessToReportIssues'] * 0.8
    # ... other adjustments for ia_input and ac_input ...
    # Clipping values to realistic ranges
    df['LeadershipConsistency'] = df['LeadershipConsistency'].clip(0, 100)
    # ... other clipping ...
    return df

# Simulation
simulated_data = simulate_risk_culture_indicators(base_data, lc_input, sta_input, pr_input, ia_input, ac_input)
```
This function takes the base synthetic data and the user inputs from the sidebar. It then modifies certain columns in the dataframe based on these inputs.
*   For continuous inputs (sliders), a simple linear adjustment is applied using the formula:
    $$
    NewValue = OldValue + (Input - 50) \cdot 0.1
    $$
    This formula means:
    *   If the `Input` is 50, the `NewValue` is the same as `OldValue` (adjustment is 0).
    *   If the `Input` is above 50, the value increases (e.g., Input 100 gives an increase of $(100-50) \cdot 0.1 = 5$).
    *   If the `Input` is below 50, the value decreases (e.g., Input 0 gives a decrease of $(0-50) \cdot 0.1 = -5$).
    *   The scaling factor $0.1$ determines how sensitive the metric is to the input slider.
    This relationship is explicitly displayed in the app using `st.latex()`.
*   For categorical inputs (selectboxes), specific multiplicative factors are applied to relevant metrics. For example, a 'Strict' punishment regime reduces `WillingnessToReportIssues` by multiplying it by 0.8.
*   Finally, the function clips the values to ensure they stay within meaningful ranges (e.g., percentages between 0 and 1, scores between 0 and 10 or 0 and 100).

After simulation, the `simulated_data` dataframe is used to generate visualizations:
*   A `plotly.express.line` chart shows the trend of 'SelfRaisedIssues' over time.
*   A `plotly.express.bar` chart compares the average 'RootCauseFixes' and 'SuperficialFixes'.
*   A `plotly.express.scatter` plot visualizes the relationship between 'EmployeePerceptionFairness' and 'WillingnessToReportIssues'.

```python
st.subheader("Trend Plot: Quantum of Self-Raised Issues")
fig_trend = px.line(simulated_data, x='Date', y='SelfRaisedIssues', title="Trend of Self-Raised Issues")
st.plotly_chart(fig_trend, use_container_width=True)

# ... other plots ...
```
`st.plotly_chart` is used to render the interactive Plotly figures in the Streamlit application. `use_container_width=True` makes the charts automatically adjust to the width of the main content area.

Lastly, the `generate_recommendations` function provides text-based recommendations based on the average values of certain simulated metrics. This is a simplified example of how simulated outcomes can be used to drive business insights.

```python
def generate_recommendations(simulated_data, user_inputs):
    """Generates actionable recommendations based on simulated data and user inputs."""
    # ... logic based on average values ...
    return recommendations

# Recommendations
st.subheader("Actionable Recommendations")
user_inputs = {'lc_input': lc_input, 'sta_input': sta_input, 'pr_input': pr_input, 'ia_input': ia_input, 'ac_input': ac_input}
recommendations = generate_recommendations(simulated_data, user_inputs)
for recommendation in recommendations:
    st.markdown(f"- {recommendation}")
```
This section demonstrates how the application provides value by not just showing data but also interpreting it based on predefined rules (business logic) to suggest potential actions.

Experiment with the sliders and dropdowns in the sidebar. Observe how changing Leadership Consistency, Supervisor Training Adherence, Punishment Regime, Incentive Alignment, or Accountability Clarity affects the plots and the generated recommendations in real-time.

## Exploring the "Raw Data Overview" Page
Duration: 0:05:00

The "Raw Data Overview" page, handled by the `run_page2` function in `application_pages/page2.py`, serves a simpler purpose: allowing the user to inspect the underlying dataframes that are used for simulation and visualization.

Similar to Page 1, this page also includes the input widgets in the sidebar and calls the `generate_synthetic_data` and `simulate_risk_culture_indicators` functions. This is necessary because the simulation parameters from the sidebar need to be read to generate the correct `simulated_data` for display on this page.

```python
# Input widgets (using defaults) - These are the same widgets as in page1
lc_input = st.sidebar.slider("Leadership Consistency ($LC_{input}$):", 0, 100, 50, help="...")
# ... other widgets ...

# Data Generation
base_data = generate_synthetic_data(num_records, start_date, random_seed)

# Simulation
simulated_data = simulate_risk_culture_indicators(base_data, lc_input, sta_input, pr_input, ia_input, ac_input)
```

The primary functionality of this page is to display the generated dataframes using `st.dataframe`:
```python
st.subheader("Initial Data (First 5 Rows)")
st.dataframe(base_data.head())
st.subheader("Initial Data (Summary Statistics)")
st.dataframe(base_data.describe())

st.subheader("Simulated Data (First 5 Rows)")
st.dataframe(simulated_data.head())
st.subheader("Simulated Data (Summary Statistics)")
st.dataframe(simulated_data.describe())
```
This provides a direct view of the data structure and how the simulation has altered the original values. It shows:
*   The first few rows (`.head()`) of the base (initial) data.
*   Summary statistics (`.describe()`) of the base data, giving an idea of the initial distributions.
*   The first few rows of the *simulated* data, showing the direct impact of the user's inputs.
*   Summary statistics of the *simulated* data, illustrating how the overall distributions of the metrics have shifted due to the simulation parameters.

This page is useful for developers or users who want to understand the data itself and verify the simulation logic's output at a granular level.

<aside class="positive">
Using `st.dataframe` is a quick and easy way to display tabular data in Streamlit. It provides basic interactivity like scrolling and column sorting.
</aside>

## Exploring the "About This Lab" Page
Duration: 0:03:00

The "About This Lab" page, handled by the `run_page3` function in `application_pages/page3.py`, is designed to provide context and detailed information about the application's purpose, the concepts it explores, and the simulation methodology.

The content is primarily presented using Streamlit's markdown function (`st.markdown`):

```python
def run_page3():
    st.header("About This Lab")
    st.markdown("""
    This "Risk Management Framework Lab 1" provides an interactive platform...

    ### Key Concepts Covered:
    *   **Risk Culture:** ...
    *   **Leadership Consistency:** ...
    *   ...

    ### Data Simulation:
    The data used in this application is synthetically generated...
    The formula used for adjusting continuous variables...
    $$
    NewValue = OldValue + (Input - 50) \cdot 0.1
    $$
    ...

    ### How to Use:
    Navigate to the "Simulation and Visualizations" page...

    ### References:
    *   PRMIA ...
    *   Various academic papers...
    """)
```

This page is essential for giving users a solid understanding of what the application represents. It explicitly lists the key concepts related to risk culture being demonstrated and provides a clear explanation of the data simulation process, including the mathematical formula used for continuous variables.

This page also highlights the educational aspect, referencing resources like the PRMIA Operational Risk Manager Handbook, indicating that the concepts are based on established risk management principles.

<aside class="positive">
Including an "About" or "Info" page in your Streamlit apps is a good practice to provide context, explain complex logic (like simulation), and guide users.
</aside>

## Key Takeaways and Next Steps
Duration: 0:02:00

Congratulations! You have successfully explored the functionalities of the QuLab: Risk Culture & Accountability Dashboard.

You learned how a multi-page Streamlit application can be structured using sidebar navigation and separate Python modules for each page. You saw how user inputs from sidebar widgets can drive data simulation logic, dynamically changing metrics based on predefined rules. You also observed how interactive visualizations powered by Plotly can effectively communicate the results of this simulation and how simple business logic can generate actionable recommendations. Finally, you understand the importance of providing context and explaining the underlying methodology, as demonstrated by the "About This Lab" page.

This application serves as a basic framework for building more sophisticated simulation and analysis tools. Here are some potential next steps or ideas for enhancement:

*   **More Complex Simulation Models:** Implement more nuanced or interconnected relationships between the input factors and the risk culture indicators. Introduce feedback loops or time-delayed effects.
*   **Real-World Data Integration:** Adapt the application to load and analyze real (anonymized) risk culture survey data or incident data.
*   **Historical Trends:** Allow users to specify historical periods and visualize the simulated impact over longer timescales.
*   **Scenario Comparison:** Enable users to save different input scenarios and compare their simulated outcomes side-by-side.
*   **User Authentication:** Add user login to save settings or simulation results.
*   **Improved UI/UX:** Enhance the layout, add more informative tooltips, or incorporate advanced components.
*   **Separate Simulation Logic:** Refactor the simulation function into a dedicated module or class to avoid code duplication between `page1.py` and `page2.py`.

By experimenting with the code and adding new features, you can further deepen your understanding of building interactive data applications with Streamlit and explore more complex simulations.


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

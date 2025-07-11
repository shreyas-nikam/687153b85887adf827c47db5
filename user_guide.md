id: 687153b85887adf827c47db5_user_guide
summary: Risk Management Framework Lab 1 User Guide
feedback link: https://docs.google.com/forms/d/e/1FAIpQLSfWkOK-in_bMMoHSZfcIvAeO58PAH9wrDqcxnJABHaxiDqhSA/viewform?usp=sf_link
environments: Web
status: Published
# Risk Management Framework Lab 1 - Stress Test Scenario Visualizer

## Introduction to Financial Stress Testing
Duration: 0:05

Welcome to the **Risk Management Framework Lab 1 - Stress Test Scenario Visualizer**. In the unpredictable world of finance, understanding how adverse events can impact a firm's health is paramount. Financial stress testing is a crucial analytical technique used to evaluate the potential vulnerability of an entity to exceptional, but plausible, adverse events or movements in financial markets.

This interactive application provides a hands-on way to explore this concept. It allows you to:
*   Load and validate financial data.
*   Apply different types of hypothetical stress scenarios (like economic downturns or market shocks).
*   Visualize the potential outcomes and key risk metrics derived from these scenarios.

By using this tool, you'll gain a deeper understanding of:
*   The importance of robust data for analysis.
*   How different stress methodologies work conceptually.
*   The potential impact of correlated risks across financial components.
*   How visualizing financial data under stress aids in risk assessment and strategic planning.

Navigate through the application using the sidebar to follow the steps outlined in this codelab.

<aside class="positive">
<b>Understanding stress testing is vital</b> for regulatory compliance (like Dodd-Frank in the US or Capital Requirements Directive in Europe), capital adequacy planning, and informed business strategy. This lab helps demystify the process.
</aside>

## Step 1: Data Loading and Validation
Duration: 0:05

The first crucial step in any financial analysis, especially stress testing, is obtaining reliable baseline data. This page is dedicated to that process.

When you are on the "1. Data Loading & Validation" page (selected from the sidebar navigation), you will see options to get your data.

You have two choices for the data source:
1.  **Use demo data:** This option loads a small, synthetic dataset provided with the application. It's useful for quickly exploring the application's features without needing your own file.
2.  **Upload CSV:** This allows you to upload your own financial data.

<aside class="negative">
If you choose to upload your own CSV, make sure it contains the required columns: <b>`Date`</b>, <b>`Base_Revenue`</b>, and <b>`Base_Costs`</b>. The application also checks for duplicate dates, which are not allowed for this analysis.
</aside>

The application automatically validates the data once loaded or uploaded. If there are issues (missing columns, duplicate dates, file format errors), you will see an error message. If successful, a success message will appear, and you will see a preview of the loaded data in a table format.

<aside class="positive">
The validation step is critical. **Bad data leads to bad analysis.** Ensuring your base data is clean and complete is foundational for meaningful stress testing results.
</aside>

This loaded data serves as the baseline for all subsequent stress test simulations and analyses.

## Step 2: Interactive Stress Test Simulation
Duration: 0:10

Once your base data is loaded and validated, you can proceed to the "2. Stress Test Simulation" page. This is where you define and apply hypothetical stress scenarios.

This page introduces three common stress testing methodologies:
1.  **Sensitivity:** This method examines the impact of a shock to a *single* specific parameter, like a reduction in revenue or an increase in costs.
2.  **Scenario:** This method applies a broader stress factor across *all* relevant base parameters, simulating a general economic downturn that affects revenues and costs proportionally.
3.  **Firm-Wide:** This method simulates a more severe, systemic crisis with a significant aggregate impact across all base parameters.

In the sidebar, you can select the **Stress Test Methodology** you want to apply.

Based on your selection, the sidebar will show specific parameters you can adjust:
*   **Sensitivity:** You'll choose which base parameter (`Base_Revenue` or `Base_Costs`) to shock and set the **Shock Magnitude** as a percentage reduction.
*   **Scenario:** You'll set a single **Scenario Severity Factor** (between 0.0 and 1.0) which acts as a multiplier reducing all base parameters.
*   **Firm-Wide:** You'll set a **Systemic Crisis Scale** (between 0.0 and 1.0), similar to the scenario factor but representing a typically larger impact.

The application uses specific formulas to calculate the "Adjusted" values based on the "Base" values and your chosen parameters:

*   **Sensitivity:**
    $$ \text{Adjusted Parameter} = \text{Base Parameter} \times \left(1 - \frac{\text{Shock Magnitude}}{100}\right) $$
*   **Scenario:**
    $$ \text{Adjusted Base Component} = \text{Base Component} \times (1 - \text{Scenario Severity Factor}) $$
*   **Firm-Wide:**
    $$ \text{Adjusted Base Component} = \text{Base Component} \times (1 - \text{Systemic Crisis Scale}) $$

As you adjust the parameters in the sidebar, the application immediately recalculates the stressed data. You will see a preview of this new `Stressed Data` which now includes columns like `Adjusted_Revenue` and `Adjusted_Costs`.

<aside class="positive">
Interactively adjusting parameters helps build intuition about how different levels of stress impact your financial components.
</aside>

The calculated stressed data is then used for the final step: analyzing the impact and visualizing the results.

## Step 3: Risk Capacity Metrics & Visualizations
Duration: 0:15

Having applied a stress scenario, the "3. Risk Metrics & Visualizations" page allows you to quantify the impact and visually explore the results.

This page first presents key **Risk Capacity Metrics**. These metrics help you understand how well the firm's capital and liquidity would hold up under the applied stress. The calculated metrics include:
*   Initial Capital (a starting value set in the application)
*   Minimum Capital Remaining (the lowest point your capital reaches under stress)
*   Capital Drawdown (the total reduction in capital from its initial value)
*   Capital Drawdown Percentage (the drawdown expressed as a percentage of initial capital)
*   Minimum Liquidity Position (the lowest point your liquidity reaches under stress)
*   Liquidity Shortfall (the absolute value if the minimum liquidity position drops below zero)

The key formulas for these metrics are:
*   **Capital Drawdown**:
    $$ \text{Capital Drawdown} = \text{Initial Capital} - \text{Minimum Capital Remaining} $$
*   **Capital Drawdown Percentage**:
    $$ \text{Capital Drawdown Percentage} = \left( \frac{\text{Capital Drawdown}}{\text{Initial Capital}} \right) \times 100 $$
*   **Liquidity Shortfall**: This represents the amount needed to avoid a negative liquidity position.
    $$ \text{Liquidity Shortfall} = \begin{cases} |\text{Minimum Liquidity Position}| & \text{if } \text{Minimum Liquidity Position} < 0 \\ 0 & \text{otherwise} \end{cases} $$

These metrics are displayed prominently at the top of the page.

Below the metrics, you can explore the data through interactive visualizations. Use the sidebar on this page to select the **Plot Type**:
*   **Trend:** Shows how key financial values (Base, Adjusted, Net Earnings, Capital, Liquidity) evolve over time. This helps visualize the trajectory under stress.
*   **Relationship:** Allows you to plot any two numeric columns against each other using a scatter plot. This is useful for identifying correlations between different metrics under stress. You select the columns for the X and Y axes from dropdowns in the sidebar.
*   **Comparison:** Presents a bar chart comparing the values of two selected numeric columns over time. This helps highlight the difference or similarity between components under stress. You select the two columns to compare from dropdowns in the sidebar.

<aside class="positive">
Visualizations make complex data understandable at a glance. Use trend plots to see the impact timeline, relationship plots to find correlations, and comparison plots to assess relative changes.
</aside>

By examining the metrics and exploring the visualizations, you gain a comprehensive view of the stress scenario's impact and the firm's resilience. This information is crucial for risk reporting, capital adequacy assessments, and making informed decisions.


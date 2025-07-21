id: 687153b85887adf827c47db5_user_guide
summary: Risk Management Framework Lab 1 User Guide
feedback link: https://docs.google.com/forms/d/e/1FAIpQLSfWkOK-in_bMMoHSZfcIvAeO58PAH9wrDqcxnJABHaxiDqhSA/viewform?usp=sf_link
environments: Web
status: Published
# Understanding Risk with QuLab: A Stress Testing Application

## Introduction to Stress Testing and QuLab
Duration: 0:05

Welcome to QuLab, an interactive application designed to help you explore the critical concept of Risk Management through the lens of stress test scenario visualization. In the dynamic world of finance, understanding how various adverse events can impact a firm's financial health is paramount. Stress testing is a vital tool for this, allowing organizations to assess their resilience against hypothetical but severe economic and market shocks.

This application provides a practical platform to:
*   **Comprehend Core Concepts**: Dive into different types of stress tests: **Sensitivity**, **Scenario**, and **Firm-Wide** stress testing. Each method offers unique insights into financial vulnerabilities.
*   **Visualize Impact**: See how correlated threats can simultaneously affect multiple portfolios and processes within a firm.
*   **Analyze Financial Metrics**: Understand the intricate relationship between economic parameters and their ripple effects on crucial financial components such as income, costs, market risk losses, and liquidity.
*   **Interactive Exploration**: Engage with interactive visualizations that illustrate financial trajectories under stress, correlations between impact metrics, and aggregated comparisons of losses.

By the end of this codelab, you will have a clear understanding of how stress testing helps firms prepare for the unexpected and maintain financial stability.

<aside class="positive">
<b>Why is this important?</b> Stress testing is a regulatory requirement for many financial institutions and a best practice for all businesses. It helps identify vulnerabilities before they become crises, informing strategic decisions and capital planning.
</aside>

## Step 1: Data Loading & Selection
Duration: 0:05

The first step in any analytical process is to get your data ready. This page allows you to bring your financial base data into QuLab, which will then be used for simulating various stress scenarios.

<aside class="positive">
A good understanding of your base financial data is crucial, as it forms the foundation for all subsequent stress test simulations and analyses.
</aside>

On this page, you will find two options to load data:

*   **Synthetic Data**: This option provides a pre-generated, small dataset for immediate use. It's perfect for quick demonstrations and getting a feel for the application without needing your own data. The synthetic data includes `Date`, `Base_Revenue`, and `Base_Costs` columns.
*   **Upload CSV**: If you have your own financial data, you can upload it here. The application expects your CSV file to contain at least the following columns:
    *   `Date`: The date of the financial record.
    *   `Base_Revenue`: Your firm's revenue under normal, unstressed conditions.
    *   `Base_Costs`: Your firm's costs under normal, unstressed conditions.

### How to use this page:

1.  **Select Data Source**: In the main area, choose between "Synthetic Data" or "Upload CSV" using the radio buttons.
2.  **Upload (if applicable)**: If you select "Upload CSV", a file uploader will appear. Click to browse and select your CSV file.
3.  **View Data**: Once loaded (either synthetic or uploaded), the application will display a preview of your financial data in a table format. This table shows the `Date`, `Base_Revenue`, and `Base_Costs` columns, ensuring your data is correctly loaded.

<aside class="negative">
<b>Data Validation:</b> The application performs basic validation. If your uploaded CSV is missing required columns (`Date`, `Base_Revenue`, `Base_Costs`) or contains duplicate dates, you will see an error message. Ensure your data adheres to these requirements for successful processing.
</aside>

Once your data is successfully loaded and displayed, it's stored for use in the next steps.

## Step 2: Stress Test Simulation
Duration: 0:10

Now that your base financial data is loaded, this page is where the magic of stress testing happens. You can apply various stress scenarios to your data to see how your financial metrics might change under adverse conditions.

<aside class="positive">
This step is where you define the hypothetical "shocks" to your financial system. Experiment with different parameters to understand their varied impacts.
</aside>

On the left sidebar, you will find controls to select the type of stress test and configure its parameters. The main area will display the "stressed" data, showing how your `Base_Revenue` and `Base_Costs` are adjusted.

### Understanding Stress Test Types:

QuLab supports three fundamental types of stress tests:

1.  **Sensitivity Stress Test**:
    *   **Concept**: This type of test focuses on the impact of a shock to a *single* financial parameter. It helps understand how sensitive your firm's financials are to changes in one specific variable.
    *   **Parameters**:
        *   **Parameter to Shock**: You can choose either `Base_Revenue` or `Base_Costs`.
        *   **Shock Magnitude (% Reduction)**: A slider from $0\%$ to $100\%$. This defines how much the selected parameter will be reduced. For example, a $10\%$ reduction means your revenue or costs will be $10\%$ lower (or higher, for costs, if interpreted as a reduction in ability to manage costs) than the base value.
    *   **Impact**: Only the selected parameter will be adjusted. For example, if you shock `Base_Revenue`, only `Adjusted_Revenue` will change, while `Adjusted_Costs` might remain the same (depending on how the model is designed to propagate the shock).

2.  **Scenario Stress Test**:
    *   **Concept**: This test simulates a broader economic or market downturn where multiple, related financial parameters are affected simultaneously. It's often based on plausible, predefined economic scenarios (e.g., a moderate recession).
    *   **Parameter**:
        *   **Scenario Severity Factor**: A slider from $0.0$ to $1.0$. This factor represents the overall severity of the economic scenario. A value of $0.2$ means that base financial components (like `Base_Revenue` and `Base_Costs`) are generally reduced by $20\%$ as a ripple effect of the scenario.
    *   **Impact**: All "Base" financial components will be adjusted by this factor to reflect the widespread impact of the scenario.

3.  **Firm-Wide Stress Test**:
    *   **Concept**: This is the most comprehensive stress test, simulating a severe systemic crisis that impacts nearly all aspects of a firm's financial operations. It's designed to assess resilience against extreme, unlikely but plausible events.
    *   **Parameter**:
        *   **Systemic Crisis Scale**: A slider from $0.0$ to $1.0$. Similar to the scenario severity factor, this value scales the impact across all base financial components, representing a severe aggregate reduction. A value of $0.5$ could simulate a $50\%$ reduction in various base financial components due to a widespread crisis.
    *   **Impact**: Similar to the scenario test, all "Base" financial components are significantly adjusted to reflect the severe and pervasive impact of a firm-wide crisis.

### How to use this page:

1.  **Ensure Data is Loaded**: If you haven't loaded data in Step 1, a warning will appear. Please go back to the "Data Loading & Selection" page.
2.  **Select Stress Test Type**: In the left sidebar, choose one of the three stress test types from the dropdown menu.
3.  **Adjust Parameters**: Depending on your selected stress test type, relevant sliders and select boxes will appear in the sidebar. Adjust these to define the intensity or focus of your stress test.
4.  **View Stressed Data**: The main area will dynamically update to show the `stressed_data` DataFrame. You will see new columns like `Adjusted_Revenue` and `Adjusted_Costs`, reflecting the impact of your chosen stress test. Compare these "Adjusted" values to your original "Base" values to see the immediate effect of the stress.

The `stressed_data` generated here will be automatically passed to the next page for in-depth visualization and analysis.

## Step 3: Visualizations
Duration: 0:15

After simulating stress scenarios, the next crucial step is to analyze and visualize the results. This page provides tools to understand the impact of the stress on key financial metrics and to gain insights into your firm's risk capacity.

<aside class="positive">
Visualizations transform raw data into actionable insights, making it easier to identify trends, relationships, and potential vulnerabilities under stress.
</aside>

If you haven't run a simulation on the "Stress Test Simulation" page, a warning will appear. Please ensure you have generated `stressed_data` first.

### Risk Capacity Metrics:

At the top of the page, you'll see a section dedicated to "Risk Capacity Metrics". These are derived calculations that provide a high-level summary of your firm's financial health under the applied stress. Key metrics include:

*   **Net Earnings Under Stress**: This is the difference between `Adjusted_Revenue` and `Adjusted_Costs`, showing your profitability under the stressed scenario.
*   **Capital Impact**: Represents the change in capital due to the stress. This is often an aggregate of various losses (e.g., revenue decline, cost increase).
*   **Capital Remaining**: Shows the estimated capital remaining after accounting for the cumulative impact of the stress over time, starting from an initial capital value.
*   **Capital Drawdown**: The total reduction in capital from its initial value to its minimum point during the stress period.
*   **Capital Drawdown Percentage**: The percentage of initial capital that was drawn down, indicating the severity of capital erosion.
*   **Liquidity Impact**: The estimated effect of stress on your firm's liquid assets.
*   **Liquidity Position**: The estimated liquid assets remaining over time, starting from an initial liquidity value.
*   **Liquidity Shortfall**: Indicates if your liquidity position drops below zero, representing the amount by which it falls short of meeting obligations.

These metrics offer a quantitative view of how well your firm can absorb the shocks defined in your stress test.

### Interactive Visualizations:

Below the metrics, you can generate various plots to explore the `stressed_data` in more detail. Use the "Select Plot Type" dropdown to choose your desired visualization:

1.  **Trend Plots**:
    *   **Concept**: These line charts show how different financial metrics evolve over time under the stress scenario. They are excellent for observing patterns, identifying periods of significant decline or recovery, and comparing the "Base" vs. "Adjusted" trajectories.
    *   **What you'll see**: Plots for `Base_Revenue`, `Base_Costs`, `Adjusted_Revenue`, `Adjusted_Costs`, `Net_Earnings_Under_Stress`, `Capital_Remaining`, and `Liquidity_Position`.

2.  **Relationship Plots (Scatter Plots)**:
    *   **Concept**: These scatter plots illustrate the correlation and relationship between any two numeric columns in your stressed data. They help identify if certain metrics move together or have an inverse relationship under stress.
    *   **What you'll see**: A matrix of scatter plots showing relationships between all numeric columns in your data, such as `Adjusted_Revenue` vs. `Adjusted_Costs`, or `Capital_Remaining` vs. `Liquidity_Position`.

3.  **Comparison Plots (Bar Charts)**:
    *   **Concept**: These bar charts allow you to directly compare the values of two selected columns over time. This is particularly useful for side-by-side comparisons, such as `Base_Revenue` vs. `Adjusted_Revenue`, to clearly see the impact of the stress.
    *   **How to use**: When you select "comparison" plot type, two new dropdowns will appear: "Select first column for comparison" and "Select second column for comparison". Choose any two columns from your data to compare them.

### How to use this page:

1.  **Review Risk Metrics**: First, examine the "Risk Capacity Metrics" to get an immediate overview of the stress impact.
2.  **Select Plot Type**: Choose "trend", "relationship", or "comparison" from the dropdown.
3.  **Configure Comparison (if applicable)**: If you selected "comparison", use the two new dropdowns to choose the columns you wish to compare.
4.  **Analyze Visualizations**: Observe the generated charts. Hover over plot elements for specific data points. Look for:
    *   Significant deviations from base values in trend plots.
    *   Strong or weak correlations in relationship plots.
    *   Clear differences between compared metrics in bar charts.

By exploring these visualizations, you can gain a deeper understanding of the specific vulnerabilities exposed by your stress tests and assess the overall financial resilience of your firm.

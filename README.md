# QuLab: Risk Management Framework Lab 1 - Stress Test Scenario Visualizer

This interactive Streamlit application, **"Risk Management Framework Lab 1 - Stress Test Scenario Visualizer"**, is designed to provide financial professionals with a practical platform for understanding and visualizing the potential impacts of various financial stress test scenarios.

Based on concepts explored in the 'PRMIA Operational Risk Manager Handbook', this application focuses on demonstrating how correlated threats can simultaneously affect multiple financial components.

The primary goal is to enhance comprehension of stress testing methodologies and their simulated effects on a firm's financial health under adverse conditions.

## Features

*   **Flexible Data Loading**: Load financial data using synthetic demo data or upload your own CSV file.
*   **Robust Data Validation**: Ensures uploaded data includes required columns (`Date`, `Base_Revenue`, `Base_Costs`), has unique dates, and is in a loadable format.
*   **Interactive Stress Testing**: Select and configure different stress testing methodologies:
    *   **Sensitivity Analysis**: Shock a single parameter by a defined percentage.
    *   **Scenario Analysis**: Apply a broad severity factor across all base parameters.
    *   **Firm-Wide Stress**: Simulate an extensive, systemic impact across the data.
*   **Formula Transparency**: View the mathematical formulas used for each stress test type directly within the application.
*   **Risk Capacity Metrics**: Calculation and display of key metrics under stress, including:
    *   Initial Capital
    *   Minimum Capital Remaining
    *   Capital Drawdown & Percentage
    *   Minimum Liquidity Position
    *   Liquidity Shortfall
    *   Explanation of metric formulas.
*   **Dynamic Visualizations**: Generate interactive plots using Plotly to visualize financial performance under stress:
    *   **Trend Plots**: Show the evolution of key financial metrics over time.
    *   **Relationship Plots**: Explore correlations between different numeric parameters.
    *   **Comparison Plots**: Compare the values of two selected numeric columns over time.
*   **Session Management**: Data flows between pages using Streamlit's session state, allowing for a connected workflow.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

*   Python 3.7+
*   `pip` package manager

### Installation

1.  **Clone the repository** (or download the code files if not in a repo):
    ```bash
    git clone <repository_url>
    cd <repository_directory>
    ```
    (Replace `<repository_url>` and `<repository_directory>` with the actual repository information)

2.  **Navigate to the project directory**:
    ```bash
    cd risk-management-lab # Or the name of the directory
    ```

3.  **Install dependencies**:
    Create a `requirements.txt` file in the project root with the following content:
    ```
    streamlit
    pandas
    plotly
    ```
    Then install the packages:
    ```bash
    pip install -r requirements.txt
    ```

## Usage

To run the Streamlit application:

1.  Open your terminal or command prompt.
2.  Navigate to the root directory of the project (where `app.py` is located).
3.  Run the Streamlit command:
    ```bash
    streamlit run app.py
    ```
4.  Your default web browser should open a new tab with the application running. If it doesn't, the terminal will provide a local URL (usually `http://localhost:8501`) that you can copy and paste into your browser.

**Navigating the Application:**

*   Use the **sidebar** on the left to navigate between the three main pages:
    1.  **Data Loading & Validation**: Start here to load your financial data.
    2.  **Stress Test Simulation**: Configure and apply stress scenarios to the loaded data.
    3.  **Risk Metrics & Visualizations**: View key risk metrics and interactive charts based on the stressed data.
*   Follow the on-screen instructions and use the sidebar inputs (radio buttons, file uploader, select boxes, sliders) to interact with each page.

To stop the application, close the terminal window where you ran the `streamlit run` command.

## Project Structure

```
.
├── app.py                      # Main application entry point and navigation
├── application_pages/          # Directory containing individual page scripts
│   ├── page1.py                # Data Loading and Validation logic
│   ├── page2.py                # Stress Test Simulation logic
│   └── page3.py                # Risk Metrics and Visualizations logic
└── requirements.txt            # List of Python dependencies
```

## Technology Stack

*   **Python**: The core programming language.
*   **Streamlit**: Framework for building the web application user interface.
*   **Pandas**: For data manipulation and analysis.
*   **Plotly**: For generating interactive visualizations.

## Contributing

This project is primarily intended as a lab exercise for educational purposes. Contributions are welcome, but please open an issue first to discuss any significant changes or features you'd like to add.

1.  Fork the repository.
2.  Create your feature branch (`git checkout -b feature/AmazingFeature`).
3.  Commit your changes (`git commit -m 'Add some AmazingFeature'`).
4.  Push to the branch (`git push origin feature/AmazingFeature`).
5.  Open a Pull Request.

## License

This project is licensed under the MIT License - see the LICENSE.md file for details (Note: As this is a lab, a formal LICENSE.md might not exist. If you plan to distribute, add one).

## Contact

If you have questions or feedback regarding this lab project, please reach out via [Your Preferred Contact Method, e.g., Email or GitHub Issues].


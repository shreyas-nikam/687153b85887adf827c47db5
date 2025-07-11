# QuLab: Loan Risk-Sensitive Pricing Simulation Lab

## Project Title and Description

**QuLab: Loan Risk-Sensitive Pricing Simulation Lab**

This project is a Streamlit-based interactive lab designed to explore the critical concepts of risk-sensitive pricing in financial transactions, specifically focusing on loan portfolios. It demonstrates how different pricing strategies impact portfolio profitability and risk profiles by simulating synthetic loan transactions.

The lab highlights the distinction between risk-insensitive pricing (where pricing doesn't fully account for transaction-specific risk) and risk-sensitive pricing (where pricing is adjusted based on the risk taken) and analyzes the outcomes using key financial risk metrics.

## Features

*   **Synthetic Data Generation:** Generates a dataset of synthetic loan transactions with various attributes (Principal, Interest Rate, Tenor, PD, LGD, Costs).
*   **Key Risk Metric Calculation:** Computes essential risk metrics for each transaction:
    *   Expected Loss (EL)
    *   Economic Capital (EC)
    *   Net Risk Adjusted Reward (NRAR)
    *   Risk-Adjusted Return on Risk-Adjusted Capital (RARORAC)
*   **Pricing Strategy Comparison:** Simulates and compares the results of applying:
    *   **Risk-Insensitive Pricing:** Uses the original, unadjusted interest rate.
    *   **Risk-Sensitive Pricing:** Iteratively adjusts the interest rate for each transaction to meet a predefined hurdle rate, compensating for the risk taken.
*   **Interactive Visualization:** Provides visualizations to compare the performance and characteristics of the two pricing strategies, including:
    *   RARORAC distribution histograms.
    *   Scatter plot showing Risk-Sensitive Interest Rate vs. Principal, colored by RARORAC.
*   **Educational Content:** Includes introductory material explaining the concepts and a conclusion interpreting the simulation results.
*   **Multi-page Navigation:** Uses a sidebar for easy navigation between the Introduction, Simulation, and Conclusion sections.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine.

### Prerequisites

*   Python 3.7+
*   pip package manager

### Installation

1.  Clone this repository (or download the code files):
    ```bash
    git clone <repository_url> # Replace <repository_url> with the actual URL if available
    cd qu-lab-risk-pricing # Change directory to your project folder
    ```
    (If you just downloaded the files, navigate to the directory containing `app.py`.)

2.  Install the required Python packages. You can install them directly:
    ```bash
    pip install streamlit pandas numpy plotly
    ```
    Alternatively, you could create a `requirements.txt` file with the following content and install using `pip install -r requirements.txt`:
    ```
    streamlit
    pandas
    numpy
    plotly
    ```

## Usage

1.  Ensure you are in the project directory where `app.py` is located.
2.  Run the Streamlit application from your terminal:
    ```bash
    streamlit run app.py
    ```
3.  Your web browser should automatically open a new tab with the QuLab application.
4.  Use the sidebar navigation to switch between the "Introduction", "Simulation", and "Conclusion" pages.
5.  On the "Simulation" page, you will see generated data, formulas, a comparison table of results for the two strategies, and interactive plots illustrating the outcomes.

## Project Structure

The project is organized as follows:

```
qu-lab-risk-pricing/
├── app.py
└── application_pages/
    ├── __init__.py         # (Optional) Makes application_pages a Python package
    ├── conclusion.py       # Content for the Conclusion page
    ├── introduction.py     # Content for the Introduction page
    └── simulation.py       # Core simulation logic and display
```

*   `app.py`: The main entry point for the Streamlit application. Handles page setup, navigation, and routing.
*   `application_pages/`: Directory containing separate Python files for each major section (page) of the application.
    *   `introduction.py`: Contains the `run_introduction` function to display the introduction content.
    *   `simulation.py`: Contains the functions for data generation, calculations, simulation logic, and displaying results and plots for the main simulation section.
    *   `conclusion.py`: Contains the `run_conclusion` function to display the conclusion and interpretation.

## Technology Stack

*   **Streamlit:** Used for building the interactive web application interface.
*   **Python:** The core programming language.
*   **Pandas:** Used for data manipulation and analysis, handling transaction data in DataFrames.
*   **NumPy:** Used for numerical operations, especially for generating synthetic data and calculations.
*   **Plotly:** Used for generating interactive data visualizations.

## Contributing

Contributions are welcome! If you'd like to contribute, please fork the repository and submit a pull request.

## License

This project is licensed under the [MIT License](LICENSE) - see the LICENSE file for details. (Assuming an MIT license; replace if a different license is used or add a LICENSE file).

## Contact

If you have any questions or feedback, please contact [Your Name/Organization Name] or open an issue on this repository.

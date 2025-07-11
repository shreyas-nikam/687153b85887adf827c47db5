# QuLab: Risk Culture & Accountability Dashboard

![QuantUniversity Logo](https://www.quantuniversity.com/assets/img/logo5.jpg)

An interactive Streamlit application designed as a lab project to simulate and visualize the impact of key organizational factors on risk culture indicators.

## Project Description

This project, "Risk Management Framework Lab 1" or "QuLab," provides a hands-on platform to explore the dynamics of **Risk Culture & Accountability** within an organization. Drawing inspiration from concepts found in resources like the PRMIA Operational Risk Manager Handbook, this dashboard allows users to manipulate critical factors such as leadership consistency, supervisory practices, incentive structures, punishment regimes, and accountability clarity.

By adjusting these parameters, users can observe how they influence key risk culture indicators like the proportion of self-raised issues, the effectiveness of fixes (root cause vs. superficial), employee perception of fairness, and overall willingness to report issues. The application simulates these interactions and presents the results through interactive visualizations and actionable recommendations.

### Purpose and Objectives

*   **Understand Key Concepts:** Gain insights into the concept of "Risk Culture" and its components.
*   **Analyze Influence:** Facilitate understanding of how leadership, supervision, incentives, punishment, and accountability impact risk culture indicators.
*   **Quantitative Impact:** Analyze the simulated quantitative effects of different cultural interventions.
*   **Identify Areas for Improvement:** Identify potential weak points in a simulated risk culture and generate concrete recommendations for strengthening it.

## Features

*   **Interactive Simulation:** Adjust parameters for Leadership Consistency, Supervisor Training Adherence, Punishment Regime, Incentive Alignment, and Accountability Clarity.
*   **Real-time Visualization:** See how changes in parameters affect simulated trends and relationships through dynamic plots.
*   **Key Indicators:** Visualize metrics like Self-Raised Issues, Root Cause Fixes, Superficial Fixes, Employee Perception of Fairness, and Willingness to Report Issues.
*   **Actionable Recommendations:** Receive generated recommendations based on the simulated outcomes.
*   **Data Overview:** Inspect the structure and summary statistics of both the initial synthetic data and the data after simulation.
*   **Informative "About" Section:** Learn about the core concepts, simulation methodology (including formulas), and references used in the lab.
*   **Sidebar Navigation:** Easy navigation between the simulation, data overview, and about pages.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

You need Python installed on your system. The application requires the following Python libraries:

*   `streamlit`
*   `pandas`
*   `numpy`
*   `plotly`

You can install them using pip:

```bash
pip install streamlit pandas numpy plotly
```

### Installation

1.  Clone this repository (or download the code files):

    ```bash
    git clone <repository_url> # Replace with the actual repository URL if available
    ```
    Alternatively, if you just have the files:
    Place `app.py` in the root directory and the three page files (`page1.py`, `page2.py`, `page3.py`) inside a subdirectory named `application_pages`.

2.  Navigate to the project directory:

    ```bash
    cd qu_risk_culture_lab # Or the name of your project directory
    ```

## Usage

To run the application, open your terminal or command prompt, navigate to the project directory (where `app.py` is located), and execute the following command:

```bash
streamlit run app.py
```

This will start the Streamlit server, and the application will open in your default web browser. If it doesn't open automatically, look for the local URL provided in the terminal output (usually `http://localhost:8501`).

*   Use the sidebar to navigate between the "Simulation and Visualizations", "Raw Data Overview", and "About This Lab" pages.
*   On the "Simulation and Visualizations" page, use the sliders and dropdowns in the sidebar to change the input parameters and observe how the visualizations and recommendations update in real-time.
*   The "Raw Data Overview" page shows the initial synthetic data and the data generated after applying your selected simulation parameters.
*   The "About This Lab" page provides context on the concepts and the simulation model.

## Project Structure

The project is organized as follows:

```
qu_risk_culture_lab/
├── app.py                      # Main Streamlit application entry point
└── application_pages/
    ├── __init__.py             # (Optional) Makes the directory a Python package
    ├── page1.py                # Code for the Simulation and Visualizations page
    ├── page2.py                # Code for the Raw Data Overview page
    └── page3.py                # Code for the About This Lab page
```

*   `app.py` handles the main layout, logo, title, description, sidebar navigation, and routing to different pages based on the user's selection.
*   The `application_pages` directory contains the logic and layout for each specific page within the application.
*   The `generate_synthetic_data` and `simulate_risk_culture_indicators` functions are defined and used within `page1.py` and `page2.py` to create and transform the data based on user inputs.

## Technology Stack

*   **Streamlit:** For building the interactive web application interface.
*   **Pandas:** For data manipulation and analysis (DataFrames).
*   **NumPy:** For numerical operations and generating synthetic data.
*   **Plotly Express:** For creating interactive visualizations (line, bar, scatter plots).

## Data Simulation Details

The application uses synthetically generated data to mimic risk culture metrics over time. The base data is created using random distributions. User inputs in the sidebar on the "Simulation and Visualizations" page influence this base data through defined simulation logic:

*   **Continuous Inputs (Leadership Consistency, Supervisor Training Adherence):** These inputs (sliders 0-100) adjust the base values proportionally. The formula used is:
    $$
    NewValue = OldValue + (Input - 50) \cdot 0.1
    $$
    An input of 50 represents the baseline, while values above or below 50 increase or decrease the corresponding metric.

*   **Categorical Inputs (Punishment Regime, Incentive Alignment, Accountability Clarity):** These inputs (dropdowns) apply multiplicative factors to relevant risk culture indicators to reflect their significant impact on behavior and outcomes (e.g., a 'Strict' punishment regime might reduce Willingness to Report Issues by a factor of 0.8).

All resulting simulated values are clipped to realistic ranges (e.g., proportions between 0 and 1, scale values between 0 and 10 or 0 and 100).

## Contributing

Contributions are welcome! If you'd like to contribute to this project, please follow these steps:

1.  Fork the repository.
2.  Create a new branch (`git checkout -b feature/your-feature-name`).
3.  Make your changes and commit them (`git commit -m 'Add some feature'`).
4.  Push to the branch (`git push origin feature/your-feature-name`).
5.  Open a Pull Request.

Please ensure your code adheres to good practices and includes necessary documentation.

## License

This project is licensed under the [LICENSE NAME] - see the LICENSE.md file for details (Note: Replace `[LICENSE NAME]` with the actual license, e.g., MIT, Apache 2.0, and include a `LICENSE.md` file in your repository).

## Contact

If you have any questions or feedback regarding this project, you can reach out to [Your Name/Organization Name] or through the resources provided by QuantUniversity.

---

*This README was generated based on the provided code for the Streamlit application.*

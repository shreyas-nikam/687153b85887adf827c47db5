# QuLab: Interactive Risk Management Framework with Stress Test Visualization

[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://your-streamlit-share-link.streamlit.app/)

## 📝 Project Description

QuLab is an interactive Streamlit application designed to explore and visualize the Risk Management Framework through the lens of stress test scenario simulation. It provides a dynamic platform for users to understand and visualize the potential impact of various stress test scenarios on a firm's financial resources. The primary objective is to enhance comprehension of how correlated threats can simultaneously affect multiple portfolios and processes within a financial institution.

This application allows users to simulate and visualize the outcomes of different stress test types: **Sensitivity**, **Scenario**, and **Firm-Wide** stress testing. It facilitates an understanding of the relationship between economic and market parameters and their ripple effects on crucial financial metrics such as income, costs, market risk losses, counterparty losses, credit losses, liquidity, provisions, reserves, and operational losses. Through interactive visualizations, QuLab illustrates financial trajectories under stress, correlations between impact metrics, and aggregated comparisons of losses.

## ✨ Features

*   **Flexible Data Loading**:
    *   Utilize a pre-built synthetic financial dataset for immediate exploration.
    *   Upload your own custom CSV files containing financial data (requires `Date`, `Base_Revenue`, `Base_Costs` columns).
*   **Robust Data Validation**: Ensures that uploaded data adheres to structural requirements (e.g., mandatory columns, no duplicate dates) to prevent errors.
*   **Multi-Type Stress Testing**:
    *   **Sensitivity Analysis**: Isolate and shock individual financial parameters (e.g., `Base_Revenue`, `Base_Costs`) to observe their specific impact.
    *   **Scenario Analysis**: Simulate broader economic downturns or specific adverse events that affect multiple base components proportionally.
    *   **Firm-Wide Stress Testing**: Model severe systemic crises that apply a broad, aggregate reduction across all base financial components.
*   **Interactive Parameter Control**: Adjust stress test parameters (e.g., shock magnitude, scenario severity factor, systemic crisis scale) using intuitive sliders and select boxes.
*   **Key Risk Metric Calculation**: Automatically computes and displays vital risk capacity metrics under stress, including:
    *   Initial Capital & Minimum Capital Remaining
    *   Capital Drawdown & Capital Drawdown Percentage
    *   Minimum Liquidity Position & Liquidity Shortfall
*   **Dynamic Visualizations**: Generate interactive Plotly charts to illustrate stress test results:
    *   **Trend Plots**: Visualize the trajectory of key financial components (e.g., Revenue, Costs, Net Earnings, Capital, Liquidity) over time under stress.
    *   **Relationship Plots**: Explore correlations and relationships between various financial metrics using scatter plots.
    *   **Comparison Plots**: Use bar charts to compare selected financial components side-by-side.
*   **User-Friendly Interface**: Built with Streamlit for a clean, intuitive, and responsive web application experience, accessible directly from your browser.

## 🚀 Getting Started

Follow these instructions to set up and run the QuLab application on your local machine.

### Prerequisites

*   Python 3.8+
*   `pip` (Python package installer)
*   `git` (optional, for cloning the repository)

### Installation

1.  **Clone the Repository (Optional, if you have the files locally):**

    ```bash
    git clone https://github.com/yourusername/QuLab.git
    cd QuLab
    ```
    (Replace `https://github.com/yourusername/QuLab.git` with the actual repository URL)

2.  **Create a Virtual Environment (Recommended):**

    ```bash
    python -m venv venv
    # On Windows:
    venv\Scripts\activate
    # On macOS/Linux:
    source venv/bin/activate
    ```

3.  **Install Dependencies:**
    Create a `requirements.txt` file in your project root with the following content:

    ```
    streamlit
    pandas
    plotly
    ```

    Then, install the dependencies:

    ```bash
    pip install -r requirements.txt
    ```

## 🖥️ Usage

1.  **Run the Streamlit Application:**

    Once all dependencies are installed, navigate to the project's root directory (where `app.py` is located) in your terminal and run:

    ```bash
    streamlit run app.py
    ```

2.  **Access the Application:**

    Your web browser should automatically open to the Streamlit application (usually at `http://localhost:8501`). If not, copy and paste the URL provided in your terminal into your browser.

3.  **Application Walkthrough:**

    *   **Navigation**: Use the sidebar to navigate between the different pages: "Data Loading & Selection", "Stress Test Simulation", and "Visualizations".
    *   **Data Loading & Selection**:
        *   Start by selecting your data source: "Synthetic Data" (pre-loaded for convenience) or "Upload CSV".
        *   If uploading, ensure your CSV file contains `Date`, `Base_Revenue`, and `Base_Costs` columns.
        *   The loaded data will be displayed.
    *   **Stress Test Simulation**:
        *   Once data is loaded, select a "Stress Test Type" from the sidebar: "Sensitivity", "Scenario", or "Firm-Wide".
        *   Adjust the relevant parameters (e.g., "Shock Magnitude", "Scenario Severity Factor", "Systemic Crisis Scale") using the sliders in the sidebar.
        *   The simulated stressed data will be displayed in a table.
    *   **Visualizations**:
        *   After running a simulation, this page will automatically display key "Risk Capacity Metrics".
        *   Select a "Plot Type" ("trend", "relationship", "comparison") from the dropdown.
        *   For "comparison" plots, select the two columns you wish to compare.
        *   Interactive Plotly charts will visualize the results, allowing you to zoom, pan, and hover for details.

## 📁 Project Structure

```
QuLab/
├── app.py
├── application_pages/
│   ├── page1.py
│   ├── page2.py
│   └── page3.py
├── requirements.txt
└── README.md
```

*   `app.py`: The main entry point for the Streamlit application. It sets up the page configuration, displays the main title, and handles navigation to different application pages.
*   `application_pages/`: A directory containing separate Python modules for each distinct page or functional section of the application, promoting modularity and organization.
    *   `page1.py`: Manages the "Data Loading & Selection" functionality, including loading synthetic data, handling CSV uploads, and performing data validation.
    *   `page2.py`: Implements the "Stress Test Simulation" logic, allowing users to select different stress test types and adjust parameters to simulate impacts on financial data.
    *   `page3.py`: Handles the "Visualizations" section, responsible for calculating risk capacity metrics and generating interactive charts (trend, relationship, comparison) using Plotly.
*   `requirements.txt`: Lists all Python dependencies required to run the application.
*   `README.md`: This comprehensive guide to the project.

## 🛠️ Technology Stack

*   **Python**: The core programming language.
*   **Streamlit**: The open-source app framework used to build and deploy the interactive web application.
*   **Pandas**: A powerful data manipulation and analysis library, used extensively for handling financial datasets.
*   **Plotly Express**: A high-level Python library that allows for rapid interactive data visualization.

## 🤝 Contributing

Contributions are welcome! If you have suggestions for improvements, bug fixes, or new features, please follow these steps:

1.  Fork the repository.
2.  Create a new branch (`git checkout -b feature/YourFeatureName`).
3.  Make your changes and commit them (`git commit -m 'Add new feature'`).
4.  Push to the branch (`git push origin feature/YourFeatureName`).
5.  Open a Pull Request.

## 📜 License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file (if present, otherwise assume standard MIT) for details.

## ✉️ Contact

For questions or feedback, please reach out to:
*   **Email**: info@quantuniversity.com
*   **Website**: [www.quantuniversity.com](https://www.quantuniversity.com)

## License

## QuantUniversity License

© QuantUniversity 2025  
This notebook was created for **educational purposes only** and is **not intended for commercial use**.  

- You **may not copy, share, or redistribute** this notebook **without explicit permission** from QuantUniversity.  
- You **may not delete or modify this license cell** without authorization.  
- This notebook was generated using **QuCreate**, an AI-powered assistant.  
- Content generated by AI may contain **hallucinated or incorrect information**. Please **verify before using**.  

All rights reserved. For permissions or commercial licensing, contact: [info@quantuniversity.com](mailto:info@quantuniversity.com)

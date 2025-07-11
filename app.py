import streamlit as st
st.set_page_config(page_title="QuLab", layout="wide")
st.sidebar.image("https://www.quantuniversity.com/assets/img/logo5.jpg")
st.sidebar.divider()
st.title("QuLab")
st.divider()
st.markdown(r"""
In this lab, **"Risk Management Framework Lab 1 - Stress Test Scenario Visualizer"**, we explore the crucial domain of financial stress testing. This interactive Streamlit application provides a robust platform for financial professionals to deeply understand and visualize the potential impact of various stress test scenarios on a firm's financial health.

The primary objective is to enhance comprehension of how correlated threats, as detailed in the 'PRMIA Operational Risk Manager Handbook', can simultaneously affect multiple portfolios and processes within a financial institution.

**Key Objectives of this Application:**
*   To enable users to simulate and visualize the outcomes of different stress test types: **Sensitivity**, **Scenario**, and **Firm-Wide** stress testing.
*   To facilitate an understanding of the relationship between economic and market parameters and their ripple effects on crucial financial metrics.
*   To clearly present estimated impacts on vital financial components such as income, costs, market risk losses, counterparty losses, credit losses, liquidity, provisions, reserves, and operational losses.
*   To offer interactive visualizations that illustrate financial trajectories under stress, correlations between impact metrics, and aggregated comparisons of losses.

This application is designed for risk analysts, portfolio managers, and regulatory compliance professionals, serving as a dynamic tool for comprehensive risk assessment, capital planning, and strategic decision-making in an uncertain financial landscape.

Navigate through the pages using the sidebar to load data, apply stress scenarios, and visualize the results.
""")

# Your code starts here
page = st.sidebar.selectbox(label="Navigation", options=["1. Data Loading & Validation", "2. Stress Test Simulation", "3. Risk Metrics & Visualizations"])

if page == "1. Data Loading & Validation":
    from application_pages.page1 import run_page1
    run_page1()
elif page == "2. Stress Test Simulation":
    from application_pages.page2 import run_page2
    run_page2()
elif page == "3. Risk Metrics & Visualizations":
    from application_pages.page3 import run_page3
    run_page3()
# Your code ends

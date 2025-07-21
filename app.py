
import streamlit as st
st.set_page_config(page_title="QuLab", layout="wide")
st.sidebar.image("https://www.quantuniversity.com/assets/img/logo5.jpg")
st.sidebar.divider()
st.title("QuLab")
st.divider()
st.markdown("""
In this lab, we will explore the Risk Management Framework through stress test scenario visualization.
This application provides an interactive platform to understand and visualize the potential impact of various stress test scenarios on a firm's financial resources.
The primary objective is to enhance comprehension of how correlated threats can simultaneously affect multiple portfolios and processes.

We will simulate and visualize the outcomes of different stress test types: Sensitivity, Scenario, and Firm-Wide stress testing.
We will facilitate an understanding of the relationship between economic and market parameters and their ripple effects on financial metrics.
We will clearly present estimated impacts on crucial financial components such as income, costs, market risk losses, counterparty losses, credit losses, liquidity, provisions, reserves, and operational losses.
We will offer interactive visualizations that illustrate financial trajectories under stress, correlations between impact metrics, and aggregated comparisons of losses.
""")
# Your code starts here
page = st.sidebar.selectbox(label="Navigation", options=["Data Loading & Selection", "Stress Test Simulation", "Visualizations"])
if page == "Data Loading & Selection":
    from application_pages.page1 import run_page1
    run_page1()
elif page == "Stress Test Simulation":
    from application_pages.page2 import run_page2
    run_page2()
elif page == "Visualizations":
    from application_pages.page3 import run_page3
    run_page3()
# Your code ends

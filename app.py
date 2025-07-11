
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

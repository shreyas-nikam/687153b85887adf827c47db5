
import streamlit as st

st.set_page_config(page_title="QuLab", layout="wide")

st.sidebar.image("https://www.quantuniversity.com/assets/img/logo5.jpg")
st.sidebar.divider()

st.title("QuLab")
st.divider()

st.markdown("""
In this lab, we will explore the concepts of risk-sensitive pricing and how it impacts portfolio profitability. We will use synthetic loan transactions to simulate different pricing strategies and analyze their results.

The key concepts covered in this lab include:

*   Expected Loss (EL)
*   Economic Capital (EC)
*   Net Risk Adjusted Reward (NRAR)
*   Risk-Adjusted Return on Risk-Adjusted Capital (RARORAC)

We will compare risk-insensitive and risk-sensitive pricing strategies to understand the importance of pricing discipline in maintaining a healthy and profitable portfolio.

All formulae in markdown must be enclosed in `$...\$` or `$$...$$` for proper Streamlit rendering.

For example:

$$ \text{Expected Loss} = \text{Principal} \times \text{Probability of Default}_{PD} \times \text{Loss Given Default}_{LGD} $$
""")

page = st.sidebar.selectbox(label="Navigation", options=["Introduction", "Simulation", "Conclusion"])

if page == "Introduction":
    from application_pages.introduction import run_introduction
    run_introduction()
elif page == "Simulation":
    from application_pages.simulation import run_simulation
    run_simulation()
elif page == "Conclusion":
    from application_pages.conclusion import run_conclusion
    run_conclusion()


import streamlit as st

def run_conclusion():
    st.header("Conclusion and Interpretation")
    st.markdown("""
    This section summarizes the key insights derived from the pricing strategy simulation.

    **Analysis:**
    Compare `RARORAC_Risk_Insensitive` and `RARORAC_Risk_Sensitive` for each deal. You will likely observe that not all deals pass the set hurdle rate in risk-insensitive pricing. Risk-sensitive pricing actively adjusts rates upward until the hurdle is cleared, or identifies when it's infeasible to meet it (marked as `NaN`).

    **What Does This Demonstrate?**
    -   **Risk-Insensitive Pricing** can lead to approving deals that generate negative value or insufficient returns, potentially driving down overall portfolio quality and shareholder value.
    -   **Risk-Sensitive Pricing** enforces financial discipline—only deals that adequately compensate for the risks to capital are accepted or repriced to be acceptable. Deals where it's impossible to meet the hurdle rate might be marked as `NaN` or a very high interest rate, indicating they should be rejected.

    **Conclusion:**
    Risk-sensitive pricing is essential for sustainable, profitable lending—it aligns incentives, manages credit quality, and protects economic capital.
    """)
    st.markdown("---")
    st.markdown("#### References")
    st.markdown("[1] PRMIA Operational Risk Manager Handbook, Updated November 2015.")

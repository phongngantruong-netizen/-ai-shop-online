import streamlit as st
import pandas as pd

# Professional web configuration for businesses
st.set_page_config(page_title="AI Profit Analyzer", layout="wide", page_icon="💸")

st.title("💸 AI Automated E-Commerce Profit Calculator")
st.success("⚡ EXCLUSIVE VIP TOOL - HELPS SHOP OWNERS TRACK CASH FLOW & PREVENT LOSSES")

# 3-step guide expander to help you automate user onboarding
with st.expander("📖 3-STEP USER GUIDE (LIFETIME USE)", expanded=True):
    st.markdown("""
    *   **Step 1:** Enter your total **Gross Revenue** from e-commerce platforms (TikTok, Shopee, Amazon...) in the first input box.
    *   **Step 2:** Look at the table below, click **"＋ Add row"** to enter your expenses (Wholesale cost, Platform fees, Ads spent, Shipping costs...).
    *   **Step 3:** Click the rocket button to let the AI automatically calculate your net profit and generate expense charts.
    """)

st.write("---")

# 1. Gross Revenue Input Box (Revenue before expenses)
st.subheader("💰 1. Total Platform Revenue:")
doanh_thu = st.number_input("Total revenue displayed on your platform app ($):", min_value=0.0, value=0.0, step=10.0)

st.write("---")

# 2. Dynamic Expense Input Table for Online Businesses
st.subheader("📉 2. Shop Operating Expenses Table:")

# Create default expense categories for ease of use
data_chi_phi_mac_dinh = pd.DataFrame([
    {"Expense Category": "Wholesale / COGS", "Amount ($)": 0.0},
    {"Expense Category": "Platform Fees (%)", "Amount ($)": 0.0},
    {"Expense Category": "Advertising Spent (Ads)", "Amount ($)": 0.0},
    {"Expense Category": "Shipping / Packaging Cost", "Amount ($)": 0.0}
])

# Activate Streamlit's dynamic row editing feature
bang_chi_phi = st.data_editor(
    data_chi_phi_mac_dinh,
    num_rows="dynamic", # Users can click "+" to add other costs like "Livestream Host Salary"
    use_container_width=True
)

st.write("---")

# 3. Button to trigger Pandas AI Engine for Net Profit Calculation
if st.button("🚀 ACTIVATE AI TO CALCULATE NET PROFIT"):
    # Convert table data to Pandas DataFrame (Fixed your old bug here!)
    df_chi_phi = pd.DataFrame(bang_chi_phi)
    
    # Calculate Total Expenses
    tong_chi_phi = df_chi_phi["Amount ($)"].sum()
    
    # Calculate Net Profit (Take-home money)
    loi_nhuan_rong = doanh_thu - tong_chi_phi
    
    # Calculate Profit Margin (%)
    ty_suat = (loi_nhuan_rong / doanh_thu * 100) if doanh_thu > 0 else 0
    
    # Display results via high-converting Executive Dashboard Metrics
    c1, c2, c3 = st.columns(3)
    with c1:
        st.metric(label="📊 Total Operating Expenses", value=f"${tong_chi_phi:,.2f}")
    with c2:
        # Green text for profit, red alert text for loss
        if loi_nhuan_rong >= 0:
            st.metric(label="🤑 Actual Net Profit", value=f"${loi_nhuan_rong:,.2f}")
        else:
            st.metric(label="😭 Your Shop is In a LOSS", value=f"${loi_nhuan_rong:,.2f}", delta="- HIGH RISK!")
    with c3:
        st.metric(label="📈 Net Profit Margin", value=f"{ty_suat:.1f} %")
        
    # Handle visual celebration and charts
    st.write("---")
    if loi_nhuan_rong > 0:
        st.balloons() # Explode balloons to celebrate profitable shop
        st.success("🎉 Congratulations! Your shop is operating with great profit margins. Keep it up!")
        
        # Automatically generate bar chart of expense distribution
        st.write("📊 **Shop Expense Structure Breakdown Chart:**")
        st.bar_chart(df_chi_phi.set_index("Expense Category")["Amount ($)"])
    elif doanh_thu == 0 and tong_chi_phi == 0:
        st.info("💡 Please enter your revenue and expense data to let the AI calculate, boss!")
    else:
        st.error("🚨 Warning: Your expenses exceed your revenue! Check your ad spend or COGS immediately!")

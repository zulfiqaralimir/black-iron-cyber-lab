import streamlit as st

st.set_page_config(
    page_title="Security Log Analyzer",
    page_icon="🛡",
    layout="wide"
)

st.title("🛡 Security Log Analyzer")
st.write("Welcome to your cybersecurity tool! Use the sidebar to navigate.")

# Sidebar navigation
st.sidebar.title("Navigation")
page = st.sidebar.radio("Go to:", ["Upload Logs", "View Report", "Anomalies"])

if page == "Upload Logs":
    st.header("📁 Upload Log Files")
    st.write("Upload your `.log` or `.txt` files here. Functionality coming soon!")

elif page == "View Report":
    st.header("📊 Security Report")
    st.write("The report will appear here after logs are processed.")

elif page == "Anomalies":
    st.header("🚨 Detected Anomalies")
    st.write("Failed logins, brute-force attacks, and privilege escalations will be shown here.")

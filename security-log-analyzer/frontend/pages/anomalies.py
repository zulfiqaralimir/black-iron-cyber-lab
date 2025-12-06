import streamlit as st
import os
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../../")))

from backend.log_parser import analyze_log

st.title("🚨 Detected Anomalies")

UPLOAD_DIR = "uploaded_logs"

# Check uploaded files
if not os.path.exists(UPLOAD_DIR):
    st.warning("No log files found. Please upload logs first.")
else:
    files = os.listdir(UPLOAD_DIR)

    if len(files) == 0:
        st.warning("No files uploaded yet.")
    else:
        selected_file = st.selectbox("Select a log file:", files)

        if selected_file:
            file_path = os.path.join(UPLOAD_DIR, selected_file)

            st.info(f"Analyzing file: {selected_file}")

            results = analyze_log(file_path)

            # Failed logins
            failed_logins = results.get("failed_logins", [])

            st.subheader("🚫 Failed Login Attempts")
            st.write(f"**Total Failed Logins:** {len(failed_logins)}")

            if len(failed_logins) > 0:
                st.error("Potential brute-force activity detected!")
                st.code("\n".join(failed_logins), language="text")
            else:
                st.success("No anomalies found for failed logins.")

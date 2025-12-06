import streamlit as st
import os

UPLOAD_DIR = "uploaded_logs"

# Create folder if not exists
if not os.path.exists(UPLOAD_DIR):
    os.makedirs(UPLOAD_DIR)

st.title("📁 Upload Log Files")
st.write("Upload your `.log` or `.txt` files to analyze them.")

uploaded_file = st.file_uploader("Choose a log file", type=["log", "txt"])

if uploaded_file is not None:
    file_path = os.path.join(UPLOAD_DIR, uploaded_file.name)

    # Save file
    with open(file_path, "wb") as f:
        f.write(uploaded_file.getbuffer())

    st.success(f"File uploaded successfully: {uploaded_file.name}")
    st.info("You can now go to the **View Report** or **Anomalies** page to analyze your logs.")

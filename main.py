import streamlit as st
from src/api_server.py import process_data

st.title("🚀 ORION: AI-Driven Space Operations Dashboard")

if st.button("Run ORION AI"):
    st.write("Processing data with AI agents...")
    result = process_data()
    st.write(result)


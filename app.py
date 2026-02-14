import streamlit as st
from risk import score_url

st.title("SecureStack Scanner")

url = st.text_input("Enter URL")

if st.button("Scan"):
    st.write(score_url(url))

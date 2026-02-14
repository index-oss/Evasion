import streamlit as st

st.title("SecureStack Mini Demo")

url = st.text_input("Enter URL")

if st.button("Check"):
    if url.startswith("https://"):
        st.success("Looks Safe")
    else:
        st.error("Potentially Risky")

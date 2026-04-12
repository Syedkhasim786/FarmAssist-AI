import streamlit as st
from agent import agent

st.set_page_config(page_title="FarmAssist AI", layout="centered")

st.title("🌾 FarmAssist AI")
st.write("Your smart agriculture assistant")

query = st.text_input("Ask your question:")

if st.button("Get Advice"):
    if query:
        response = agent(query)
        st.success(response)

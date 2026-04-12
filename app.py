import streamlit as st
from agent import agent

st.set_page_config(page_title="FarmAssist AI", layout="centered")

st.title("🌾 FarmAssist AI")
st.markdown("### Smart Agriculture Assistant for Farmers 🇮🇳")

st.write("Ask about crops, soil, fertilizers, or seasons")

query = st.text_input("Enter your question:")

if st.button("Get Advice"):
    if query:
        with st.spinner("Analyzing..."):
            response = agent(query)
        st.success(response)

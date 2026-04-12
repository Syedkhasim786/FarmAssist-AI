import streamlit as st
from agent import agent

st.set_page_config(page_title="FarmAssist AI", layout="centered")

st.title("🌾 FarmAssist AI")
st.markdown("### Smart Agriculture Assistant 🇮🇳")

# Language selection
lang = st.selectbox("Select Language", ["english", "hindi", "telugu"])

query = st.text_input("Ask your question:")

if st.button("Get Advice"):
    if query:
        with st.spinner("Analyzing..."):
            response = agent(query, lang)
        st.success(response)

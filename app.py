import streamlit as st
from agent import agent

st.set_page_config(page_title="FarmAssist AI", layout="centered")
st.title("🌾 FarmAssist AI")
st.markdown("### Smart Agriculture Assistant 🇮🇳")

lang = st.selectbox("Select Language", ["english", "hindi", "telugu", "tamil", "kannada", "marathi"])

query = st.text_input("Ask your question:")

if st.button("Get Advice"):
    if query:
        lang_map = {
            "english": "English",
            "hindi": "Hindi (हिंदी)",
            "telugu": "Telugu (తెలుగు)",
            "tamil": "Tamil (தமிழ்)",
            "kannada": "Kannada (ಕನ್ನಡ)",
            "marathi": "Marathi (मराठी)",
        }
        lang_label = lang_map.get(lang, "English")

        # Wrap the query with strict language instructions
        enforced_query = f"""You are FarmAssist AI, an expert agriculture assistant for Indian farmers.
IMPORTANT: You MUST respond ONLY in {lang_label} language.
Do NOT write anything in English. Do NOT use English as a prefix or label.
Your entire response must be written in {lang_label} script only.

Farmer's question: {query}"""

        with st.spinner("Analyzing..."):
            response = agent(enforced_query, lang)
        st.success(response)
    else:
        st.warning("Please enter a question.")

from tools import *
from database import save_to_db
from transformers import pipeline

# Better model than GPT-2
generator = pipeline("text2text-generation", model="google/flan-t5-base")


def agent(query, lang="english"):
    q = query.lower()

    if "weather" in q:
        response = get_weather()

    elif "predict" in q:
        # Simple example (you can improve later)
        response = predict_crop("black", "summer")

    elif "soil" in q or "crop" in q:
        response = get_crop_recommendation(query)

    elif "season" in q:
        response = get_season_advice(query)

    elif "fertilizer" in q:
        response = get_fertilizer_advice(query)

    else:
        result = generator(query, max_length=100)
        response = result[0]['generated_text']

    # 🌐 Translate
    response = translate_response(response, lang)

    # 💾 Save memory
    save_to_db(query, response)

    return response

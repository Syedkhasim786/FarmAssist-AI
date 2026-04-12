from tools import *
from database import save_to_db

def agent(query, lang="english"):
    q = query.lower()

    if "weather" in q:
        response = get_weather()

    elif "predict" in q:
        response = predict_crop("black", "summer")

    elif "soil" in q or "crop" in q:
        response = get_crop_recommendation(query)

    elif "season" in q:
        response = get_season_advice(query)

    elif "fertilizer" in q:
        response = get_fertilizer_advice(query)

    else:
        response = "I can help with crops, soil, weather, fertilizer, and predictions."

    response = translate_response(response, lang)
    save_to_db(query, response)

    return response

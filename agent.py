from tools import *
from database import save_to_db

def agent(query, lang="english"):
    q = query.lower()

    if "weather" in q:
        key = get_weather()

    elif "predict" in q:
        key = predict_crop("black", "summer")

    elif any(word in q for word in ["season", "summer", "winter", "rainy", "monsoon", "kharif", "rabi"]):
        key = get_season_advice(query)

    elif any(word in q for word in ["soil", "crop", "grow", "plant", "cultivate", "sow", "recommend"]):
        key = get_crop_recommendation(query)

    elif any(word in q for word in ["fertilizer", "fertiliser", "manure", "compost", "nutrient", "urea"]):
        key = get_fertilizer_advice(query)

    else:
        key = "fallback"

    response = translate_response(key, lang)
    save_to_db(query, response)
    return response

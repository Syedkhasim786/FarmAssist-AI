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

    # ✅ Improved fallback (what you wanted)
    else:
        if lang == "telugu":
            response = "క్షమించండి, దీనిపై నాకు సమాచారం లేదు. దయచేసి పంటలు, మట్టి, వాతావరణం లేదా ఎరువుల గురించి అడగండి."
        elif lang == "hindi":
            response = "क्षमा करें, मुझे इस विषय में जानकारी नहीं है। कृपया फसल, मिट्टी, मौसम या उर्वरक के बारे में पूछें।"
        else:
            response = "Sorry, I don't have information on that. Please ask about crops, soil, weather, fertilizer, or crop prediction."

    response = translate_response(response, lang)
    save_to_db(query, response)

    return response

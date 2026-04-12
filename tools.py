def get_crop_recommendation(query):
    query = query.lower()

    if "black soil" in query:
        return "Cotton, soybean, and sunflower grow well in black soil."
    elif "sandy" in query:
        return "Groundnut, watermelon, and coconut are suitable for sandy soil."
    elif "loamy" in query:
        return "Wheat, sugarcane, rice, and vegetables grow well in loamy soil."
    else:
        return "Please specify soil type (black, sandy, loamy) for better advice."


def get_season_advice(query):
    query = query.lower()

    if "summer" in query:
        return "In summer, grow crops like maize, cotton, and groundnut. Ensure proper irrigation."
    elif "winter" in query:
        return "In winter, crops like wheat, mustard, and barley are suitable."
    elif "rainy" in query or "monsoon" in query:
        return "During monsoon, rice, maize, and pulses grow well."
    else:
        return "Specify season (summer, winter, rainy) for better advice."


def get_fertilizer_advice(query):
    return "Use nitrogen-rich fertilizers for leafy crops and phosphorus for root development. Organic compost is always beneficial."

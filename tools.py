def get_crop_recommendation(query):
    query = query.lower()

    if "black soil" in query:
        return "Cotton and soybean grow well in black soil."
    elif "sandy" in query:
        return "Groundnut, watermelon, and coconut are suitable for sandy soil."
    elif "loamy" in query:
        return "Wheat, sugarcane, and vegetables grow well in loamy soil."
    else:
        return "Please specify soil type for better recommendation."

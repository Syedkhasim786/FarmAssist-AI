import requests

# 🌱 Crop Recommendation
def get_crop_recommendation(query):
    query = query.lower()

    if "black soil" in query:
        return "Cotton, soybean, and sunflower grow well in black soil."
    elif "sandy" in query:
        return "Groundnut, watermelon, and coconut are suitable for sandy soil."
    elif "loamy" in query:
        return "Wheat, sugarcane, rice, and vegetables grow well in loamy soil."
    else:
        return "Please specify soil type (black, sandy, loamy)."


# 🌦️ Season Advice
def get_season_advice(query):
    query = query.lower()

    if "summer" in query:
        return "Grow maize, cotton, and groundnut in summer with proper irrigation."
    elif "winter" in query:
        return "Wheat, mustard, and barley are suitable for winter."
    elif "rainy" in query or "monsoon" in query:
        return "Rice, maize, and pulses grow well during monsoon."
    else:
        return "Specify season (summer, winter, rainy)."


# 🌿 Fertilizer Advice
def get_fertilizer_advice(query):
    return "Use nitrogen for leafy growth, phosphorus for roots, and compost for sustainability."


# 🌦️ Weather (placeholder)
def get_weather(city="Hyderabad"):
    return f"Weather feature coming soon for {city}."


# 📊 Crop Prediction
def predict_crop(soil, season):
    soil = soil.lower()
    season = season.lower()

    if soil == "black" and season == "summer":
        return "Predicted crop: Cotton"
    elif soil == "loamy" and season == "winter":
        return "Predicted crop: Wheat"
    elif soil == "sandy" and season == "summer":
        return "Predicted crop: Groundnut"
    else:
        return "Try rice or maize based on your conditions."


# 🌐 Translation (IMPROVED 🔥)
def translate_response(text, lang):
    text_lower = text.lower()

    # Telugu translations (basic mapping)
    if lang == "telugu":
        if "cotton" in text_lower:
            return "పత్తి, సోయాబీన్ మరియు సూర్యకాంతి పంటలు నల్ల మట్టిలో బాగా పెరుగుతాయి."
        elif "groundnut" in text_lower:
            return "వేరుశెనగ, పుచ్చకాయ మరియు కొబ్బరి ఇసుక మట్టిలో బాగా పెరుగుతాయి."
        elif "wheat" in text_lower:
            return "గోధుమలు, చెరకు, బియ్యం మరియు కూరగాయలు లోమీ మట్టిలో బాగా పెరుగుతాయి."
        elif "summer" in text_lower:
            return "వేసవిలో మక్కజొన్న, పత్తి మరియు వేరుశెనగ పంటలు వేయండి."
        elif "winter" in text_lower:
            return "శీతాకాలంలో గోధుమలు, ఆవాలు మరియు బార్లీ పంటలు అనుకూలం."
        elif "rainy" in text_lower or "monsoon" in text_lower:
            return "వర్షాకాలంలో బియ్యం, మక్కజొన్న మరియు పప్పుధాన్యాలు బాగా పెరుగుతాయి."
        else:
            return "క్షమించండి, దీనిపై నాకు సమాచారం లేదు. దయచేసి వ్యవసాయానికి సంబంధించిన ప్రశ్నలు అడగండి."

    # Hindi translations (basic mapping)
    elif lang == "hindi":
        if "cotton" in text_lower:
            return "कपास, सोयाबीन और सूरजमुखी काली मिट्टी में अच्छी तरह उगते हैं।"
        elif "groundnut" in text_lower:
            return "मूंगफली, तरबूज और नारियल रेतीली मिट्टी में अच्छे होते हैं।"
        elif "wheat" in text_lower:
            return "गेहूं, गन्ना, चावल और सब्जियां दोमट मिट्टी में अच्छी होती हैं।"
        elif "summer" in text_lower:
            return "गर्मी में मक्का, कपास और मूंगफली उगाएं।"
        elif "winter" in text_lower:
            return "सर्दी में गेहूं, सरसों और जौ उगाना अच्छा है।"
        elif "rainy" in text_lower or "monsoon" in text_lower:
            return "बरसात में धान, मक्का और दालें अच्छी होती हैं।"
        else:
            return "क्षमा करें, मुझे इस विषय में जानकारी नहीं है। कृपया कृषि से जुड़े प्रश्न पूछें।"

    # Default English
    return text

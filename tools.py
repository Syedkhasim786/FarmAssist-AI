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


# 🌦️ Weather API
def get_weather(city="Hyderabad"):
   api_key = "YOUR_API_KEY"
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"

    try:
        data = requests.get(url).json()
        temp = data["main"]["temp"]
        weather = data["weather"][0]["description"]
        return f"Weather in {city}: {temp}°C, {weather}"
    except:
        return "Weather data not available."


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
        return "Try rice or maize depending on conditions."


# 🌐 Language Translation
def translate_response(text, lang):
    if lang == "telugu":
        return "తెలుగు: " + text
    elif lang == "hindi":
        return "हिंदी: " + text
    return text

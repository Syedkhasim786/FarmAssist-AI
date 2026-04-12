import requests

def get_weather(city="Hyderabad"):
    api_key = "YOUR_API_KEY"  # get from OpenWeather
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"

    try:
        data = requests.get(url).json()
        temp = data["main"]["temp"]
        weather = data["weather"][0]["description"]
        return f"Current weather in {city}: {temp}°C, {weather}"
    except:
        return "Unable to fetch weather data"

import requests

# 🌱 Crop Recommendation
def get_crop_recommendation(query):
    query = query.lower()
    if "black soil" in query or "black" in query:
        return "cotton"
    elif "sandy" in query:
        return "groundnut"
    elif "loamy" in query:
        return "wheat"
    elif "red soil" in query or "red" in query:
        return "red_soil"
    else:
        return "specify_soil"

# 🌦️ Season Advice
def get_season_advice(query):
    query = query.lower()
    if "summer" in query:
        return "summer"
    elif "winter" in query:
        return "winter"
    elif "rainy" in query or "monsoon" in query:
        return "monsoon"
    else:
        return "specify_season"

# 🌿 Fertilizer Advice
def get_fertilizer_advice(query):
    return "fertilizer"

# 🌦️ Weather
def get_weather(city="Hyderabad"):
    return "weather_soon"

# 📊 Crop Prediction
def predict_crop(soil, season):
    soil = soil.lower()
    season = season.lower()
    if soil == "black" and season == "summer":
        return "predict_cotton"
    elif soil == "loamy" and season == "winter":
        return "predict_wheat"
    elif soil == "sandy" and season == "summer":
        return "predict_groundnut"
    else:
        return "predict_general"

# 🌐 Translation (Full Coverage)
TRANSLATIONS = {
    "english": {
        "cotton":          "Cotton, soybean, and sunflower grow well in black soil.",
        "groundnut":       "Groundnut, watermelon, and coconut are suitable for sandy soil.",
        "wheat":           "Wheat, sugarcane, rice, and vegetables grow well in loamy soil.",
        "red_soil":        "Ragi, groundnut, and cotton are suitable for red soil.",
        "specify_soil":    "Please specify soil type: black, sandy, loamy, or red.",
        "summer":          "Grow maize, cotton, and groundnut in summer with proper irrigation.",
        "winter":          "Wheat, mustard, and barley are suitable for winter.",
        "monsoon":         "Rice, maize, and pulses grow well during monsoon.",
        "specify_season":  "Please specify season: summer, winter, or rainy/monsoon.",
        "fertilizer":      "Use nitrogen for leafy growth, phosphorus for roots, and compost for sustainability.",
        "weather_soon":    "Weather feature coming soon for your city.",
        "predict_cotton":  "Predicted crop: Cotton (black soil + summer).",
        "predict_wheat":   "Predicted crop: Wheat (loamy soil + winter).",
        "predict_groundnut":"Predicted crop: Groundnut (sandy soil + summer).",
        "predict_general": "Try rice or maize based on your conditions.",
        "fallback":        "Sorry, I don't have information on that. Please ask about crops, soil, weather, fertilizer, or seasons.",
    },
    "telugu": {
        "cotton":          "పత్తి, సోయాబీన్ మరియు సూర్యకాంతి నల్ల మట్టిలో బాగా పెరుగుతాయి.",
        "groundnut":       "వేరుశెనగ, పుచ్చకాయ మరియు కొబ్బరి ఇసుక మట్టిలో అనుకూలంగా ఉంటాయి.",
        "wheat":           "గోధుమలు, చెరకు, వరి మరియు కూరగాయలు లోమీ మట్టిలో బాగా పెరుగుతాయి.",
        "red_soil":        "రాగి, వేరుశెనగ మరియు పత్తి ఎర్ర మట్టికి అనుకూలంగా ఉంటాయి.",
        "specify_soil":    "దయచేసి మట్టి రకాన్ని పేర్కొనండి: నల్ల, ఇసుక, లోమీ లేదా ఎర్ర మట్టి.",
        "summer":          "వేసవిలో మక్కజొన్న, పత్తి మరియు వేరుశెనగ పండించండి.",
        "winter":          "శీతాకాలంలో గోధుమలు, ఆవాలు మరియు బార్లీ అనుకూలంగా ఉంటాయి.",
        "monsoon":         "వర్షాకాలంలో వరి, మక్కజొన్న మరియు పప్పుధాన్యాలు బాగా పెరుగుతాయి.",
        "specify_season":  "దయచేసి సీజన్ పేర్కొనండి: వేసవి, శీతాకాలం లేదా వర్షాకాలం.",
        "fertilizer":      "ఆకుల పెరుగుదలకు నత్రజని, వేర్లకు భాస్వరం మరియు సేంద్రీయతకు కంపోస్ట్ వాడండి.",
        "weather_soon":    "వాతావరణ సేవ త్వరలో అందుబాటులోకి వస్తుంది.",
        "predict_cotton":  "అంచనా పంట: పత్తి (నల్ల మట్టి + వేసవి).",
        "predict_wheat":   "అంచనా పంట: గోధుమలు (లోమీ మట్టి + శీతాకాలం).",
        "predict_groundnut":"అంచనా పంట: వేరుశెనగ (ఇసుక మట్టి + వేసవి).",
        "predict_general": "మీ పరిస్థితుల ఆధారంగా వరి లేదా మక్కజొన్న ప్రయత్నించండి.",
        "fallback":        "క్షమించండి, దీనిపై నాకు సమాచారం లేదు. దయచేసి పంటలు, మట్టి, వాతావరణం లేదా ఎరువుల గురించి అడగండి.",
    },
    "hindi": {
        "cotton":          "कपास, सोयाबीन और सूरजमुखी काली मिट्टी में अच्छी तरह उगते हैं।",
        "groundnut":       "मूंगफली, तरबूज और नारियल रेतीली मिट्टी के लिए उपयुक्त हैं।",
        "wheat":           "गेहूं, गन्ना, चावल और सब्जियां दोमट मिट्टी में अच्छी होती हैं।",
        "red_soil":        "रागी, मूंगफली और कपास लाल मिट्टी के लिए उपयुक्त हैं।",
        "specify_soil":    "कृपया मिट्टी का प्रकार बताएं: काली, रेतीली, दोमट या लाल।",
        "summer":          "गर्मी में मक्का, कपास और मूंगफली उगाएं।",
        "winter":          "सर्दी में गेहूं, सरसों और जौ उगाना अच्छा है।",
        "monsoon":         "बरसात में धान, मक्का और दालें अच्छी होती हैं।",
        "specify_season":  "कृपया मौसम बताएं: गर्मी, सर्दी या बरसात।",
        "fertilizer":      "पत्तियों की वृद्धि के लिए नाइट्रोजन, जड़ों के लिए फॉस्फोरस और जैविकता के लिए कम्पोस्ट उपयोग करें।",
        "weather_soon":    "मौसम सुविधा जल्द ही उपलब्ध होगी।",
        "predict_cotton":  "अनुमानित फसल: कपास (काली मिट्टी + गर्मी)।",
        "predict_wheat":   "अनुमानित फसल: गेहूं (दोमट मिट्टी + सर्दी)।",
        "predict_groundnut":"अनुमानित फसल: मूंगफली (रेतीली मिट्टी + गर्मी)।",
        "predict_general": "आपकी स्थिति के अनुसार चावल या मक्का आज़माएं।",
        "fallback":        "क्षमा करें, मुझे इस विषय में जानकारी नहीं है। कृपया फसल, मिट्टी, मौसम या उर्वरक के बारे में पूछें।",
    },
    "tamil": {
        "cotton":          "கருப்பு மண்ணில் பருத்தி, சோயாபீன் மற்றும் சூரியகாந்தி நன்றாக வளரும்.",
        "groundnut":       "மணல் மண்ணில் கடலை, தர்பூசணி மற்றும் தேங்காய் பயிரிடலாம்.",
        "wheat":           "களிமண்ணில் கோதுமை, கரும்பு, அரிசி மற்றும் காய்கறிகள் நன்றாக வளரும்.",
        "red_soil":        "சிவப்பு மண்ணுக்கு கேழ்வரகு, கடலை மற்றும் பருத்தி ஏற்றது.",
        "specify_soil":    "தயவுசெய்து மண் வகையை குறிப்பிடுங்கள்: கருப்பு, மணல், களிமண் அல்லது சிவப்பு.",
        "summer":          "கோடையில் மக்காச்சோளம், பருத்தி மற்றும் கடலை பயிரிடுங்கள்.",
        "winter":          "குளிர்காலத்தில் கோதுமை, கடுகு மற்றும் வாற்கோதுமை ஏற்றது.",
        "monsoon":         "மழைக்காலத்தில் அரிசி, மக்காச்சோளம் மற்றும் பயறு வகைகள் நன்றாக வளரும்.",
        "specify_season":  "தயவுசெய்து பருவத்தை குறிப்பிடுங்கள்: கோடை, குளிர் அல்லது மழை.",
        "fertilizer":      "இலை வளர்ச்சிக்கு நைட்ரஜன், வேர்களுக்கு பாஸ்பரஸ், நிலைத்தன்மைக்கு உரம் பயன்படுத்துங்கள்.",
        "weather_soon":    "வானிலை சேவை விரைவில் கிடைக்கும்.",
        "predict_cotton":  "கணிக்கப்பட்ட பயிர்: பருத்தி (கருப்பு மண் + கோடை).",
        "predict_wheat":   "கணிக்கப்பட்ட பயிர்: கோதுமை (களிமண் + குளிர்காலம்).",
        "predict_groundnut":"கணிக்கப்பட்ட பயிர்: கடலை (மணல் மண் + கோடை).",
        "predict_general": "உங்கள் நிலைமைகளின் அடிப்படையில் அரிசி அல்லது மக்காச்சோளம் முயற்சிக்கவும்.",
        "fallback":        "மன்னிக்கவும், இதுபற்றி என்னிடம் தகவல் இல்லை. பயிர், மண், வானிலை அல்லது உரம் பற்றி கேளுங்கள்.",
    },
    "kannada": {
        "cotton":          "ಕಪ್ಪು ಮಣ್ಣಿನಲ್ಲಿ ಹತ್ತಿ, ಸೋಯಾಬೀನ್ ಮತ್ತು ಸೂರ್ಯಕಾಂತಿ ಚೆನ್ನಾಗಿ ಬೆಳೆಯುತ್ತವೆ.",
        "groundnut":       "ಮರಳು ಮಣ್ಣಿನಲ್ಲಿ ಕಡಲೆಕಾಯಿ, ಕಲ್ಲಂಗಡಿ ಮತ್ತು ತೆಂಗಿನಕಾಯಿ ಸೂಕ್ತ.",
        "wheat":           "ಲೋಮಿ ಮಣ್ಣಿನಲ್ಲಿ ಗೋಧಿ, ಕಬ್ಬು, ಅಕ್ಕಿ ಮತ್ತು ತರಕಾರಿಗಳು ಚೆನ್ನಾಗಿ ಬೆಳೆಯುತ್ತವೆ.",
        "red_soil":        "ಕೆಂಪು ಮಣ್ಣಿಗೆ ರಾಗಿ, ಕಡಲೆಕಾಯಿ ಮತ್ತು ಹತ್ತಿ ಸೂಕ್ತ.",
        "specify_soil":    "ದಯವಿಟ್ಟು ಮಣ್ಣಿನ ಪ್ರಕಾರ ತಿಳಿಸಿ: ಕಪ್ಪು, ಮರಳು, ಲೋಮಿ ಅಥವಾ ಕೆಂಪು.",
        "summer":          "ಬೇಸಿಗೆಯಲ್ಲಿ ಮೆಕ್ಕೆಜೋಳ, ಹತ್ತಿ ಮತ್ತು ಕಡಲೆಕಾಯಿ ಬೆಳೆಯಿರಿ.",
        "winter":          "ಚಳಿಗಾಲದಲ್ಲಿ ಗೋಧಿ, ಸಾಸಿವೆ ಮತ್ತು ಬಾರ್ಲಿ ಸೂಕ್ತ.",
        "monsoon":         "ಮಳೆಗಾಲದಲ್ಲಿ ಅಕ್ಕಿ, ಮೆಕ್ಕೆಜೋಳ ಮತ್ತು ದ್ವಿದಳ ಧಾನ್ಯಗಳು ಚೆನ್ನಾಗಿ ಬೆಳೆಯುತ್ತವೆ.",
        "specify_season":  "ದಯವಿಟ್ಟು ಋತುವನ್ನು ತಿಳಿಸಿ: ಬೇಸಿಗೆ, ಚಳಿಗಾಲ ಅಥವಾ ಮಳೆಗಾಲ.",
        "fertilizer":      "ಎಲೆ ಬೆಳವಣಿಗೆಗೆ ಸಾರಜನಕ, ಬೇರುಗಳಿಗೆ ರಂಜಕ ಮತ್ತು ಸಾವಯವತೆಗೆ ಗೊಬ್ಬರ ಬಳಸಿ.",
        "weather_soon":    "ಹವಾಮಾನ ಸೇವೆ ಶೀಘ್ರದಲ್ಲೇ ಲಭ್ಯವಾಗುತ್ತದೆ.",
        "predict_cotton":  "ಊಹಿಸಿದ ಬೆಳೆ: ಹತ್ತಿ (ಕಪ್ಪು ಮಣ್ಣು + ಬೇಸಿಗೆ).",
        "predict_wheat":   "ಊಹಿಸಿದ ಬೆಳೆ: ಗೋಧಿ (ಲೋಮಿ ಮಣ್ಣು + ಚಳಿಗಾಲ).",
        "predict_groundnut":"ಊಹಿಸಿದ ಬೆಳೆ: ಕಡಲೆಕಾಯಿ (ಮರಳು ಮಣ್ಣು + ಬೇಸಿಗೆ).",
        "predict_general": "ನಿಮ್ಮ ಪರಿಸ್ಥಿತಿಗಳ ಆಧಾರದ ಮೇಲೆ ಅಕ್ಕಿ ಅಥವಾ ಮೆಕ್ಕೆಜೋಳ ಪ್ರಯತ್ನಿಸಿ.",
        "fallback":        "ಕ್ಷಮಿಸಿ, ಇದರ ಬಗ್ಗೆ ನನ್ನಲ್ಲಿ ಮಾಹಿತಿ ಇಲ್ಲ. ಬೆಳೆ, ಮಣ್ಣು, ಹವಾಮಾನ ಅಥವಾ ಗೊಬ್ಬರದ ಬಗ್ಗೆ ಕೇಳಿ.",
    },
    "marathi": {
        "cotton":          "काळ्या मातीत कापूस, सोयाबीन आणि सूर्यफूल चांगले वाढतात.",
        "groundnut":       "वालुकामय मातीत शेंगदाणे, टरबूज आणि नारळ योग्य आहेत.",
        "wheat":           "चिकणमातीत गहू, ऊस, तांदूळ आणि भाज्या चांगल्या वाढतात.",
        "red_soil":        "लाल मातीसाठी नाचणी, शेंगदाणे आणि कापूस योग्य आहेत.",
        "specify_soil":    "कृपया मातीचा प्रकार सांगा: काळी, वालुकामय, चिकणमाती किंवा लाल.",
        "summer":          "उन्हाळ्यात मका, कापूस आणि शेंगदाणे लावा.",
        "winter":          "हिवाळ्यात गहू, मोहरी आणि जव योग्य आहेत.",
        "monsoon":         "पावसाळ्यात तांदूळ, मका आणि डाळी चांगल्या वाढतात.",
        "specify_season":  "कृपया हंगाम सांगा: उन्हाळा, हिवाळा किंवा पावसाळा.",
        "fertilizer":      "पानांच्या वाढीसाठी नायट्रोजन, मुळांसाठी फॉस्फरस आणि सेंद्रियतेसाठी कंपोस्ट वापरा.",
        "weather_soon":    "हवामान सेवा लवकरच उपलब्ध होईल.",
        "predict_cotton":  "अंदाजित पीक: कापूस (काळी माती + उन्हाळा).",
        "predict_wheat":   "अंदाजित पीक: गहू (चिकणमाती + हिवाळा).",
        "predict_groundnut":"अंदाजित पीक: शेंगदाणे (वालुकामय माती + उन्हाळा).",
        "predict_general": "तुमच्या परिस्थितीनुसार तांदूळ किंवा मका वापरून पहा.",
        "fallback":        "माफ करा, याबद्दल माझ्याकडे माहिती नाही. पीक, माती, हवामान किंवा खताबद्दल विचारा.",
    },
}

def translate_response(text, lang):
    lang = lang.lower()
    translations = TRANSLATIONS.get(lang, TRANSLATIONS["english"])
    return translations.get(text, translations["fallback"])

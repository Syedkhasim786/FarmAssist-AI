def translate_response(text, lang):
    if lang == "telugu":
        return "తెలుగు: " + text
    elif lang == "hindi":
        return "हिंदी: " + text
    return text

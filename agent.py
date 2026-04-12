from tools import (
    get_crop_recommendation,
    get_season_advice,
    get_fertilizer_advice
)
from database import save_to_db
from transformers import pipeline

generator = pipeline("text-generation", model="gpt2")

def agent(query):
    query_lower = query.lower()

    if "soil" in query_lower or "crop" in query_lower:
        response = get_crop_recommendation(query)

    elif "season" in query_lower or "weather" in query_lower:
        response = get_season_advice(query)

    elif "fertilizer" in query_lower or "fertiliser" in query_lower:
        response = get_fertilizer_advice(query)

    else:
        result = generator(query, max_length=120, num_return_sequences=1)
        response = result[0]['generated_text']

    save_to_db(query, response)
    return response

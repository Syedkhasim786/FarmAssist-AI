from tools import get_crop_recommendation
from database import save_to_db
from transformers import pipeline

generator = pipeline("text-generation", model="gpt2")

def agent(query):
    query_lower = query.lower()

    if "soil" in query_lower or "crop" in query_lower:
        response = get_crop_recommendation(query)
    else:
        result = generator(query, max_length=100, num_return_sequences=1)
        response = result[0]['generated_text']

    save_to_db(query, response)
    return response

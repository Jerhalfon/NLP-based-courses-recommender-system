import pandas as pd
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity
from sentence_transformers import SentenceTransformer

def run_recommendations(user_input, courses, data):
    # Vector the data
    # Model instance
    model = SentenceTransformer('sentence-transformers/all-MiniLM-L6-v2')
    # Encode
    course_embeddings = courses
    
    user_embedded = model.encode(user_input)
    
    array_sim = {}
    # Loop in courses
    for i in range(len(course_embeddings)):
        # Pair of vectors to compare
        comp_pair = [user_embedded, course_embeddings[i]]
        # Calculation of the cosine_similarity
        array_sim[i] = (cosine_similarity(comp_pair[0].reshape(1, -1), comp_pair[1].reshape(1, -1)))
    
    sorted_dict = dict(sorted(array_sim.items(), key=lambda item: item[1], reverse=True))
    
    top_10_items = dict(list(sorted_dict.items())[:10])
    
    # Extract the keys from the top 10 dictionary
    top_10_keys = list(top_10_items.keys())

    # Filter the DataFrame based on the keys
    top_10_courses = data.loc[top_10_keys]
    bottom_10_items = dict(list(sorted_dict.items())[-10:])
    
    # Extract the keys from the top 10 dictionary
    bottom_10_keys = list(bottom_10_items.keys())

    # Filter the DataFrame based on the keys
    bottom_10_courses = data.loc[bottom_10_keys]
    
    return(top_10_courses)

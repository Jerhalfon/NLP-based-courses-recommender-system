from flask import Flask, render_template, request
from recommender_model import run_recommendations
import pandas as pd
import numpy as np
import pickle


app = Flask(__name__)

# Display the form page
@app.route('/')
def index():
    return render_template('index.html')

# Handle form submission and display courses results
@app.route('/submit', methods=['POST'])
def submit():
    # Process the form data and generate course recommendations
    subject = request.form['subject']
    technology = request.form['technology']
    problem = request.form['problem']
    answer = subject + technology + technology
    
    data = pd.read_csv("data/courses_udemy_last.csv")
    
    courses_embed = []
    # Open the file in read binary mode
    with open('course_embeddings_all_mini.pkl', 'rb') as file:
    # Use pickle to load the list from the file
        courses_embed = pickle.load(file)

    courses = run_recommendations(answer, courses_embed, data)

    # Convert the series to a list
    titles = courses['Title'].tolist()
    categories = courses["Category"].tolist()
    prices = courses["Price"].tolist()
    urls = courses["URL"].tolist()
    levels = courses["Level"].tolist()


    # Render the results page with the recommended courses
    return render_template('results.html', data={'courses': titles, 'categories': categories , 'prices' : prices, 'urls' : urls, 'levels' : levels})

if __name__ == '__main__':
    app.run()

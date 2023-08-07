# Course Recommender System based on Sentence Transformers

## Table of Contents
- [Introduction](#introduction)
- [Motivation](#motivation)
- [Features](#features)
- [How It Works](#how-it-works)
- [Technologies Used](#technologies-used)
- [Installation](#installation)
- [Usage](#usage)
- [Results](#results)
- [Contributing](#contributing)
- [License](#license)

## Introduction
Welcome to the Course Recommender System repository! This project aims to revolutionize the education sector by leveraging the power of Natural Language Processing (NLP) models, specifically Sentence Transformers. Our vision is to create a dynamic and personalized education system that caters to individual competencies and interests. The heart of our application is an NLP-driven recommender system that assists high school students in finding suitable courses on platforms like Udemy.

## Motivation
Traditional education systems often struggle to keep pace with the rapidly evolving tech landscape. The lack of personalization in curricula can lead to inefficiencies and mismatches between students' interests and educational offerings. Our goal is to provide a solution that empowers students to make informed decisions about their education journey, thereby creating a more effective and fulfilling learning experience.

## Features
- NLP-driven course recommendation based on user responses to a questionnaire.
- Utilization of Sentence Transformers to convert text into meaningful embedded vectors.
- Calculation of cosine similarity to measure the relationship between user inputs and course descriptions.
- Fast and efficient model based on the all-MiniLM-L6-v2 architecture from Hugging Face.
- Benchmarking against a random recommender using NDCG (Normalized Discounted Cumulative Gain) as the scoring metric.

## How It Works
1. Users provide responses to a questionnaire.
2. The application employs Sentence Transformers to convert open-text responses into embedded vectors.
3. Cosine similarity is computed between user embeddings and course descriptions.
4. Courses with the highest similarity scores are recommended to the user.

## Technologies Used
- Python
- Sentence Transformers
- Hugging Face Transformers
- Cosine Similarity
- Flask (for potential deployment)

## Installation
1. Clone this repository: `git clone https://github.com/your-username/course-recommender.git`
2. Navigate to the project directory: `cd course-recommender`
3. Install dependencies: `pip install -r requirements.txt`

## Usage
1. Run the application: `python app.py`
2. Access the web interface at `http://localhost:5000` (or follow deployment instructions if available).
3. Complete the questionnaire and receive personalized course recommendations.

## Results
Our recommender system has demonstrated significant improvements over a random recommender, with an NDCG@5 score of 0.51 compared to 0.256 from the benchmark. The model's ability to extract meaningful information from text showcases its potential to revolutionize education systems globally.

## Contributing
We welcome contributions from the community! If you'd like to get involved, please follow these steps:
1. Fork the repository.
2. Create a new branch: `git checkout -b feature-new-feature`.
3. Make your changes and commit them: `git commit -m 'Add some feature'`.
4. Push to the branch: `git push origin feature-new-feature`.
5. Open a pull request describing your changes.

## License
This project is licensed under the [MIT License](LICENSE).

---

Together, let's reshape the future of education through personalized learning experiences!

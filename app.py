import streamlit as st
import joblib
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import nltk
from nltk.sentiment import SentimentIntensityAnalyzer
from sklearn.feature_extraction.text import TfidfVectorizer

# Download NLTK resources (only if not available to avoid unnecessary downloads)
nltk.download('vader_lexicon', quiet=True)
sia = SentimentIntensityAnalyzer()

# Load trained sentiment model and vectorizer
try:
    model = joblib.load("sentiment_model.pkl")  # Load pre-trained SVM model
    vectorizer = joblib.load("tfidf_vectorizer.pkl")  # Load the vectorizer used during model training
except FileNotFoundError as e:
    st.error(f"Required model file not found: {e}")
    st.stop()

# Streamlit UI
st.title("Sentiment Analysis App")
st.subheader("Enter text to analyze sentiment:")

# User input
user_input = st.text_area("Input Text", "", height=150)

if st.button("Analyze Sentiment"):
    if user_input.strip():  # Ensures input is not empty or just whitespace
        try:
            # **Transform the input using the pre-trained vectorizer**
            review_vectorized = vectorizer.transform([user_input])

            # Predict sentiment using the trained model
            prediction = model.predict(review_vectorized)[0]  # Ensure input matches expected feature shape
            sentiment_label = "Positive 😊" if prediction == 1 else "Negative 😞"

        except Exception as e:
            st.error(f"Error in model prediction: {e}")
            st.stop()

        # Get sentiment scores using NLTK
        sentiment_scores = sia.polarity_scores(user_input)

        # Display results
        st.subheader("Predicted Sentiment:")
        st.markdown(f"**{sentiment_label}**")

        st.subheader("Sentiment Scores:")
        st.write(f"✔ **Positive:** {sentiment_scores['pos']}")
        st.write(f"⚖ **Neutral:** {sentiment_scores['neu']}")
        st.write(f"❌ **Negative:** {sentiment_scores['neg']}")

        # Visualizing sentiment breakdown
        fig, ax = plt.subplots()
        labels = ['Positive', 'Neutral', 'Negative']
        scores = [sentiment_scores['pos'], sentiment_scores['neu'], sentiment_scores['neg']]
        ax.bar(labels, scores, color=['green', 'gray', 'red'])
        ax.set_title("Sentiment Score Breakdown")
        ax.set_ylabel("Score")
        st.pyplot(fig)
    else:
        st.warning("Please enter meaningful text for analysis!")

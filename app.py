import streamlit as st
import pickle
import matplotlib.pyplot as plt
import nltk
from nltk.sentiment import SentimentIntensityAnalyzer

# Download NLTK Sentiment Analyzer
nltk.download('vader_lexicon')
sia = SentimentIntensityAnalyzer()

# Load trained sentiment model
model = pickle.load(open("sentiment_model.pkl", "rb"))  # import model

# Streamlit UI
st.title("Sentiment Analysis App")
st.write("Enter text to analyze sentiment!")

user_input = st.text_area("Input Text", "")

if st.button("Analyze Sentiment"):
    if user_input:
        # Apply sentiment model
        prediction = model.predict([user_input])[0]  # Modify this based on your model
        
        # Get sentiment score using NLTK
        sentiment_scores = sia.polarity_scores(user_input)
        
        # Map prediction to sentiment label
        sentiment_label = "Positive 😊" if prediction == 1 else "Negative 😞"

        st.subheader("Predicted Sentiment:")
        st.write(sentiment_label)
        
        st.subheader("Sentiment Scores:")
        st.write(f"Positive: {sentiment_scores['pos']}, Neutral: {sentiment_scores['neu']}, Negative: {sentiment_scores['neg']}")

        # Plot sentiment scores
        fig, ax = plt.subplots()
        labels = ['Positive', 'Neutral', 'Negative']
        scores = [sentiment_scores['pos'], sentiment_scores['neu'], sentiment_scores['neg']]
        ax.bar(labels, scores, color=['green', 'gray', 'red'])
        ax.set_title("Sentiment Score Breakdown")
        st.pyplot(fig)
    else:
        st.warning("Please enter some text!")


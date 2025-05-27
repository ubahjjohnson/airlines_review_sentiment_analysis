# Upgrade necessary packages
import streamlit as st
import joblib
import matplotlib.pyplot as plt
import nltk
from nltk.sentiment import SentimentIntensityAnalyzer

# # Download NLTK resources (only if not available to avoid unnecessary downloads)
# nltk.download('vader_lexicon', quiet=True)
# sia = SentimentIntensityAnalyzer()

# Load trained sentiment model
model = joblib.load("sentiment_model.pkl")

# Streamlit UI
st.title("Sentiment Analysis App")
st.subheader("Enter text to analyze sentiment:")

# User input
user_input = st.text_area("Input Text", "", height=150)

if st.button("Analyze Sentiment"):
    if user_input.strip():  # Ensures input is not empty or just whitespace
        # Predict sentiment using trained model
        try:
            prediction = model.predict([user_input])[0]  # Adjust based on your model
            sentiment_label = "Positive 😊" if prediction == 1 else "Negative 😞"
        except Exception as e:
            st.error(f"Error in model prediction: {e}")
            st.stop()

        # Get sentiment scores using NLTK
        sentiment_scores = model.polarity_scores(user_input)

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

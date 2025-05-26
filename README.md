# British Airways Customer Review Analysis

This repository contains the code and analysis of customer reviews for British Airways, scraped from `airlinequality.com`. The project aims to extract valuable insights into customer satisfaction, identify key areas of strength and weakness, and understand overall sentiment towards the airline.

## 🚀 Features

* **Web Scraping:** Automated collection of British Airways customer reviews from `airlinequality.com` (first 1000 pages).

* **Data Cleaning & Preprocessing:** Preparation of raw review data for analysis.

* **Comprehensive Analysis:**

  * Overall customer satisfaction assessment.

  * Detailed sentiment analysis of review texts.

  * Evaluation of aspect-specific ratings (e.g., seat comfort, food, service).

  * Analysis of customer recommendation rates.

  * Identification of trends in review volume over time.

* **Key Driver Identification:** Pinpointing specific factors influencing positive and negative customer experiences.

* **Interactive Visualizations:** Generation of various plots to effectively communicate findings.

## 📊 Data Source

Customer reviews were programmatically scraped from [airlinequality.com](https://www.airlinequality.com/). The dataset comprises reviews collected from the first 1000 pages dedicated to British Airways.

## 🛠️ Methodology

1. **Data Acquisition:** The `BeautifulSoup` library was used to parse HTML content and extract review details (e.g., review text, overall rating, aspect ratings, recommendation status) from `airlinequality.com`.

2. **Data Storage:** Scraped data was structured and stored efficiently, typically in a Pandas DataFrame.

3. **Sentiment Analysis:** NLTK's VADER (Valence Aware Dictionary and sEntiment Reasoner) was employed to classify review texts into positive, negative, and neutral sentiments based on their compound scores.

4. **Quantitative Analysis:** Statistical methods were applied to analyze numerical ratings and categorical data.

5. **Visualization:** `Matplotlib` and `Seaborn` were used to create a variety of plots for data exploration and presentation of insights.

## 📈 Key Metrics Analyzed

* **Overall Satisfaction Score:** Average rating and distribution of customer satisfaction.

* **Sentiment Score:** Distribution of positive, negative, and neutral sentiments derived from review texts.

* **Aspect-Specific Ratings:** Average ratings for different service aspects like seat comfort, food & beverages, cabin crew service, etc.

* **Frequency of Keywords/Topics:** Identification of frequently mentioned terms in reviews.

* **Review Volume Over Time:** Trends in the number of reviews submitted over yearly periods.

* **Recommendation Rate:** Percentage of customers who would recommend British Airways (based on 'True'/'false' responses).

## 📉 Visualizations Used

* **Bar Charts:** For distributions (e.g., overall ratings, sentiment categories) and comparisons (e.g., average aspect ratings).

* **Pie Charts:** To show proportions (e.g., sentiment distribution, recommendation rate).

* **Line Charts:** For visualizing trends over time (e.g., review volume).

* **Histograms:** To display the distribution of continuous variables (e.g., VADER compound scores).

* **Word Clouds:** For a quick visual representation of the most frequent words in reviews.

* **Stacked Bar Charts:** To compare proportions across different categories (e.g., recommendation rate by cabin class, sentiment distribution by recommendation group).

* **Box Plots:** To show the distribution of ratings across different groups (e.g., overall rating by recommendation status).

## 💻 Technologies Used

* **Python 3.x**

* **Pandas:** For data manipulation and analysis.

* **Beautiful Soup 4:** For web scraping.

* **NLTK:** Specifically, VADER for sentiment analysis.

* **Matplotlib:** For static plotting.

* **Seaborn:** For enhanced statistical data visualization.

* **WordCloud:** For generating word cloud visualizations.

## ▶️ How to Run

1. **Clone the repository:**

   ```
   git clone https://github.com/ubahjjohnson/british-airways-review-analysis.git
   cd british-airways-review-analysis
   
   ```

2. **Install dependencies:**

   ```
   pip install -r requirements.txt
   # Or manually:
   # pip install pandas beautifulsoup4 nltk matplotlib seaborn wordcloud
   
   ```

3. **Download NLTK VADER lexicon:**

   ```
   import nltk
   nltk.download('vader_lexicon')
   
   ```

4. **Execute the scraping script and Analysis Script**:

   ```
   python british-Airways-Reviews-Analysis.ipynb
   
   ```

   *(Note: The scraping process for 1000 pages can take a significant amount of time and may require handling rate limits or IP blocking. Ensure ethical scraping practices.)*

## 💡 Results & Insights

The analysis provides a clear picture of British Airways' performance from a customer perspective. Key insights include:

* The data indicates that 60% of customers would not recommend the flight, compared to 40% who would.
  
* Among all cabin classes, Economy Class shows the highest dissatisfaction, resulting in the highest number of customers who would not recommend the flight..

* Despite 57% of customers falling into the positive sentiment category, a portion of these individuals still chose not to recommend the flight.


## 📧 Contact

For any questions or collaborations, please contact [e-mail](mailto:ubahjohnson@gmail.com) or connect on [LinkedIn](https://www.linkedin.com/in/johnson-ubah).

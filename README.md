# Sentiment Analysis on Covid19 Tweets

## Overview
The COVID-19 pandemic had a profound impact globally, and during that time, social media became a crucial platform for information sharing and communication. Millions of tweets were posted daily, reflecting public sentiment about the pandemic. 
This project analyzes those tweets to understand how people felt about COVID-19 and to build a classification model to predict the sentiment of the tweets .

## Data Set
The dataset contains manually tagged tweets related to COVID-19. To ensure privacy, names and usernames have been anonymized. The dataset includes the following information:
1. **Location 📍** : The geographical location from where the tweet was posted
2. **Tweet At 📅** : The date on which the tweet was posted.
3.**Original Tweet 🐦** :  The content of the tweet.
4. **Sentiment 💬** : The sentiment of the tweet (Positive, Negative, Neutral).

## Data Analysis
### Sentiment Distribution
- **Sentiment Breakdown**: Out of all tweets provided in the dataset, 18.7% were classified as Neutral, 43.8% as Positive, and 37.5% as Negative.
### Word Cloud
- **Word Clouds**: We generated word clouds to visualize the most common words used in each sentiment category. Larger words represent higher frequency. These word clouds provided a clear visual representation of the language associated with each sentiment.
### Most Frequent Locations
- **Top Locations**: The most frequent tweet locations were London, England; United States; India; Australia; and Canada.
### Hashtags and Mentions
- **Top Hashtags**: The most frequently used hashtags were #coronavirus, #covid_19, #Coronavirus, #COVID2019, and #COVID19.
- **Top Mentions**: The most frequently mentioned accounts were @realdonaldtrump, @youtube, @borisjohnson, @tesco, and @amazon.
### Time Series Analysis
- **Tweet Frequency Over Time**: We plotted a line chart showing the number of tweets posted for different sentiments from mid-March to mid-April 2020. This analysis provided insights into how public sentiment evolved during the early stages of the pandemic.

## Text processing

Text preprocessing is a crucial step in preparing raw text for sentiment analysis. The objective is to clean the text by removing noise, such as punctuation, special characters, numbers, and irrelevant terms. Here's an overview of the preprocessing steps used:

-**Twitter Handles**: Removed Twitter handles (@user) as they do not contribute to sentiment analysis.
-**Links and Hashtags**: Removed links and hashtags to reduce noise in the data.
-**Punctuation and Special Characters**: Removed these elements to clean the text further.
-**Stop Words**: Removed common stop words using NLTK's stop words list.
-**Stemming**: Applied stemming to reduce words to their root form (e.g., "playing" to "play").
-**Tokenization**: Converted sentences into tokens (words) using NLTK's word_tokenize() function.
The preprocessing of the text data is an essential step as it makes the raw text ready for mining.

##  Challenges Faced:
- **Text Preprocessing**: Ensuring the text was adequately cleaned and preprocessed for sentiment analysis.
- **Vectorization**: Converting text data into numerical vectors for model training while retaining meaningful information.
- **Model Training**: Building and optimizing the classification model to improve performance.

## Conclusion:
This project provided valuable insights into public sentiment during the COVID-19 pandemic through the analysis of tweets. By preprocessing the text data and leveraging NLP techniques, we successfully built a sentiment classification model. The challenges faced, including text preprocessing, vectorization, and model training, were addressed to improve the accuracy and performance of the model. This analysis not only sheds light on the public's emotional response to the pandemic but also serves as a foundation for further research in social media sentiment analysis.

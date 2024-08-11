# Sentiment Analysis on Covid19 Tweets


## Overview
The COVID-19 pandemic had a profound impact globally, and during that time, social media became a crucial platform for information sharing and communication. Millions of tweets were posted daily, reflecting public sentiment about the pandemic. 

This project focuses on analyzing those past tweets to understand how people felt about COVID-19, using the BERT (Bidirectional Encoder Representations from Transformers) classifier model for sentiment analysis.

## Data Set

The tweets have been pulled from Twitter and manual tagging has been done then. The names and usernames have been given codes to avoid any privacy concerns. You can find the dataset here.

Columns:

1. Location 📍
2. Tweet At 📅
3. Original Tweet 🐦
4. Sentiment 💬

## Data Analysis
- In the data analysis part of the project, we started by examining the sentiment distribution in our dataset. We found that out of all tweets related to COVID-19, 19% were classified as neutral, 44% as positive, and 37% as negative.

- To get a sense of the most common words used in each category, we generated word clouds for the tweets in each sentiment category. The word clouds gave us a visual representation of the most frequent words used in each sentiment category, with larger words indicating higher frequency. Here are the word clouds for each category:

- I also created a bar chart to display the most frequent words for each category. This can help us identify the common themes or topics associated with each category of tweets.

I further explored the data to determine the most frequent origin countries of tweets. The most frequent origin countries of tweets in the analyzed dataset are: Unknown, England, United States, and India.

I also analyzed the most frequent hashtags and mentions in the dataset. The most frequently used hashtags were #coronavirus, #covid_19, #Coronavirus, #COVID2019, and #COVID19. The most frequently mentioned accounts were @realdonaldtrump, @youtube, @borisjohnson, @tesco, and @amazon.

Overall, these analyses provided valuable insights into the sentiment and content of COVID-19 related tweets, as well as the countries and accounts most commonly associated with these tweets.

## PROBLEM FACED:
Text preprocessing.
Vectorization.
Model Training and performance improvement

## CONCLUSION:
We conclude that the machine is generating the best results for the Logistic Regression with Grid Search CV (count vectorizer) model with an Accuracy of 78.28% followed by the Logistic Regression with Grid Search CV (TF/ID vectorizer) model with an Accuracy of 77.43%.
Also, we observed that no overfitting is seen for the data, and we can deploy this model.
Even being in the unprecedented situation of CoVid-19, people's positive sentiments outnumbered negative sentiments.
However, negative sentiments also has a significant chunk which various Government agencies, NGOs, etc can use to help boost the morale of the people and then
In the future ,we can repeat the analysis and compare it with the present sentimental analysis to gauge the impact of the initiatives on the ground.

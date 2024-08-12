# Sentiment Analysis on Covid19 Tweets


## Overview
The COVID-19 pandemic had a profound impact globally, and during that time, social media became a crucial platform for information sharing and communication. Millions of tweets were posted daily, reflecting public sentiment about the pandemic. 

This project focuses on analyzing those past tweets to understand how people felt about COVID-19 and build a classification model to predict the sentiment of the tweets .

## Data Set

The tweets have been pulled from Twitter and manual tagging has been done then. The names and usernames have been given codes to avoid any privacy concerns.

The following information in provided in the dataset:
1. Location 📍
2. Tweet At 📅
3. Original Tweet 🐦
4. Sentiment 💬

## Data Analysis

- In the data analysis part of the project, we started by examining the sentiment distribution in our dataset. We found that out of all tweets related to COVID-19, 18.7% were classified as neutral, 43.8% as positive, and 37.5% as negative.

- To get a sense of the most common words used in each category, we generated word clouds for the tweets in each sentiment category. The word clouds gave us a visual representation of the most frequent words used in each sentiment category, with larger words indicating higher frequency. Here are the word clouds for each category:

- I further explored the data to determine the most frequent location of tweets. The most frequent location of tweets in the analyzed dataset are: London, England, United States, India, Australia, Canada.

- I also analyzed the most frequent hashtags and mentions in the dataset. The most frequently used hashtags were #coronavirus, #covid_19, #Coronavirus, #COVID2019, and #COVID19. The most frequently mentioned accounts were @realdonaldtrump, @youtube, @borisjohnson, @tesco, and @amazon.

- Lastly, I ploted a line chart of the numerr of tweets posted for different sentiments from Mid-March to Mid-April in the yaer 2020.
  
Overall, these analyses provided valuable insights into the sentiment and content of COVID-19 related tweets, as well as the countries and accounts most commonly associated with these tweets.

## Text processing

The preprocessing of the text data is an essential step as it makes the raw text ready for mining.

*  The objective of this step is to clean noise those are less relevant to find 
the sentiment of tweets such as punctuation, special characters, numbers, and terms which don’t carry much weightage in context to the text.
*  As mentioned earlier, the tweets contain lots of twitter handles (@user). We will remove all these twitter handles from the data as they don’t convey much information.
* We are having twitter links in the data which are not useful for our Model. It will make our data noisy.
* As discussed, punctuations, numbers and special characters do not help much. It is better to remove them from the text just as we removed the twitter handles,links and hashtags.
* Stop words are those words in natural language that have a very little meaning, such as "is", "an", "the", etc.To remove stop words from a sentence, you can divide your text into words and then remove the word if it exits in the list of stop words provided by NLTK.
* Stemming is a rule-based process of stripping the suffixes (“ing”, “ly”, “es”, “ed”, “s” etc) from a word. For example – “play”, “player”, “played”, “plays” and “playing” are the different variations of the word – “play”.
* In tokenization we convert group of sentence into token . It is also called text segmentation or lexical analysis. It is basically splitting data into small chunk of words. Tokenization in python can be done by python NLTK library’s word_tokenize() function.

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

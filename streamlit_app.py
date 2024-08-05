import streamlit as st
import pandas as pd

st.title('Covid19 Tweets')

st.info('This app helps in predicting the sentiment of tweets')

with st.expander('Data'):
  try: 
    df = pd.read_csv("https://raw.githubusercontent.com/vrishti29/machineslearning/master/data/Coronavirus_Tweets.csv", encoding='utf-8')
  except UnicodeDecodeError:
    df = pd.read_csv("https://raw.githubusercontent.com/vrishti29/machineslearning/master/data/Coronavirus_Tweets.csv", encoding='latin1')

  df


with st.expander('Data visualization'):

  

with stsidebar:
  st.header('Input Features')
  sentiment = st.selectbox("Sentiment", ('Extremely Positive', 'Positive', 'Neutral', 'Neutral', 'Extremely Neutral'))

data = {'Sentiment': sentiment}

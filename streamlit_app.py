import streamlit as st
import pandas as pd

st.title('Machine Learning App')

st.info('This app builds a machine learnign Model')

with st.expander('Data'):
  try: 
    df = pd.read_csv("https://raw.githubusercontent.com/vrishti29/machineslearning/master/data/Coronavirus_Tweets.csv", encoding='utf-8')
  except UnicodeDecodeError:
    df = pd.read_csv("https://raw.githubusercontent.com/vrishti29/machineslearning/master/data/Coronavirus_Tweets.csv", encoding='latin1')

  df
  
  '''st.write('**X**')
  X = df.drop['Sentiment', axis = 1]
  X'''

  st.write('**y**')
  y = df.Sentiment
  y

with st.expander('Data visualization'):
  sentiment_count = df['Sentiment'].value_counts()
  st.scatter_chart(data=df, x='Sentiment', y='sentiment_count', color = 'Sentiment')


with stsidebar:
  st.header('Input Features')
  sentiment = st.selectbox("Sentiment", ('Extremely Positive', 'Positive', 'Neutral', 'Neutral', 'Extremely Neutral'))

data = {'Sentiment': sentiment}

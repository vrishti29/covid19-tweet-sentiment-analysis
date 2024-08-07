import streamlit as st
import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
from wordclous import WordCloud

st.title('Tweet Sentiment Analysis')
st.markdown("---", unsafe_allow_html=True)
st.info('This app shows the analysis of the tweeets')


file = st.file_uploader("Upload the File", type=["csv"])
df = pd.read_csv(file, encoding='latin1')

with st.expander('Data'):
  st.write(df)

#sentiment_count = df['Sentiment'].value_counts()
#with st.expander('Data visualization'):
#  st.scatter_chart(df[['Sentiment_count']])
  

with stsidebar:
  st.header('Input Features')
  sentiment = st.selectbox("Sentiment", ('Extremely Positive', 'Positive', 'Neutral', 'Neutral', 'Extremely Neutral'))

data = {'Sentiment': sentiment}

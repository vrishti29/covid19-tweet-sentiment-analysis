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

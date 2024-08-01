import streamlit as st
import pandas as pd

st.title('Machine Learning App')

st.info('This app builds a machine learnign Model')

df = pd.read_csv("https://raw.githubusercontent.com/vrishti29/machineslearning/master/data/Coronavirus_Tweets.csv")
df

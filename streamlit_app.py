import streamlit as st
import pandas as pd
from wordcloud import WordCloud
import matplotlib.pyplot as plt
import string

# Streamlit file uploader
uploaded_file = st.file_uploader("Choose a CSV file")

# Function to generate a word cloud
def generate_wordcloud(text):
    wordcloud = WordCloud(width=800, height=400, background_color='white').generate(text)
    return wordcloud

# Ensure the uploaded file is not None
if uploaded_file is not None:
    try:
        # Read the CSV file
        dataframe = pd.read_csv(uploaded_file, encoding='latin1')

        # Display the dataframe
        st.write('*Data*')
        st.write(dataframe)
            
        df_copy = dataframe.copy()
        df = df_copy[['OriginalTweet', 'Sentiment']]

        #data cleaning
        #converting to lower case
        df["OriginalTweet"] = df["OriginalTweet"].str.lower()

        #removing extra words
        df.loc[:, 'OriginalTweet'] = df['OriginalTweet'].str.replace('http\S+ | www.\S+', '', case = False)

        #removing hashtags
        df['clean_tweets'] = df['OriginalTweet'].str.replace("[^a-zA-Z#//]", " ")


        df['Sentiment'] = df['Sentiment'].replace({
        'Extremely Positive': 'Positive',
        'Extremely Negative': 'Negative'})

        sentiment_count = df_copy['Sentiment'].value_counts()
        sentiment_count_df = sentiment_count.reset_index()
        sentiment_count_df = df['Sentiment'].value_counts().to_list()
        labels = ['Positive','Negative','Netural']
        plt.figure(figsize=(10,8))
        plt.pie(x=sentiment_count_df, explode=[0.04, 0.04, 0.04], labels=labels, autopct="%.2f%%",radius=1.1)
        plt.title("Proportion of Sentiments", fontsize = 20)
        plt.legend(bbox_to_anchor = (1.05, 1), loc='upper left', borderaxespad = 0)
        st.pyplot(plt)

        
        
        # Assuming the text data is in a column named 'Original Tweet'
        if 'clean_tweets' in df.columns:
            text = ' '.join(df['clean_tweets'].dropna().astype(str).tolist())
            
            # Generate word cloud
            wordcloud = generate_wordcloud(text)
            
            # Display the word cloud using matplotlib
            fig, ax = plt.subplots()
            ax.imshow(wordcloud, interpolation='bilinear')
            ax.axis('off')
            st.pyplot(fig)
        else:
            st.error("The CSV file does not contain a 'Tweets' column.")


        
    except Exception as e:
        st.error(f"An error occurred: {e}")

else:
    st.warning("Please upload a CSV file.")

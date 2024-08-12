import streamlit as st
import pandas as pd
import numpy as np
from wordcloud import WordCloud, STOPWORDS
import matplotlib.pyplot as plt
import string
import seaborn as sns
import nltk 
from nltk.corpus import stopwords
import plotly.graph_objects as go
import plotly.express as px

nltk.download('stopwords')
nltk.download('wordnet')


st.markdown("<h1 style = 'text-align: center;'>Sentiment Analysis</h1>",unsafe_allow_html=True)
st.markdown("---", unsafe_allow_html=True)

# Streamlit file uploader
uploaded_file = st.file_uploader("Choose a CSV file")


# Function to generate a word cloud
def generate_wordcloud(text):
    wordcloud = WordCloud(width=800, height=400, background_color='white').generate(text)
    return wordcloud

def remove_punctuations(text):
    for punctuations in string.punctuation:
        text = text.replace(punctuations, '')
    return text

", ".join(stopwords.words('english'))
STOPW = set(stopwords.words('english'))
to_delete = ["no","nor","aren't",'couldn',"couldn't",'didn',"didn't",'doesn',
            "doesn't",'don',"don't",'hadn',"hadn't",'hasn',"hasn't",'haven',"haven't",'isn',
             "isn't",'mightn',"mightn't",'mustn',"mustn't",'needn',"needn't",'no','not', "shan't",
            'shan',"shan't",'shouldn',"shouldn't","that'll",'wasn',"wasn't",'weren',"weren't","won't",
            'wouldn',"wouldn't"]
STOPW.difference_update(to_delete)

def remove_stopwords(text):
    return [word for word in str(text).split() if word not in STOPW]

# Ensure the uploaded file is not None
if uploaded_file is not None:
    try:
        # Read the CSV file
        dataframe = pd.read_csv(uploaded_file, encoding='latin1')

        # Display the dataframe
        with st.expander('Data'):
            st.write(dataframe)

        #Display shape of dataset
        shape_dataset = dataframe.shape
        st.write('The dataset has', shape_dataset[0], 'rows and', shape_dataset[1], 'columns.')

        # Looking for Columns in dataset
        st.write("Columns in the dataset:", dataframe.columns.tolist())
        
        # Looking for unique values in columns of dataset
        for i in dataframe.columns:
            st.write("Total Unique Values in", i, "-", len(dataframe[i].unique()))

        # Checking null value
        print("Null values in each column:",dataframe.isnull().sum())

        # Checking  missing values in 'Location' column
        miss_value = dataframe['Location'].isnull().sum()/(dataframe.shape[0]) * 100
        st.write("We have {:.2f} % of missing values in 'Location' Column".format(miss_value))
        
        # Plot No- 1 : Heatmap of the missing values
        st.markdown("<h3 style = 'text-align: center;'>Heatmap for missing values</h3>",unsafe_allow_html=True)
        plt.figure(figsize=(15, 5))
        sns.heatmap(dataframe.isnull(), cbar=True, yticklabels=False)
        plt.xlabel("Column_Name", size=14, weight="bold")
        plt.title("Places of missing values in column",fontweight="bold",size=17)
        st.pyplot(plt)
        

        # Plot No- 2 : Countplot for top 15 locations
        st.markdown("<h3 style = 'text-align: center;'>Countplot for top 15 locations</h3>",unsafe_allow_html=True)
        plt.figure(figsize=(10,6))
        sns.countplot(y=dataframe.Location, order = dataframe.Location.value_counts().iloc[:15].index, palette ='icefire')
        plt.title('Top 15 locations')
        st.pyplot(plt)


        # Creating dataframe for location
        location = pd.DataFrame(dataframe['Location'].value_counts().sort_values(ascending=False))
        location = location.rename(columns={'Location':'count'})

        # Plot No- 3 : Interactive pie plot of Top 15 locations 
        st.markdown("<h3 style = 'text-align: center;'>Pie plot of Top 15 locations</h3>",unsafe_allow_html=True)
        data = {
            "values": location['count'][:15],
            "labels": location.index[:15],
            "domain": {"column": 0},
            "name": "Location Name",
            "hoverinfo":"label+percent+name",
            "hole": .3,
            "type": "pie"
        }
        layout = go.Layout(title="<b>Percentage of Location</b>", legend=dict(x=1.0, y=1.0, orientation="v"))
        data = [data]
        fig = go.Figure(data = data, layout = layout)
        fig.update_layout(title_x=0.5)
        st.plotly_chart(fig)


        #Tweet Date
        # Count value of TweetAt (Tweeting date)
        dataframe['TweetAt'].value_counts()

        # Checking unique Tweet dates in TweetAt
        dataframe.TweetAt.unique()

        # Plot No- 4 : Distribution of Dates of Tweets
        st.markdown("<h3 style = 'text-align: center;'>Distribution of Dates of Tweets</h3>",unsafe_allow_html=True)
        plt.figure(figsize=(10,6))
        sns.countplot(x='TweetAt', data=dataframe, palette ='Dark2')
        plt.xticks(rotation=45, ha='right')
        plt.title("Tweeting Dates")
        plt.ylabel("Count", fontsize = 12)
        plt.xlabel("TweetAt",fontsize = 12)
        st.pyplot(plt)

        # Grouping the data by 'TweetAt' and 'Sentiment' and counting the number of 'OriginalTweet'
        grp_tweetAt = dataframe.groupby(['TweetAt', 'Sentiment']).count()['OriginalTweet'].unstack()

        # Plot No - 5 : plot according to Number of tweets by sentiment over time
        st.markdown("<h3 style = 'text-align: center;'>Plot according to Number of tweets by sentiment over time</h3>",unsafe_allow_html=True)
        plt.figure(figsize=(12,6))
        grp_tweetAt=dataframe.groupby(['TweetAt','Sentiment']).size().unstack()
        grp_tweetAt.plot(ax=plt.gca())
        plt.xlabel('Date')
        plt.ylabel('Count')
        plt.title('Number of Tweets by Sentiment Over Time', fontweight='bold')
        plt.legend(title='Sentiment', loc='upper left')
        plt.grid(True)
        st.pyplot(plt)

        #Sentiment
        # Checking sentiment count value
        dataframe.Sentiment.value_counts()

        # Plot No- 6 : Sentiments count value as countplot 
        st.markdown("<h3 style = 'text-align: center;'>Sentiments count value as countplot</h3>",unsafe_allow_html=True)
        plt.figure(figsize=(10,6))
        splot = sns.countplot(x='Sentiment', data=dataframe, order=['Extremely Negative', 'Negative', 'Neutral', 'Positive', 'Extremely Positive'], palette="mako_r")
        # adding annotation
        for p in splot.patches:
            splot.annotate(format(p.get_height(), '.0f'), (p.get_x() + p.get_width() / 2., p.get_height()), ha = 'center', va = 'center', xytext = (0,9), textcoords = 'offset points')
        plt.title("Sentiment")
        plt.ylabel("Count", fontsize = 12)
        plt.xlabel("Sentiments",fontsize = 12)
        st.pyplot(plt)

        df_copy = dataframe.copy()
        df= df_copy[['OriginalTweet', 'Sentiment']]


        #data cleaning
        df['Sentiment'] = df['Sentiment'].replace({
        'Extremely Positive': 'Positive',
        'Extremely Negative': 'Negative'})

        #converting to lower case
        df["OriginalTweet"] = df["OriginalTweet"].str.lower()

        #removing extra words
        df['clean_tweets'] = df['OriginalTweet'].str.replace('http\S+ | www.\S+', '', case = False)

        #removing hashtags
        df['clean_tweets'] = df['clean_tweets'].str.replace("[^a-zA-Z#//]", " ")

        #remove punctuation
        df["clean_tweets"] = df['clean_tweets'].apply(lambda x : remove_punctuations(x))

        #remove stopwords
        df['clean_tweets'] = df['clean_tweets'].apply(lambda x: remove_stopwords(x))    

        # sentiments of tweets distribution table
        label_distribution = df.groupby('Sentiment').count()['OriginalTweet'].reset_index().sort_values(by='OriginalTweet', ascending=False)
        st.write(label_distribution)

        sentiment_count = df['Sentiment'].value_counts()
        sentiment_count_df = sentiment_count.reset_index()
        sentiment_count_df = df['Sentiment'].value_counts().to_list()
        labels = ['Positive','Negative','Netural']
        plt.figure(figsize=(10,8))
        plt.pie(x=sentiment_count_df, explode=[0.04, 0.04, 0.04], labels=labels, autopct="%.2f%%",radius=1.1)
        plt.title("Proportion of Sentiments", fontsize = 20)
        plt.legend(bbox_to_anchor = (1.05, 1), loc='upper left', borderaxespad = 0)
        st.pyplot(plt)

        word_counts = {label: [] for label in label_distribution.Sentiment}

        for text, target in zip(df['clean_tweets'], df['Sentiment']):
            if isinstance(text, str):
                word = text.split()
                word_counts[target].extend(word)

        fig, axes = plt.subplots(3, 1, figsize=(8, 30))


        
        # Assuming the text data is in a column named 'Original Tweet'
        
        
        cld_df = df[['clean_tweets', 'Sentiment']]
        with st.expander('cloud data'):
            st.write(cld_df)

        # Encoding the sentiments from 0 to 2 i.e., from extremely positive to extremely negative
        sentiment_map = {"Negative":3, "Neutral":2, "Positive":1}
        cld_df['Sentiment'] = cld_df['Sentiment'].map(sentiment_map)

        # Plot No- 24 : Most occuring words of all in Tweets
        if 'clean_tweets' in df.columns:
            all_words = ' '.join(df['clean_tweets'].dropna().astype(str).tolist())
            
            # Generate word cloud
            wordcloud = WordCloud(
                background_color = "white",
                width=800, 
                height=500, 
                random_state=21, 
                max_font_size=110, 
                stopwords = set(STOPWORDS), 
                colormap='Set2', 
                collocations=False,
            ).generate(all_words)
            
            # Display the word cloud using matplotlib
            fig, ax = plt.subplots(figsize = (10, 7))
            ax.imshow(wordcloud, interpolation='bilinear')
            ax.axis('off')
            st.pyplot(fig)

        else:
            st.error("The CSV file does not contain a 'Tweets' column.")        


        # Plot No- 26 : Most common occuring words in "Positive" sentiment
        Positive =' '.join([text for text in cld_df['clean_tweets'][cld_df['Sentiment'] == 1] if isinstance(text, str)])

        wordcloud = WordCloud(background_color = "pink", width=800, height=500, random_state=21, max_font_size=110, stopwords = set(STOPWORDS),colormap='brg',collocations=False).generate(Positive)
        plt.figure(figsize=(10, 7))
        plt.imshow(wordcloud, interpolation="bilinear")
        plt.axis('off')
        st.pyplot(plt)

        # Plot No- 27 : Most common occuring words in "Neutral" sentiment
        Neutral =' '.join([text for text in cld_df['clean_tweets'][cld_df['Sentiment'] == 2]])

        wordcloud = WordCloud(background_color = "white", width=800, height=500, random_state=21, max_font_size=110, stopwords = set(STOPWORDS),colormap='nipy_spectral',collocations=False).generate(Neutral)
        plt.figure(figsize=(10, 7))
        plt.imshow(wordcloud, interpolation="bilinear")
        plt.axis('off')
        st.pyplot(plt)

        # Plot No- 28 : Most common occuring words in "Negative" sentiment
        Negative =' '.join([text for text in cld_df['clean_tweets'][cld_df['Sentiment'] == 3]])

        wordcloud = WordCloud(width=800, height=500, random_state=21, max_font_size=110, stopwords = set(STOPWORDS),colormap='prism',collocations=False).generate(Negative)
        plt.figure(figsize=(10, 7))
        plt.imshow(wordcloud, interpolation="bilinear")
        plt.axis('off')
        st.pyplot(plt)





        
    except Exception as e:
        st.error(f"An error occurred: {e}")

else:
    st.warning("Please upload a CSV file.")

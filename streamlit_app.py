import streamlit as st
import pandas as pd
import numpy as np
from wordcloud import WordCloud
import matplotlib.pyplot as plt
import string
import seaborn as sns
import nltk 
from nltk.corpus import stopwords
import plotly.graph_objects as go

nltk.download('stopwords')
nltk.download('wordnet')


st.markdown("<h1 style = 'text-align: center;'>Sentiment Analysis</h1>",unsafe_allow_html=True)
st.markdown("---", unsafe_allow_html=True)

# Streamlit file uploader
uploaded_file = st.file_uploader("Choose a CSV file")

# Plot No- 1 : Heatmap of the missing values
def plot_missing_values_heatmap(dataframe):
    plt.figure(figsize=(15, 5))
    sns.heatmap(dataframe.isnull(), cbar=True, yticklabels=False)
    plt.xlabel("Column_Name", size=14, weight="bold")
    plt.title("Places of missing values in column",fontweight="bold",size=17)
    st.pyplot(plt)

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
        
        #Heatmap for missing values
        st.markdown("<h3 style = 'text-align: center;'>Heatmapf or missing values</h3>",unsafe_allow_html=True)
        st.write(plot_missing_values_heatmap)
        

        # Looking the count value of different Location 
        st.write(dataframe.Location.value_counts().head(15))
        
        
        # Looking for the unique location values in the dataset
        st.write(dataframe.Location.unique())

        # Plot No- 2 : Countplot for top 15 locations
        plt.figure(figsize=(10,6))
        sns.countplot(y=dataframe.Location, order = dataframe.Location.value_counts().iloc[:15].index, palette ='icefire')
        plt.title('Top 15 locations')
        st.pyplot(plt)

        # Creating dataframe for location
        location = pd.DataFrame(dataframe['Location'].value_counts().sort_values(ascending=False))
        location = location.rename(columns={'Location':'count'})

        # Plot No- 3 : Interactive pie plot of Top 15 locations 
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

        # Plot No- 4
        # Distribution of Dates of Tweets
        plt.figure(figsize=(10,6))
        sns.countplot(x='TweetAt', data=dataframe, palette ='Dark2')
        plt.xticks(rotation=45, ha='right')
        plt.title("Tweeting Dates")
        plt.ylabel("Count", fontsize = 12)
        plt.xlabel("TweetAt",fontsize = 12)
        st.pyplot(plt)


        #Sentiment
        # Checking sentiment count value
        dataframe.Sentiment.value_counts()
        # Plot No- 5
        # Plotting the Sentiments count value as countplot 
        plt.figure(figsize=(10,6))
        splot = sns.countplot(x='Sentiment', data=dataframe, order=['Extremely Negative', 'Negative', 'Neutral', 'Positive', 'Extremely Positive'], palette="mako_r")
        # adding annotation
        for p in splot.patches:
            splot.annotate(format(p.get_height(), '.0f'), (p.get_x() + p.get_width() / 2., p.get_height()), ha = 'center', va = 'center', xytext = (0,9), textcoords = 'offset points')
        plt.title("Sentiment")
        plt.ylabel("Count", fontsize = 12)
        plt.xlabel("Sentiments",fontsize = 12)
        st.pyplot(plt)


        # Grouping the data by 'TweetAt' and 'Sentiment' and counting the number of 'OriginalTweet'
        grp_tweetAt = dataframe.groupby(['TweetAt', 'Sentiment']).count()['OriginalTweet'].unstack()

        # Plotting the grouped data
        plt.figure(figsize=(12, 6))
        grp_tweetAt.plot(ax=plt.gca())  # Use ax=plt.gca() to plot on the same axes

        plt.ylabel('Count')
        plt.title('Original Tweet Count by Sentiment Over Time', fontweight='bold')
        plt.legend(title='Sentiment')
        st.write(plt)

        df_copy = dataframe.copy()
        df = df_copy[['OriginalTweet', 'Sentiment']]

        #data cleaning
        df['Sentiment'] = df['Sentiment'].replace({
        'Extremely Positive': 'Positive',
        'Extremely Negative': 'Negative'})

        #converting to lower case
        df["OriginalTweet"] = df["OriginalTweet"].str.lower()

        #removing extra words
        df.loc[:, 'OriginalTweet'] = df['OriginalTweet'].str.replace('http\S+ | www.\S+', '', case = False)

        #removing hashtags
        df['clean_tweets'] = df['OriginalTweet'].str.replace("[^a-zA-Z#//]", " ")

        #remove punctuation
        df["clean_tweets"] = df['clean_tweets'].apply(lambda x : remove_punctuations(x))

        #remove stopwords
        df['clean_tweets'] = df['clean_tweets'].apply(lambda x: remove_stopwords(x))    

        # sentiments of tweets distribution table
        label_distribution = df.groupby('Sentiment').count()['OriginalTweet'].reset_index().sort_values(by='OriginalTweet', ascending=False)
        st.write(label_distribution(cmap='winter'))

        


        word_counts = {label: [] for label in label_distribution.Sentiment}

        for text, target in zip(df['clean_tweets'], df['Sentiment']):
            text = [word for word in text.split()]
            word_counts[target].extend(text)

        fig, axes = plt.subplots(3, 1, figsize=(8, 30))

        for axis, (target, words) in zip(axes.flatten(), word_counts.items()):
            bar_info = pd.Series(words).value_counts()[:20]
            sns.barplot(x=bar_info.values, y=bar_info.index, ax=axis)
            axis.set_title(f'Top 20 words for {target} sentiment')
        st.pyplot(plt)
        

        sentiment_count = df_copy['Sentiment'].value_counts()
        sentiment_count_df = sentiment_count.reset_index()
        sentiment_count_df = df['Sentiment'].value_counts().to_list()
        labels = ['Positive','Negative','Netural']
        plt.figure(figsize=(10,8))
        plt.pie(x=sentiment_count_df, explode=[0.04, 0.04, 0.04], labels=labels, autopct="%.2f%%",radius=1.1)
        plt.title("Proportion of Sentiments", fontsize = 20)
        plt.legend(bbox_to_anchor = (1.05, 1), loc='upper left', borderaxespad = 0)
        st.pyplot(plt)

        fig, axes = plt.subplots(3, 1, figsize=(8, 30))

        for axis, (target, words) in zip(axes.flatten(), word_counts.items()):
            bar_info = pd.Series(words).value_counts()[:20]
            sns.barplot(x=bar_info.values, y=bar_info.index, ax=axis)
            axis.set_title(f'Top 20 words for {target} sentiment')
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

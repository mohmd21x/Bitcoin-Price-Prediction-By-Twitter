import pandas as pd
import numpy as np
import nltk
import re
nltk.download("stopwords")
from nltk.corpus import stopwords
from nltk.stem.porter import *

from nltk.sentiment.vader import SentimentIntensityAnalyzer

nltk.download('vader_lexicon')
nltk.download('wordnet')
nltk.download('omw-1.4')

class Sentiment:
    def __init__(self,data,label):
        """A class for sentiment analysis
        data--> The data to be analyzed
        label--> The name of the label where the texts are located """
        self.df = data
        self.label=label
        self.sid = SentimentIntensityAnalyzer()


    def tweet_to_words(self,tweet):
        ''' Convert tweet text into a sequence of words '''
        
        # convert to lowercase
        text = tweet.lower()
        # remove non letters
        text = re.sub(r"[^a-zA-Z0-9]", " ", text)
        # tokenize
        words = text.split()
        # remove stopwords
        # words = [w for w in words if w not in stop_words]
        # apply stemming
        words = [nltk.wordnet.WordNetLemmatizer().lemmatize(w) for w in words]
        # return list
        return words

    def apply_to_data_tweet_to_words(self):
        self.df["cleantext"]=self.df[self.label].apply(self.tweet_to_words)
        print(u"-----apply_to_data_tweet_to_words-----\u2713")

    def unlist(self,mylist):
            return " ".join(mylist)

    def compute_vader_scores(self):
        self.df["comp"] = self.df["cleantext"].apply(lambda x: self.sid.polarity_scores(self.unlist(x))["compound"])
        self.df['cleantext'] = self.df["cleantext"].apply(lambda x: self.unlist(x))
        print(u"-----compute_vader_scores-----\u2713")
        
    def labeling(self,comp):
        if comp >=0.15:
             l = 1 # Positive
        elif comp <=-0.15:
            l = -1 # Negative 
        else :
            l = 0
        return l
        
    def labeling_data(self):
        self.df["label"]=self.df["comp"].apply(self.labeling)
        print(u"-----labeling_data-----\u2713")

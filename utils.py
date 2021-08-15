import csv
from sentiment.base import SentimentModel

import re
import ssl

import nltk
from nltk.stem.wordnet import WordNetLemmatizer
from nltk.corpus import stopwords

def clean_reviews(reviews):
    #create a list of stop words
    stop_words = set(stopwords.words("english"))

    add_stopwords = ["photo", "camera", "app"]
    stop_words = stop_words.union(add_stopwords)

    clean_descriptions = []
    for review in reviews:
        review = review.lower()
        
        #remove punctuation
        review = re.sub('[^a-zA-Z]', ' ', review)
        
        #remove tags
        review = re.sub("&lt;/?.*?&gt;"," &lt;&gt; ", review)
        
        #remove special characters and digits
        review = re.sub("(\\d|\\W)+"," ", review)
        
        split_text = review.split()
        
        #Lemmatisation
        lem = WordNetLemmatizer()
        split_text = [lem.lemmatize(word) for word in split_text if not word in stop_words and len(word) >2] 
        split_text = " ".join(split_text)
        clean_descriptions.append(split_text)

    return 

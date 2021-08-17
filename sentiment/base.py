import csv
#import dependencies
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import re

from sklearn import preprocessing, decomposition, model_selection, metrics, pipeline
from sklearn.feature_extraction.text import TfidfVectorizer, CountVectorizer
from sklearn.cluster import KMeans

import nltk
from nltk.stem.wordnet import WordNetLemmatizer
from nltk.corpus import stopwords

# field names 
fields = ['rating', 'date', 'title', 'review'] 
    
# name of csv file 
filename = "app_store_reviews.csv"

class SentimentModel():

    def __init__(self, reviews):
        stop_words = set(stopwords.words("english"))
        add_stopwords = ["photo", "camera", "app"]
        self.stop_words = stop_words.union(add_stopwords)

        self.modifiedReviews = self.preprocess(reviews)
        self.vec_text, self.words = self.tfv()
        self.kmeans = self.kmeans()

    def clean_reviews(self, reviews):

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
            split_text = [lem.lemmatize(word) for word in split_text if not word in self.stop_words and len(word) >2] 
            split_text = " ".join(split_text)
            clean_descriptions.append(split_text)

        return pd.DataFrame(clean_descriptions)

    def preprocess(self, reviews):

        modifiedReviews = pd.DataFrame()
            # writing to csv file 
        with open(filename, 'w') as csvfile: 
            # creating a csv writer object 
            csvwriter = csv.writer(csvfile) 
                
            # writing the fields 
            csvwriter.writerow(fields)

            modifiedReviews['date'] = reviews['date'].dt.strftime("%b%d%Y")
            modifiedReviews['review'] = reviews['review'].str.replace('\n', ' ')
            modifiedReviews['review_length'] = reviews['review'].str.len()
            modifiedReviews['titlelength'] = reviews['title'].str.len()

            for _, row in modifiedReviews.iterrows():
                csvwriter.writerow(row)

        # writing to csv file 
        with open("clean_" + filename, 'w') as csvfile: 
            # creating a csv writer object 
            csvwriter = csv.writer(csvfile)

            cleaned_reviews = self.clean_reviews(modifiedReviews['review'].values)

            reviews['review'] = cleaned_reviews

            for _, row in reviews.iterrows():
                csvwriter.writerow(row)

        return modifiedReviews

    def tfv(self):
        tfv = TfidfVectorizer(
            stop_words = self.stop_words,
            ngram_range = (1,1)
        )
        vec_text = tfv.fit_transform(self.modifiedReviews['review'].values)
        words = tfv.get_feature_names()
        return vec_text, words

    def kmeans(self):
        #setup kmeans clustering
        kmeans = KMeans(n_clusters = 21, n_init = 17, n_jobs = -1, tol = 0.01, max_iter = 200)
        #fit the data 
        kmeans.fit(self.vec_text)
        #this loop transforms the numbers back into words
        common_words = kmeans.cluster_centers_.argsort()[:,-1:-11:-1]
        for num, centroid in enumerate(common_words):
            print(str(num) + ' : ' + ', '.join(self.words[word] for word in centroid))

        return kmeans

    def visualize_kmeans(self):
        #add the cluster label to the data frame
        self.modifiedReviews['cluster'] = self.kmeans.labels_
        
        clusters = self.modifiedReviews.groupby(['cluster', 'rating']).size()
        
        fig, ax1 = plt.subplots(figsize = (26, 15))
        sns.heatmap(clusters.unstack(level = 'rating'), ax = ax1, cmap = 'Reds')
        ax1.set_xlabel('rating').set_size(18)
        ax1.set_ylabel('cluster').set_size(18)
        
        clusters = self.modifiedReviews.groupby(['cluster', 'above_avg']).size()
        
        fig2, ax2 = plt.subplots(figsize = (30, 15))
        sns.heatmap(clusters.unstack(level = 'above_avg'), ax = ax2, cmap="Reds")
        ax2.set_xlabel('Above Average Rating').set_size(18)
        ax2.set_ylabel('Cluster').set_size(18)
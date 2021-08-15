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

class SentimentModel():

    def __init__(self, reviews):
        self.df = reviews

    def explore(self):
        print(self.df)
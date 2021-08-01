import json
import pandas as pd
from tqdm import tqdm

import seaborn as sns
import matplotlib.pyplot as plt

from pygments import highlight
from pygments.lexers import JsonLexer
from pygments.formatters import TerminalFormatter

# for scraping app info and reviews from Google Play
from google_play_scraper import app, Sort, reviews

# for pretty printing data structures
from pprint import pprint

# for storing in MongoDB
import pymongo
from pymongo import MongoClient

# for keeping track of timing
import datetime as dt
from tzlocal import get_localzone

# for building in wait times
import random
import time

%matplotlib inline
%config InlineBackend.figure_format='retina'

sns.set(style='whitegrid', palette='muted', font_scale=1.2)

GOOGLE_PLAY_ID = "com.atom_finance"

## Set up Mongo client
# client = MongoClient(host='localhost', port=27017)

# ## Database for project
# playstore_db = client['play_store_db']

# ## Set up new collection within project db for app info
# info_collection = playstore_db['info_collection']

# ## Set up new collection within project db for app reviews
# review_collection = playstore_db['review_collection']

info = app(GOOGLE_PLAY_ID)
del info['comments']

# pprint(info)

# info_collection.insert_one(info)

rvws, token = reviews(
        GOOGLE_PLAY_ID, # app's ID, found in app's url
        lang='en',            # defaults to 'en'
        country='us',         # defaults to 'us'
        sort=Sort.NEWEST,     # defaults to Sort.MOST_RELEVANT
        filter_score_with=5,  # defaults to None (get all scores)
        count=200             # defaults to 100
        # , continuation_token=token
    )

df = pd.DataFrame(rvws)
content_column = df["content"]
# print(content_column)

from monkeylearn import MonkeyLearn

API_KEY = "092c9806157cb60f124b38a6433dce235433e701"

ml = MonkeyLearn(API_KEY)
model_id = "cl_pi3C7JiL"
result = ml.classifiers.classify(model_id, content_column.tolist())
print(result.body)
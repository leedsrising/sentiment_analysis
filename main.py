from sentiment.base import SentimentModel
from app_store.app_store_scan import scraper

import pandas as pd
import ssl
from random import randint

from pymongo import MongoClient
# pprint library is used to make the output look more pretty
from pprint import pprint

URI = 'mongodb+srv://LeedsRising:ypf4bah-TWY3acd9kcq@app-reviews-cluster.ppkin.mongodb.net/test'

# connect to MongoDB, change the << MONGODB URL >> to reflect your own connection string
client = MongoClient(URI, ssl_cert_reqs=ssl.CERT_NONE)

db=client.ios_app_store_reviews

reviews = scraper()
print(reviews)

db.collection.insert_many(reviews.to_dict('records'))

# sentModel = SentimentModel(reviews)

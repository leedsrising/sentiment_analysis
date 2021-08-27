import pandas as pd
import ssl
from random import randint
from mongo import Mongo

# pprint library is used to make the output look more pretty
from pprint import pprint

URI = 'mongodb+srv://LeedsRising:ypf4bah-TWY3acd9kcq@app-reviews-cluster.ppkin.mongodb.net/test'

mc = Mongo()
# mc.read_main()
reviews = mc.read_mongo()
print(reviews)


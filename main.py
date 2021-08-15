import csv
from sentiment.base import SentimentModel
from app_store.app_store_scan import scraper

import pandas as pd

from utils import clean_reviews

# field names 
fields = ['rating', 'date', 'title', 'review'] 
    
# name of csv file 
filename = "app_store_reviews.csv"

reviews = scraper()
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

    cleaned_reviews = clean_reviews(modifiedReviews['review'].values)

    reviews['review'] = cleaned_reviews

    for _, row in reviews.iterrows():
        csvwriter.writerow(row)

sentModel = SentimentModel(modifiedReviews)
print(sentModel.explore())
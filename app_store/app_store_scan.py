import pandas as pd

# for scraping app info from App Store
from itunes_app_scraper.scraper import AppStoreScraper

# for scraping app reviews from App Store
from app_store_scraper import AppStore

# for pretty printing data structures
from pprint import pprint

# for keeping track of timing
import datetime as dt
from tzlocal import get_localzone

# for building in wait times
import random
import time

APP_NAME = "dispo-live-in-the-moment"
APP_ID = "1491684197"

## Set up App Store Scraper
scraper = AppStoreScraper()

requested_app = AppStore(
  country='us',        # required, 2-letter code
  app_name=APP_NAME, # required, found in app's url
  app_id=APP_ID    # technically not required, found in app's url
)

## Use review method to scrape reviews from App Store
reviews = requested_app.review()
print(reviews)

# Get start time
# start = dt.datetime.now(tz=get_localzone())
# fmt= "%m/%d/%y - %T %p"

# # Print starting output for app
# # print('---'*20)
# # print('---'*20)    
# # print(f'***** {APP_NAME} started at {start.strftime(fmt)}')
# # print()

# # Instantiate AppStore for app
# app_ = AppStore(country='us', app_name=APP_NAME, app_id=APP_ID)

# # Scrape reviews posted since February 28, 2020 and limit to 10,000 reviews
# app_.review()

# # Add keys to store information about which app each review is for
# for rvw in app_.reviews:
#     rvw['app_name'] = APP_NAME
#     rvw['app_id'] = APP_ID

# # Print update that scraping was completed
# # print(f"""Done scraping {APP_NAME}. 
# # Scraped a total of {app_.reviews_count} reviews.\n""")

# # Convert list of dicts to Pandas DataFrame and write to csv
# review_df = pd.DataFrame(reviews)
# # review_df.to_csv('Data/' + APP_NAME + '.csv', index=False)
# print(review_df)

# Get end time
# end = dt.datetime.now(tz=get_localzone())

# Print ending output for app
# print(f"""Successfully wrote {APP_NAME} reviews to csv
# at {end.strftime(fmt)}.\n""")
# print(f'Time elapsed for {APP_NAME}: {end-start}')
# print('---'*20)
# print('---'*20)
# print('\n')
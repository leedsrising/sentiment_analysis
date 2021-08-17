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
HOW_MANY = 2351

def scraper():

  ## Set up App Store Scraper
  scraper = AppStoreScraper()

  requested_app = AppStore(
    country='us',        # required, 2-letter code
    app_name=APP_NAME, # required, found in app's url
    app_id=APP_ID    # technically not required, found in app's url
  )

  accum = []

  requested_app.review(how_many=HOW_MANY)

  for review in requested_app.reviews:
    accum.append(review)

  return pd.DataFrame(accum)
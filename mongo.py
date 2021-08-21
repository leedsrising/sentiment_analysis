
from pymongo import MongoClient
import ssl
import pandas as pd
from pprint import pprint
from config import USERNAME, MONGO_PW, MONGO_URI_PREFIX, MONGO_URI_POSTFIX, COLLECTION, DB_NAME

class Mongo():
    
    def __init__(self):
        self.mongo_uri = MONGO_URI_PREFIX + MONGO_PW + MONGO_URI_POSTFIX
        self.client = MongoClient(self.mongo_uri, ssl_cert_reqs=ssl.CERT_NONE)
        self.db = self.client[DB_NAME]

    def read_main(self):
        serverStatusResult=self.db.command("serverStatus")
        pprint(serverStatusResult)

    def read_mongo(self, query={}):
        """ Read from Mongo and Store into DataFrame """

        cursor = self.db[COLLECTION].find(query)
        df =  pd.DataFrame(list(cursor))

        return df

    def insert(self, records, db=None):

        db.collection.insert_many(records.to_dict('records'))
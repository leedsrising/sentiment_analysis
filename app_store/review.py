import datetime
import mongoengine

class Review(mongoengine.Document):
    registered_date = mongoengine.DateTimeField(default=datetime.datetime.now)
    review = mongoengine.StringField(required=True)
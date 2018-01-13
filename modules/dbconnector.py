from pymongo import MongoClient
from pymongo.collation import Collation
import datetime
from modules import main

class dbconnector :
    def __init__(self):
        self.client = MongoClient('localhost', 27017)
        self.db = self.client.hackathon
        self.coll = self.db['table']

    def db_insert(self,source,title,res) :
        self.coll.insert_one({
            'source':source,
            'title':title,
            'res':res.toJson(),
            'time': str(datetime.time)
        })

    def update_db(self) :
        res = self.coll.find();
        for x in res:
            y = main.get_feed(x['source'],x['title'])
            self.coll.update_one({
                'source':x['source'],
                'title':x['title'],
                'res':y.toJson(),
                'time': str(datetime.time)
            })

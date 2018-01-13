from pymongo import MongoClient
from pymongo.collation import Collation
import datetime
from modules import main

class dbconnector :

    def __init__(self):
        self.client = MongoClient('localhost', 27017)
        self.db = self.client.hackathon
        self.coll = self.db['table']

    def db_insert(self,source,title) :
        res = main.get_feed(source,title);
        self.coll.insert_one({
            'source':source,
            'title':title,
            'res':res.toJson(),
            'time': str(datetime.time)
        })
        return res

    def db_get(self,source,title):
        result = []
        res = self.coll.find({
            'source':source,
            'title':title
        })
        if len(result) == 0:
            result = self.db_insert(source,title).toJson()
        else :
            for x in res:
                result.append(x)
        return result

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

from pymongo import MongoClient
from pymongo.collation import Collation
import datetime
from modules import main
from gi.repository import GLib
import json;
import pyrebase


class dbconnector :

    def __init__(self):
        self.conf = {
          'apiKey': "AIzaSyB5ZW4igirOCICYO_lYxiTRbYJ61R-OVuo",
          'authDomain': "epic-shit.firebaseapp.com",
          'databaseURL': "https://epic-shit.firebaseio.com",
          'projectId': "epic-shit",
          'storageBucket': "epic-shit.appspot.com",
          'messagingSenderId': "135240258150"
        }
        self.config = json.dumps(self.conf)
        self.firebase = pyrebase.initialize_app(self.conf)
        self.db = self.firebase.database()
        self.data = self.db.child("data")

    def db_insert(self,source,title) :
        res = main.get_feed(source,title);
        self.data.push({
            'source':source,
            'title':title,
            'res':res.toJson(),
            'time': str(datetime.time)
        })
        return res

    def db_get(self,source,title):
        result = []
        res = self.data.order_by_child("source").equal_to(source).order_by_child('title').equal_to(title)

        if len(result) == 0:
            result = self.db_insert(source,title).toJson()
        else :
            for x in res:
                result.append(x)
        return result


    def update_db(self) :
        res = self.data.get();
        for x in res:
            y = main.get_feed(x['source'],x['title'])
            self.data.update({
                'source':x['source'],
                'res':y.toJson(),
                'title':x['title'],
                'time': str(datetime.time)
            })

    def initiate_update(self) :
        GLib.timeout_add_seconds(1, self.update_db)

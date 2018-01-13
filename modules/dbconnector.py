from pymongo import MongoClient
from pymongo.collation import Collation
import datetime
from modules import main
from gi.repository import GLib
import json;
import pyrebase;

class dbconnector :

    def __init__(self):
        self.config = {
          'apiKey': "AIzaSyB5ZW4igirOCICYO_lYxiTRbYJ61R-OVuo",
          'authDomain': "epic-shit.firebaseapp.com",
          'databaseURL': "https://epic-shit.firebaseio.com",
          'projectId': "epic-shit",
          'storageBucket': "epic-shit.appspot.com",
          'messagingSenderId': "135240258150",
          "serviceAccount": "settings.json"
        }
        self.firebase = pyrebase.initialize_app(self.config)
        self.db = self.firebase.database()


    def db_insert(self,source,title) :
        res = main.get_feed(source,title).toJson();
        # print(res)
        self.db.child("data").push({
            'src':source,
            'title':title,
            'time': str(datetime.datetime.now()),
            'res':res,
        })
        return res

    def db_get(self,source,title):
        result = []
        all_data = self.db.child('data').order_by_child('src').equal_to(source).order_by_child('title').equal_to(title).get()
        try :
            result = all_data.val()
        except :
            result = self.db_insert(source,title)
        return result


    def update_db(self) :
        res = self.db.child('data').get();
        for x in res:
            y = main.get_feed(x['source'],x['title'])
            self.data.update({
                'source':x['source'],
                'res':y.toJson(),
                'title':x['title'],
                'time': str(datetime.time)
            })

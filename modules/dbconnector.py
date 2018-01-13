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
        print(res)
        self.db.child("data").push({
            'src':source,
            'title':title,
            'time': str(datetime.datetime.now()),
            'res':res,
        })
        return res

    def db_get(self,source,title):
        result = []
        all_data = self.db.get()
        print(all_data.val())
        if len(all_data.val()) == 0:
            result = self.db_insert(source,title)
        else :
            for x in all_data:
                result.append(x)
        return result


    def update_db(self) :
        res = self.db.get();
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

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
            'id':source+'-'+title
        })
        return res

    def db_get(self,source,title):
        result = []
        all_data = self.db.child('data').order_by_child('id').equal_to(source+'-'+title).get()
        try :
            result = all_data.val()
        except :
            result = self.db_insert(source,title)
        return True


    def update_db(self) :
        res = self.db.child('data').get()
        r = res.val()
        for key in list(r.keys()):
            x = r[key]
            y = main.get_feed(x['src'],x['title'])
            self.db.child('data').child(key).update({
                'res':y.toJson(),
                'time': str(datetime.datetime.now())
            })

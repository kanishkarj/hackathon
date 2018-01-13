import datetime
from modules import main
import pyrebase
import threading
import os

def firebaseUpdate(r,key,db) :
    x = r[key]
    y = main.get_feed(x['src'],x['title'])

    db.child('data').child(key).update({
        'res':y.toJson(),
        'time': str(datetime.datetime.now())
    })

class dbconnector :

    def __init__(self):
        self.config = {
          'apiKey': os.environ['APIKEY'],
          'authDomain': os.environ['AUTHDOMAIN'],
          'databaseURL':os.environ['DATABASEURL'],
          'projectId':os.environ['PROJECTID'],
          'storageBucket': os.environ['STORAGEBUCKET'],
          'messagingSenderId':os.environ['MESSAGINGSENDERID'],
          "serviceAccount": os.environ['SERVICEACCOUNT'],
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
            t = threading.Thread(target = firebaseUpdate, args = (r,key,self.db))
            t.setDaemon(True)
            t.start()
        print("hey! i just updated")

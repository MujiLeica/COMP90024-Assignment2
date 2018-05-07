import couchdb
import json
from collections import defaultdict
import time
import datetime

VIEWS = ['boxsum','avgsentiment','daysum','hoursum']

while True:
    couch = couchdb.Server("http://43.240.97.247:5984")
    d = defaultdict()
    try:
            print(datetime.datetime.now(),"retrieving results from couchdb views")
            db = couch["tweet_clean"]

            for name in VIEWS:
                    i = 0
                    viewname = "box/"+name

                    filename = name+".json"
                    
                    viewresult = db.view(viewname,group=True)
                    
                    for item in viewresult:
                        d[i] = defaultdict()
                        d[i]["key"] = item.key
                        d[i]["value"] = item.value
                        d["count"] = i
                        i+=1
                    with open(filename, "w") as f:
                        json.dump(d,f)
                    d.clear()
            time.sleep(3600);
    except Exception as ex:
            print("An exception heppened when pulling data from couchdb:",str(ex))
            time.sleep(300);

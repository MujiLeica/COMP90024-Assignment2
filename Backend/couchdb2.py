import couchdb
import json
from collections import defaultdict
import time
import datetime

VIEWS = ['avgsentiment','daysum','hoursum','locsum','lensum','hashtagsum']

while True:
    couch = couchdb.Server("http://115.146.95.234:5984")
    d = defaultdict()
    try:
            print(datetime.datetime.now(),"retrieving results from couchdb views")
            db = couch["neighbourhood"]

            for name in VIEWS:
                    i = 0
                    viewname = "box/"+name

                    filename = name+".json"

                    viewresult = db.view(viewname,group=True)

                    for item in viewresult:
                        d[i] = defaultdict()
                        d[i]["key"] = item.key
                        d[i]["value"] = item.value
                        i+=1
                    d['count'] = i
                    with open(filename, "w") as f:
                            json.dump(d,f)
                    d.clear()
            time.sleep(3600)
    except Exception as ex:
            print("An exception heppened when pulling data from couchdb:",str(ex))
            time.sleep(300)


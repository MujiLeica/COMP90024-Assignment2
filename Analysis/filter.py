#This program filter raw tweet medadata into a cleaner format
#to reduce storage space required and processing time.
import couchdb
from textblob import TextBlob

#connect to local server
couchserver = couchdb.Server("http://localhost:5984/")
#delete database if exist
dbname = "clean_data"
if dbname in couchserver:
        del couchserver[dbname]
clean = couchserver.create(dbname)

#connect to remote server
remoteserver = couchdb.Server("http://43.240.97.247:5984/")
if dbname in remoteserver:
        del remoteserver[dbname]
remote = remoteserver.create(dbname)

#connect to raw tweet databse
crawler = couchserver['tweet']
#filter tweets to a cleaner format
for i in crawler:
        try:
                tweet = crawler[i]["tweet"]
                id = tweet["id"]
                day = tweet["created_at"][:3]
                time = tweet["created_at"][11:13]
                location = tweet['user']['location']
                hashtags = tweet['entities']['hashtags']
                source = tweet['source'][37:44]
                rt = tweet["retweet_count"]
                coordinates = tweet["coordinates"]["coordinates"]
                text = tweet["text"]
                length = len(text)
                bbox = tweet["place"]["bounding_box"]['coordinates']
                sentiment = TextBlob(text).polarity
                
                doc = {
                        'id' : id,
                        'day' : day,
                        'hour': time,
                        'user_location': location,
                        'hashtags': hashtags,
                        'source': source,
                        'rt': rt,
                        'text' : text,
                        'length': length,
                        'bounding_box': bbox,
                        'sentiment' : sentiment,
                        'coordinates' : coordinates
                }
                #save document to two database for backup
                clean.save(doc)
                remote.save(doc)
        except Exception as e:
                pass


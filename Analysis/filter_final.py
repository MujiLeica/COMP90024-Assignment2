import couchdb
from textblob import TextBlob

#connect to local server
couchserver = couchdb.Server("http://localhost:5984/")
#create a clean_data DB if not exist
dbname = "clean_data"
if dbname in couchserver:
        del couchserver[dbname]
clean = couchserver.create(dbname)

#connect to remote server
remoteserver = couchdb.Server("http://43.240.97.247:5984/")
dbname = "tweet_clean"
if dbname in remoteserver:
        del remoteserver[dbname]

remote = remoteserver.create(dbname)

#connect to tweet DB
crawler = couchserver['tweet']

counter = 0

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
                #print(doc)
                clean.save(doc)
                remote.save(doc)
                counter = counter + 1
                if counter == 300000:
                        break
        except Exception as e:
                pass
print("30W done.")


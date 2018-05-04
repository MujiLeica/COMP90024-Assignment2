
##Update view functions
curl -X PUT http://43.240.97.247:5984/tweet_clean/_design/box --data '{"_id": "_design/box","views": {"boxsum": {"map": "function (doc) {emit(doc.bounding_box, 1);}", "reduce": "function (keys, values){return sum(values);}"}, "avgsentiment": {"map": "function (doc) {emit(doc.bounding_box, doc.sentiment);}", "reduce": "function (keys, values){return sum(values)/values.length;}"}, "daysum": {"map": "function (doc) {emit(doc.day, 1);}", "reduce": "function (keys, values){return sum(values);}"}, "hoursum": {"map": "function (doc) {emit(doc.hour, 1);}", "reduce": "function (keys, values){return sum(values);}"} }}'

curl -X PUT http://43.240.97.247:5984/tweet_clean/_design/box --data '{"_id": "_design/box","views": {"daysum": {"map": "function (doc) {emit(doc.day, 1);}", "reduce": "function (keys, values){return sum(values);}"}}}'

curl -X PUT http://43.240.97.247:5984/tweet_clean/_design/box --data '{"_id": "_design/box","views": {"hoursum": {"map": "function (doc) {emit(doc.day, 1);}", "reduce": "function (keys, values){return sum(values);}"}}}'

##Get view results

sum of tweets in boxes
curl -X GET http://43.240.97.247:5984/tweet_clean/_design/box/_view/boxsum?group_level=1

average sentiment
curl -X GET http://43.240.97.247:5984/tweet_clean/_design/box/_view/avgsentiment?group_level=1

sum of tweets for each day
curl -X GET http://43.240.97.247:5984/tweet_clean/_design/box/_view/daysum?group_level=1


sum of days for each hour
curl -X GET http://43.240.97.247:5984/tweet_clean/_design/box/_view/hoursum?group_level=1

##Update view functions
curl -X PUT http://43.240.97.247:5984/tweet_clean/_design/box --data '{"_id": "_design/box","views": {"boxsum": {"map": "function (doc) {emit(doc.bounding_box, 1);}", "reduce": "function (keys, values){return sum(values);}"}}}'



##Get view results

sum of tweets in boxes
curl -X GET http://43.240.97.247:5984/tweet_clean/_design/box/_view/boxsum?group_level=1



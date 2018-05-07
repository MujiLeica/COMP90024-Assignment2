
##Update view functions
curl -X PUT http://43.240.97.247:5984/cleantweets/_design/box --data '{"_id": "_design/box","views": {"boxsum": {"map": "function (doc) {emit(doc.bounding_box, 1);}", "reduce": "function (keys, values){return sum(values);}"}, "avgsentiment": {"map": "function (doc) {emit(doc.bounding_box, doc.sentiment);}", "reduce": "function (keys, values){return sum(values)/values.length;}"}, "daysum": {"map": "function (doc) {emit(doc.day, 1);}", "reduce": "function (keys, values){return sum(values);}"}, "hoursum": {"map": "function (doc) {emit(doc.hour, 1);}", "reduce": "function (keys, values){return sum(values);}"}, "locsum": {"map": "function (doc) {emit(doc.user_location, 1);}", "reduce": "function (keys, values){return sum(values);}"}, "lensum": {"map": "function (doc) {emit(doc.length, 1);}", "reduce": "function (keys, values){return sum(values);}"}, "hashtagsum": {"map": "function (doc) {for(key in doc.hashtags) {emit(key, 1);}}", "reduce": "function (keys, values){return sum(values);}"}}}'

curl -X PUT http://43.240.97.247:5984/tweet_clean/_design/box --data '{"_id": "_design/box","views": {"daysum": {"map": "function (doc) {emit(doc.day, 1);}", "reduce": "function (keys, values){return sum(values);}"}}}'

curl -X PUT http://43.240.97.247:5984/tweet_clean/_design/box --data '{"_id": "_design/box","views": {"hoursum": {"map": "function (doc) {emit(doc.day, 1);}", "reduce": "function (keys, values){return sum(values);}"}}}'

"locsum": {"map": "function (doc) {emit(doc.user_location, 1);}", "reduce": "function (keys, values){return sum(values);}"}

"lensum": {"map": "function (doc) {emit(doc.length, 1);}", "reduce": "function (keys, values){return sum(values);}"}

"hashtagsum": {"map": "function (doc) {for(key in doc.hashtags) {emit(key, 1);}}", "reduce": "function (keys, values){return sum(values);}"}

###for neighbor
curl -X PUT http://43.240.97.247:5984/neighbourhood/_design/box --data '{"_id": "_design/box","views": {"boxsum": {"map": "function (doc) {emit(doc.bounding_box, 1);}", "reduce": "function (keys, values){return sum(values);}"}, "avgsentiment": {"map": "function (doc) {emit(doc.bounding_box, doc.sentiment);}", "reduce": "function (keys, values){return sum(values)/values.length;}"}, "daysum": {"map": "function (doc) {emit(doc.day, 1);}", "reduce": "function (keys, values){return sum(values);}"}, "hoursum": {"map": "function (doc) {emit(doc.time, 1);}", "reduce": "function (keys, values){return sum(values);}"}, "locsum": {"map": "function (doc) {emit(doc.user_location, 1);}", "reduce": "function (keys, values){return sum(values);}"}, "lensum": {"map": "function (doc) {emit(doc.length, 1);}", "reduce": "function (keys, values){return sum(values);}"}, "hashtagsum": {"map": "function (doc) {for(var i =0;i < doc.hashtags.length; i++) {emit(doc.hashtags[i].text, 1);}}", "reduce": "function (keys, values){return sum(values);}"}, "placesum": {"map": "function (doc) {emit(doc.place_name, 1);}", "reduce": "function (keys, values){return sum(values);}"}, "usersum": {"map": "function (doc) {emit(doc.userid, 1);}", "reduce": "function (keys, values){return sum(values);}"}}}'

"placesum": {"map": "function (doc) {emit(doc.place_name, 1);}", "reduce": "function (keys, values){return sum(values);}"}

"usersum": {"map": "function (doc) {emit(doc.userid, 1);}", "reduce": "function (keys, values){return sum(values);}"}


##Get view results cleantweets

sum of tweets in boxes
curl -X GET http://43.240.97.247:5984/cleantweets/_design/box/_view/boxsum?group_level=1

average sentiment
curl -X GET http://43.240.97.247:5984/cleantweets/_design/box/_view/avgsentiment?group_level=1

sum of tweets for each day
curl -X GET http://43.240.97.247:5984/cleantweets/_design/box/_view/daysum?group_level=1


sum of days for each hour
curl -X GET http://43.240.97.247:5984/cleantweets/_design/box/_view/hoursum?group_level=1


sum of tweets of locations
curl -X GET http://43.240.97.247:5984/cleantweets/_design/box/_view/locsum?group_level=1

sum of tweets of different length
curl -X GET http://43.240.97.247:5984/cleantweets/_design/box/_view/lensum?group_level=1

sum of tweets of different hashtag
curl -X GET http://43.240.97.247:5984/cleantweets/_design/box/_view/hashtagsum?group_level=1



##Get view results for neighbour
sum of tweets in boxes
curl -X GET http://43.240.97.247:5984/neighbourhood/_design/box/_view/boxsum?group_level=1

average sentiment
curl -X GET http://43.240.97.247:5984/neighbourhood/_design/box/_view/avgsentiment?group_level=1

sum of tweets for each day
curl -X GET http://43.240.97.247:5984/neighbourhood/_design/box/_view/daysum?group_level=1


sum of days for each hour
curl -X GET http://43.240.97.247:5984/neighbourhood/_design/box/_view/hoursum?group_level=1


sum of tweets of locations
curl -X GET http://43.240.97.247:5984/neighbourhood/_design/box/_view/locsum?group_level=1

sum of tweets of different length
curl -X GET http://43.240.97.247:5984/neighbourhood/_design/box/_view/lensum?group_level=1

sum of tweets of different hashtag
curl -X GET http://43.240.97.247:5984/neighbourhood/_design/box/_view/hashtagsum?group_level=1
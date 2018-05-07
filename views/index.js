function (doc) {
    for(key in doc.hashtags) {
        emit(key, 1);
    }
    
  }

function (keys, values){
    return keys[0];
}
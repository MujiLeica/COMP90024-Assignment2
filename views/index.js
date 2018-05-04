function (doc) {
    emit(doc.bounding_box, 1);
  }

function (keys, values){
    return keys[0];
}
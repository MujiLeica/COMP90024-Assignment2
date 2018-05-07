from flask import Flask, request
from flask_restful import Resource, Api
from flask import jsonify
import json
from flask_cors import CORS

app = Flask(__name__)
CORS(app)
api = Api(app)


class test(Resource):
    def get(self):
        #result = json.load(open("result0.json","r"))
        return jsonify({'result':'ok'})

class locsum(Resource):
    def get(self):
        result = json.load(open('locsum.json'))

class hashtagsum(Resource):
    def get(self):
        result = json.load(open('hashtagsum.json'))
        return jsonify(result)

class lensum(Resource):
    def get(self):
        result = json.load(open('lensum.json'))
        return jsonify(result)

class avgsentiment(Resource):
    def get(self):
        result = json.load(open('avgsentiment.json'))
        return jsonify(result)

class hoursum(Resource):
    def get(self):
        result = json.load(open('hoursum.json'))
        
class daysum(Resource):
    def get(self):
        result = json.load(open('daysum.json'))
        return jsonify(result)

api.add_resource(test, '/test')
api.add_resource(hashtagsum, '/hashtagsum')
api.add_resource(lensum, '/lensum')
api.add_resource(locsum, '/locsum')
api.add_resource(avgsentiment, '/avgsentiment')
api.add_resource(hoursum, '/hoursum')
api.add_resource(daysum, '/daysum')

if __name__ == '__main__':
     app.run(host='0.0.0.0',port='5002',debug=True)


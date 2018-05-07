from flask import Flask, request
from flask_restful import Resource, Api
from flask import jsonify
import json

app = Flask(__name__)
api = Api(app)

class test(Resource):
	def get(self):
			result jsonify({'result':'ok'})

class boxsum(Resource):
	def get(self):
		result = json.load(open('boxsum.json'))
		return jsonify(result)

class avgsentiment(Resource):
	def get(self):
		result = json.load(open('avgsentiment.json'))
		return jsonify(result)

class hoursum(Resource):
	def get(self):
		result = json.load(open('hoursum.json'))
		return jsonify(result)

class daysum(Resource):
    def get(self):
        result = json.load(open('daysum.json'))
        return jsonify(result)
 
api.add_resource(test, '/test')
api.add_resource(boxsum, '/boxsum')
api.add_resource(avgsentiment, '/avgsentiment')
api.add_resource(hoursum, '/hoursum')
api.add_resource(daysum, '/daysum')

if __name__ == '__main__':
	app.run(host='0.0.0.0',port='5002',debug=True)
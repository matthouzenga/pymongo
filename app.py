from flask import Flask
from flask import json, jsonify,render_template, request,redirect
import os
from pymongo import MongoClient
from bson.json_util import dumps
from bson.json_util import loads


app = Flask(__name__)

#connect to mongodb

#mongo_URI = "mongodb://mongoadmin:password@localhost:27017/"
mongo_URI = "mongodb://myUserAdmin:password@mongodb:27017/"
client = MongoClient(mongo_URI)
db = client['testdb']

@app.route('/', methods=["POST", "GET"])
def index():
    #handle form being submitted
    if request.method == "POST":
        content = request.json
        input = content['name']
       #Insert new document into mongodb database

        result=db.equipment.insert_one(content)
        return jsonify('received',input)

    else:   #GET request
        cursor=db.equipment.find({})    #query all rows from database
        output = []
        for c in cursor:
            output.append({'year' : c['year'], 'name' : c['name']})
        return jsonify('results:',output)

#app.run(host='0.0.0.0', port=8080)
app.run(host='0.0.0.0', port=5000,threaded=True)
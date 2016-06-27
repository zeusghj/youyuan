# -*- coding:utf-8 -*-

from flask import Flask, request
import json
from bson import json_util
from bson.objectid import ObjectId
import pymongo

app = Flask(__name__)

mongoClient = pymongo.MongoClient('localhost', 27017)
db = mongoClient['youyuan']
def toJson(data):
    return json.dumps(data, default=json_util.default)

@app.route('/user/', methods=['GET'])

def finduser():
    if request.method == 'GET':
        lim = int(request.args.get('limit', 10))
        off = int(request.args.get('offset', 0))
        results = db['user'].find().skip(off).limit(lim)
        json_results = []
        for result in results:
            json_results.append(result)

        return toJson(json_results)

if __name__ == '__main__':
    app.run(host='0.0.0.0')
from flask import Flask, jsonify, request, render_template
import pymongo
import pprint
import dns
from brogic import access_and_put_in_list_mongo_docs
from bson import json_util
import json
import gunicorn

client = pymongo.MongoClient("mongodb+srv://bruhuser:griffith@cluster0.ccamn.mongodb.net/articles?retryWrites=true&w=majority")
db = client.get_database('articles')
collections = [db.nytimes, db.reuters, db.wired, db.economist, db.bbc]
doc_list = []
app = Flask(__name__)


@app.after_request
def after_request(response):
    response.headers.add('Access-Control-Allow-Origin', '*')
    response.headers.add('Access-Control-Allow-Headers', 'Content-Type')
    return response


@app.route('/', methods=['GET', 'POST'])
def hello():
    # POST request
    if request.method == 'POST':
        print('Incoming..')
        print(request.get_json())  # parse as JSON
        return 'OK', 200

    # GET request
    else:
        return jsonify(access_and_put_in_list_mongo_docs(collections))

# if __name__ == "__main__":
#     app.run(port=3000, debug=True)
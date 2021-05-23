from flask import Flask, jsonify, request, render_template
import pymongo
import pprint
import dns
from brogic import access_and_put_in_list_mongo_docs
from bson import json_util
import json

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


@app.route('/hello', methods=['GET', 'POST'])
def hello():

    # POST request
    if request.method == 'POST':
        print('Incoming..')
        print(request.get_json())  # parse as JSON
        return 'OK', 200

    # GET request
    else:
        return json.loads(json_util.dumps(access_and_put_in_list_mongo_docs()))

@app.route('/test')
def test_page():
    # look inside `templates` and serve `index.html`
    return render_template('index.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000,debug=True)
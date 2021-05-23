import pymongo
import pprint
import dns
from flask import Flask, jsonify, request, render_template

app = Flask(__name__)

client = pymongo.MongoClient("mongodb+srv://bruhuser:griffith@cluster0.ccamn.mongodb.net/articles?retryWrites=true&w=majority")
db = client.get_database('articles')
collections = [db.nytimes, db.reuters, db.wired, db.economist, db.bbc]


nytimes_headlines = []
nytimes_summaries = []
nytimes_urls = []
@app.route('/', methods = ['GET','POST'])
def nytimes():
    if request.method == 'POST':
        print("Incoming...")
        print(request.get_json())
        return 'OK', 200
    else:
        message = db.nytimes.find()
        return jsonify(message)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000,debug=True)
import pymongo
import pprint
import dns
from flask import Flask
import jsonify

app = Flask(__name__)

client = pymongo.MongoClient("mongodb+srv://bruhuser:griffith@cluster0.ccamn.mongodb.net/articles?retryWrites=true&w=majority")
db = client.get_database('articles')
collections = [db.nytimes, db.reuters, db.wired, db.economist, db.bbc]


nytimes_headlines = []
nytimes_summaries = []
nytimes_urls = []
@app.route('/')
def nytimes():
    return str(db.nytimes.find())

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000,debug=True)
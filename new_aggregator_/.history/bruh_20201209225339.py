from flask import Flask
import requests
from bs4 import BeautifulSoup
from concurrent.futures import ThreadPoolExecutor
import re
import time
import pymongo
import dns
from script import Source, Article, Queue, upload_mongo
client = pymongo.MongoClient("mongodb+srv://bruhuser:griffith@cluster0.ccamn.mongodb.net/articles?retryWrites=true&w=majority")
db = client.get_database('articles')

app = Flask(__name__)

source_to_db = {
    'nytimes': db.nytimes,
    'bbc': db.bbc,
    ...
}

def parse_sources():
    collections = [db.nytimes, db.reuters, db.wired, db.economist, db.bbc]
    sources = ['http://www.nytimes.com/', 'https://www.reuters.com/', 'https://www.wired.com', 'https://www.economist.com/', 'https://www.bbc.com']
    for source in sources:
        index = sources.index(source)
        source_obj = Source(source)
        list_articles = source_obj.articles
        article_object_holder = []
        for x in list_articles:
            x = Article(x, source)
            article_object_holder.append(x)
            print(x.url)
            print(x.headline)
            print(x.summary)
            print("\n")
        upload_mongo(article_object_holder, collections[index])

@app.route('/')
def say_hello():
    parse_sources()
    return "done"

executor = ThreadPoolExecutor (max_workers=None)

@app.route("/parse-sources", methods=['GET', 'POST'])
def parse_sources_runner():
    # from threading import Thread
    # heavy_thread = Thread(
    #     target=parse_sources,
    # )
    # heavy_thread.daemon = True
    # heavy_thread.start()

    # with ThreadPoolExecutor (max_workers=None) as executor:
    #     executor.map(parse_sources)
    executor.submit(parse_sources)

    return "blah"


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000,debug=True)
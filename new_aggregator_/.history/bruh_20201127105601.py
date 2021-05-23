from flask import Flask
from script import Source, Article, Queue, upload_mongo

app = Flask(__name__)

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
    return "hello its working"


@app.route("/parse-sources", methods=['GET', 'POST'])
def parse_sources_runner():
    # create thread
    # start thread
    return "blah"
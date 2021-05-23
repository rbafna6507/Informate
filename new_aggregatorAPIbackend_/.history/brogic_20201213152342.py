from flask import Flask, jsonify, request, render_template
import pymongo
import pprint
import dns


client = pymongo.MongoClient("mongodb+srv://bruhuser:griffith@cluster0.ccamn.mongodb.net/articles?retryWrites=true&w=majority")
db = client.get_database('articles')
collections = [db.nytimes, db.reuters, db.wired, db.economist, db.bbc]
doc_list = []

def access_and_put_in_list_mongo_docs(collection):
    for collection in collections:
        documents_in_collection = collection.find()
        for document in documents_in_collection:
            dict(document)
            doc_list.append(document)
    return doc_list

def get_headline_info_link(list of documents):
    # return dictionaries of headline info link in list

def send_to_js(lists of dictionaries):
    # return json object in endpoint that sends all this data
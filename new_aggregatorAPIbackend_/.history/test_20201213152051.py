from flask import Flask, jsonify, request, render_template
import pymongo
import pprint
import dns


client = pymongo.MongoClient("mongodb+srv://bruhuser:griffith@cluster0.ccamn.mongodb.net/articles?retryWrites=true&w=majority")
db = client.get_database('articles')
collections = [db.nytimes, db.reuters, db.wired, db.economist, db.bbc]
doc_list = []

for collection in collections:
    documents_in_collection = collection.find()
    for document in documents_in_collection:
        dict(document)
        doc_list.append(document)
    print(doc_list)
    print("\n\n\n\n\n")

from flask import Flask, jsonify, request, render_template
import pymongo
import pprint
import dns


client = pymongo.MongoClient("mongodb+srv://bruhuser:griffith@cluster0.ccamn.mongodb.net/articles?retryWrites=true&w=majority")
db = client.get_database('articles')
collections = [db.nytimes, db.reuters, db.wired, db.economist, db.bbc]
doc_list = []

def access_and_put_in_list_mongo_docs(dbcollections):
    for collection in dbcollections:
        documents_in_collection = collection.find()
        for document in documents_in_collection:
            temp_hold_document_info = []
            temp_hold.append(str(document['Headline']), str(document['Info']), str(document['Link']), str(document['Source']))
            documents_in_collection.append(temp_hold_document_info)
    return doc_list
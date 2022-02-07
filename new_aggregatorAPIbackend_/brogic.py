from flask import Flask, jsonify, request, render_template
import pymongo
import pprint
import dns


client = pymongo.MongoClient("mongodb+srv://bruhuser:griffith@cluster0.ccamn.mongodb.net/articles?retryWrites=true&w=majority")
db = client.get_database('articles')
collections = [db.nytimes, db.reuters, db.wired, db.economist, db.bbc]
doc_list = []

def access_and_put_in_list_mongo_docs(dbcollections):
    doc_list = []
    for collection in dbcollections:

        documents_in_collection = collection.find()
        for document in documents_in_collection:
            temp_hold_document_info = {}
            temp_hold_document_info['source'] = str(document['Source'])
            temp_hold_document_info['headline'] = str(document['Headline'])
            temp_hold_document_info['info'] = str(document['Info'])
            temp_hold_document_info['link'] = str(document['Link'])
            doc_list.append(temp_hold_document_info)
    return doc_list
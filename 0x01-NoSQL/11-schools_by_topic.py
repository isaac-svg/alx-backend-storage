#!/usr/bin/env python3
""" MongoDb for python """

def schools_by_topic(mongo_collection, topic):
    """ gets documents by topic """
    documents = mongo_collection.find({"topics": topic})
    list_docs = [d for d in documents]
    return list_docs

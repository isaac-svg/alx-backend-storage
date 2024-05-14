#!/usr/bin/env python3
""" MongoDb for python """


def list_all(mongo_collection):
    """ List all documents in a collection """
    documents = mongo_collection.find()

    if documents.count() == 0:
        return []

    return documents

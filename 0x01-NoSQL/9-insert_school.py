#!/usr/bin/env python3
""" MongoDb for python """


def insert_school(mongo_collection, **kwargs):
    """ Inserts document in a collection """
    document_id = mongo_collection.insert(kwargs)
    return document_id

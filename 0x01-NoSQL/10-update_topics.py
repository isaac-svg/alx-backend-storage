#!/usr/bin/env python3
""" MongoDb for python """


def update_topics(mongo_collection, name, topics):
    """ Performs an update on all documents using the name as key"""
    query = {"name": name}
    new_values = {"$set": {"topics": topics}}

    mongo_collection.update_many(query, new_values)

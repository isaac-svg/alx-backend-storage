#!/usr/bin/env python3
""" MongoDb for python """


def top_students(mongo_collection):
    """ Get all students sorted by their average score """

    top_student = mongo_collection.aggregate([
        {
            "$project": {
                "name": "$name",
                "averageScore": {"$avg": "$topics.score"}
            }
        },
        {"$sort": {"averageScore": -1}}
    ])

    return top_student

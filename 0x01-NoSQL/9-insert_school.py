#!/usr/bin/env python3
"""
9-insert_school
"""


def insert_school(mongo_collection, **kwargs):
    """inserts a new document in a collection based on kwargs

    Args:
        mongo_collection:pymongo collection object
        kwargs: list allows you to receive arbitrary keyword arguments

    Return:
        New inserted id
    """
    document_insert = kwargs
    result_insertion = mongo_collection.insert_one(document_insert)

    return result_insertion.inserted_id

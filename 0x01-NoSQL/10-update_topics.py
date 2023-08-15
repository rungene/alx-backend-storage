#!/usr/bin/env python3
"""
10-update_topics
"""


def update_topics(mongo_collection, name, topics):
    """Updates all topics of a school document based on the name(filter)
    Args:
        mongo_collection: pymongo collection object
        name(string): school name to update
        topics(list string): list of topics approached in the school
    """
    topics_update = {'$set': {'topics': topics}}
    filter_criteria = {'name': name}
    mongo_collection.update_one(filter_criteria, topics_update, upsert=True)

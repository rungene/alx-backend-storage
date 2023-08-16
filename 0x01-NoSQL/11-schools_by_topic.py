#!/usr/bin/env python3
"""
11-schools_by_topic
"""


def schools_by_topic(mongo_collection, topic):
    """function with a query that matches the desired item within the list.

    Args:
        mongo_collection: pymongo collection object
        topic: (string) will be topic searched

    Return:
        list of school having a specific topic
    """
    query_search = {'topics': topic}
    matching_doc_list = mongo_collection.find(query_search)
    
    return matching_doc_list

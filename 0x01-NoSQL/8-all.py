#!/usr/bin/env python3
"""
8-all
"""


def list_all(mongo_collection):
    """ists all documents in a collection

    Args:
        mongo_collection: pymongo collection object

    Return:
        lists all documents in a collection or empty list
    """
    documents = list(mongo_collection.find())
    if not documents:
        return []
    return documents

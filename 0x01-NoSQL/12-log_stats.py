#!/usr/bin/env python3
"""
12-log_stats
"""
from pymongo import MongoClient


if __name__ == "__main__":
    client = MongoClient('mongodb://127.0.0.1:27017')
    nginx_collection = client.logs.nginx

    total_doc_count = nginx_collection.count_documents({})
    print("{} logs".format(total_doc_count))

#!/usr/bin/env python3
"""task 8"""
import pymongo


def list_all(mongo_collection):
    """a function that lists all documents in a collection"""
    list_documents = mongo_collection.find()
    if list_documents is None:
        return []
    else:
        return list_documents

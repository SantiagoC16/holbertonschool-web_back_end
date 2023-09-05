#!/usr/bin/env python3
"""task 8"""
import pymongo


def list_all(mongo_collection):
    list_documents = mongo_collection.find()
    if list_documents is None:
        return []
    else:
        return list_documents

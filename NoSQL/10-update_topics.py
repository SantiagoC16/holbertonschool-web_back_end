#!/usr/bin/env python3
"""task 10"""
import pymongo


def update_topics(mongo_collection, name, topics):
    """a function that changes all topics of a school document based on the name"""
    mongo_collection.updateMany({"name": name}, {"$set": {"topics": topics}})

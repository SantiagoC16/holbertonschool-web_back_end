#!/usr/bin/env python3
"""task 11"""
import pymongo


def schools_by_topic(mongo_collection, topic):
    """a function that returns the list of school having a specific topic"""
    return mongo_collection.find({"topics": topic})

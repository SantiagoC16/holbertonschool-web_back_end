#!/usr/bin/env python3
"""task 9"""
import pymongo


def insert_school(mongo_collection, **kwargs):
    """a function that inserts a new document in a collection based on kwargs"""
    to_insert = mongo_collection.find()

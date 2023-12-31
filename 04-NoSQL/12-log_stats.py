#!/usr/bin/env python3
"""task 12"""
from pymongo import MongoClient
list_all = __import__('8-all').list_all
insert_school = __import__('9-insert_school').insert_school

if __name__ == "__main__":
    client = MongoClient('mongodb://127.0.0.1:27017')
    nginx_collection = client.logs.nginx

    print("{} logs".format(nginx_collection.count_documents({})))
    print("Methods:")
    get = nginx_collection.count_documents({"method": "GET"})
    print("\tmethod GET: {}".format(get))
    post = nginx_collection.count_documents({"method": "POST"})
    print("\tmethod POST: {}".format(post))
    put = nginx_collection.count_documents({"method": "PUT"})
    print("\tmethod PUT: {}".format(put))
    patch = nginx_collection.count_documents({"method": "PATCH"})
    print("\tmethod PATCH: {}".format(patch))
    delete = nginx_collection.count_documents({"method": "DELETE"})
    print("\tmethod DELETE: {}".format(delete))
    get_status = nginx_collection.count_documents(
        {"method": "GET", "path": "/status"})
    print("{} status check".format(get_status))

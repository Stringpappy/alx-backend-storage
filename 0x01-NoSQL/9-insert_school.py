#!/usr/bin/env python3
"""
 module insert a new document to a table/cll.
"""


def insert_school(mongo_collection, **kwargs):
    """
    function that  Inserts a new document in a collection.
    """
    result = mongo_collection.insert_one(kwargs)
    return result.inserted_idi

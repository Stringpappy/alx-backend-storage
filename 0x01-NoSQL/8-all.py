#!/usr/bin/env python3
"""
module that list all document in a table.
"""


def list_all(mongo_collection):
    """
    function that Lists all documents in a collection.
    """
    return [doc for doc in mongo_collection.find()]

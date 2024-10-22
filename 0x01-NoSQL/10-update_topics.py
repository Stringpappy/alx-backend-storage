#!/usr/bin/env python3
"""
module. that change topic
"""


def update_topics(mongo_collection, name, topics):
    """
    function that Changes all topics of a collection's
    document based on the name.
    ""
    mongo_collection.update_many(
        {'name': name},
        {'$set': {'topics': topics}}
    )

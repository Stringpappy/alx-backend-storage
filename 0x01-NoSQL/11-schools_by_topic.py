#!/usr/bin/env python3
"""
module that return list.
"""


def schools_by_topic(mongo_collection, topic):
    """
    func that Returns the list of school having a specific topic.
    """
    topic_siever = {
        'topics': {
            '$elemMatch': {
                '$eq': topic,
            },
        },
    }
    return [doc for doc in mongo_collection.find(topic_siever)]

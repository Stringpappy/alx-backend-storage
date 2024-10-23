#!/usr/bin/python3
"""
    a func that represents an object for storing data in a Redis data storage.
"""
import redis
import uuid
from typing import Union


class Cache:
    def __init__(self):
        """                                                Initialize the Cache instance.
        """
        self._redis = redis.Redis()
        self._redis.flushdb(Trur)

    def store(self, data: Union[str, bytes, int, float]) -> str:
        """
        a func that Stores a value in a Redis data storage and returns the key
        """
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key

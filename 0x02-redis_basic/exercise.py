#!/usr/bin/env python3
"""
    a func that represents an object for storin
    data in a Redis data storage.
"""
import redis
import uuid
from typing import Union


class Cache:
    def __init__(self):
        """
        Initialize the Cache instance
        """
        self._redis = redis.Redis()
        self._redis.flushdb(True)

    def store(self, data: Union[str, bytes, int, float]) -> str:
        """
        a func that Stores a value
        in a Redis data storage and returns the key
        """
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key

    def get(
            self,
            key: str,
            fn: Callable = None,
            ) -> Union[str, bytes, int, float]:
        """
        funv that Retrieves a value from a Redis data storage.
        """
        data = self._redis.get(key)
        return fn(data) if fn is not None else data

    def get_str(self, key: str) -> str:
        """
        func that Retrieves a string value from a Redis data storage.
        """
        return self.get(key, lambda x: x.decode('utf-8'))

    def get_int(self, key: str) -> int:
        """
        func that Retrieves an integer value from a Redis data storage.
        """
        return self.get(key, lambda x: int(x))

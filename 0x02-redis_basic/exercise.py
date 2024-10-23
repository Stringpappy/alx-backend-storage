#!/usr/bin/env python3
"""
pythom module that uses Redis NoSQL data storage.
"""
import uuid
import redis
from functools import wraps
from typing import Any, Callable, Union


class Cache:
    """
    a func that represents an object for storing data in a Redis data storage.
    """
    def __init__(self) -> None:
        """
        Initialize the Cache instance.
        """
        self._redis = redis.Redis()
        self._redis.flushdb(True)

    @call_history
    @count_calls
    def store(self, data: Union[str, bytes, int, float]) -> str:
        """
        a func that Stores a value in a Redis data storage and returns the key
        """
        data_key = str(uuid.uuid4())
        self._redis.set(data_key, data)
        return data_key

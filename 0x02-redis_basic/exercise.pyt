#!/usr/bin/env python3
"""
refis module
"""
import redis
import uuid
from typing import Union, Callable, Optional, Any


def count_calls(method: Callable) -> Callable:
    """
    funcTracks the number of calls made to a method in a Cache class.
    """
    @wraps(method)
    def provoke(self, *args, **kwargs) -> Any:
        """
        fun that call on the given method after incrementing it call counter.
        """
        if isinstance(self._redis, redis.Redis):
            self._redis.incr(method.__qualname__)
        return method(self, *args, **kwargs)
    return provoke


class Cache:
    """A simple cache class using Redis to store and retrieve data."""
    def __init__(self):
        """Initializes the Redis client and flushes the database."""
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: Union[str, bytes, int, float]) -> str:
        """Stores the given data in Redis and returns a unique key.
        """
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key

    def get(self, key: str, fn: /
            Optional[Callable[[bytes], Any]] = None) -> Optional[Any]:
        """Retrieves data from Redis by key
        and applies an optional conversion functiom.
        """
        value = self._redis.get(key)
        if value is None:
            return None
        if fn:
            return fn(value)
        return value

    def get_str(self, key: str) -> Optional[str]:
        """Retrieves data as a UTF-8 string from Redis.
        """
        return self.get(key, fn=lambda x: x.decode('utf-8'))

    def get_int(self, key: str) -> Optional[int]:
        """Retrieves data as an integer from Redis
        """
        return self.get(key, fn=lambda x: int(x))

#!/usr/bin/env python3
import redis
from typing import Union, Callable, Optional
import uuid
from functools import wraps


def count_calls(method: Callable) -> Callable:
    """decorator that takes a single method Callable argument and
    returns a Callable.
    """
    @wraps(method)
    def wrapper(self, *args, **kwargs):
        """Wrapper function"""
        method_key = method.__qualname__
        self._redis.incr(method_key)
        result = method(self, *args, **kwargs)
        return result
    return wrapper


class Cache:
    """
    This class interacts with Redis database via redis.Redis() client
    """

    def __init__(self):
        """
        Initialise Cache class instance and create Redis client
        flush the instance
        """
        self._redis = redis.Redis()
        self._redis.flushdb()

    @count_calls
    def store(self, data: Union[str, bytes, int, float]) -> str:
        """
        generate a random key (e.g. using uuid)
        """
        random_key = str(uuid.uuid4())

        self._redis.set(random_key, data)

        return random_key

    def get(self, key: str,
            fn: Optional[Callable] = None) -> Union[str, bytes, int, float]:
        """
        Takes in a key(string) and Callable object used to
        convert data to desired format
        """
        if self._redis.exists(key):
            value = self._redis.get(key)
            if fn is not None:
                return fn(value)
            return value
        else:
            return None

    def get_str(self, key: str) -> str:
        """
        Converts retrived values to strings
        """
        value = self.get(key)
        if value is not None:
            return value.decode('utf-8')
        return ""

    def get_int(self, key: str) -> int:
        """
        Converts retrived values to strings
        """
        value = self.get(key)
        if value is not None:
            return int(value)
        return 0

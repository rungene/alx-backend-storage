#!/usr/bin/env python3
"""
exercise module
"""
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


def call_history(method: Callable) -> Callable:
    """decocaror taking a single method(callable as args
    and resturns a callable"""
    @wraps(method)
    def wrapper(self, *args, **kwargs):
        """Wrapper function"""
        # Call the original function
        result = method(self, *args, **kwargs)
        method_name = method.__qualname__
        # Store input params as string
        input_list_key = method_name + ':inputs'
        # Convert args to a string
        input_data = str(args)
        self._redis.rpush(input_list_key, input_data)

        # Output stored in diffrent list
        output_list_key = method_name + ':outputs'
        self._redis.rpush(output_list_key, str(result))

        # retur output of original function call
        return result

    # return decorated function
    return wrapper


def replay(method: Callable) -> None:
    """display the history of calls of a particular function.
    """
    method_name = method.__qualname__
    input_list_key = method_name + ':inputs'
    output_list_key = method_name + ':outputs'

    cache = redis.Redis()
    calls = cache.get(method_name).decode('utf-8')
    print('{} was called {} times:'.format(method_name, calls))

    # Retrieve all elements
    input_data = cache.lrange(input_list_key, 0, -1)
    output_data = cache.lrange(output_list_key, 0, -1)

    # Loop over output and inputs using zip
    for input_str, output_str in zip(input_data, output_data):
        print('{}(*{}) -> {}'.format(method.__qualname__,
                                     input_str.decode('utf-8'),
                                     output_str.decode('utf-8')))


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

    @call_history
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

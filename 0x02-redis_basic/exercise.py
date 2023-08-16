#!/usr/bin/env python3
import redis
from typing import Union
import uuid


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

    def store(self, data: Union[str, bytes, int, float]) -> str:
        """
        generate a random key (e.g. using uuid)
        """
        random_key = str(uuid.uuid4())

        self._redis.set(random_key, data)

        return random_key

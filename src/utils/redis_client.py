import os

import redis

from src.utils.logging_config import logger


class RedisClient:
    def __init__(self, redis_url=None):
        redis_url = redis_url or os.getenv("REDIS_URL")
        logger.info(f"Connecting to Redis at: {redis_url}")
        self.client = redis.StrictRedis.from_url(redis_url, decode_responses=True)

    def get(self, key: str):
        return self.client.get(key)

    def set(self, key: str, value: str, expire: int = 3600):
        self.client.set(key, value, ex=expire)


redis_client = RedisClient()

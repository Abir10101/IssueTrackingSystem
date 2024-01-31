import redis
from app.config import app_config
from flask import current_app

class Queue:

    def __init__(self):
        self.r_write = redis.StrictRedis(
            host=app_config.QUEUE_MASTER_HOST,
            port=app_config.QUEUE_MASTER_PORT,
            password=app_config.QUEUE_MASTER_PASSWORD,
            decode_responses=True
        )
        self.r_read = redis.StrictRedis(
            host=app_config.QUEUE_SLAVE_HOST,
            port=app_config.QUEUE_SLAVE_PORT,
            password=app_config.QUEUE_SLAVE_PASSWORD,
            decode_responses=True
        )

    def push_message(self, channel :str, message :str):
        return self.r_write.publish(channel, message)

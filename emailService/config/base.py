import os

class BaseConfig:

    #Message Queue
    QUEUE_MASTER_HOST = os.getenv("QUEUE_MASTER_HOST", default = "localhost")
    QUEUE_MASTER_PORT = os.getenv("QUEUE_MASTER_PORT", default = 6378)
    QUEUE_MASTER_PASSWORD = os.getenv("QUEUE_MASTER_PASSWORD", default = "abir101")
    QUEUE_SLAVE_HOST = os.getenv("QUEUE_SLAVE_HOST", default = "localhost")
    QUEUE_SLAVE_PORT = os.getenv("QUEUE_SLAVE_PORT", default = 6379)
    QUEUE_SLAVE_PASSWORD = os.getenv("QUEUE_SLAVE_PASSWORD", default = "abir101")

    # Email
    SENDER_EMAIL_NAME = os.getenv("SENDER_EMAIL_NAME", default = "asdf@gmail.com")
    SENDER_EMAIL_PASSWORD = os.getenv("SENDER_EMAIL_PASSWORD", default = "asdf")

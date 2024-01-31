import json
from .queue import Queue
from .emailClass import Email

def main():
    mail = Email()
    queue = Queue()
    subscriber = queue.read_message(["UserRegistered", "TicketCreated"])

    for message in subscriber.listen():
        if message["type"] == "message":
            if message["channel"] =="UserRegistered":
                data = json.loads(message["data"])
                mail.send_mail(data["email"], f'{data["name"]} is registered successfully')

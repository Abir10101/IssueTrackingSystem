import smtplib, ssl
from config import app_config

class Email:

    def __init__(self):
        self.smtp_server = "smtp.gmail.com"
        self.port = 465
        self.sender_email = app_config.SENDER_EMAIL_NAME
        self.sender_pass = app_config.SENDER_EMAIL_PASSWORD
        self.context = ssl.create_default_context()

    def send_mail(self, receiver_email, message):
        with smtplib.SMTP_SSL(self.smtp_server, self.port, context=self.context) as server:
            server.login(self.sender_email, self.sender_pass)
            server.sendmail(self.sender_email, receiver_email, message)

import smtplib
import ssl
import os
from dotenv import load_dotenv

load_dotenv()  # Tải các biến môi trường từ tệp .env

def send_email(message):
    host = "smtp.gmail.com"
    port = 465

    username = "phanhoang4501@gmail.com"
    password = os.getenv("PASSWORD")  # Lấy mật khẩu từ tệp .env
    receiver = "phanhoang4501@gmail.com"
    context = ssl.create_default_context()

    with smtplib.SMTP_SSL(host, port, context=context) as server:
        server.login(username, password)
        server.sendmail(username, receiver, message)

import smtplib ,ssl

def send_email(message):
    host = "smtp.gmail.com"
    port = 465

    username = "phanhoang4501@gmail.com"
    password = "tspnmoqpezvsmxbf"
    context = ssl.create_default_context()
    receiver = "phanhoang4501@gmail.com"

    with smtplib.SMTP_SSL(host, port, context=context) as server:
        server.login(username, password)
        server.sendmail(username, receiver, message)


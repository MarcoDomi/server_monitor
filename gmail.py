import smtplib
from email.message import EmailMessage


def send_mail(subject, content):
    email = "marcod082@gmail.com"

    msg = EmailMessage()
    msg.set_content(content)
    msg["subject"] = subject
    msg["from"] = email
    msg['to'] = email

    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.ehlo()
    server.starttls()

    server.login(email, "xyau bflg qqwp lfgi")
    server.send_message(msg)
    server.quit()

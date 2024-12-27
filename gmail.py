import smtplib
from email.message import EmailMessage

def get_email_info():
    with open("email-info.txt") as file:
        email = file.readline()
        code = file.readline()

    return (email, code)

def send_mail(subject, content):
    email, code = get_email_info()

    msg = EmailMessage()
    msg.set_content(content)
    msg["subject"] = subject
    msg["from"] = email
    msg['to'] = email

    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.ehlo()
    server.starttls()

    server.login(email, code)
    server.send_message(msg)
    server.quit()

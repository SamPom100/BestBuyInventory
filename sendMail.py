import smtplib
from email.message import EmailMessage


def sendMail(subject, body):
    gmail_user = ''
    gmail_password = ''

    server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
    server.ehlo()
    server.login(gmail_user, gmail_password)

    msg = EmailMessage()
    msg.set_content(body)
    msg['Subject'] = subject
    msg['From'] = ''
    msg['To'] = ''

    server.send_message(msg)
    server.quit()
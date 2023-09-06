import smtplib, ssl
import os


port = 465
smtp_server = "smtp.gmail.com"
SENDER = "Do not reply"
USERNAME = os.environ.get('USER_EMAIL')
PASSWORD = os.environ.get('USER_PASSWORD')
message = """\
Subject: GitHub Email Report

This is your daily email report.
"""

context = ssl.create_default_context()
with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
    server.login(USERNAME,PASSWORD)
    server.sendmail(SENDER,USERNAME,message)
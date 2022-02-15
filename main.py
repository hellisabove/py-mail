#!/usr/bin/env python3
import smtplib
import ssl

def mail_shit():
    port = 587  # For starttls
    smtp_server = "smtp.server" # Here you put your email provider smtp server
    sender_email = "yout@email.com" # Here you put your email address
    receiver_email = "your@gmail.com" # Here you put the receiver's email address
    password = input("Type your password and press enter:")
    # Here you put your message along with a Subject and rest of message
    message = """\
    Subject: 
    
    """
    
    context = ssl.create_default_context()
    with smtplib.SMTP(smtp_server, port) as server:
        server.ehlo()  # Can be omitted
        server.starttls(context=context)
        server.ehlo()  # Can be omitted
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, message)

#mailer.py
import smtplib
import os

def send_emails(emails, schedule, forecast):
    # Connect to the smtp server
    server = smtplib.SMTP('smtp.gmail.com', '587')

    # Start TLS encryption
    server.starttls()

    # Login
    password = os.environ['PASSWORD']
    from_email = os.environ['EMAIL']
    server.login(from_email, password)

    # Send email to entire list
    for to_email, name in emails.items():
        message = 'Subject: Python Emailer\n'
        message += 'Hello ' + name + '!\n\n'
        message += forecast + '\n\n' + schedule
        message += '\n\nCome on down!'
        server.sendmail(from_email, to_email, message)

    server.quit()

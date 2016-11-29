import dotenv
import os
dotenv.load_dotenv(dotenv.find_dotenv())
import requests
import smtplib

def get_emails():
    emails = {}
    
    try:
        email_file = open('emails2.txt', 'r')
    
        for line in email_file:
            (email, name) = line.split(',')
            emails[email] = name.strip()
    except FileNotFoundError as err:
        print(err)

    return emails

def get_schedule():
    try:
        schedule_file = open('schedule.txt', 'r')
    
        schedule = schedule_file.read()
    except FileNotFoundError as err:
        print(err)
    
    return schedule

def get_weather_forecast():
    # Make request to OpenWeather
    url = 'http://api.openweathermap.org/data/2.5/find?q=Orlando,fl&units=imperial&appid=' + os.environ['APPID']
    weather_request = requests.get(url)
    
    # Parse response 
    weather_json = weather_request.json()
    desc = weather_json['list'][0]['weather'][0]['description']
    temp_max = weather_json['list'][0]['main']['temp_max']
    temp_min = weather_json['list'][0]['main']['temp_min']

    # Build message to be returned
    forecast = 'The Circus forecast for today is '
    forecast += desc + ' with a high of ' + str(temp_max) + ' degrees'
    forecast += ' and a low of ' + str(temp_min) + ' degrees' + '.'

    return forecast

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
        message += '\nCome on down!'
        server.sendmail(from_email, to_email, message)

    server.quit()

def main():
    emails = get_emails()
    print(emails)

    schedule = get_schedule()
    print(schedule)

    forecast = get_weather_forecast()
    print(forecast)

    send_emails(emails, schedule, forecast)

main()


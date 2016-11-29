#weather.py
import requests
import os

def get_weather_forecast():
    # Make request to OpenWeather
    url = 'http://api.openweathermap.org/data/2.5/find?q=Orlando,fl&units=imperial&appid=' + os.environ['APPID']
    weather_request = requests.get(url)
    
    # Parse response 
    weather_json = weather_request.json()
    desc = weather_json['list'][0]['weather'][0]['description']
    temp_max = weather_json['list'][0]['main']['temp_max']
    temp_min = weather_json['list'][0]['main']['temp_min']

    # Build weather forecast message
    forecast = 'The Circus forecast for today is '
    forecast += desc + ' with a high of ' + str(temp_max) + ' degrees'
    forecast += ' and a low of ' + str(temp_min) + ' degrees' + '.'

    return forecast
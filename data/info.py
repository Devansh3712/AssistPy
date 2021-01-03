'''
Module for weather data of a
city given by user
'''

#Import modules
try:
    import requests
    import json
    import platform
    import datetime

except:
    print('Info module not setup')
    exit()

#Return data template
weather_template = '''
Temperature: {}
Humidity: {}
Weather Report: {}
'''

#Return data template
sysinfo_template = '''
System: {}
Node Name: {}
Machine : {}
'''

#Return data template
datetime_template = '''
Date: {} {}, {}
Day: {}
Time: {}:{} {}
'''

#Class for providing weather data of a city
class Weather:

    def __init__(self, city = str):
        self.city    = city
        #API key for accessing data
        self.api_key = "c958565bfec6edea5314899b41958b9f"

    def weather_data(self):

        #Using OpenWeatherMap API
        base_url = "https://api.openweathermap.org/data/2.5/weather?"
        url      = base_url + "q=" + self.city + "&appid=" + self.api_key
        response = requests.get(url)

        if response.status_code == 200:

            data     = response.json()
            main     = data['main']
            temp     = main['temp']
            humidity = main['humidity']
            report   = data['weather']

            return weather_template.format(temp, humidity, report[0]['description'])

        else:
            return 'Error in HTTP request'

#Class for providing local machine information
class Info:

    def system_info():

        my_system = platform.uname()

        return sysinfo_template.format(my_system.system, my_system.node, my_system.machine)

#Class for providing current date and time
class TimeDate:

    def current_date_time():

        #Initializing current datetime object
        now      = datetime.datetime.now()

        date     = now.strftime("%d")
        month    = now.strftime("%B")
        year     = now.strftime("%Y")
        day      = now.strftime("%A")
        hour     = now.strftime("%I")
        minute   = now.strftime("%M")
        meridian = now.strftime("%p")

        return datetime_template.format(date, month, year, day, hour, minute, meridian)

'''
Devansh Singh, 2021
GitHub: Devansh3712
'''
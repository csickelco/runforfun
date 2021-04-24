import requests
import datetime

# api-endpoint
URL = "https://api.openweathermap.org/data/2.5/onecall"
EXCLUDE = "minutely,daily,current"
UNITS="Imperial"

class Weather:
    def __init__(self, main, description, icon):
        self.main = main
        self.description = description
        self.icon = icon

    def info(self):
        return {
            'main': self.main,
            'description': self.description,
            'icon': self.icon
        }

class HourlyWeather:

    def __init__(self, date, temp, feels_like, wind_speed, wind_gust, precipitation_probability, weather):
        self.date = date
        self.temp = temp
        self.feels_like = feels_like
        self.wind_speed = wind_speed
        self.wind_gust = wind_gust
        self.precipitation_probability = precipitation_probability
        self.weather = weather

    def info(self):
        return {
            'date': self.date,
            'temp': self.temp,
            'feels_like': self.feels_like,
            'wind_speed': self.wind_speed,
            'wind_gust': self.wind_gust,
            'precipitation_probability': self.precipitation_probability,
            'weather': ', '.join([str(w.info()) for w in self.weather])
        }


def get_weather(api_key, latitude, longitude, date_time):
    date_time_hour = date_time.replace(minute=0)
    params = {'lat': latitude, 'lon': longitude, 'exclude': EXCLUDE, 'units': UNITS, 'appid': api_key}

    # sending get request and saving the response as response object
    r = requests.get(url=URL, params=params)

    # extracting data in json format
    data = r.json()
    hourly_weather = data['hourly']
    for hour in hourly_weather:
        hour_date = hour['dt']
        hour_timestamp = datetime.datetime.fromtimestamp(hour_date)
        if hour_timestamp == date_time_hour:
            weathers = hour['weather']
            hourly_weathers = []
            for weatherInstance in weathers:
                hourly_weathers.append(Weather(weatherInstance['main'], weatherInstance['description'], weatherInstance['icon']))
            return HourlyWeather(hour_timestamp, hour['temp'], hour['feels_like'], hour['wind_speed'], hour['wind_gust'],
                           hour['pop'], hourly_weathers)
    return None

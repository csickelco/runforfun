import requests
from datetime import datetime
from dateutil import tz

# Constants
ISO_8601_FORMAT = "%Y-%m-%dT%H:%M:%S%z"
URL = "https://api.sunrise-sunset.org/json"


class SunriseSunset:

    def __init__(self, sunrise, sunset, civilTwilightBegin, civilTwilightEnd):
        self.sunrise = sunrise
        self.sunset = sunset
        self.civilTwilightBegin = civilTwilightBegin
        self.civilTwilightEnd = civilTwilightEnd

    def info(self):
        return {
            'sunrise': self.sunrise,
            'sunset': self.sunset,
            'civilTwilightBegin': self.civilTwilightBegin,
            'civilTwilightEnd': self.civilTwilightEnd
        }


def get_sunrise_sunset(latitude, longitude, date_val):

    to_zone = tz.gettz('America/New_York')

    call_params = {'lat': latitude, 'lng': longitude, 'date': date_val, 'formatted': 0}

    # sending get request and saving the response as response object
    r = requests.get(url=URL, params=call_params)

    # extracting data in json format
    data = r.json()

    # extracting sunrise, civil_twilight_begin
    sunrise_utc = datetime.strptime(data['results']['sunrise'], ISO_8601_FORMAT)
    sunrice_local = sunrise_utc.astimezone(to_zone)
    sunset_utc = datetime.strptime(data['results']['sunset'], ISO_8601_FORMAT)
    sunset_local = sunset_utc.astimezone(to_zone)
    civil_twilight_begin_utc = datetime.strptime(data['results']['civil_twilight_begin'], ISO_8601_FORMAT)
    civil_twilight_begin_local = civil_twilight_begin_utc.astimezone(to_zone)
    civil_twilight_end_utc = datetime.strptime(data['results']['civil_twilight_end'], ISO_8601_FORMAT)
    civil_twilight_end_local = civil_twilight_end_utc.astimezone(to_zone)

    return SunriseSunset(sunrice_local, sunset_local, civil_twilight_begin_local, civil_twilight_end_local)

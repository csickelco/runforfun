import sys
from util import emailer
from api import sunrise_sunset
from api import weather
from dao import training_plan_dao
from dao import dress_my_run_dao
import datetime

if len(sys.argv) < 7:
    print("Usage: python3 runforfun/runforfun.py {send_email_address} {receiver_email} {password} {trainingPlan} {dressRules} {weatherAPIKey}")
    sys.exit(0)

sender_email = sys.argv[1]
receiver_email = sys.argv[2]
password = sys.argv[3]
training_plan = sys.argv[4]
dress_rules = sys.argv[5]
weather_api_key = sys.argv[6]

latitude = "43.161030"
longitude = "-77.610924"

print("Running for runforfun...")

sunriseSunset = sunrise_sunset.get_sunrise_sunset()
tomorrow = datetime.date.today() + datetime.timedelta(days=1)
workout = training_plan_dao.get_workout_for_date(training_plan, tomorrow)

if workout is None:
    print('No planned workout for tomorrow')
else:
    forecast = weather.get_weather(weather_api_key, latitude, longitude, workout.workout_date_time)
    dress = dress_my_run_dao.get_dress_for_weather(dress_rules, forecast.temp)

    # Create the plain-text and HTML version of your message
    text = """\
    This is your run reminder from runforfun!"""
    html = f"""\
    <html>
      <body>
        <p>This is your run reminder from runforfun!</p>
        <p><b>Workout:</b></p>
        <ul>
            <li>Distance: {workout.distance} miles</li>
            <li>Duration: {workout.duration} minutes</li>
            <li>Time: {workout.workout_date_time}</li>
            <li>Notes: {workout.notes}</li>
        </ul>
        <p><b>What to Wear:</b></p>
        <p>{dress.dress_items}</p>
        </p>
        <p><b>Weather:</b></p>
        <ul>
            <li>Temperature: {forecast.temp}</li>
            <li>Feels Like Temperature: {forecast.feels_like}</li>
            <li>Wind Speed: {forecast.wind_speed}</li>
            <li>Wind Gust: {forecast.wind_gust}</li>
            <li>Precipitation Probability: {forecast.precipitation_probability}</li>
            <li>Description: {forecast.weather[0].description}</li>
            <li>Icon: {forecast.weather[0].icon}</li>
        </ul>
        <b>Sunrise/Sunset:</b>
        <ul>
            <li>Sunrise: {sunriseSunset.sunrise}</li>
            <li>Sunset: {sunriseSunset.sunset}</li>
            <li>Twilight Begin: {sunriseSunset.civilTwilightBegin}</li>
            <li>Twilight End: {sunriseSunset.civilTwilightEnd}</li>
        </ul>
      </body>
    </html>
    """
    emailer.send_email(sender_email, receiver_email, password, "Run Reminder", text, html)

print("Successfully completed runforfun")
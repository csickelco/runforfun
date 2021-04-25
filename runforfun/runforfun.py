import sys
import datetime
from util import emailer
from util import template_engine
from api import sunrise_sunset
from api import weather
from dao import training_plan_dao
from dao import dress_my_run_dao
from dao import routes_dao

if len(sys.argv) < 8:
    print("Usage: python3 runforfun/runforfun.py {send_email_address} {receiver_email} {password} {trainingPlan} {dressRules} {routes} {weatherAPIKey}")
    sys.exit(0)

sender_email = sys.argv[1]
receiver_email = sys.argv[2]
password = sys.argv[3]
training_plan = sys.argv[4]
dress_rules = sys.argv[5]
routes = sys.argv[6]
weather_api_key = sys.argv[7]

latitude = "43.161030"
longitude = "-77.610924"

print("Running for runforfun...")

plan_sunrise_sunset = sunrise_sunset.get_sunrise_sunset()
tomorrow = datetime.date.today() + datetime.timedelta(days=1)
workout = training_plan_dao.get_workout_for_date(training_plan, tomorrow)

if workout is None:
    print('No planned workout for tomorrow')
else:
    forecast = weather.get_weather(weather_api_key, latitude, longitude, workout.workout_date_time)
    dress = dress_my_run_dao.get_dress_for_weather(dress_rules, forecast.temp)
    routes = routes_dao.get_suggested_routes(routes, workout.distance)

    html = template_engine.render_run_plan(workout, routes, plan_sunrise_sunset, forecast, dress)
    emailer.send_email(sender_email, receiver_email, password, "Run Reminder", 'Run For Fun Plan"', html)

print("Successfully completed runforfun")
import sys
import datetime
import configparser
from util import emailer
from util import template_engine
from api import sunrise_sunset
from api import weather
from dao import training_plan_dao
from dao import dress_my_run_dao
from dao import routes_dao

if len(sys.argv) < 2:
    print("Usage: python3 runforfun/runforfun.py {user}")
    sys.exit(0)

# Read System Configuration
system_config = configparser.ConfigParser()
system_config.read(f'../config/system.ini')
sender_email = system_config['DEFAULT']['sender_email']
password = system_config['DEFAULT']['password']
weather_api_key = system_config['DEFAULT']['weather_api_key']

# Read User Configuration
user_config_path = sys.argv[1]
user_config = configparser.ConfigParser()
user_config.read(f'../config/users/{user_config_path}/user.ini')
receiver_email = user_config['DEFAULT']['receiver_email']
latitude = float(user_config['DEFAULT']['latitude'])
longitude = float(user_config['DEFAULT']['longitude'])

training_plan = f'../config/users/{user_config_path}/training_plan.csv'
dress_rules = f'../config/users/{user_config_path}/dress_rules.csv'
routes = f'../config/users/{user_config_path}/routes.csv'

print("Running for runforfun...")

plan_sunrise_sunset = sunrise_sunset.get_sunrise_sunset(latitude, longitude, 'tomorrow')
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
import sys
from util import emailer
from api import sunrise_sunset

if len(sys.argv) < 4:
    print("Usage: python3 runforfun/runforfun.py {send_email_address} {receiver_email} {password")
    sys.exit(0)

sender_email = sys.argv[1]
receiver_email = sys.argv[2]
password = sys.argv[3]

print("Running for runforfun...")
sunriseSunset = sunrise_sunset.get_sunrise_sunset()
print(f'Sunrise/Sunst: {sunriseSunset.info()}')

# Create the plain-text and HTML version of your message
text = """\
This is your run reminder from runforfun!"""
html = f"""\
<html>
  <body>
    <p>This is your run reminder from runforfun!</p>
    <b>Sunrise/Sunset</b>
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
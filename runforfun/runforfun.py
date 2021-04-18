import sys
from util import emailer

if len(sys.argv) < 4:
    print("Usage: python3 runforfun/runforfun.py {send_email_address} {receiver_email} {password")
    sys.exit(0)

sender_email = sys.argv[1]
receiver_email = sys.argv[2]
password = sys.argv[3]

# Create the plain-text and HTML version of your message
text = """\
This is your run reminder from runforfun!"""
html = """\
<html>
  <body>
    <p>This is your run reminder from runforfun!</p>
  </body>
</html>
"""

print("Running for runforfun...")
emailer.send_email(sender_email, receiver_email, password, "Run Reminder", text, html)
print("Successfully completed runforfun")
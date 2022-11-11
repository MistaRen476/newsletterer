# Install Courier SDK: pip install trycourier
from trycourier import Courier
import os

client = Courier(auth_token=os.environ.get("AUTH_TOKEN"))

emails = open("emails.txt").read().split("\n")

# replace templateId with the Id of any template to change the email
templateId = "GR2X59V1JRMJTFJJPCR01C4PRRG2"

for email in emails:
  resp = client.send_message(
    message={
      "to": {
        "email": email,
      },
      "template": templateId,
      "data": {
      },
    }
  )

print(resp['requestId'])
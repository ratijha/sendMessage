from twilio.rest import Client
import datetime as dt
import travel
import os
from threading import Timer
import argparse
import logging
TWILIO_ACCOUNT_SID = os.environ.get("TWILIO_ACCOUNT_SID")
TWILIO_AUTH_TOKEN = os.environ.get("TWILIO_AUTH_TOKEN")
client = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)

# client.messages.create(to="+919902187842", from_="+12052674717",body="python")
logfiletouse = 'log.txt'
logging.basicConfig(filename=logfiletouse, level=logging.DEBUG,
                            format='%(asctime)s,%(levelname)s,%(message)s',datefmt="%Y-%m-%d %H-%M-%S")
# nextDay = dt.datetime.now() + dt.timedelta(days=1)
# dateString = nextDay.strftime('%d-%m-%Y') + " 05-00-00"
# newDate = nextDay.strptime(dateString, '%d-%m-%Y %H-%M-%S')
# delay = (newDate - dt.datetime.now()).total_seconds()
# res = Timer(delay, travel.travel('Karaikkudi', 'Bangalore', '20170910'), ()).start()
# slack_client.api_call("chat.postMessage", token=token, channel=channel,
#                       text="", as_user=True)
# time.sleep(READ_WEBSOCKET_DELAY)
parser = argparse.ArgumentParser()
parser.add_argument('--date',  required=True)
parser.add_argument('--phonenumber',  required=True)
args = parser.parse_args()

res = travel.travel('Karaikkudi', 'Bangalore', args.date)
logging.info("results found {0}".format(res))
# client.messages.create(to="+919902187842", from_="+12052674717",body=res)
if not res:
    res = "No Buses Found"
client.messages.create(to=args.phonenumber,
                         from_="+12052674717",
                         body="{0}".format(res))

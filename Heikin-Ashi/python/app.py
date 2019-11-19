import requests
import json
from twilio.rest import Client
from datetime import datetime, timedelta
from flask import Flask, request
import schedule
import time
from threading import Thread
app = Flask(__name__)
global HA_Close_latest 
HA_Close_latest = 0 
global HA_Open_latest 
HA_Open_latest = 0
global temp
temp = 0
def sms():
    print("Running periodic task!")
    utc_datetime_current = datetime.datetime.utcnow()
    utc_datetime_prev = utc_datetime_current - timedelta(hours=2)
    utc_datetime_prev = utc_datetime_prev.strftime("%Y/%m/%d %H:%M")
    utc_datetime_current = utc_datetime_current.strftime("%Y/%m/%d %H:%M")
    split_utc_datetime_current = utc_datetime_current.strip(' ')
    date_utc_datetime_current = split_utc_datetime_current[0]
    time_utc_datetime_current = split_utc_datetime_current[1]
    split_datetime_prev = utc_datetime_prev.strip(' ')
    time_utc_datetime_prev = split_utc_datetime_prev[1]
    response = requests.get('https://globalmetals.xignite.com/xGlobalMetals.json/GetBars?Symbol=XAU&Currency=USD&AsOfDate='+date_utc_datetime_current+'&StartTime='+time_utc_datetime_prev+'&EndTime='+time_utc_datetime_current+'&PriceType=Mid&TickPrecision=Minute&TickPeriods=120&_token=F1EA90FFBFF4462993E99968CE39F08C')
      if(response.status_code == 200):
        latest = response.content
        latest = json.loads(latest)
        latest = latest[0]
        if(latest["Open"]!=0 and latest["Close"]!=0 and latest["Low"]!=0 and latest["High"]!=0 ):
            if(HA_Close_latest == 0):  
                HA_Open_latest = (1320.978+1319.854) /2
            else:


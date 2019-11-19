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

# Backtesting for a certain date
import requests
import json
def heikenashi_calc (date,startTime,endTime,flag,Prev_HA_Open,Prev_HA_Close):
    if(flag == 0):
  latest = response.content
            latest = json.loads(latest)
            latest = latest[0]

# Backtesting for a certain date
import requests
import json
def heikenashi_calc (date,startTime,endTime,flag,Prev_HA_Open,Prev_HA_Close):
    if(flag == 0):
  latest = response.content
            latest = json.loads(latest)
            latest = latest[0]
 if(latest["Open"]!=0 and latest["Close"]!=0 and latest["Low"]!=0 and latest["High"]!=0 ):
HA_Open_latest = (Prev_HA_Open+Prev_HA_Close) /2

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
 HA_Close_latest = (latest["Open"] + latest["Close"] +  latest["Low"] + latest["High"]) /4
return HA_Open_latest,HA_Close_latest
  # do something
    else:
        #do someting
  response = requests.get('https://globalmetals.xignite.com/xGlobalMetals.json/GetBars?Symbol=XAU&Currency=USD&AsOfDate='+date+'&StartTime='+startTime+'&EndTime='+endTime+'&PriceType=Mid&TickPrecision=Minute&TickPeriods=120&_token=F1EA90FFBFF4462993E99968CE39F08C')
        if(response.status_code == 200):
 latest = response.content
            latest = json.loads(latest)
 latest = latest[0]
            if(latest["Open"]!=0 and latest["Close"]!=0 and latest["Low"]!=0 and latest["High"]!=0 ):

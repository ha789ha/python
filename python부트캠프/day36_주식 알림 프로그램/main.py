import requests
import datetime
import pandas as pd
from twilio.rest import Client

# variables
STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla Inc"

NEWS_API = "91c5d1a19240486a809659043ad30c0a"
STOCK_API = "EBYTCCZUKE1RW5TR"

NEWS_ENDPOINT = "https://newsapi.org/v2/everything"
STOCK_ENDPOINT = "https://www.alphavantage.co/query"

account_sid = "AC3306113769342c8fd73505b3d4bdfe3c"
auth_token = "a0cbf65643909755570e06609087349e"


## Get stock Info api
parameter ={
    'function' : 'TIME_SERIES_DAILY',
    'symbol' : STOCK_NAME,
    'apikey' : STOCK_API

}
response = requests.get(url=STOCK_ENDPOINT, params=parameter)
response.raise_for_status()
data = response.json()

# Calculating the increase/decrease ratio
yesterday_price = float(list(data['Time Series (Daily)'].values())[1]['4. close'])
before_yesterday_price = float(list(data['Time Series (Daily)'].values())[2]['4. close'])
difference = abs(yesterday_price - before_yesterday_price)
percent = difference/yesterday_price

## get stock news api
news_param = {
    'apiKey':NEWS_API,
    'q' : COMPANY_NAME
}
news = requests.get(url=NEWS_ENDPOINT, params=news_param)
news_data = news.json()


# Set messeges from twilio api
client = Client(account_sid, auth_token)
if percent > 5:
    message = client.messages \
        .create(
        body=f'TSLA: 🔺{percent}% \n Headline: {news_data["articles"][0]["title"]}',
        from_='+1 980 385 7686',
        to='+82 10 4934 5696'
    )
    print(message.status)


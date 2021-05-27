import encodings
from twilio.rest import Client
import requests
import os
from datetime import datetime
import json
import smtplib

# ------------------------------------ dates handling ----------------------------- #
current_date = datetime.today()
print(current_date.date())

current_day = current_date.day
current_day_month = current_date.month
current_year = current_date.year
previous_day = current_day - 1
two_previous_days = current_day - 2

format(current_day)

previous_day_api_data = ('{:04d}-{:02d}-{:02d}'.format(current_year, current_day_month, previous_day))
two_previous_days_api_data = ('{:04d}-{:02d}-{:02d}'.format(current_year, current_day_month, two_previous_days))

# ---------------------------------- constant variables ------------------------------- #
STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"
STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"
ALPHAVANTAGE_API_KEY = "UM9TMTRB3BWDKANL"
ALPHAVANTAGE_API_PARAMS = {
    "function": "TIME_SERIES_DAILY",
    "symbol": "TSLA",
    "interval": "60min",
    "apikey": "UM9TMTRB3BWDKANL"
}

NEWSAPI_PARAMS = {
    "apikey": "ba98208f6f8941b1855c38f877a58636",
    "q": "TSLA",
    "from": previous_day_api_data,
    "to": current_date.date(),
}

account_sid = 'AC61ede28bb8fef058ac9b2421fed00753'
auth_token = '16d12df86503b606211cc6a3687a445b'
client = Client(account_sid, auth_token)

print(previous_day)
EMAIL = "jayber1@yahoo.com"
PASSWORD = "yvfngtkvredjkygx"

# ------------------------- api calls news, stock prices ----------------------------- #

stock_price = requests.get(STOCK_ENDPOINT, params=ALPHAVANTAGE_API_PARAMS)
daily_prices = stock_price.json()

news_data = requests.get(NEWS_ENDPOINT, params=NEWSAPI_PARAMS)
news = news_data.json()

# ----------------------- creation of files for ease of reading ---------------------- #
with open("daily_stock_prices.json", "w") as file:
    json.dump(daily_prices, file, indent=4)
with open("news.json", "w") as file:
    json.dump(news, file, indent=4)

# ------------------------------- process code --------------------------------------- #

two_days_close_price = float((daily_prices['Time Series (Daily)'][two_previous_days_api_data]['4. close']))
previous_day_close_price = float((daily_prices['Time Series (Daily)'][previous_day_api_data]['4. close']))

if previous_day_close_price > two_days_close_price:
    positive_rev_in_cash = previous_day_close_price - two_days_close_price
    positive_rev_in_percent = positive_rev_in_cash / previous_day_close_price * 100
    txt = ("""subject: your daily update \n\nhell yea you made {:1.2f}$ which is 🔺{:5.2f} % \n
here are some of today's news\ntitle{}\n{:1000}\n\ntitle{:1000}\n{}""")

    to_send = (txt.format(positive_rev_in_cash, positive_rev_in_percent, news['articles'][0]['title'],
                          news['articles'][0]['description'],news['articles'][1]['title'],
                          news['articles'][1]['description']
                          ))
    
    message = client.messages.create(body=to_send,from_='+16827309600',to='+972526767682')

 

else:
    negative_rev_in_cash = two_days_close_price - previous_day_close_price
    negative_rev_in_percent = negative_rev_in_cash / previous_day_close_price * 100

    txt = ("ohhh what a shame you lost {:1.2f}$ which is -{:5.2f} % ")
    print(txt.format(negative_rev_in_cash, negative_rev_in_percent))


import requests
import os
from datetime import datetime
import json

# ------------------------------------------- gets current date -----------------------------------------
current_date = datetime.today()
print(current_date.date())
print(type(current_date.date()))
current_day = current_date.day
current_day_month = current_date.month
current_year = current_date.year
previous_day = current_day - 1 
print(f"{current_year}-{current_day_month}-{current_day}")


# ------------------------------------------- constant variables ----------------------------------------

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
    "from": current_date.date(),
    "to": current_date.date(),
    }






stock_price = requests.get(STOCK_ENDPOINT, params=ALPHAVANTAGE_API_PARAMS)

daily_prices = stock_price.json()



with open("daily_stock_prices.json", "w") as file:
    json.dump(daily_prices, file, indent=4)

print(daily_prices['Time Series (Daily)'])
news_data = requests.get(NEWS_ENDPOINT, params=NEWSAPI_PARAMS)

news = news_data.json()

# print(news['articles'])

with open("news.json", "w") as file:
    json.dump(news, file, indent=4)


## STEP 1: Use https://newsapi.org/docs/endpoints/everything
# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").
# HINT 1: Get the closing price for yesterday and the day before yesterday. Find the positive difference between the two prices. e.g. 40 - 20 = -20, but the positive difference is 20.
# HINT 2: Work out the value of 5% of yerstday's closing stock price.


## STEP 2: Use https://newsapi.org/docs/endpoints/everything
# Instead of printing ("Get News"), actually fetch the first 3 articles for the COMPANY_NAME. 
# HINT 1: Think about using the Python Slice Operator


## STEP 3: Use twilio.com/docs/sms/quickstart/python
# Send a separate message with each article's title and description to your phone number. 
# HINT 1: Consider using a List Comprehension.


# Optional: Format the SMS message like this:
# """
# TSLA: 🔺2%
# Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
# Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
# or
# "TSLA: 🔻5%
# Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
# Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
# """

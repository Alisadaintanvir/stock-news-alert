import os
import requests
from datetime import datetime, timedelta
from message import SendMessage
from dotenv import load_dotenv
load_dotenv()

ALPHAVANTAGE_API = os.environ.get("ALPHAVANTAGE_API")
NEWSAPI_API = os.environ.get("NEWSAPI_API")
STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"

message = SendMessage()

# Getting yesterday date and day before yesterday date
now = datetime.now()
yesterday = (datetime.today() - timedelta(days=1)).date()
day_before_yesterday = (datetime.today() - timedelta(days=2)).date()

alphavantage_params = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK,
    "apikey": ALPHAVANTAGE_API
}
url = f'https://www.alphavantage.co/query?'
response = requests.get(url, alphavantage_params)
response.raise_for_status()

data = response.json()["Time Series (Daily)"]
data_list = [value for (key, value) in data.items()]

yesterday_closing_price = data_list[0]['4. close']
day_before_yesterday_closing_price = data_list[1]['4. close']
difference = abs(float(yesterday_closing_price) - float(day_before_yesterday_closing_price))

difference_percentage = (difference / float(yesterday_closing_price)) * 100


if difference_percentage < 5:
    news_api_url = "https://newsapi.org/v2/everything?"
    news_api_params = {
        "q": COMPANY_NAME,
        "apikey": NEWSAPI_API,
        "pageSize": 1
    }
    news_api_response = requests.get(news_api_url, news_api_params)
    news_api_response.raise_for_status()
    articles = news_api_response.json()["articles"]
    # Send a separate message with the percentage change and each article's title and description to your phone number.
    message.send(articles, COMPANY_NAME, difference_percentage)

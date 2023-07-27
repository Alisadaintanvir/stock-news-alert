# Stock Price and News Notifier
This script retrieves the daily stock price data for a given stock symbol (TSLA - Tesla Inc) from Alpha Vantage API and checks if there was a significant percentage change in the stock price compared to the previous day's closing price. If the percentage change is less than 5%, it fetches the latest news articles related to the company (Tesla Inc) from NewsAPI and sends them, along with the percentage change, to a specified phone number using the SendMessage class.

## Prerequisites
Python 3.x
Required Python packages: `requests`

## Setup
Sign up for a free account and obtain API keys from the following services:

- Alpha Vantage API: Alpha Vantage
- NewsAPI: NewsAPI
- Set the obtained API keys as environment variables with the names ALPHAVANTAGE_API and NEWSAPI_API, respectively.

Make sure the message.py file with the SendMessage class is present in the same directory as this script.

## Usage
Clone this repository to your local machine.

Navigate to the project directory and run the script:

`python main.py`

## Description
The script performs the following steps:

Imports necessary libraries and modules.
Fetches the closing stock prices of the specified stock symbol (TSLA - Tesla Inc) from the Alpha Vantage API for yesterday and the day before yesterday.
Calculates the percentage difference between the closing prices of the two days.
If the percentage difference is less than 5%, it fetches the top 3 news articles related to the specified company (Tesla Inc) using the News API.
Sends a message to your phone number containing the percentage change and each article's title and description.
Please ensure that the message module (defined in message.py) is set up correctly to send messages to your phone number.

## Note: The script uses the "datetime" module to fetch the stock prices for yesterday and the day before yesterday.

Disclaimer: The script's purpose is to provide a basic demonstration of fetching stock prices and news articles. It may require additional error handling, logging, and security measures for production use.

## License
This project is licensed under the MIT License.

### Feel free to modify and use it according to your needs.

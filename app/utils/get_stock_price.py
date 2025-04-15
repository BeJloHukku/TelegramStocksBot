import yfinance as yf
import requests

def get_stock_price(ticker: str) -> float:
    stock = yf.Ticker(ticker)
    price = stock.history(period="1d")['Close'].iloc[-1]
    return price



def get_price_for_russian_stock(ticker: str) -> float:
    url = f"https://iss.moex.com/iss/engines/stock/markets/shares/securities/{ticker}.json"
    response = requests.get(url).json()
    price = response["securities"]["data"][0][3]  
    return float(price)



import yfinance as yf

def get_stock_history(ticker, period):
    stock = yf.Ticker(ticker)
    history = stock.history(period=period)
    return history['Close'].to_string()


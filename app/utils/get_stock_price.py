import requests


def get_price(ticker: str) -> float:
    url = f"https://iss.moex.com/iss/engines/stock/markets/shares/securities/{ticker}.json"
    response = requests.get(url).json()
    price = response["marketdata"]["data"][-1][2]  
    return float(price)


print(get_price('ROSN'))



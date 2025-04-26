import requests


def get_information(ticker: str) -> dict:
    url = f"https://iss.moex.com/iss/engines/stock/markets/shares/securities/{ticker}.json"
    response = requests.get(url).json()
    shortname = response['securities']['data'][0][2]
    columns = response['marketdata']['columns']
    data = response['marketdata']['data'][-1]
    information = dict(zip(columns, data))
    information['shortname'] = shortname
    return information











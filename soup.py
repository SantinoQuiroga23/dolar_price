import requests
from icecream import ic

dolar_oficial: str = "https://dolarapi.com/v1/dolares/oficial"
dolar_blue: str = "https://dolarapi.com/v1/dolares/blue"
dolar_bolsa: str = "https://dolarapi.com/v1/dolares/bolsa"
crypto_price: str = 'https://api.coingecko.com/api/v3/simple/price'

lista: list = [dolar_blue, dolar_oficial, dolar_bolsa, crypto_price]

ids: str = "usd-coin"

def crypto(url: str, ids: str):
    params = {'ids': ids, 'vs_currencies': 'ars'}
    response = requests.get(url, params=params)

    if response.ok:
        data: dict = response.json()
    else:
        ic("error: crypto currency its not avaible")
    return data

def dolar(url: str):
    response = requests.get(url=url)

    if response.ok:
        data: dict = response.json()
    else:
        ic("error")
    return data


if __name__ == '__main__':
    dolar(url=dolar_oficial)
    crypto(url=crypto_price, ids=ids)


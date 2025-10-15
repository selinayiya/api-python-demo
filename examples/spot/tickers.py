from azpython.spot import Spot

az = Spot(host="https://sapi.az.com", access_key='', secret_key='')
print(az.get_tickers(symbol='btc_usdt'))
print(az.get_tickers(symbols=['btc_usdt', 'eth_usdt']))

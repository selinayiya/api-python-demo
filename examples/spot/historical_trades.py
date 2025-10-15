from azpython.spot import Spot

az = Spot(host="https://sapi.az.com", access_key='', secret_key='')
print(az.get_trade_history(symbol='btc_usdt'))
print(az.get_trade_history(symbol='btc_usdt', limit=10))

from azpython.spot import Spot

az = Spot(host="https://sapi.az.com", access_key='', secret_key='')
print(az.get_symbol_config(symbol='btc_usdt'))

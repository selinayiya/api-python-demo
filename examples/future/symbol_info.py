from azpython.perp import Perp

az = Perp(host="https://fapi.az.com", access_key='', secret_key='')
print(az.get_market_config(symbol='btc_usdt'))

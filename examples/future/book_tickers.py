from azpython.perp import Perp

az = Perp(host="https://fapi.az.com", access_key='', secret_key='')
print(az.get_book_ticker(symbol='btc_usdt'))

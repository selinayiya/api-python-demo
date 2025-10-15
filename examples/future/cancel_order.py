from azpython.perp import Perp

az = Perp(host="https://fapi.az.com", access_key='', secret_key='')
res = az.cancel_order(order_id=12345678)
print(res)

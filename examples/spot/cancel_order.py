from azpython.spot import Spot

az = Spot(host="https://sapi.az.com", access_key='', secret_key='')
res = az.cancel_order(order_id=12345678)
print(res)

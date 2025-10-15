# -*- coding:utf-8 -*-

from azpython.spot import Spot

az = Spot(host="https://sapi.az.com", access_key='', secret_key='')
print(az.transfer(from_account="SPOT", to_account="FUTURES_U", currency="usdt", amount=10))

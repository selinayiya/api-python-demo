# -*- coding:utf-8 -*-
from azpython.spot import Spot

az = Spot(host="https://sapi.az.com", access_key='', secret_key='')
print(az.listen_key())

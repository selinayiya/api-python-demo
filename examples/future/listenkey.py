# -*- coding:utf-8 -*-
from azpython.perp import Perp

az = Perp(host="https://fapi.az.com", access_key='', secret_key='')
print(az.listen_key())

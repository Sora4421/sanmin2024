# -*- coding: utf-8 -*-
"""
Created on Thu Aug  1 19:52:06 2024

@author: USER
"""

import requests
import json

url = "https://data.moenv.gov.tw/api/v2/aqx_p_432?language=zh&api_key=4bbcef77-dbf7-4ce6-b069-06f1dda1eb92"

data = requests.get(url).text

air = json.loads(data)

allair = air['records']

for item in allair:
    print("縣市:",item['sitename'])
    print("地區:",item['county'])
    print("AQI:",item['aqi'])
    print("空氣品質:",item['status'])
    print()
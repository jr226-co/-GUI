import colorama
from termcolor import colored
colorama.init()

import json
import urllib.request

import time


try:
    url = 'https://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/2.5_day.geojson'
    res = urllib.request.urlopen(url)
    # json_loads() でPythonオブジェクトに変換S
    data = json.loads(res.read().decode('utf-8'))  

    url = data['features'][0]['properties']['detail']
    res = urllib.request.urlopen(url)
    # json_loads() でPythonオブジェクトに変換S
    data = json.loads(res.read().decode('utf-8'))
    print(data)
    # 深さdata['properties']['products']['origin'][0]['properties']['depth']
    # M data['properties']['products']['origin'][0]['properties']['magnitude']
    #time data['properties']['products']['origin'][0]['properties']['eventtime']



except urllib.error.HTTPError as e:
    print('HTTPError: ', e)
except json.JSONDecodeError as e:
    print('JSONDecodeError: ', e)
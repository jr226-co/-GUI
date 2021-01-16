import colorama
from termcolor import colored
colorama.init()
from decimal import Decimal, ROUND_HALF_UP, ROUND_HALF_EVEN
import json
import urllib.request

import time

from bs4 import BeautifulSoup 
from requests import get 
import time

def hi():
    us = "0"
    hi = "0"
    while True:
        url = 'https://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/2.5_day.geojson'
        res = urllib.request.urlopen(url)
        # json_loads() でPythonオブジェクトに変換S
        data = json.loads(res.read().decode('utf-8'))  
        url = data['features'][0]['properties']['detail']
        res = urllib.request.urlopen(url)
        # json_loads() でPythonオブジェクトに変換S
        data = json.loads(res.read().decode('utf-8'))
        # 深さdata['properties']['products']['origin'][0]['properties']['depth']
        # M data['properties']['products']['origin'][0]['properties']['magnitude']
        #time data['properties']['products']['origin'][0]['properties']['eventtime']
        #場所　data['properties']['place']
        m = Decimal(str(data['properties']['products']['origin'][0]['properties']['magnitude'])).quantize(Decimal('0.1'), rounding=ROUND_HALF_UP)
        h = Decimal(str(data['properties']['products']['origin'][0]['properties']['depth'])).quantize(Decimal('0'), rounding=ROUND_HALF_UP)
        if us == data['properties']['products']['origin'][0]['properties']['eventtime']:
            pass
        else:
            us = data['properties']['products']['origin'][0]['properties']['eventtime']
            print ("\n--------------------------------------------------------------------------------------")
            print(f"[{m}]{data['properties']['place']} {h}km {data['properties']['products']['origin'][0]['properties']['eventtime']}【USGS】")
        
        url = "https://www.hinet.bosai.go.jp/?LANG=ja"
            
        html = get(url)
        #html = open(html.content.,encoding="utf-8") 
        soup = BeautifulSoup(html.content, 'lxml') 
        icon_part = soup.find_all("table",class_="top_rtmap")
        #M icon_part[0].contents[13].contents[2]
        #深さ　icon_part[0].contents[11].contents[2]
        # sinegn icon_part[0].contents[3].contents[2]
        #time icon_part[0].contents[5].contents[2]
        if hi == icon_part[0].contents[5].contents[2]:
            pass
        else:
            hi = icon_part[0].contents[5].contents[2]
            print ("\n--------------------------------------------------------------------------------------")
            print(f"[{icon_part[0].contents[13].contents[2].text}]{icon_part[0].contents[3].contents[2].text} {icon_part[0].contents[5].contents[2].next}【Hi-net】")
            time.sleep(10)





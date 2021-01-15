import colorama
from termcolor import colored
colorama.init()


# Requestsを利用してWebページを取得する
from bs4 import BeautifulSoup 
from requests import get 
import time




#def soku():

while True:
    url = "https://eqdata.sakura.ne.jp/kyoshin/ws/2moni/2sec_alm_2monitw.html#"

    html = get(url)
    soup = BeautifulSoup(html.content, 'lxml') 
    icon_part = soup.find_all("div", id="baseMap")
    try:
        if icon_part[0].contents[72].text !="":
            s = icon_part[0].contents[72].text
            print(colored(f"{s}","yellow"))
        else:
            time.sleep(2)
    except:
        time.sleep(2)

import colorama
from termcolor import colored
colorama.init()

ss= ["1","3","5","7","9","11"]
# Requestsを利用してWebページを取得する
from bs4 import BeautifulSoup 
from requests import get 
import time



nai = []
def jr():
    url = "https://www3.jrhokkaido.co.jp/webunkou/index.asp?a=2"
    html = get(url)
    soup = BeautifulSoup(html.content, 'lxml') 
    icon_part = soup.find_all("div", id="InfoGeneral")
    while True:
        try:
            print ("\n--------------------------------------------------------------------------------------")
            print("JR北海道　運行情報")
            print(icon_part[0].contents[1].contents[0])
            for  ss1 ,sss in  enumerate(icon_part[0].contents[3].contents):
                if str(sss) == "<br/>":
                    pass
                else:
                    try:
                        k = icon_part[0].contents[3].contents[ss1].contents
                        print(" ")
                        for  ss11 ,ss1 in  enumerate(k):
                            
                            if str(ss1) == "<br/>":
                                pass
                            else:
                                
                                print(ss1)
                            
                    except:
                        print(sss)
            else:
                time.sleep(1800)


        except:
            time.sleep(1800)
                    


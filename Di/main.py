from tkinter.font import families
import warnings
import PySimpleGUI as sg
import feedparser
import textwrap
from multiprocessing import  Process 
from plyer import notification
import datetime
import pytz 

from urllib.request import urlopen
import xmltodict
import sindo
import zisin
import keihou
import kisyou
import kins
import jr
import sys
import ken
import ziso

ame = []
zi = []
zui = []
sono =[]
ts = []
kou = 0
tst = 0
zen_syu =["高頻度定時","高頻度随時","高頻度地震火山","高頻度その他",
        "長期定時","長期随時","長期地震火山","長期その他"]


zen_URL =['http://www.data.jma.go.jp/developer/xml/feed/regular.xml',
        "http://www.data.jma.go.jp/developer/xml/feed/extra.xml",
        "http://www.data.jma.go.jp/developer/xml/feed/eqvol.xml",
        "http://www.data.jma.go.jp/developer/xml/feed/other.xml",
        "http://www.data.jma.go.jp/developer/xml/feed/regular_l.xml",
        "http://www.data.jma.go.jp/developer/xml/feed/extra_l.xml",
        "http://www.data.jma.go.jp/developer/xml/feed/eqvol_l.xml",
        "http://www.data.jma.go.jp/developer/xml/feed/other_l.xml",]

zen_nai = ["0","0","0","0","0","0","0","0"]
bann = [0,1,2,3,4,5,6,7]

syunai = ["府県気象情報","地方気象情報","全般気象情報","府県天気概況"]
kei = ["気象特別警報・警報・注意報","気象警報・注意報（Ｈ２７）"]
zi = ["震源・震度に関する情報"]
soku  = ["震度速報"]


import datetime
import time

#  セクション1 - オプションの設定と標準レイアウト

sg.LOOK_AND_FEEL_TABLE['MyNewTheme'] = {
	'BACKGROUND': '#103456',
	'TEXT': 'black',
	'INPUT': '#DDE0DE',
	'SCROLL': '#E3E3E3',
	'TEXT_INPUT': 'black',
	'BUTTON': ('black', '#ffffff'),
	'PROGRESS': sg.DEFAULT_PROGRESS_BAR_COLOR,
	'BORDER': 1,
	'SLIDER_DEPTH': 0,
	'PROGRESS_DEPTH': 0
}
# テーマの適用
sg.theme('MyNewTheme')


layout = [
    [sg.Text("高頻度")],
    [sg.Button("自動"),sg.Button("更新")],
    [sg.Button("終了")],
    ]

# セクション 2 - ウィンドウの生成
window = sg.Window('防災情報[仮]', layout, size=(200, 150),resizable=True)
    

# セクション 3 - イベントループ

    
def loop_a():
    while True:  # Event Loop
    
        event, values = window.read()
    
        global kou

        if event in ( None,'終了'):
            window.close()

        if event == "自動":
            Process(target=loop_b).start()
            
        if event == "更新":
            for (a, b,c) in zip(bann ,zen_URL,zen_syu):           
                news_dic = feedparser.parse(b)
                latest_entry = news_dic['entries'][0]
                rss1 = latest_entry.title + " " +latest_entry.author
                rss2 =  latest_entry.content
                rss3 = latest_entry.link
                ta = latest_entry.updated    
    
                d = datetime.datetime.fromisoformat(ta.replace('Z', '+00:00'))
                d =  d.astimezone(datetime.timezone(datetime.timedelta(hours=9)))
                print ("\n--------------------------------------------------------------------------------------")
                print (c)
                print (rss1)
                print (rss2[0]["value"])
                print (f"発表日時:{d}")
                print(rss3)                            
                zen_nai[a] = rss1
                if latest_entry.title  in syunai:
                    kisyou.zyou(latest_entry.link)
                elif  latest_entry.title in kei:       
                    keihou.keihou(latest_entry.link)
                elif latest_entry.title in zi :
                    sindo.zisin(latest_entry.link)
                elif latest_entry.title in soku:
                    zisin.sokuhou(latest_entry.link)


def loop_b():
    
    
    global kou,tst,ame
    while True: 
        for (a, b,c) in zip(bann ,zen_URL,zen_syu):           
            
            news_dic = feedparser.parse(b)

            try:
                latest_entry = news_dic['entries'][0]
                rss1 = latest_entry.title + " " +latest_entry.author
                rss2 =  latest_entry.content
                rss3 = latest_entry.link
                ta = latest_entry.updated
        
        
                d = datetime.datetime.fromisoformat(ta.replace('Z', '+00:00'))
                d =  d.astimezone(datetime.timezone(datetime.timedelta(hours=9)))


        
                if   zen_nai[a]  == ta:
                    pass
                
                else:

                    print ("\n--------------------------------------------------------------------------------------")
                    print (c)
                    print (rss1)
                    print (rss2[0]["value"])
                    print (f"発表日時:{d}")
                    print(rss3)
                    if latest_entry.title  in syunai:
                        kisyou.zyou(latest_entry.link)
                    elif  latest_entry.title in kei:       
                        keihou.keihou(latest_entry.link)
                    elif latest_entry.title in zi :
                        sindo.zisin(latest_entry.link)
                    elif latest_entry.title in soku:
                        zisin.sokuhou(latest_entry.link)
                    
                    if zen_nai[a] == "0":
                        pass
                    else:    
                        notification.notify(
                            title=f'{rss1}',
                            message=f' {textwrap.fill(rss2[0]["value"], 1000)}',
                            app_name='アプリ名だよ',    
                        )
                    zen_nai[a] = ta
            except:
                print("エラー:")
                print(b)
                print(c)
                        

                    
        else:
            
            time.sleep(10)




def jrs():
    jr.jr()
def kens():
    ken.lv()
def zisos():
    ziso.hi()

            

if __name__ == '__main__':
    Process(target=loop_a).start() 
    Process(target=jrs).start() 
    Process(target=kens).start()     
    Process(target=zisos).start()   

    
    
    
    



    
    



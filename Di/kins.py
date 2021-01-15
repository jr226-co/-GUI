
import colorama
from termcolor import colored
colorama.init()

import json
import urllib.request

import time


def kin():
    hou = '0'
    while True:

        try:
            url = 'https://api.iedred7584.com/eew/json/'
            res = urllib.request.urlopen(url)
            # json_loads() でPythonオブジェクトに変換S
            data = json.loads(res.read().decode('utf-8'))
            try:
                if hou == '0' and data['Type']['Detail'][0:2] == '最終':
                    time.sleep(1)
                    hou = data['Serial']
                    pass

                
                elif hou == data['Serial']:
                    pass
                else:

                    if str(data['Warn']) == 'True':
                        ir = "red"
                    else:
                        ir = "yellow"
                    if data['Type']['Detail'][0:2] == '最終':
                        hoiso = f"第{data['Serial']}報 (最終)"

                    else:
                        hoiso = f"第{data['Serial']}報"
                    
                    print(colored(f"■■■{data['Title']['String']}[{hoiso}]■■■",ir))
                    print(colored(f"震源:{data['Hypocenter']['Name']}",ir))
                    print(colored(f"深さ:約{data['Hypocenter']['Location']['Depth']['Int']}km  M:{data['Hypocenter']['Magnitude']['Float']}",ir))
                    print(colored(f"発生時間：{data['OriginTime']['String']}",ir))
                    if ir == 'red':
                        print(colored("発表地域：",ir))
                        for da in data['WarnForecast']['Regions']:
                            print(colored(f"{da},",ir),end='')
                    hou = data['Serial']
                        
                    
            except KeyError:
                print(f"■■■{data['Title']['String']}[第{data['Serial']}報]■■■")
                print("先ほどの緊急地震速報は取り消しされました")
                time.sleep(1)

        except urllib.error.HTTPError as e:
            print('HTTPError: ', e)
        except json.JSONDecodeError as e:
            print('JSONDecodeError: ', e)
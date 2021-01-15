import websocket
import threading
import time
import json
import ast
nai = {}
def lv():
    def syu():
        from bs4 import BeautifulSoup 
        from requests import get 
        import time
        url = "https://kwatch-24h.net/socket.io/1/?t=1610188002218"
        
        html = get(url)
        #html = open(html.content.,encoding="utf-8") 
        soup = BeautifulSoup(html.content, 'lxml') 
        icon_part = soup.find_all("body")

        
        url = "wss://kwatch-24h.net/socket.io/1/websocket/" + icon_part[0].contents[0].next[:20]
        return url

    def on_message(ws, message):
        na = message
        na = na[4:]
        nai = ast.literal_eval(na)
        if nai['args'][0]['r'] >= 1 or  nai['args'][0]['y'] >=10 or nai['args'][0]['l'] >= 100:
            print ("\n--------------------------------------------------------------------------------------")
            print(f"赤：{nai['args'][0]['r']}")
            print(f"黄：{nai['args'][0]['y']}")
            print(f"緑：{nai['args'][0]['g']}")
            print(f"Lv：{nai['args'][0]['l']}")

        

    


    def on_error(ws, error):
        print('Error:{}'.format(error))

    def on_close(ws):
        print('再接続')
        main()
    
    def on_open(ws):
        def run(*args):
            print('Open')
            for i in range(3):
                time.sleep(1)
                message = "Hello " + str(i)
                ws.send(message)
                print('Sent:{}'.format(message))
            time.sleep(1)
            ws.close()
            print('Thread terminating...')
            threading.start_new_thread(run, ())


    def main():
        websocket.enableTrace(False)
        url = syu()
        ws = websocket.WebSocketApp(url,
                                on_message = on_message,
                                on_error = on_error,
                                on_close = on_close)
        ws.on_open = on_open
        ws.run_forever()


    main()


from typing import NoReturn
import feedparser
import xml.etree.ElementTree as ET
import pprint
from urllib.request import urlopen
from bs4 import BeautifulSoup
from feedparser import encodings



def zisin(url):
    news_dic = feedparser.parse(url)
    instance = urlopen(url)

        # instanceからHTMLを取り出して、BeautifulSoupで扱えるようにパースします
    import xmltodict


    show_xml_output = instance
    text = {}

    nai = {}
    si = 0
    ti = 0
    ss ={}
    yy ={}
    sa = []
    tis = []
    details_root = xmltodict.parse(show_xml_output )
    ss = details_root
    print('震源・震度に関する情報')
    print(f"震源:{details_root['Report']['Body']['Earthquake']['Hypocenter']['Area']['Name']}")
    print(details_root['Report']['Head']['Headline']['Text'])
    print (f"マグニチュード:{details_root['Report']['Body']['Earthquake']['jmx_eb:Magnitude']['#text']}")
    print (f"{details_root['Report']['Body']['Earthquake']['Hypocenter']['Area']['jmx_eb:Coordinate']['@description']}")

    print(f"最大震度：{str(details_root['Report']['Body']['Intensity']['Observation']['MaxInt'])}")
    print(f"情報:{details_root['Report']['Body']['Comments']['ForecastComment']['Text']}")
    text['data'] = {
            print(f"地震ID:{details_root['Report']['Head']['EventID']}")

        }




    kk = details_root['Report']['Body']['Intensity']['Observation']['Pref']
    for sd ,sl in enumerate(kk):
        try:
            if si == '1':
                si = '0'
            else:
                pass
            for  k ,ss in  enumerate(kk[sd]['Area']):   
                k = int(k)
        
                yy = kk[sd]['Area'] 
                try:
                    if ti == kk[sd]['Name']:    


                        
                        if si == yy['City'][sd]['MaxInt']:
                            if yy['City'][sd]['Name']   in sa:
                                break

                            else:
                                print(f",{yy['City'][sd]['Name']}", end='')
                                sa.append (yy['City'][sd]['Name'])
                                si =  yy['City'][sd]['MaxInt']
                                break
                                
                        else:
                            si =  yy['City'][sd]['MaxInt']
                        
                            print(f"震度{yy['City'][sd]['MaxInt']}:" ,end='' )
                            print(yy['City'][sd]['Name'], end='')
                            break                       
                    else:
                        if kk[sd]['Name'] not  in  tis:

                            try:
                            
                                print("\n ")
                                print(f"{kk[sd]['Name']}")
                                ti = kk[sd]['Name']
                            
                                sa.append (yy[sd]['City']['Name'])
                                sa.pop()
                                
                        
                                try:
                                    print(f"震度{kk[sd]['City'][0]['MaxInt']}:",end='')
                                    print(kk[sd]['City'][0]['Name'], end='')
                                    si =  kk[sd]['MaxInt']
                                    ti = kk[sd]['Name']
                                    tis.append(kk[sd]['Name'])
                                    sa.append(kk[sd]['City'][0]['Name'])
                
                                except:
                                    
                                    for  kls ,ss1 in  enumerate(yy):
                                        for  kl ,ss1 in  enumerate(yy[kls]['City']):
                                            try:
                                                if yy[kls]['City'][kl]['Name'] not in sa :
                                                    

                                                    if si == yy[kls]['City'][kl]['MaxInt']:
                                                        print(f",{yy[kls]['City'][kl]['Name']}",end='')
                                                    else:
                                                        print(f"震度{yy[kls]['City'][kl]['MaxInt']}:",end='')
                                                        print(f"{yy[kls]['City'][kl]['Name']}",end='')

                                                    si =  yy[kls]['City'][kl]['MaxInt']
                                                    ti = kk[sd]['Name']
                                                    tis.append( kk[sd]['Name'])
                                                    sa.append(yy[kls]['City'][kl]['Name'])
                                                else:
                                                    pass
                                            except:
                                                if yy[kls]['City']['Name'] not in sa :

                                                    if si == yy[kls]['City']['MaxInt']:
                                                        print(f",{yy[kls]['City'][kl]['Name']}",end='')
                                                    else:
                                            
                                                        print(f"震度{yy[kls]['City']['MaxInt']}:",end='')
                                                        print(f"{yy[kls]['City']['Name']}",end='')

                                                    si =  yy[kls]['City']['MaxInt']
                                                    ti = kk[sd]['Name']
                                                    
                                                    tis.append(kk[sd]['Name'])
                                                    sa.append(yy[kls]['City']['Name'])
                                                else:
                                                    pass

                                        

                            except:
                                try:
                                    print(f"震度{yy['City']['MaxInt']}:",end='')
                                    print(f"{yy['City']['Name']}", end='')
                                    si =  kk[sd]['MaxInt']
                                    ti = kk[sd]['Name']
                                    tis.append(kk[sd]['Name'])
                                    sa.append (yy['City']['Name'])
                                    break
                                except:
                                    for  kls ,ss1s in  enumerate(yy['City']):

                                        if yy['City'][kls]['Name'] not in sa :

                                            if si == yy['City'][kls]['MaxInt']:
                                                print(f",{yy['City'][kls]['Name']}",end='')
                                            else:
                                                print(" ")
                                                print(f"震度{yy['City'][kls]['MaxInt']}:",end='')
                                                print(f"{yy['City'][kls]['Name']}",end='')

                        
                                            si =  yy['City'][kls]['MaxInt']
                                            ti = yy['City'][kls]['Name']
                                            tis.append(kk[sd]['Name'])
                                            sa.append(yy['City'][kls]['Name'])    
                                        else:
                                            pass                           


                        else:
                            break
                except:

                    if ti == kk[sd]['Name']:    


                        try:    
                            if si == yy['City']['MaxInt']:
                                if yy['City']['Name']   in sa:
                                    break

                                else:
                                    print(f",{yy['City']['Name']}", end='')
                                    sa.append (yy['City']['Name'])
                                    break
                                    
                            else:
                                si =  yy['City']['MaxInt']
                                print("  ")
                                print(f"震度{yy['City']['MaxInt']}:" ,end='' )
                                print(yy['City']['Name'], end='')
                                break   
                        except:
                            for ok ,sl in enumerate(yy):
                                for oks ,sl in enumerate(yy[ok]['City']):
                                    try:
                                        if yy[ok]['City'][oks]['Name'] not in sa:
                                            if si == yy[ok]['City'][oks]['MaxInt']:

                                                print(f",{yy[ok]['City'][oks]['Name']}", end='')
                                                sa.append (yy[ok]['City'][oks]['Name'])
                                                    
                                                    
                                            else:
                                                si =  yy[ok]['City'][oks]['MaxInt']
                                                print("  ")
                                                print(f"震度{yy[ok]['City'][oks]['MaxInt']}:" ,end='' )
                                                print(yy[ok]['City'][oks]['Name'], end='')   
                                                sa.append(yy[ok]['City'][oks]['Name'])
                                        else:
                                            pass
                                    except:
                                        if si == yy[ok]['City']['MaxInt']:
                                            tan = yy[ok]['City']
                                            if tan['Name']   in sa:
                                                break

                                            else:
                                                print(f",{tan['Name']}", end='')
                                                sa.append (tan['Name'])
                                                break
                                                
                                        else:
                                            si =  yy[ok]['City']['MaxInt']
                                            print("  ")
                                            print(f"震度{yy[ok]['City']['MaxInt']}:" ,end='' )
                                            print(yy[ok]['City']['Name'], end=',')
                                            break   


                    else:
                        if kk[sd]['Name'] not  in  tis:
                        
                            try:

                                print(f"震度{yy['City'][0]['MaxInt']}:",end='')
                                print(yy['City'][0]['Name'], end=',')
                                si =  kk[sd]['MaxInt']
                                ti = kk[sd]['Name']
                                tis.append(kk[sd]['Name'])
                                sa.append(yy['City'][0]['Name'])
                                break
                            except:
                                try:
                                    print(f"震度{yy['City']['MaxInt']}:",end='')
                                    print(yy['City']['Name'], end=',')
                                    si =  kk[sd]['MaxInt']
                                    ti = kk[sd]['Name']
                                    tis.append(kk[sd]['Name'])
                                    sa.append (yy['City']['Name'])
                                    break
                                except:
                                    for  kls ,ss1s in  enumerate(yy['City']):

                                        if yy['City'][kls]['Name'] not in sa :

                                            if si == yy[kls]['City']['MaxInt']:
                                                print(f",{yy['City'][kls]['MaxInt']}",end='')
                                            else:
                                    
                                                print(f"震度{yy['City'][kls]['MaxInt']}:",end='')
                                                print(f"{yy['City'][kls]['Name']}",end='')

                        
                                            si =  yy['City'][kls]['MaxInt']
                                            ti = yy['City'][kls]['Name']
                                            tis.append(kk[sd]['Name'])
                                            sa.append(yy['City'][kls]['Name'])    
                                        else:
                                            pass                       
        except:
            try:
                for  kp ,ssl in  enumerate(kk[sd]):   
                    try:
                        for  k ,ss in  enumerate(kk[kp]['Area']):   
                            k = int(k)
            
                    
                            yy = kk[sd]['Area'] 
                            
                            try:
                                if ti == kk[kp]['Name']:    


                                    
                                    if si == yy['City']['MaxInt']:
                                        if yy['City']['Name']   in sa:
                                            break

                                        else:
                                            print(f",{yy['City']['Name']}", end='')
                                            sa.append (yy['City']['Name'])
                                            break
                                            
                                    else:
                                        si =  yy['City']['MaxInt']
                                        print("  ")
                                        print(f"震度{yy['City']['MaxInt']}:" ,end='' )
                                        print(yy['City']['Name'], end='')
                                        break                       
                                else:
                                    if kk[kp]['Name'] not  in  tis:

                                    
                                        try:

                                            sa.append (yy['City'][0]['Name'])

                                            print(f"震度{yy['City'][0]['MaxInt']}:",end='')
                                            print(yy['City'][0]['Name'], end='')
                                            si =  kk[kp]['MaxInt']
                                            ti = kk[kp]['Name']
                                            tis.append(kk[kp]['Name'])
                                            sa.append(yy['City'][0]['Name'])
                                            

                                            break
                                        except:
                                            try:
                                                lll = yy['City']['MaxInt']
                                                print("\n ")
                                                print(f"{kk[kp]['Name']}")
                                                
                                            
                                                print(f"震度{yy['City']['MaxInt']}:",end='')
                                                print(f"{yy['City']['Name']}", end='')
                                                si =  kk[kp]['MaxInt']
                                                ti = kk[kp]['Name']
                                                tis.append(kk[kp]['Name'])
                                            
                                                sa.append (yy['City']['Name'])
                                            except:                                
                                                print(f"震度{yy[0]['City']['MaxInt']}:",end='')
                                                si =  kk[kp]['Area'][0]['City']['MaxInt']
                                                ti = kk[kp]['Area'][0]['City']['Name']
                                                tis.append(kk[kp]['Name'])                                
                                                sa.append (kk[kp]['Area'][0]['City']['Name'])                         
                                                for ss ,sls in enumerate(kk[kp]):
                                        
                                                    try:
                                                        si =  yy[kp]['City']['MaxInt']
                                                        print(f"震度{yy[kp]['City']['MaxInt']}:",end='')
                                                        print(yy[kp]['City']['Name'], end=',')
                                                        
                                                        ti = yy[kp]['City']['Name']
                                                        tis.append(kk[kp]['Name'])
                                                        break
                                                    
                                                        
                                                    except:   
                                                        try: 
                                                            si =  yy[kp]['City']['MaxInt']
                                                            print("\n ")
                                                            print(f"{kk[kp]['Name']}")
                                        
                                                            print(f"震度{yy[kp]['City']['MaxInt']}:",end='')
                                                            print(yy[kp]['City']['Name'] ,end=',')
                                                            si =  yy[kp]['City']['MaxInt']
                                                            ti = yy[kp]['City']['Name']
                                                            tis.append(kk[kp]['Name'])
                                                            sa.append (yy[kp]['City']['Name'])
                                                            break
                                                            


                                                        except:            
                                                            try : 
                                
                                                                if si == kk[kp]['Area'][ss]['City']['MaxInt']:
                                                                    print(yy[ss]['City']['Name'] ,end=',')
                                                                else:                                        
                                                                    print(f"震度{yy[ss]['City']['MaxInt']}:",end='')
                                                                    print(yy[ss]['City']['Name'] ,end=',')
                                                                
                                                        
                                                                si =  yy[ss]['City']['MaxInt']
                                                                ti =  yy[ss]['City']['Name']
                                                                tis.append(kk[kp]['Name'])
                                                                sa.append (yy[ss]['City']['Name'])
                                                                break
                                                
                                                            except:
                                                                try:
                                                                    if si ==  kk[kp]['Area']['City']['MaxInt']:

                                                                        print(f"震度{yy[kp]['City']['MaxInt']}:",end='')
                                                                        print(yy[kp]['Name'] ,end=',')
                                                                
                                                                    else:
                                                                        print(yy[kp]['City']['Name'] ,end='')

                                                                    si =  kk[kp]['City']['MaxInt']
                                                                    ti = yy[kp]['City']['Name']
                                                                    tis.append(kk[kp]['Name'])
                                                                    sa.append (yy[kp]['City']['Name'])
                                                                    break
                                                                
                                                                except:
                                                                    try:
                                                                        if si ==  kk[kp]['Area'][ss]['City']['MaxInt']:

                                                                            print(f"震度{yy[kp]['City'][ss]['MaxInt']}:",end='')
                                                                            print(yy[kp]['Name'] ,end=',')
                                                                    
                                                                        else:
                                                                            print(yy[kp]['City']['Name'] ,end='')

                                                                        si =  kk[kp]['Area'][ss]['City']['MaxInt']
                                                                        ti = yy[kp]['City'][ss]['Name']
                                                                        tis.append(kk[kp]['Name'])
                                                                        sa.append (yy[kp]['City'][ss]['Name'])
                                                                        break
                                                                    except:
                                                                        try:
                                                                            for sss ,slss in enumerate(kk[kp]['Area'][ss]['City']):
                                                                                if si ==  kk[kp]['Area'][ss]['City'][sss]['MaxInt']:

                                                                                    
                                                                                    print(yy[kp]['City'][sss]['Name'] ,end=',')
                                                                            
                                                                                else:
                                                                                    print(f"震度{yy[kp]['City'][sss]['MaxInt']}:",end='')
                                                                                    print(yy[kp]['City'][sss]['Name'] ,end='')

                                                                                si =  kk[kp]['Area'][ss]['City'][sss]['MaxInt']
                                                                                ti = yy[kp]['City'][sss]['Name']
                                                                                tis.append(kk[kp]['Name'])
                                                                
                                                                        except:
                                                                            break
                                                
                                    else:
                                        break
                            except:

                                if ti == kk[kp]['Name']:   


                                    try:    
                                        if si == yy['City']['MaxInt']:
                                            if yy['City']['Name']   in sa:
                                                break

                                            else:
                                                print(f",{yy['City']['Name']}", end='')
                                                sa.append (yy['City']['Name'])
                                                break
                                                
                                        else:
                                            si =  yy['City']['MaxInt']
                                            print("  ")
                                            print(f"震度{yy['City']['MaxInt']}:" ,end='' )
                                            print(yy['City']['Name'], end='')
                                            break   
                                    except:
                                        for ok ,sl in enumerate(yy):
                                            for oks ,sl in enumerate(yy[ok]['City']):
                                                try:
                                                    if  yy[ok]['City'][oks]['Name'] not in sa:
                                                        if si == yy[ok]['City'][oks]['MaxInt']:
                                                            tan = yy[ok]['City'][oks]

                                                            print(f",{tan['Name']}", end='')
                                                            sa.append (tan['Name'])
                                                                
                                                                
                                                        else:
                                                            si =  yy[ok]['City'][oks]['MaxInt']
                                                            print("  ")
                                                            print(f"震度{yy[ok]['City'][oks]['MaxInt']}:" ,end='' )
                                                            print(yy[ok]['City'][oks]['Name'], end='')     
                                                            sa.append(yy[ok]['City'][oks]['Name'])                                       
                                                            
                                                        

                                                    else:
                                                        pass
                                                        
                                                except:
                                                    try:
                                                        if  yy[ok]['City']['Name'] not in sa:
                                                            if si == yy[ok]['City']['MaxInt']:
                                                                tan = yy[ok]['City']
                                                                if tan['Name']   in sa:
                                                                    pass
                                                                    

                                                                else:
                                                                    print(f",{tan['Name']}", end='')
                                                                    sa.append (tan['Name'])
                                                                    
                                                                    
                                                            else:
                                                                tan = yy[ok]['City']
                                                                if yy[ok]['City']['Name']   in sa:
                                                                    pass
                                                                    
                                                                else:
                                                                    si =  yy[ok]['City']['MaxInt']
                                                                    print("  ")
                                                                    print(f"震度{yy[ok]['City']['MaxInt']}:" ,end='' )
                                                                    print(yy[ok]['City']['Name'], end=',')
                                                        else:
                                                            pass
                                                

                                                    except:
                                                        for okss ,slll in enumerate(yy[ok]['City']):
                                                            if yy[ok]['City']['Name'] not in sa:
                                                                if si == yy[ok]['City']['MaxInt']:
                                                                    tan = yy[ok]['City']
                                                                    if tan['Name']   in sa:
                                                                        pass
                                                                        

                                                                    else:
                                                                        print(f",{tan['Name']}", end='')
                                                                        sa.append (tan['Name'])
                                                                        
                                                                        
                                                                else:
                                                                    
                                                                    if tan['Name']   in sa:
                                                                        pass
                                                                        
                                                                    else:
                                                                        si =  yy[ok]['City']['MaxInt']
                                                                        print("  ")
                                                                        print(f"震度{yy[ok]['City']['MaxInt']}:" ,end='' )
                                                                        print(yy[ok]['City']['Name'], end=',')
                                                            else:
                                                                pass                                                    

                                                            


                                else:
                                    if kk[kp]['Name'] not  in  tis:

                                    
                                        try:
                                            sll = yy['City'][0]['MaxInt']
                                            print("\n ")
                                            print(f"{kk[kp]['Name']}")

                                            print(f"震度{yy['City'][0]['MaxInt']}:",end='')
                                            print(yy['City'][0]['Name'], end=',')
                                            si =  kk[kp]['MaxInt']
                                            ti = kk[kp]['Name']
                                            tis.append(kk[kp]['Name'])
                                            sa.append(yy['City'][0]['Name'])
                                            break
                                        except:
                                            try:
                                                
                                                print(f"震度{yy['City']['MaxInt']}:",end='')
                                                print(yy['City']['Name'], end=',')
                                                si =  kk[kp]['MaxInt']
                                                ti = kk[kp]['Name']
                                                tis.append(kk[kp]['Name'])
                                                sa.append (yy['City']['Name'])
                                                break
                                            except:
                                                try:
                                                    for kai ,sl in enumerate(yy):
                                                        print(f"震度{yy[kai]['City']['MaxInt']}:",end='')
                                                        print(yy[kai]['City']['Name'], end=',')
                                                        si =  kk[sd]['MaxInt']
                                                        ti = kk[sd]['Name']
                                                        tis.append(kk[sd]['Name'])
                                                        sa.append (yy[kai]['City']['Name'])
                                                        break
                                                except:
                                                    for kai ,sl in enumerate(yy):
                                                        try:
                                                            for kais ,sl in enumerate(yy[kai]['City']):
                                                                if yy[kai]['City'][kais]['Name'] not in sa:
                                                                
                                                                    if si == yy[kai]['City'][kais]['MaxInt']:                                                                       
                                                                        print(f",{yy[kai]['City'][kais]['Name']}", end='')
                                                                        si =  yy[kai]['City'][kais]['MaxInt']
                                                                        ti = kk[kp]['Name']
                                                                        tis.append(kk[kp]['Name'])
                                                                        sa.append (yy[kai]['City'][kais]['Name'])
                                                                    
                                                                    else:
                                                                        print(" ")
                                                                        print(f"震度{yy[kai]['City'][kais]['MaxInt']}:",end='')               
                                                                        print(f"{yy[kai]['City'][kais]['Name']}", end='')
                                                                        si =  yy[kai]['City'][kais]['MaxInt']
                                                                        ti = kk[kp]['Name']
                                                                        tis.append(kk[kp]['Name'])
                                                                        sa.append (yy[kai]['City'][kais]['Name'])
                                                                else:
                                                                    pass
                                                                    
                                                        except:
                                                            try:

                                                                for kais ,sl in enumerate(yy[kai]['City']):
                                                                    if  yy[kai]['City'][kais]['Name']  not in sa:  
                                                                        if si == yy[kai]['City'][kais]['MaxInt']:  
                                                                                                                                            
                                                                            print(f",{yy[kai]['City'][kais]['Name']}", end='')
                                                                            si =  yy[kai]['City'][kais]['MaxInt']
                                                                            ti = kk[kp]['Name']
                                                                            tis.append(kk[kp]['Name'])
                                                                            sa.append (yy[kai]['City'][kais]['Name'])
                                                                        
                                                                        else:
                                                                            print(f"震度{yy[kai]['City'][kais]['MaxInt']}:",end='')               
                                                                            print(yy[kai]['City'][kais]['Name'], end=',')
                                                                            si =  yy[kai]['City'][kais]['MaxInt']
                                                                            ti = kk[kp]['Name']
                                                                            tis.append(kk[kp]['Name'])
                                                                            sa.append (yy[kai]['City'][kais]['Name'])
                                                                    else:
                                                                        pass
                                                                        
                                                            except:
                                                                try:
                                                                    if yy[kai]['City']['Name'] not in sa:
                                                                        if si == yy[kai]['City']['MaxInt']:                                                                       
                                                                            print(f",{yy[kai]['City']['Name']}", end='')
                                                                            si =  yy[kai]['City']['MaxInt']
                                                                            ti = kk[kp]['Name']
                                                                            tis.append(kk[kp]['Name'])
                                                                            sa.append (yy[kai]['City']['Name'])
                                                                            
                                                                        else:
                                                                            print(" ")
                                                                            print(f"震度{yy[kai]['City']['MaxInt']}:",end='')               
                                                                            print(f"{yy[kai]['City']['Name']}", end='')
                                                                            si =  yy[kai]['City']['MaxInt']
                                                                            ti = kk[kp]['Name']
                                                                            tis.append(kk[kp]['Name'])
                                                                    else:
                                                                        pass
                                                                        
                                                                except:
                                                                    if yy['City']['Name'] not in sa:
                                                                        if si == yy['City']['MaxInt']:                                                                       
                                                                            print(yy['City']['Name'], end=',')
                                                                            si =  yy['City']['MaxInt']
                                                                            ti = kk[kp]['Name']
                                                                            tis.append(kk[kp]['Name'])
                                                                            sa.append (yy['City']['Name'])
                                                                            
                                                                        else:
                                                                            if yy['City']['Name'] not in sa:

                                                                                print(f"震度{yy['City']['MaxInt']}:",end='')               
                                                                                print(yy['City']['Name'], end=',')
                                                                                si =  yy['City']['MaxInt']
                                                                                ti = kk[kp]['Name']
                                                                                tis.append(kk[kp]['Name'])
                                                                                sa.append (yy['City']['Name'])    
                                                                            
                                                                            else:
                                                                                si =  yy['City']['MaxInt']
                                                                                ti = kk[kp]['Name']
                                                                                tis.append([kk][kp]['Name'])
                                                                                sa.append (yy['City']['Name']) 
                                                                    else:
                                                                        pass 
                                                                                                                    



                                                            


                                                            
                                    else:
                                        try:                            
                                            for ss ,sls in enumerate(kk[kp]):
                                    
                                                try:
                                                    si =  yy[kp]['City']['MaxInt']
                                                    print(f"震度{yy[kp]['City']['MaxInt']}:",end='')
                                                    print(yy[kp]['City']['Name'], end=',')
                                                    
                                                    ti = yy[kp]['City']['Name']
                                                    tis.append(kk[kp]['Name'])
                                                    break
                                                
                                                    
                                                except:   
                                                    try: 
                                                        si =  yy[kp]['City']['MaxInt']
                                                        print("\n ")
                                                        print(f"{kk[kp]['Name']}")
                                    
                                                        print(f"震度{yy[kp]['City']['MaxInt']}:",end='')
                                                        print(yy[kp]['City']['Name'] ,end=',')
                                                        si =  yy[kp]['City']['MaxInt']
                                                        ti = yy[kp]['City']['Name']
                                                        tis.append(kk[kp]['Name'])
                                                        sa.append (yy[kp]['City']['Name'])
                                                        break
                                                        


                                                    except:            
                                                        try : 
                                
                                                            if si == kk[kp]['Area'][ss]['City']['MaxInt']:
                                                                print(yy[ss]['City']['Name'] ,end=',')
                                                            else:                                        
                                                                print(f"震度{yy[ss]['City']['MaxInt']}:",end='')
                                                                print(yy[ss]['City']['Name'] ,end=',')
                                                            
                                                    
                                                            si =  yy[ss]['City']['MaxInt']
                                                            ti =  yy[ss]['City']['Name']
                                                            tis.append(kk[kp]['Name'])
                                                            sa.append (yy[ss]['City']['Name'])
                                                
                                                        except:
                                                            try:
                                                                if si ==  kk[kp]['Area']['City']['MaxInt']:

                                                                    print(f"震度{yy[kp]['City']['MaxInt']}:",end='')
                                                                    print(yy[kp]['Name'] ,end=',')
                                                            
                                                                else:
                                                                    print(yy[kp]['City']['Name'] ,end='')

                                                                si =  kk[kp]['City']['MaxInt']
                                                                ti = yy[kp]['City']['Name']
                                                                tis.append(kk[kp]['Name'])
                                                                sa.append (yy[kp]['City']['Name'])
                                                                break
                                                                
                                                            except:
                                                                try:
                                                                    if si ==  kk[kp][ss]['City']['MaxInt']:

                                                                        print(f"震度{yy[kp]['City'][ss]['MaxInt']}:",end='')
                                                                        print(yy[kp]['Name'] ,end=',')
                                                                
                                                                    else:
                                                                        print(yy[kp]['City']['Name'] ,end='')

                                                                    si =  kk[kp]['Area'][ss]['City']['MaxInt']
                                                                    ti = yy[kp]['City'][ss]['Name']
                                                                    tis.append(kk[kp]['Name'])
                                                                    sa.append (yy[kp]['City'][ss]['Name'])
                                                                    break
                                                                except:
                                                                    try:
                                                                        for sss ,slss in enumerate(kk[kp]['Area'][ss]['City']):
                                                                            if si ==  kk[kp]['Area'][ss]['City'][sss]['MaxInt']:

                                                                                
                                                                                print(yy[kp]['City'][sss]['Name'] ,end=',')
                                                                        
                                                                            else:
                                                                                print(f"震度{yy[kp]['City'][sss]['MaxInt']}:",end='')
                                                                                print(yy[kp]['City'][sss]['Name'] ,end='')

                                                                            si =  kk[kp]['Area'][ss]['City'][sss]['MaxInt']
                                                                            ti = yy[kp]['City'][sss]['Name']
                                                                            tis.append(kk[kp]['Name'])
                                                            
                                                                    except:
                                        
                                                                        break
                                        except:                            
                                            for ss ,sls in enumerate(kk[kp]['Area']['City']):
                                    
                                                try:
                                                    si =  yy[kp]['City']['MaxInt']
                                                    print(f"震度{yy[kp]['City']['MaxInt']}:",end='')
                                                    print(yy[kp]['City']['Name'], end=',')
                                                    
                                                    ti = yy[kp]['City']['Name']
                                                    tis.append(kk[kp]['Name'])
                                                    break
                                                
                                                    
                                                except:   
                                                    try: 
                                                        si =  yy[kp]['City']['MaxInt']
                                                        print("\n ")
                                                        print(f"{kk[kp]['Name']}")
                                    
                                                        print(f"震度{yy[kp]['City']['MaxInt']}:",end='')
                                                        print(yy[kp]['City']['Name'] ,end=',')
                                                        si =  yy[kp]['City']['MaxInt']
                                                        ti = yy[kp]['City']['Name']
                                                        tis.append(kk[kp]['Name'])
                                                        sa.append (yy[kp]['City']['Name'])
                                                        break
                                                        


                                                    except:            
                                                        try : 
                                
                                                            if si == kk[kp]['Area'][ss]['City']['MaxInt']:
                                                                print(yy[ss]['City']['Name'] ,end=',')
                                                            else:                                        
                                                                print(f"震度{yy[ss]['City']['MaxInt']}:",end='')
                                                                print(yy[ss]['City']['Name'] ,end=',')
                                                            
                                                    
                                                            si =  yy[ss]['City']['MaxInt']
                                                            ti =  yy[ss]['City']['Name']
                                                            tis.append(kk[kp]['Name'])
                                                            sa.append (yy[ss]['City']['Name'])
                                                
                                                        except:
                                                            try:
                                                                if si ==  kk[kp]['Area']['City']['MaxInt']:

                                                                    print(f"震度{yy[kp]['City']['MaxInt']}:",end='')
                                                                    print(yy[kp]['Name'] ,end=',')
                                                            
                                                                else:
                                                                    print(yy[kp]['City']['Name'] ,end='')

                                                                si =  kk[kp]['City']['MaxInt']
                                                                ti = yy[kp]['City']['Name']
                                                                tis.append(kk[kp]['Name'])
                                                                sa.append (yy[kp]['City']['Name'])
                                                                break
                                                                
                                                            except:
                                                                try:
                                                                    if si ==  kk[kp][ss]['City']['MaxInt']:

                                                                        print(f"震度{yy[kp]['City'][ss]['MaxInt']}:",end='')
                                                                        print(yy[kp]['Name'] ,end=',')
                                                                
                                                                    else:
                                                                        print(yy[kp]['City']['Name'] ,end='')

                                                                    si =  kk[kp]['Area'][ss]['City']['MaxInt']
                                                                    ti = yy[kp]['City'][ss]['Name']
                                                                    tis.append(kk[kp]['Name'])
                                                                    sa.append (yy[kp]['City'][ss]['Name'])
                                                                    break
                                                                except:
                                                                    try:
                                                                        for sss ,slss in enumerate(kk[kp]['Area'][ss]['City']):
                                                                            if si ==  kk[kp]['Area'][ss]['City'][sss]['MaxInt']:

                                                                                
                                                                                print(yy[kp]['City'][sss]['Name'] ,end=',')
                                                                        
                                                                            else:
                                                                                print(f"震度{yy[kp]['City'][sss]['MaxInt']}:",end='')
                                                                                print(yy[kp]['City'][sss]['Name'] ,end='')

                                                                            si =  kk[kp]['Area'][ss]['City'][sss]['MaxInt']
                                                                            ti = yy[kp]['City'][sss]['Name']
                                                                            tis.append(kk[kp]['Name'])
                                                            
                                                                    except:
                                                                        break                                                                
                    except:
                        break
            except:
                try:
                    for  k ,ss in  enumerate(kk['Area']):   
                        k = int(k)
        
                
                        yy = kk['Area'] 
                        
                        try:
                            if ti == kk['Name']:    


                                
                                if si == yy['City']['MaxInt']:
                                    if yy['City']['Name']   in sa:
                                        break

                                    else:
                                        print(f",{yy['City']['Name']}", end='')
                                        sa.append (yy['City']['Name'])
                                        break
                                        
                                else:
                                    if yy['City']['Name'] in sa :
                                        pass

                                    else:    

                                        si =  yy['City']['MaxInt']
                                        print("  ")
                                        print(f"震度{yy['City']['MaxInt']}:" ,end='' )
                                        print(yy['City']['Name'], end='')
                                                        
                            else:
                                if kk['Name'] not  in  tis:

                                
                                    try:

                                        sa.append (yy['City'][0]['Name'])
                                        print("\n ")
                                        print(f"{kk['Name']}")

                                        print(f"震度{yy['City'][0]['MaxInt']}:",end='')
                                        print(yy['City'][0]['Name'], end='')
                                        si =  kk['MaxInt']
                                        ti = kk['Name']
                                        tis.append(kk['Name'])
                                        

                                        break
                                    except:
                                        try:
                                            print("\n ")
                                            print(f"{kk['Name']}")
                                            
                                        
                                            print(f"震度{yy['City']['MaxInt']}:",end='')
                                            print(f"{yy['City']['Name']}", end='')
                                            si =  kk['MaxInt']
                                            ti = kk['Name']
                                            tis.append(kk['Name'])
                                        
                                            sa.append (yy['City']['Name'])
                                        except:                                
                                            print(f"震度{yy[0]['City']['MaxInt']}:",end='')
                                            si =  kk['Area'][0]['City']['MaxInt']
                                            ti = kk['Area'][0]['City']['Name']
                                            tis.append(kk['Name'])                                
                                            sa.append (kk['Area'][0]['City']['Name'])                         
                                            for ss ,sls in enumerate(kk):
                                    
                                                try:
                                                    si =  yy['City']['MaxInt']
                                                    print(f"震度{yy['City']['MaxInt']}:",end='')
                                                    print(yy['City']['Name'], end=',')
                                                    
                                                    ti = yy['City']['Name']
                                                    tis.append(kk['Name'])
                                                    break
                                                
                                                    
                                                except:   
                                                    try: 
                                                        si =  yy['City']['MaxInt']
                                                        print("\n ")
                                                        print(f"{kk['Name']}")
                                    
                                                        print(f"震度{yy['City']['MaxInt']}:",end='')
                                                        print(yy['City']['Name'] ,end=',')
                                                        si =  yy['City']['MaxInt']
                                                        ti = yy['City']['Name']
                                                        tis.append(kk['Name'])
                                                        sa.append (yy['City']['Name'])
                                                        break
                                                        


                                                    except:            
                                                        try : 
                            
                                                            if si == kk['Area'][ss]['City']['MaxInt']:
                                                                print(yy[ss]['City']['Name'] ,end=',')
                                                            else:                                        
                                                                print(f"震度{yy[ss]['City']['MaxInt']}:",end='')
                                                                print(yy[ss]['City']['Name'] ,end='')
                                                            
                                                    
                                                            si =  yy[ss]['City']['MaxInt']
                                                            ti =  yy[ss]['City']['Name']
                                                            tis.append(kk['Name'])
                                                            sa.append (yy[ss]['City']['Name'])
                                            
                                                        except:
                                                            try:
                                                                if si ==  kk['Area']['City']['MaxInt']:

                                                                    print(f"震度{yy['City']['MaxInt']}:",end='')
                                                                    print(yy['Name'] ,end=',')
                                                            
                                                                else:
                                                                    print(yy['City']['Name'] ,end='')

                                                                si =  kk['City']['MaxInt']
                                                                ti = yy['City']['Name']
                                                                tis.append(kk['Name'])
                                                                sa.append (yy['City']['Name'])
                                                                break
                                                            
                                                            except:
                                                                try:
                                                                    if si ==  kk['Area'][ss]['City']['MaxInt']:

                                                                        print(f"震度{yy['City'][ss]['MaxInt']}:",end='')
                                                                        print(yy['Name'] ,end=',')
                                                                
                                                                    else:
                                                                        print(yy['City']['Name'] ,end='')

                                                                    si =  kk['Area'][ss]['City']['MaxInt']
                                                                    ti = yy['City'][ss]['Name']
                                                                    tis.append(kk['Name'])
                                                                    sa.append (yy['City'][ss]['Name'])
                                                                    break
                                                                except:
                                                                    try:
                                                                        for sss ,slss in enumerate(kk['Area'][ss]['City']):
                                                                            if si ==  kk['Area'][ss]['City'][sss]['MaxInt']:

                                                                                
                                                                                print(yy['City'][sss]['Name'] ,end=',')
                                                                        
                                                                            else:
                                                                                print(f"震度{yy['City'][sss]['MaxInt']}:",end='')
                                                                                print(yy['City'][sss]['Name'] ,end='')

                                                                            si =  kk['Area'][ss]['City'][sss]['MaxInt']
                                                                            ti = yy['City'][sss]['Name']
                                                                            tis.append(kk['Name'])
                                                            
                                                                    except:
                                                                        break
                                            
                                else:
                                    break
                        except:

                            if ti == kk['Name']:   


                                try:    
                                    if si == yy['City']['MaxInt']:
                                        if yy['City']['Name']   in sa:
                                            break

                                        else:
                                            print(f",{yy['City']['Name']}", end='')
                                            sa.append (yy['City']['Name'])
                                            break
                                            
                                    else:
                                        si =  yy['City']['MaxInt']
                                        print("  ")
                                        print(f"震度{yy['City']['MaxInt']}:" ,end='' )
                                        print(yy['City']['Name'], end='')
                                        break   
                                except:
                                    for ok ,sl in enumerate(yy):
                                        for oks ,sl in enumerate(yy[ok]['City']):
                                            try:
                                                if si == yy[ok]['City'][oks]['MaxInt']:
                                                    tan = yy[ok]['City'][oks]
                                                    if tan['Name']   in sa:
                                                        break

                                                    else:
                                                        print(f",{tan['Name']}", end='')
                                                        sa.append (tan['Name'])
                                                        break
                                                        
                                                else:
                                                    si =  yy[ok]['City'][oks]['MaxInt']
                                                    print("  ")
                                                    print(f"震度{yy[ok]['City'][oks]['MaxInt']}:" ,end='' )
                                                    print(yy[ok]['City'][oks]['Name'], end='')
                                                    break   
                                            except:
                                                if si == yy[ok]['City']['MaxInt']:
                                                    tan = yy[ok]['City']
                                                    if tan['Name']   in sa:
                                                        break

                                                    else:
                                                        print(f",{tan['Name']}", end='')
                                                        sa.append (tan['Name'])
                                                        break
                                                        
                                                else:
                                                    si =  yy[ok]['City']['MaxInt']
                                                    print("  ")
                                                    print(f"震度{yy[ok]['City']['MaxInt']}:" ,end='' )
                                                    print(yy[ok]['City']['Name'], end=',')
                                                    break   


                            else:
                                if kk['Name'] not  in  tis:

                                
                                    try:
                                        print("\n ")
                                        print(f"{kk['Name']}")

                                        print(f"震度{yy['City'][0]['MaxInt']}:",end='')
                                        print(yy['City'][0]['Name'], end=',')
                                        si =  kk['MaxInt']
                                        ti = kk['Name']
                                        tis.append(kk['Name'])
                                        sa.append(yy['City'][0]['Name'])
                                        break
                                    except:
                                        try:
                                            
                                            print(f"震度{yy['City']['MaxInt']}:",end='')
                                            print(yy['City']['Name'], end=',')
                                            si =  kk['MaxInt']
                                            ti = kk['Name']
                                            tis.append(kk['Name'])
                                            sa.append (yy['City']['Name'])
                                            break
                                        except:
                                            try:
                                                for kai ,sl in enumerate(yy):
                                                    print(f"震度{yy[kai]['City']['MaxInt']}:",end='')
                                                    print(yy[kai]['City']['Name'], end=',')
                                                    si =  kk[sd]['MaxInt']
                                                    ti = kk[sd]['Name']
                                                    tis.append(kk[sd]['Name'])
                                                    sa.append (yy[kai]['City']['Name'])
                                                    break
                                            except:
                                                for kai ,sl in enumerate(yy):
                                                    try:
                                                        for kais ,sl in enumerate(yy[kai]['City']):
                                                            
                                                            if si == yy[kai]['City'][kais]['MaxInt']:                                                                       
                                                                print(yy[kai]['City'][kais]['Name'], end=',')
                                                                si =  yy[kai]['City'][kais]['MaxInt']
                                                                ti = kk['Name']
                                                                tis.append(kk['Name'])
                                                                sa.append (yy[kai]['City'][kais]['Name'])
                                                                break
                                                            else:
                                                                print(f"震度{yy[kai]['City'][kais]['MaxInt']}:",end='')               
                                                                print(yy[kai]['City'][kais]['Name'], end=',')
                                                                si =  yy[kai]['City'][kais]['MaxInt']
                                                                ti = kk['Name']
                                                                tis.append(kk['Name'])
                                                                sa.append (yy[kai]['City'][kais]['Name'])
                                                                break
                                                    except:
                                                        try:

                                                            for kais ,sl in enumerate(yy[kai]['City']):
                                                                
                                                                if si == yy[kai]['City'][kais]['MaxInt']:                                                                       
                                                                    print(yy[kai]['City'][kais]['Name'], end=',')
                                                                    si =  yy[kai]['City'][kais]['MaxInt']
                                                                    ti = kk['Name']
                                                                    tis.append(kk['Name'])
                                                                    sa.append (yy[kai]['City'][kais]['Name'])
                                                                    break
                                                                else:
                                                                    print(f"震度{yy[kai]['City'][kais]['MaxInt']}:",end='')               
                                                                    print(yy[kai]['City'][kais]['Name'], end=',')
                                                                    si =  yy[kai]['City'][kais]['MaxInt']
                                                                    ti = kk['Name']
                                                                    tis.append(kk['Name'])
                                                                    sa.append (yy[kai]['City'][kais]['Name'])
                                                                    break
                                                        except:
                                                            try:
                                                                if si == yy[kai]['City']['MaxInt']:                                                                       
                                                                    print(yy[kai]['City']['Name'], end=',')
                                                                    si =  yy[kai]['City']['MaxInt']
                                                                    ti = kk['Name']
                                                                    tis.append(kk['Name'])
                                                                    sa.append (yy[kai]['City']['Name'])
                                                                    break
                                                                else:
                                                                    print(f"震度{yy[kai]['City']['MaxInt']}:",end='')               
                                                                    print(yy[kai]['City']['Name'], end=',')
                                                                    si =  yy[kai]['City']['MaxInt']
                                                                    ti = kk['Name']
                                                                    tis.append(kk['Name'])
                                                                    break
                                                            except:
                                                                sa.append (yy['City']['Name'])
                                                                if si == yy['City']['MaxInt']:                                                                       
                                                                    print(yy['City']['Name'], end=',')
                                                                    si =  yy['City']['MaxInt']
                                                                    ti = kk['Name']
                                                                    tis.append(kk['Name'])
                                                                    sa.append (yy['City']['Name'])
                                                                    break
                                                                else:
                                                                    if yy['City']['Name'] not in sa:

                                                                        print(f"震度{yy['City']['MaxInt']}:",end='')               
                                                                        print(yy['City']['Name'], end=',')
                                                                        si =  yy['City']['MaxInt']
                                                                        ti = kk['Name']
                                                                        tis.append(kk['Name'])
                                                                        sa.append (yy['City']['Name'])    
                                                                        break 
                                                                    else:
                                                                        si =  yy['City']['MaxInt']
                                                                        ti = kk['Name']
                                                                        tis.append(kk['Name'])
                                                                        sa.append (yy['City']['Name'])  
                                                                        break                                               



                                                        


                                                        
                                else:                            
                                    for ss ,sls in enumerate(kk):
                            
                                        try:
                                            si =  yy['City']['MaxInt']
                                            print(f"震度{yy['City']['MaxInt']}:",end='')
                                            print(yy['City']['Name'], end=',')
                                            
                                            ti = yy['City']['Name']
                                            tis.append(kk['Name'])
                                            break
                                        
                                            
                                        except:   
                                            try: 
                                                si =  yy['City']['MaxInt']
                                                print("\n ")
                                                print(f"{kk['Name']}")
                            
                                                print(f"震度{yy['City']['MaxInt']}:",end='')
                                                print(yy['City']['Name'] ,end=',')
                                                si =  yy['City']['MaxInt']
                                                ti = yy['City']['Name']
                                                tis.append(kk['Name'])
                                                sa.append (yy['City']['Name'])
                                                break
                                                


                                            except:            
                                                try : 
                        
                                                    if si == kk['Area'][ss]['City']['MaxInt']:
                                                        print(yy[ss]['City']['Name'] ,end=',')
                                                    else:                                        
                                                        print(f"震度{yy[ss]['City']['MaxInt']}:",end='')
                                                        print(yy[ss]['City']['Name'] ,end=',')
                                                    
                                            
                                                    si =  yy[ss]['City']['MaxInt']
                                                    ti =  yy[ss]['City']['Name']
                                                    tis.append(kk['Name'])
                                                    sa.append (yy[ss]['City']['Name'])
                                        
                                                except:
                                                    try:
                                                        if si ==  kk['Area']['City']['MaxInt']:

                                                            print(f"震度{yy['City']['MaxInt']}:",end='')
                                                            print(yy['Name'] ,end=',')
                                                    
                                                        else:
                                                            print(yy['City']['Name'] ,end='')

                                                        si =  kk['City']['MaxInt']
                                                        ti = yy['City']['Name']
                                                        tis.append(kk['Name'])
                                                        sa.append (yy['City']['Name'])
                                                        break
                                                        
                                                    except:
                                                        try:
                                                            if si ==  kk['Area'][ss]['City']['MaxInt']:

                                                                print(f"震度{yy['City'][ss]['MaxInt']}:",end='')
                                                                print(yy['Name'] ,end=',')
                                                        
                                                            else:
                                                                print(yy['City']['Name'] ,end='')

                                                            si =  kk['Area'][ss]['City']['MaxInt']
                                                            ti = yy['City'][ss]['Name']
                                                            tis.append(kk['Name'])
                                                            sa.append (yy['City'][ss]['Name'])
                                                            break
                                                        except:
                                                            try:
                                                                for sss ,slss in enumerate(kk['Area'][ss]['City']):
                                                                    if si ==  kk['Area'][ss]['City'][sss]['MaxInt']:

                                                                        
                                                                        print(yy['City'][sss]['Name'] ,end=',')
                                                                
                                                                    else:
                                                                        print(f"震度{yy['City'][sss]['MaxInt']}:",end='')
                                                                        print(yy['City'][sss]['Name'] ,end='')

                                                                    si =  kk['Area'][ss]['City'][sss]['MaxInt']
                                                                    ti = yy['City'][sss]['Name']
                                                                    tis.append(kk['Name'])
                                                    
                                                            except:
                                                                break
                except:
                    break
from urllib.request import urlopen
import xmltodict

import colorama
from termcolor import colored
colorama.init()

def keihou(url):
    instance = urlopen(url)
    show_xml_output = instance
    details_root = xmltodict.parse(show_xml_output)
    xml =  details_root['Report']['Body']['Warning'][3]
    hyo = details_root['Report']['Control']
    print ("--------------------------------------------------------------------------------------")

    print(f"{hyo['Title']}  {hyo['EditorialOffice']} {hyo['Status']}")
    print(f"{details_root['Report']['Head']['Title']}  {details_root['Report']['Head']['InfoType']}")

    for i, nai in enumerate(xml['Item']):   
        print(" ")     
        print(f"{xml['Item'][i]['Area']['Name']} ")

        for s, nai1 in  enumerate(xml['Item'][i]['Kind']):    
            try:   
                if ' 特別警報' in xml['Item'][i]['Kind'][s]['Name']:
                    print(colored(f"{xml['Item'][i]['Kind'][s]['Name']} ({xml['Item'][i]['Kind'][s]['Status']})","magenta"))
                elif '警報' in xml['Item'][i]['Kind'][s]['Name']:
                    print(colored(f"{xml['Item'][i]['Kind'][s]['Name']} ({xml['Item'][i]['Kind'][s]['Status']})","red"))
                else:
                    print(f"{xml['Item'][i]['Kind'][s]['Name']} ({xml['Item'][i]['Kind'][s]['Status']})")
            except:

                print("警報・注意報等発表なし")
                break
        else:
            print(xml['Item'][i]['ChangeStatus']) 
            print(" ")

    print(f"発表時間: {details_root['Report']['Head']['ReportDateTime']}") 

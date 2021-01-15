

from urllib.request import urlopen





    # instanceからHTMLを取り出して、BeautifulSoupで扱えるようにパースします
import xmltodict



text = {}

nai = {}
si = 0
ti = 0
ss ={}
yy ={}
sa = []
tis = []


def sokuhou(url):
    instance = urlopen(url)
    show_xml_output = instance    
    details_root = xmltodict.parse(show_xml_output )
    print(f"{details_root['Report']['Control']['Title']} {details_root['Report']['Control']['EditorialOffice']} {details_root['Report']['Control']['Status']}")
    print(f"{details_root['Report']['Head']['Headline']['Text']}")

    yy  = details_root['Report']['Head']['Headline']['Information']['Item']
    for sls in yy:
        print(" ")
        print(sls['Kind']['Name'])
        for sl in sls['Areas']['Area']:
            print(sl['Name'], end=',')
    
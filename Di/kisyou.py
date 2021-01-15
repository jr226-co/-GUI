from urllib.request import urlopen
import xmltodict

           
def zyou(url):
    instance = urlopen(url)
    show_xml_output = instance

    details_root = xmltodict.parse(show_xml_output)
    print ("--------------------------------------------------------------------------------------")
    print(f"{details_root['Report']['Control']['Title']} {details_root['Report']['Control']['EditorialOffice']} ({details_root['Report']['Control']['Status']})")
    print(f"{details_root['Report']['Head']['Title']} ({details_root['Report']['Head']['InfoType']})")
    print(details_root['Report']['Body']['Comment']['Text']['#text'])
    print(f"発表時間 {details_root['Report']['Head']['ReportDateTime']}")



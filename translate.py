import requests
from bs4 import BeautifulSoup as bs
from lxml import etree

def sorgula(kelime):
    re = requests.get(f"https://www.zargan.com/tr/q/{kelime}-ceviri-nedir")
    ar= bs(re.content,"html.parser")
    dom = etree.HTML(str(ar))

    el = dom.xpath("/html/body/div[1]/section/div[3]/div[3]/div/div[1]/div[2]/div[1]/ol/li[1]/text()")
    el2 =dom.xpath("/html/body/div[1]/section/div[3]/div[3]/div/div[1]/div[2]/div[1]/ol/li[2]/text()")
    anlam =""
    anlam2 = ""
    if len(el):
        anlam =  (el[1].split("\n"))[0]
    if len(el2):
       anlam2 =  (el2[1].split("\n"))[0]
    ret= anlam+ "," +anlam2
    return ret

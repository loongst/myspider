import requests
import re
from bs4 import BeautifulSoup
import bs4

def getHtml(url):
    try:
        r = requests.get(url,timeout=30)
        r.raise_for_status
        r.encoding=r.apparent_encoding
        return r.text
    except:
        print(IndentationError)
        return ""
    
    
def getUlist(ulist,demo):
    
    soup = BeautifulSoup(demo,"html.parser")
    for tr in soup.find('tbody').children:
        if isinstance(tr,bs4.element.Tag):
            tds=tr("td")
            ulist.append([tds[0].string,tds[1].string,tds[3].string])

def printUlist(ulist,num):
    print("{0:^10}\t{1:{3}^16}\t{2:^10}".format("排名","学校","分数",chr(12288)))

    for i in range(num):
        ui=ulist[i]
        print("{0:^10}\t{1:{3}^16}\t{2:^10}".format(ui[0],ui[1],ui[2],chr(12288)))


def main():
    uinfo=[]
    url="http://www.zuihaodaxue.com/Greater_China_Ranking2019_0.html"
    html=getHtml(url)
    getUlist(uinfo,html)
    printUlist(uinfo,20)

main()



0-99 [1-9]?\d
100-199  1\d{2}
200-249  2[0-4]\d 
250-255 25[0-5]
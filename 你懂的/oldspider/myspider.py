import os
import requests
from urllib.parse import urlencode,quote,unquote

class Myspider:

    def __init__(self,url):
        self.url=unquote(url)
        self.filename=os.path.basename(self.url)
        self.filepath=url.split('/')[-2]
        self.headers={"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.106 Safari/537.36","Host":"www.loongxu.com"}

    def downfile(self):
        
        if not os.path.exists(self.filepath):
            
            os.makedirs(self.filepath)
            os.chdir(self.filepath)
            print("文件下载目录为："+self.filepath)
        
        if os.path.exists(self.filepath+self.filename):

            r = requests.get(self.url,headers=self.headers)

            with open(self.filename,"wb+") as f:
                f.write(r.content)

            if self.filename:
                print("文件下载成功！")

        else:
            print("文件已存在，停止下载！")

class tbspider:
    def __init__(self,url):
        self.url=url
        pass

    def getHtmltext(self,url):
        pass

    def parsePage(self,ilt,html):
        pass

    def printGoodslist(self,ilt):
        pass

    def main():
        wd=""
        url="http://www.chaojida.net/index.php/vod/search.html?wd=%E6%8A%A4%E5%A3%AB"



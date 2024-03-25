from selenium import webdriver
import time
import re
import pymysql
import random
import os
import subprocess
import signal
from bs4 import BeautifulSoup

# 需要在windows中，因为反爬需要
# 需要设置chrome的路径
# 需要设置数据库的配置
# 默认爬取最新200条数据，数据库中相关数据则直接修改


class spiderCNVD():

    def init(self):
        # 不要更改
        self.pageSize = 100
        self.pageType = [27, 28, 29, 30, 31, 32, 33, 34, 35, 38]
        # self.pageType = [27,28]
        # 最大页
        self.maxPage = 2
        self.isStop = False
        self.db = pymysql.connect(user='root', password='root',
                                  host='localhost', database='vulndb')

        # 需要在本机上使用一下命令，反防爬用
        # .\chrome.exe --remote-debugging-port=9222 --headless
        self.stf_p = subprocess.Popen(["C:\Program Files\Google\Chrome\Application\chrome.exe",
                                      '--remote-debugging-port=9232', '--force-headless-for-tests'])

        opts = webdriver.ChromeOptions()
        # opts.add_argument("--headless")
        opts.add_argument("--disable-dev-shm-usage")
        opts.add_argument("--no-sandobx")
        opts.add_argument("--window-size=100,100")
        opts.add_argument("--disable-blink-features=AutomationControlled")
        # opts.binary_location = r"C:\Program Files\Google\Chrome\Application\chrome.exe"
        opts.add_experimental_option("debuggerAddress", "127.0.0.1:9232")
        self.driver = webdriver.Chrome(options=opts)

        self.driver.get("https://www.cnvd.org.cn/flaw/typeResult?typeId=29")

        # time.sleep(2)
        self.start()

    def start(self):
        # 循环获取每个栏目的数据
        for i in self.pageType:
            self.getPageHtml(i)
        # 结束
        os.system('taskkill /f /pid %s' % self.stf_p.pid)  # win kill
        os.kill(self.stf_p.pid, signal.CTRL_C_EVENT)  # linux kill

    def getPageHtml(self, type):
        self.isStop = False
        for i in range(0, self.maxPage):

            self.driver.get(
                "https://www.cnvd.org.cn/flaw/typeResult?typeId=%d&max=100&offset=%d" % (type, self.pageSize*i))
            if self.isStop == True:
                break
            datalist = self.parseHtml(self.driver.page_source, type)
            if len(datalist) != 0:
                self.save(datalist)
            if self.isStop == True:
                break

            t = random.randint(1, 6)  # 取随机数
            print("等待%d秒" % t)
            time.sleep(t)  # 休眠t秒

    def parseHtml(self, html, type):
        datlist = []  # 存一页漏洞基本信息
        # 指定Beautiful的解析器为“html.parser”
        soup = BeautifulSoup(html, "html.parser")
        findLevel = re.compile(r'</span>(.*?)</td>', re.S)  # 危害级别匹配规则
        findDate = re.compile(r'<td width="13%">(.*?)</td>', re.S)  # 时间匹配规则
        k = 1
        items = soup.find_all('tr')
        if type == 27:
            type = "操作系统"
        elif type == 28:
            type = "应用程序"
        elif type == 29:
            type = "WEB应用"
        elif type == 30:
            type = "数据库"
        elif type == 31:
            type = "网络设备（交换机，路由器等网络终端设备）"
        elif type == 32:
            type = "安全产品"
        elif type == 33:
            type = "智能设备（物联网终端设备）"
        elif type == 34:
            type = "区块链公链"
        elif type == 35:
            type = "区块链联盟链"
        elif type == 38:
            type = "工业控制系统"
        while k < len(items):
            dat = []  # 存一个漏洞基本信息
            item = items[k]
            link = "https://www.cnvd.org.cn"+item.a["href"]  # 获取漏洞详细信息链接
            # print(link)
            title = item.a["title"]  # 获取漏洞标题
            # print(title)
            item = str(item)  # 转换为字符串
            level = re.findall(findLevel, item)[0]
            # print(level)
            date = re.findall(findDate, item)[0]
            # print(date)
            # print("___________________________")
            dat.append(title)
            dat.append(level)
            dat.append(date)
            dat.append(link)
            dat.append(type)
            datlist.append(dat)
            # print(dat)
            k += 1
        return datlist

    def save(self, datlist):
        # print(datlist[1])

        cursor = self.db.cursor()
        for dat in datlist:
            
            # print(sql)
            if not self.checkHaveOne(dat[3]):
                data = "'"+dat[0]+"'"+","+"'"+dat[1].replace(" ", "").replace("\n", "").replace(
                "\t", "")+"'"+","+"'"+dat[2]+"'"+","+"'"+dat[3]+"'"+","+"'"+dat[4]+"'"

                sql = "insert into cnvd (title,level,date,link,type) values(%s)" % data
                
            else:
                # 已存在 则蹦出循环
                # print(dat[0])
                # print("已存在 跳出循环")
                # self.isStop = True
                # break
                # 直接覆盖相关数据
                sql = "update cnvd set title='%s',level='%s',date='%s',type='%s' where link='%s'"%(dat[0],dat[1],dat[2],dat[4],dat[3])
                
            cursor.execute(sql)  # 提交数据库操作
            self.db.commit()  # 提交事务
            print(dat[0]+'已更新')
        cursor.close()

    def checkHaveOne(self, link):

        cursor = self.db.cursor()
        sql = "select * from cnvd where link='%s'" % (link)
        cursor.execute(sql)
        res = cursor.fetchone()  # 提交数据库操作
        if res is not None:
            return True
        return False
    
    

    def stop(self):
        exit("数据库已存在相关数据")


if __name__ == "__main__":
    try:
        spider = spiderCNVD()
        spider.init()
    except KeyboardInterrupt:
        pass
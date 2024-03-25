import requests
import datetime
from bs4 import BeautifulSoup
from selenium import webdriver
import re
import time
import html
import random
import pymysql

# 需要设置数据库配置
# 默认爬取最近两个月的数据
# 如果update_date和数据库中的数据不匹配，则更新数据库的信息


class spiderCVE():
    def init(self):
        # 获取当月和上个月的漏洞 ，如果数据库有数据，则停止
        # month = ['January', 'February', 'March', 'April', 'May', 'June',
        #          'July', 'August', 'September', 'October', 'November', 'December']
        today = datetime.datetime.today()
        day = today.day
        year = today.year
        month = today.month
        pagenow = 1

        # 正则
        self.r_list = {
            'id': re.compile(r'<a.*?nerability details\">(.*?)<\/a>'),
            'href': re.compile(r'<a.*?href=\"(.*?)\"'),
            'score': re.compile(r'<div.*?>(.*?)<\/div>'),
            'td': re.compile(r'<td.*?>\s*(.*?)\s*<\/td>'),
        }
        self.db = pymysql.connect(user='root', password='root',
                                  host='localhost', database='vulndb')

        # 获取当前月的所有漏洞
        self.host = "https://www.cvedetails.com/"
        self.urls = []

        self.urls.append(
            "https://www.cvedetails.com/vulnerability-list.php?page=%s&year=%s&month=%s" % (pagenow, year, month))
        # 上个月
        year2, month2 = self.getLastMonth(year, month)
        self.urls.append(
            "https://www.cvedetails.com/vulnerability-list.php?page=%s&year=%s&month=%s" % (pagenow, year2, month2))
        self.start()
        print('爬完了')

    def getLastMonth(self, year, month):
        if month == 1:
            lyear = year - 1
            lmonth = 12
        else:
            lyear = year
            lmonth = month - 1
        return lyear, lmonth

    def getDetail(self, soup):
        # 简介
        cve_summary = soup.select("td .cvesummarylong")
        summary = []
        for i in cve_summary:
            summary.append(re.findall(self.r_list['td'], str(i))[0])
        # cve 属性
        cve_detail = soup.select("tr .srrowns")
        cve_list = []
        x = 0
        for i in cve_detail:
            cve = {}
            cve['id'] = re.findall(self.r_list['id'], str(i.contents))[0]
            cve['href'] = re.findall(self.r_list['href'], str(i.contents))[0]
            if len(re.findall(self.r_list['td'], str(i.contents[9]))) != 0:
                cve['type'] = re.findall(
                    self.r_list['td'], str(i.contents[9]))[0]
            if len(re.findall(self.r_list['td'], str(i.contents[11]))) != 0:
                cve['publish_date'] = re.findall(
                    self.r_list['td'], str(i.contents[11]))[0]
            if len(re.findall(self.r_list['td'], str(i.contents[13]))) != 0:
                cve['update_date'] = re.findall(
                    self.r_list['td'], str(i.contents[13]))[0]
            if len(re.findall(self.r_list['score'], str(i.contents[15]))) != 0:
                cve['score'] = re.findall(
                    self.r_list['score'], str(i.contents[15]))[0]
            if len(re.findall(self.r_list['td'], str(i.contents[17]))) != 0:
                cve['gal'] = re.findall(
                    self.r_list['td'], str(i.contents[17]))[0]
            if len(re.findall(self.r_list['td'], str(i.contents[19]))) != 0:
                cve['access'] = re.findall(
                    self.r_list['td'], str(i.contents[19]))[0]
            if len(re.findall(self.r_list['td'], str(i.contents[21]))) != 0:
                cve['complexity'] = re.findall(
                    self.r_list['td'], str(i.contents[21]))[0]
            if len(re.findall(self.r_list['td'], str(i.contents[23]))) != 0:
                cve['auth'] = re.findall(
                    self.r_list['td'], str(i.contents[23]))[0]
            if len(re.findall(self.r_list['td'], str(i.contents[25]))) != 0:
                cve['conf'] = re.findall(
                    self.r_list['td'], str(i.contents[25]))[0]
            if len(re.findall(self.r_list['td'], str(i.contents[27]))) != 0:
                cve['integ'] = re.findall(
                    self.r_list['td'], str(i.contents[27]))[0]
            if len(re.findall(self.r_list['td'], str(i.contents[29]))) != 0:
                cve['avail'] = re.findall(
                    self.r_list['td'], str(i.contents[29]))[0]
            cve['summary'] = summary[x]
            cve_list.append(cve)
            x = x+1

        return cve_list

    def save(self, cve_all):

        cursor = self.db.cursor()
        for cve in cve_all:
            updateid = self.checkUpdate(cve['id'], cve['update_date'])
            if updateid != 0 and updateid != -1:
                sql = "update cve set type='%s',href='%s',update_date='%s',score='%s',gal='%s',access='%s',complexity='%s',auth='%s',conf='%s',integ='%s',avail='%s',summary='%s' where id=%s" % (
                    cve['type'], cve['href'], cve['update_date'], cve['score'], cve['gal'], cve['access'], cve['complexity'], cve['auth'], cve['conf'], cve['integ'], cve['avail'], html.escape(cve['summary']), updateid)
                print(cve['id']+'已更新')
                # sql = "update cve(cve_id,type,publish_date,update_date,score,gal,access,complexity,auth,conf,integ,avail,summary)set('%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s')" % (cve['id'],cve['type'],cve['publish_date'],cve['update_date'],cve['score'],cve['gal'],cve['access'],cve['complexity'],cve['auth'],cve['conf'],cve['integ'],cve['avail'],html.escape(cve['summary']))
            if updateid == 0:
                sql = "insert into cve(cve_id,href,type,publish_date,update_date,score,gal,access,complexity,auth,conf,integ,avail,summary)values('%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s')" % (
                    cve['id'], cve['href'], cve['type'], cve['publish_date'], cve['update_date'], cve['score'], cve['gal'], cve['access'], cve['complexity'], cve['auth'], cve['conf'], cve['integ'], cve['avail'], html.escape(cve['summary']))
                print(cve['id']+'已入库')
            if updateid == -1:
                print(cve['id']+'已跳过')
                pass
            else:
                cursor.execute(sql)  # 提交数据库操作
                self.db.commit()

    def checkUpdate(self, cve_id, update_date):
        # self.db = pymysql.connect(user='root', password='root',
        #                           host='localhost', database='vulndb')
        cursor = self.db.cursor()
        sql = "select cve_id,update_date,id from cve where cve_id='%s'" % (
            cve_id)
        cursor.execute(sql)
        res = cursor.fetchone()  # 提交数据库操作
        # 数据库不存在
        if res is None:
            return 0
        # 数据库是旧数据，需要更新
        # print(res[1],update_date)
        if res[1] < update_date:
            return res[2]
        # 数据库不需要更新
        return -1

    def start(self):
        for url in self.urls:
            res = requests.get(url)
            # 指定Beautiful的解析器为“html.parser”
            soup = BeautifulSoup(res.text, "html.parser")
            # 获取所有分页的连接，进而获取数据
            pagebar = soup.find(id="pagingb").findAll("a")
            cve_all = []
            # cve_all.append(self.getDetail(soup))
            for i in pagebar:
                # all_list_url.append(self.host+i.attrs['href'])
                try:
                    page_res = requests.get(self.host+i.attrs['href'])
                    # 指定Beautiful的解析器为“html.parser”
                    soup = BeautifulSoup(page_res.text, "html.parser")
                    # 获取所有分页的连接，进而获取数据
                    # cve_all.append()
                    self.save(self.getDetail(soup))
                    print('已爬完'+i.attrs['href'])
                except Exception as e:
                    print(e)
                    # 后边可以记录失败的URL，进行补爬
                    print(i.attrs['href']+"出问题了，跳过继续")
                    break
                t = random.randint(1, 6)  # 取随机数
                print("等待%d秒" % t)
                time.sleep(t)

        self.db.close()


if __name__ == "__main__":
    try:
        spider = spiderCVE()
        spider.init()
    except KeyboardInterrupt:
        exit()

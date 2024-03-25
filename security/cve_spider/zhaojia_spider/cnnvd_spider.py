import requests
import pymysql
import json
import time,random

# 默认采集最新的10*50个超危，10*50个高危
# hazardLevel 为危险级别
# pageMaxIndex 爬取的最大页数
# 爬取比对updateTime，不匹配则更新

class spiderCNNVD():
    def init(self):
        # 初始化
        self.db = pymysql.connect(user='root', password='root',
                                  host='localhost', database='vulndb')

        self.start()

    def start(self):
        headers = {
            "Content-Type": "application/json; charset=UTF-8",
            "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.87 Safari/537.36",
            "Origin": "https://www.cnnvd.org.cn",
            "Referer": "https://www.cnnvd.org.cn/home/loophole"
        }
        url = 'https://www.cnnvd.org.cn/web/homePage/cnnvdVulList'



        hazardLevel = [1,2]  # 1超危 2高危 3中危
        pageIndex = 1
        pageMaxIndex = 10 # 只爬取前多少页
        pageSize = 50 # 最多只能50个 写死

        # data = '{"pageIndex":%d,"pageSize":%d,"keyword":"","hazardLevel":%d,"vulType":"","vendor":"","product":"","dateType":""}'
        for i in hazardLevel:
            for j in range(1,pageMaxIndex+1):
                data = {
                    'pageIndex':j,
                    'pageSize':pageSize,
                    'hazardLevel':i
                }

                res = requests.post(url=url, data=str(data),headers=headers)
                print("%s-%d页已获取数据"%(i,j))
                # 获得数据
                # print(res.status_code)
                if res.status_code == 200:
                    self.save(res.text)
                    t = random.randint(1, 6)  # 取随机数
                    print("等待%d秒" % t)
                    time.sleep(t)

    def save(self,data):
        data_dict = json.loads(data)
        cursor = self.db.cursor()
        if data_dict['data']['total'] > 0 :
            records = data_dict['data']['records']
            
            for i in records:
                updateid = self.checkUpdate(i['cnnvdCode'],i['updateTime'])
                if updateid != 0 and updateid != -1:
                    sql = 'update cnnvd set hazardLevel="%s",updateTime="%s",typeName="%s",vulType="%s"'%(i['hazardLevel'],i['updateTime'],i['typeName'],i['vulType'])
                    print(i['cnnvdCode']+'已更新')
                if self.checkUpdate(i['cnnvdCode'],i['updateTime']) == 0:
                    sql = 'insert into cnnvd(source_id,vulName,cnnvdCode,cveCode,hazardLevel,createTime,publishTime,updateTime,typeName,vulType)values("%s","%s","%s","%s","%s","%s","%s","%s","%s","%s")'%(i['id'],i['vulName'],i['cnnvdCode'],i['cveCode'],i['hazardLevel'],i['createTime'],i['publishTime'],i['updateTime'],i['typeName'],i['vulType'])
                    print(i['cnnvdCode']+'已入库')
                if updateid == -1:
                    pass
                    # print(i['cnnvdCode']+'已跳过')
                else:
                    cursor.execute(sql)  # 提交数据库操作
                    self.db.commit()
    def checkUpdate(self, cnnvdCode, updateTime):
        # self.db = pymysql.connect(user='root', password='root',
        #                           host='localhost', database='vulndb')
        cursor = self.db.cursor()
        sql = "select cnnvdCode,updateTime,id from cnnvd where cnnvdCode='%s'" % (
            cnnvdCode)
        cursor.execute(sql)
        res = cursor.fetchone()  # 提交数据库操作
        # 数据库不存在
        if res is None:
            return 0
        # 数据库是旧数据，需要更新
        # print(res[1],update_date)
        if res[1] < updateTime:
            return res[2]
        # 数据库不需要更新
        return -1

if __name__ == '__main__':
    try:
        spider = spiderCNNVD()
        spider.init()
    except KeyboardInterrupt:
        exit()

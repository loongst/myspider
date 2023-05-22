import scrapy
import json
import csv

from scrapy.http import JsonRequest
class Glu2uSpider(scrapy.Spider):
    name = "glu2u"
    allowed_domains = ["cgm.glu2u.com"]
    start_urls = ["https://cgm.glu2u.com/prod-api/system/user/list/patient?pageNum=1&pageSize=800&wearingStatus=&userType=10"]


    # def start_requests(self):
        
    #     return super().start_requests()

    def parse(self, response):
        with open("data.json","a+") as f:
            f.write(response.text)
        print(response.text)
        datas=json.loads(response.text)
        headers={"Content-Type":"application/json;charset=UTF-8"}
        data=datas['rows']
        for i in data:
            personinfo={}
            personinfo['userId']=i['userId']
            personinfo['patientId']=i['patientId']
            personinfo['phonenumber']=i['phonenumber']
            personinfo['nickName']=i['nickName']

            formdata={"page":1,"pageSize":200,"startTime":"2021-01-01 14:16:15","endTime":"2023-05-19 09:13:01","patientId":i['patientId']}
            geturl="https://cgm.glu2u.com/prod-api/bloodsugar/api/v1/patientbloodofflinedatedata/get-patientbloodofflinedatedata-list"

            yield JsonRequest(url=geturl,data=formdata,headers=headers, callback=self.getinfo,meta={'personinfo': personinfo})

    def getinfo(self,response):
        with open("person.json","a+") as f:
            f.write(response.text)
        infos=json.loads(response.text)
        personinfo=response.meta.get('personinfo')
        infolist=[]
        records=infos['data']['records']
        for record in records:
            info={}
            # info['patientId']=record['patientId']
            info['time']=record['dataDate']
            info['xuetang']=record['bloodReferenceValue']
            infolist.append(info)
        personinfo['bloodinfo']=infolist
        print(personinfo)
        with open("result.json","+a") as f:
            f.write(json.dumps(personinfo, ensure_ascii=False)+',\n')




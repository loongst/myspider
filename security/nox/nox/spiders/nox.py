import scrapy
from scrapy.http import JsonRequest
import json
class NoxSpider(scrapy.Spider):
    name = "nox"
    allowed_domains = ["nox.qianxin.com"]
    start_urls = ["https://nox.qianxin.com/vulnerability"]

    def parse(self, response):
        api_url="https://nox.qianxin.com/api/web/portal/vuln_repo/list"
        headers={
        'Accept':'application/json, text/plain, */*',
        'Accept-Encoding':'gzip, deflate, br',
        'Accept-Language':'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
        'access-token':'da0d61ba189195d349d51214fff9008d',
        'Content-Type':'application/json; charset=UTF-8',
        'dark':'true',
        'key':':LXHGJYE72DNSR62KADVCIXVKGFWN5QEQ',
        'mid':'mid2',
        'Origin':'https://nox.qianxin.com',
        'Referer':'https://nox.qianxin.com/vulnerability',
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36 Edg/111.0.1661.44',
        }
        cookies={'wzws_sessionid':'oGQZWbCBOGZmZDQ4gmEzNWM3ZIAzNi4xMTAuMTkuMjM0','Hm_lvt_7f8f4477f0f0f86b081632c57ee072e5':'1679382962', 'Hm_lpvt_7f8f4477f0f0f86b081632c57ee072e5':'1679382962'}
        for i in range(3):
            data={"page_no":1+i,"page_size":10,"tag":"","vuln_keyword":""}
            datas=json.dumps(data)
            yield JsonRequest(url=api_url,data=data,headers=headers,callback=self.get_item)

    def get_item(self,response):
        print(response.text)
        content=json.loads(response.text).get('data').get('data')
        result={}
        for it in content:
            result['id']=it['id']
            result['vuln_name']=it['vuln_name']
            result['vuln_name_en']=it['vuln_name_en']
            result['qvd_code']=it['qvd_code']
            result['cve_code']=it['cve_code']
            result['cnvd_id']=it['cnvd_id']
            result['cnnvd_id']=it['cnnvd_id']
            result['threat_category']=it['threat_category']
            result['technical_category']=it['technical_category']
            result['residence_id']=it['residence_id']
            result['rating_id']=it['rating_id']
            result['not_show']=it['not_show']
            result['publish_time']=it['publish_time']
            result['description']=it['description']
            result['description_en']=it['description_en']
            result['change_impact']=it['change_impact']
            result['operator_hid']=it['operator_hid']
            result['create_hid']=it['create_hid']
            result['temp']=it['temp']
            result['other_rating']=it['other_rating']
            result['create_time']=it['create_time']
            result['update_time']=it['update_time']
            result['latest_update_time']=it['latest_update_time']
            result['rating_level']=it['rating_level']
            result['vuln_type']=it['vuln_type']
            result['poc_flag']=it['poc_flag']
            result['patch_flag']=it['patch_flag']
            result['detail_flag']=it['detail_flag']
            result['tag']=it['tag']
            result['tag_len']=it['tag_len']
            result['is_rating_level']=it['is_rating_level']

            yield result
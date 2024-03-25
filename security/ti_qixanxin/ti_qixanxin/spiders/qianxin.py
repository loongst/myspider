import scrapy
import json

class QianxinSpider(scrapy.Spider):
    name = "qianxin"
    allowed_domains = ["ti.qianxin.com"]
    start_urls = ["https://ti.qianxin.com/vulnerability"]

    def parse(self, response):
        api_url="https://ti.qianxin.com/alpha-api/v2/nox/api/web/portal/key_vuln/list"
        headers={
            # 'Accept':'application/json, text/plain, */*',
            # 'Accept-Encoding':'gzip, deflate, br',
            # 'Accept-Language':'zh-CN,zh;q=0.9',
            # 'Connection':'keep-alive',
            # 'Content-Length':'28',
            'Content-Type':'application/json',
            # 'Cookie':'UM_distinctid=1860c66e43d4e2-0f04964de7a229-26021051-384000-1860c66e43eef7; sesskey=836de8bc656f798c87dbc84be2a038c3; Hm_lvt_dd42562bd3e5b032660a309c39cd869d=1678346889,1679275382; Hm_lpvt_dd42562bd3e5b032660a309c39cd869d=1679275382; looyu_id=4d81ad104ffd3844d7128e0769643c58_20000755%3A5; Hm_lvt_d8264b8020f2466f0d32c74495e8f841=1677483880,1679276343; session=02d492c9-1297-47ba-b995-e6a8901e92b4; _99_mon=%5B0%2C0%2C0%5D; looyu_20000755=v%3A3c813f45a3820f1bfc080cae9c6a6814%2Cref%3Ahttps%253A//www.baidu.com/link%253Furl%253Di6hun5qkePsNz3KpC2V2TQYAsUiTun4TZF2KkkWMRB2_DWixh88hyj1K_BGx44S3LVtuvYUjMV3hM9xSsnd6J_%2526wd%253D%2526eqid%253Dcb9f576e00098e67000000036417b4e5%2Cr%3A%2Cmon%3A//m6816.talk99.cn/monitor%2Cp0%3Ahttps%253A//www.qianxin.com/news/detail%253Fnews_id%253D2781; Hm_lpvt_d8264b8020f2466f0d32c74495e8f841=1679276832',
            # 'Host':'ti.qianxin.com',
            # 'Origin':'https://ti.qianxin.com',
            # 'Referer':'https://ti.qianxin.com/vulnerability',
            # 'sec-ch-ua':'"Google Chrome";v="111", "Not(A:Brand";v="8", "Chromium";v="111"',
            # 'sec-ch-ua-mobile':'?0',
            # 'sec-ch-ua-platform':'"Windows"',
            # 'Sec-Fetch-Dest':'empty',
            # 'Sec-Fetch-Mode':'cors',
            # 'Sec-Fetch-Site':'same-origin',
            # 'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36',
        }
        
        for i in range(3):
            data={"page_no":str(i+1),"page_size":'10'}
            # yield scrapy.FormRequest(url=api_url,formdata=data,headers=headers,callback=self.get_item)
            yield scrapy.Request(url=api_url,method="POST",headers=headers,body=json.dumps(data),callback=self.get_item,dont_filter=True)

    def get_item(self,response):
        for it in json.loads(response.text)['data']['data']:
            id=it.get('id')
            vuln_name=it.get('vuln_name')
            vuln_name_en=it.get('vuln_name_en')
            qvd_code=it.get('qvd_code')
            cve_code=it.get('cve_code')
            cnvd_id=it.get('cnvd_id')
            cnnvd_id=it.get('cnnvd_id')
            threat_category=it.get('threat_category')
            technical_category=it.get('technical_category')
            residence_id=it.get('residence_id')
            rating_id=it.get('rating_id')
            not_show=it.get('not_show')
            publish_time=it.get('publish_time')
            description=it.get('description')
            description_en=it.get('description_en')
            change_impact=it.get('change_impact')
            operator_hid=it.get('operator_hid')
            create_hid=it.get('create_hid')
            temp=it.get('temp')
            other_rating=it.get('other_rating')
            create_time=it.get('create_time')
            update_time=it.get('update_time')
            latest_update_time=it.get('latest_update_time')
            rating_level=it.get('rating_level')
            vuln_type=it.get('vuln_type')
            poc_flag=it.get('poc_flag')
            tag=it.get('tag')
            used_flag=it.get('used_flag')
            public_flag=it.get('public_flag')
            malicious_type=it.get('malicious_type')
            qpe_prod_name=it.get('qpe_prod_name')
            qpe_manufacture_name=it.get('qpe_manufacture_name')

            yield {
                'id':id,
                'vuln_name':vuln_name,
                'vuln_name_en':vuln_name_en,
                'qvd_code':qvd_code,
                'cve_code':cve_code,
                'cnvd_id':cnvd_id,
                'cnnvd_id':cnnvd_id,
                'threat_category':threat_category,
                'technical_category':technical_category,
                'residence_id':residence_id,
                'rating_id':rating_id,
                'not_show':not_show,
                'publish_time':publish_time,
                'description':description,
                'description_en':description_en,
                'change_impact':change_impact,
                'operator_hid':operator_hid,
                'create_hid':create_hid,
                'temp':temp,
                'other_rating':other_rating,
                'create_time':create_time,
                'update_time':update_time,
                'latest_update_time':latest_update_time,
                'rating_level':rating_level,
                'vuln_type':vuln_type,
                'poc_flag':poc_flag,
                'tag':tag,
                'used_flag':used_flag,
                'public_flag':public_flag,
                'malicious_type':malicious_type,
                'qpe_prod_name':qpe_prod_name,
                'qpe_manufacture_name':qpe_manufacture_name,
            }

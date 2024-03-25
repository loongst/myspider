import requests
import json
start_urls = ["https://www.oscs1024.com/oscs/v1/intelligence/list"]
for i in range (5):
    formdata={"page":i+1,"per_page":10}
    data = json.dumps(formdata)
    headers={

        "accept-encoding":"gzip, deflate, br",
        "accept-language":"zh-CN,zh;q=0.9",
        "content-type":"application/json",
        # "cookie":"tgw_l7_route=e820e94b9fa7c80b604327cb18828928; Hm_lvt_113185c61c5bffebb22e97ff5c955cc5=1678260308; Hm_lpvt_113185c61c5bffebb22e97ff5c955cc5=1678260308",
        "origin":"https://www.oscs1024.com",
        "referer":"https://www.oscs1024.com/cm",
        "user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36",
    }

    res=requests.post(url=start_urls[0],data=data,headers=headers)
    if res.status_code==200:
            # print("+"*1000)
            content=json.loads(res.text)
            # print("-"*1000)
            # print(content)
            for i in content['data']['data']:
                name = i['title']
                url = i['url']
                time = i['public_time'].split("T")[0]
                severity = i['level']
                result= {
                    "name":name,
                    "url":url,
                    "time":time,
                    "severity":severity
                }
                print(result)
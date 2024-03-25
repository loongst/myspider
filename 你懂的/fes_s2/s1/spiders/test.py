# from selenium import webdriver
# import requests
# import time

# options=webdriver.ChromeOptions()
# options.add_argument('--headless')
# browser=webdriver.Chrome(chrome_options=options)

# url='https://loongxu.com'
# browser.get(url)

# print(browser.page_source)
# time.sleep(5)
# browser.close()
# with open(r'C:\Users\loongxu\Desktop\wordlist.txt',"w") as f:
#     for i in range(300):
#         f.write(str(i)+'\n')
# import pymysql

# params={
#     'host':'127.0.0.1',
#     'port':3306,
#     'user':'root',
#     'password':'root',
#     'database':'cl',
#     'charset':'utf8'
# }

# con=pymysql.connect(**params)
# mcursor=con.cursor()
# mcursor.execute('insert into t1(id,name,url,tag) values(null,%s,%s,%s)',('我是','中国','战士'))
# con.commit()
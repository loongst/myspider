import requests
import time
from selenium import webdriver
from scrapy.http.response.html import HtmlResponse
class SeleniumDownloadMiddleware(object):
    def __init__(self):
        self.driver=webdriver.Chrome(executable_path=r"D:\chromedriver80\chromedriver.exe")

    def process_self(self,url):
        self.driver.get(url)
        time.sleep(3)
        try:
            showMore=self.driver.find_element_by_class_name('H7E3vT')
            print(showMore)
        except expression as identifier:
            pass
        request=requests.get(url)
        source = self.driver.page_source
        response=HtmlResponse(url=self.driver.current_url,body=source,request=request)
        return response
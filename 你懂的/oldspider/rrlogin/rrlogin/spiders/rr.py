# -*- coding: utf-8 -*-
import scrapy


class RrSpider(scrapy.Spider):
    name = 'rr'
    allowed_domains = ['loongxu.com']
    start_urls = ['http://www.loongxu.com/']

    def start_requests(self):
        url="https://www.loongxu.com/wp-login.php"
        data={
            "log":"xiaolong",
            "pwd":"zheshiMIMA_haha//..",
            "wp-submit":"登录",
            "redirect_to":"https://www.loongxu.com/wp-admin/",
            "testcookie": "1"
        }
        cookies={"Cookie":"wordpress_test_cookie=WP+Cookie+check"}
        request=scrapy.FormRequest(url=url,formdata=data,callback=self.parse_page,cookies=cookies)
        yield request


    def parse_page(self, response):
        with open("123.html","w",encoding="utf-8") as f:
            f.write(response.text)
        

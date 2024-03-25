import scrapy
from scrapy_redis.spiders import RedisSpider

class CveSpider(scrapy.Spider):
    name = "cve"
    # redis_key='cve:start_urls'
    allowed_domains = ["cvedetails.com"]
    start_urls = ["https://www.cvedetails.com/vulnerability-list.php?vendor_id=0&product_id=0&version_id=0&page=1&hasexp=0&opdos=0&opec=0&opov=0&opcsrf=0&opgpriv=0&opsqli=0&opxss=0&opdirt=0&opmemc=0&ophttprs=0&opbyp=0&opfileinc=0&opginf=0&cvssscoremin=1&cvssscoremax=0&year=0&month=0&cweid=0&order=1&trc=180151&sha=0cfd1c6feb7980a3cdce726ead01bc1d6297aaef"]

    def parse(self, response):
        conlist=response.xpath("//div[@id='searchresults']/table/tr[position()>=2]")
        for con in conlist:
            group=0
            if len(con.xpath("./td"))>1:
                    CVE_ID=con.xpath("./td[2]//text()").get().strip()
                    CWE_ID=con.xpath("./td[3]//text()").get() or ""
                    Vulnerability_Type=con.xpath("./td[5]//text()").get().strip() or ""
                    Publish_Date=con.xpath("./td[6]//text()").get().strip()
                    Update_Date=con.xpath("./td[7]//text()").get().strip()
                    Score=con.xpath("./td[8]//text()").get().strip()
                    Gained_Access_Level=con.xpath("./td[9]//text()").get().strip()
                    Access=con.xpath("./td[10]//text()").get().strip()
                    Complexity=con.xpath("./td[11]//text()").get().strip()
                    Authentication=con.xpath("./td[12]//text()").get().strip()
                    Confidentiality=con.xpath("./td[13]//text()").get().strip()
                    Integrity=con.xpath("./td[14]//text()").get().strip()
                    Availability=con.xpath("./td[15]//text()").get().strip()
            else:
                 Description=con.xpath("./td//text()").get().strip()
                 group+=1

            if group:
                 yield {
                    "CVE_ID":CVE_ID,
                    "CWE_ID":CWE_ID,
                    "Vulnerability_Type":Vulnerability_Type,
                    "Publish_Date":Publish_Date,
                    "Update_Date":Update_Date,
                    "Score":Score,
                    "Gained_Access_Level":Gained_Access_Level,
                    "Access":Access,
                    "Complexity":Complexity,
                    "Authentication":Authentication,
                    "Confidentiality":Confidentiality,
                    "Integrity":Integrity,
                    "Availability":Availability,
                    "Description":Description
                 }

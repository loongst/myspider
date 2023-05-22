# Scrapy settings for ljp project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://docs.scrapy.org/en/latest/topics/settings.html
#     https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://docs.scrapy.org/en/latest/topics/spider-middleware.html

BOT_NAME = "ljp"

SPIDER_MODULES = ["ljp.spiders"]
NEWSPIDER_MODULE = "ljp.spiders"


# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = "ljp (+http://www.yourdomain.com)"

# Obey robots.txt rules
ROBOTSTXT_OBEY = False

# Configure maximum concurrent requests performed by Scrapy (default: 16)
CONCURRENT_REQUESTS = 8

# Configure a delay for requests for the same website (default: 0)
# See https://docs.scrapy.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
# DOWNLOAD_DELAY = 1
# The download delay setting will honor only one of:
#CONCURRENT_REQUESTS_PER_DOMAIN = 16
#CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
#COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)
#TELNETCONSOLE_ENABLED = False

# Override the default request headers:
DEFAULT_REQUEST_HEADERS = {
    'Accept':'application/json, text/plain, */*',
    'Accept-Encoding':'gzip, deflate, br',
    'Accept-Language':'zh-CN,zh;q=0.9',
    'Authorization':'Bearer eyJhbGciOiJIUzUxMiJ9.eyJ1c2VyX3R5cGUiOiIwMSIsInVzZXJfaWQiOjEzMDMsInVzZXJfa2V5IjoiMDRhNWMxNGMtYmYwYy00MWYzLWIxNDAtYzVmOWU4OWFkNmNjIiwidXNlcm5hbWUiOiLpvZDpvZDlk4jlsJTljZzlpY7kuK3ljLvpmaLkuInnl4XljLoifQ.zrCo0RTbIjdoWVl0Ai16kUAcpo6R_HYfi_doJVUXEtwaP2D6DnqjWDpQjCcUirFTEXtg9OhIZEnlK3ix1GoUfg',
    'Connection':'keep-alive',
    'Cookie':'username=%E9%BD%90%E9%BD%90%E5%93%88%E5%B0%94%E5%8D%9C%E5%A5%8E%E4%B8%AD%E5%8C%BB%E9%99%A2%E4%B8%89%E7%97%85%E5%8C%BA; password=SJYVRF/HPFDKDIe0ItGod1P4xjWs5Nqz1Zf7DRoH2L/38mwiBxc6y+xnPsx40er8T2vDnXbrsFCpf4s6j8rzWg==; rememberMe=true; Admin-Token=eyJhbGciOiJIUzUxMiJ9.eyJ1c2VyX3R5cGUiOiIwMSIsInVzZXJfaWQiOjEzMDMsInVzZXJfa2V5IjoiMDRhNWMxNGMtYmYwYy00MWYzLWIxNDAtYzVmOWU4OWFkNmNjIiwidXNlcm5hbWUiOiLpvZDpvZDlk4jlsJTljZzlpY7kuK3ljLvpmaLkuInnl4XljLoifQ.zrCo0RTbIjdoWVl0Ai16kUAcpo6R_HYfi_doJVUXEtwaP2D6DnqjWDpQjCcUirFTEXtg9OhIZEnlK3ix1GoUfg; Admin-Expires-In=720',
    'Host':'cgm.glu2u.com',
    'Referer':'https://cgm.glu2u.com/bloodsugar/patient',
    'Sec-Fetch-Dest':'empty',
    'Sec-Fetch-Mode':'cors',
    'Sec-Fetch-Site':'same-origin',
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36',
    'sec-ch-ua':'"Google Chrome";v="113", "Chromium";v="113", "Not-A.Brand";v="24"',
    'sec-ch-ua-mobile':'?0',
    'sec-ch-ua-platform':'"Windows"'
}

# Enable or disable spider middlewares
# See https://docs.scrapy.org/en/latest/topics/spider-middleware.html
#SPIDER_MIDDLEWARES = {
#    "ljp.middlewares.LjpSpiderMiddleware": 543,
#}

# Enable or disable downloader middlewares
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
#DOWNLOADER_MIDDLEWARES = {
#    "ljp.middlewares.LjpDownloaderMiddleware": 543,
#}

# Enable or disable extensions
# See https://docs.scrapy.org/en/latest/topics/extensions.html
#EXTENSIONS = {
#    "scrapy.extensions.telnet.TelnetConsole": None,
#}

# Configure item pipelines
# See https://docs.scrapy.org/en/latest/topics/item-pipeline.html
#ITEM_PIPELINES = {
#    "ljp.pipelines.LjpPipeline": 300,
#}

# Enable and configure the AutoThrottle extension (disabled by default)
# See https://docs.scrapy.org/en/latest/topics/autothrottle.html
#AUTOTHROTTLE_ENABLED = True
# The initial download delay
#AUTOTHROTTLE_START_DELAY = 5
# The maximum download delay to be set in case of high latencies
#AUTOTHROTTLE_MAX_DELAY = 60
# The average number of requests Scrapy should be sending in parallel to
# each remote server
#AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:
#AUTOTHROTTLE_DEBUG = False

# Enable and configure HTTP caching (disabled by default)
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
#HTTPCACHE_ENABLED = True
#HTTPCACHE_EXPIRATION_SECS = 0
#HTTPCACHE_DIR = "httpcache"
#HTTPCACHE_IGNORE_HTTP_CODES = []
#HTTPCACHE_STORAGE = "scrapy.extensions.httpcache.FilesystemCacheStorage"

# Set settings whose default value is deprecated to a future-proof value
REQUEST_FINGERPRINTER_IMPLEMENTATION = "2.7"
TWISTED_REACTOR = "twisted.internet.asyncioreactor.AsyncioSelectorReactor"
FEED_EXPORT_ENCODING = "utf-8"

import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from ..items import VpnTxtItem
import time,random,json

class YhooSg_Spider(CrawlSpider):
    name = 'yahoo_sg'
    allowed_domains = ['sg.news.yahoo.com','sg.finance.yahoo.com','sg.style.yahoo.com','sg.yahoo.com']
    start_urls = ['https://sg.yahoo.com/','https://sg.news.yahoo.com/','https://sg.finance.yahoo.com/','https://sg.style.yahoo.com/','https://sg.yahoo.com/',]
    def __init__(self):
        super(YhooSg_Spider, self).__init__(name='yahoo_sg')
        self.page=0
    rules = (
             Rule(LinkExtractor(allow=r'/.*-\d+.html'),   callback='parse_item', follow=True),
             Rule(LinkExtractor(allow=r'https://sg.news.yahoo.com/.*'), follow=True),
             Rule(LinkExtractor(allow=r'https://sg.finance.yahoo.com/.*'), follow=True),
             Rule(LinkExtractor(allow=r'https://sg.style.yahoo.com/.*'), follow=True),
             Rule(LinkExtractor(allow=r'https://sg.yahoo.com/.*'), follow=True),
             )

    def parse_item(self, response):
        item = VpnTxtItem()
        # item['url'] = response.url
        # item['status'] = 1
        # item["creat_time"] = time.time()

        try:
            item['keyword']=response.xpath("//meta[@name='news_keywords']/@content").extract_first().replace(', ','|')
        except Exception:
            item['keyword']=''
        try:
            item['title']=response.xpath("//head/title/text()").extract_first()
            #item['content']=''.join(response.xpath("//div[@class='story']//p//text()").extract())
        except Exception:
            pass
        print(response.url)
        print(item['title'])
        time.sleep(1)

        # if item['title'] is not None and len(item['content']) >= 50:
        #     self.page += 1
        #     print(time.strftime('%Y.%m.%d-%H:%M:%S'),'第',self.page,'条抓取成功,url:', item['url'])
        #     time.sleep(random.uniform(0.2, 0.8))
        #     return item
    def close(spider, reason):
        print('scrapy-arstechnica抓取完成,共抓取:',spider.page,'条数据')
        ##self.crawler.engine.close_spider(self, "关闭spider")
        #scrapy crawl yahoo_sg
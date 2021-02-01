import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from ..items import VpnTxtItem
import time,re,random,json

class VergeSpider(CrawlSpider):
    name = 'verge'
    allowed_domains = ['theverge.com']
    start_urls = ['https://www.theverge.com/']
    def __init__(self):
        super(VergeSpider, self).__init__(name='verge')
        self.page=0
    rules = (
             # Rule(LinkExtractor(allow=r'/news/.*'),   callback='parse_item', follow=True),
             # Rule(LinkExtractor(allow=r'/sports/.*'), callback='parse_item', follow=True),
             Rule(LinkExtractor(allow=r'https://www.theverge.com/.*'),follow=True),
             Rule(LinkExtractor(allow=r'https://www.theverge.com/\d+/\d+/\d+/\d+/.*'), callback='parse_item', follow=False),
             )

    def parse_item(self, response):


        item = VpnTxtItem()
        item['url'] = response.url
        item['status'] = 1
        item["creat_time"] = time.time()
        try:
            item['keyword']=response.xpath("//meta[@name='parsely-tags']/@content").extract()[0].replace(',', '')
        except Exception:
            item['keyword'] = ''
        try:
            item['title']=response.xpath("//h1[@class='c-page-title']/text()").extract_first()
            item['content']=''.join(response.xpath("//div[@class='l-col__main']//p//text()").extract())
        except Exception:
            pass
        if item['title'] is not None and len(item['content']) >= 50:
            self.page += 1
            print(time.strftime('%Y.%m.%d-%H:%M:%S'), item)
            #print(time.strftime('%Y.%m.%d-%H:%M:%S'),'第',self.page,'条抓取成功,url:', item['url'])
            time.sleep(random.uniform(0.2, 0.8))
            return item
    def close(spider, reason):
        print('scrapy-arstechnica抓取完成,共抓取:',spider.page,'条数据')

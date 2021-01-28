import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from ..items import VpnTxtItem
import time,re,random,json

class CbcSpider(CrawlSpider):
    name = 'cbc'
    allowed_domains = ['cbc.ca']
    start_urls = ['https://www.cbc.ca/news','https://www.cbc.ca/sports']
    def __init__(self):
        super(CbcSpider, self).__init__(name='cbc')
        self.page=0
    rules = (Rule(LinkExtractor(allow=r'/news/.*'), callback='parse_item', follow=True),)
    rules = (Rule(LinkExtractor(allow=r'/sports/.*'), callback='parse_item', follow=True),)
    def parse_item(self, response):
        item = VpnTxtItem()
        item['url'] = response.url
        item['status'] = 1
        item["creat_time"] = time.time()
        try:
            json_date=json.loads(response.xpath("//script[@id='initialStateDom']/text()").extract_first().replace('window.__INITIAL_STATE__ = ','')[0:-1])
            key_list=json_date['detail']['content']['gs_keywords']
            item['keyword']='|'.join(key_list)
        except Exception:
            item['keyword']=''
        try:
            item['title']=response.xpath("//h1[@class='detailHeadline']/text()").extract_first()
            item['content']=''.join(response.xpath("//div[@class='story']//p//text()").extract())
        except Exception:
            pass
        if item['title'] is not None and len(item['content']) >= 50:
            self.page += 1
            print(time.strftime('%Y.%m.%d-%H:%M:%S'),'第',self.page,'条抓取成功,url:', item['url'])
            time.sleep(random.uniform(0.2, 0.7))
            return item
    def close(spider, reason):
        print('scrapy-arstechnica抓取完成,共抓取:',spider.page,'条数据')

import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from ..items import VpnTxtItem
import time,re,random,json

class NapostSpider(CrawlSpider):
    name = 'napost'
    allowed_domains = ['nationalpost.com']
    start_urls = ['https://nationalpost.com/category/news/','https://nationalpost.com/category/life/',
                  'https://nationalpost.com/category/sports/','https://nationalpost.com/category/entertainment/']
    def __init__(self):
        super(NapostSpider, self).__init__(name='napost')
        self.page=0
    rules = (
             # Rule(LinkExtractor(allow=r'/news/.*'),   callback='parse_item', follow=True),
             # Rule(LinkExtractor(allow=r'/sports/.*'), callback='parse_item', follow=True),
             Rule(LinkExtractor(allow=r'/news/.*'), callback='parse_item', follow=True),
             Rule(LinkExtractor(allow=r'/life/.*'), callback='parse_item', follow=True),
             Rule(LinkExtractor(allow=r'/sports/.*'), callback='parse_item', follow=True),
             Rule(LinkExtractor(allow=r'/entertainment/.*'), callback='parse_item', follow=True),
             )

    def parse_item(self, response):
        item = VpnTxtItem()
        item['url'] = response.url
        item['status'] = 1
        item["creat_time"] = time.time()


        try:
            json_date = json.loads(response.xpath("//script[@id='page-data']/text()").extract_first().replace('    ',''))
            item['keyword'] = '|'.join(json_date['page']['tags']).replace('|covid-19','')
        except Exception:
             item['keyword'] = ''
        try:
            item['title']=response.xpath("//h1[@class='article-title']//text()").extract_first()
            item['content']=''.join(response.xpath("//main[@id='main-content']/article/div[@class='row']//p//text()").extract())
        except Exception:
            pass
        if item['title'] is not None and len(item['content']) >= 50:
            self.page += 1
            print(time.strftime('%Y.%m.%d-%H:%M:%S'),'第',self.page,'条抓取成功,url:', item['url'])
            time.sleep(random.uniform(0.2, 0.8))
            return item
    def close(spider, reason):
        print('scrapy-arstechnica抓取完成,共抓取:',spider.page,'条数据')

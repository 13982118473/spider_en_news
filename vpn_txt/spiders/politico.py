import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from ..items import VpnTxtItem
import time,random,json

class PoliticoSpider(CrawlSpider):
    name = 'politico'
    allowed_domains = ['politico.com']
    start_urls = ['https://www.politico.com/story/2016/10/democrats-2020-attacks-gop-challengers-230340']
    def __init__(self):
        super(PoliticoSpider, self).__init__(name='politico')
        self.page=0
    rules = (
             Rule(LinkExtractor(allow=r'https://www.politico.com/story.*'),callback='parse_item', follow=True),
             Rule(LinkExtractor(allow=r'https://www.politico.com/news/.*'), callback='parse_item', follow=True),
             )

    def parse_item(self, response):
        item = VpnTxtItem()
        item['url'] = response.url
        item['status'] = 1
        item["creat_time"] = time.time()
        try:
            if '/news/' in item['url']:
                item['keyword']='|'.join(response.xpath("//li[@class='story-tags__list-item']/a/text()").extract()).replace('2020','').replace('2021','').replace('| ','|').replace(' |','|')
            elif '/story/' in item['url']:
                item['keyword']='|'.join(response.xpath("//div[@class='story-supplement ']//li//a//text()").extract()).replace('2020','').replace('2021','').replace('| ','|').replace(' |','|')
        except Exception:
            item['keyword']=''
        try:
            if '/news/' in item['url']:
                item['title']=response.xpath("//h2[@class='headline']//text()").extract_first()
                item['content']=''.join(response.xpath("//p[@class=' story-text__paragraph']//text()").extract())
            elif '/story/' in item['url']:
                item['title'] = response.xpath("//span[@itemprop='headline']//text()").extract_first()
                item['content'] = ''.join(response.xpath("//div[@class='story-text    ']/p//text()").extract())
        except Exception:
            item['title']=None
            item['content']=''
        time.sleep(random.uniform(0.2, 0.8))
        if item['title'] is not None and len(item['content']) >= 50:
            self.page += 1
            print(time.strftime('%Y.%m.%d-%H:%M:%S'),'第',self.page,'条抓取成功,url:', item['url'])
            return item
    def close(spider, reason):
        print('scrapy-arstechnica抓取完成,共抓取:',spider.page,'条数据')
        ##self.crawler.engine.close_spider(self, "关闭spider")
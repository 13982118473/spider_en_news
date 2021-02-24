import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from ..items import VpnTxtItem
import time,random

class PoliticoEu_Spider(CrawlSpider):
    name = 'politico_eu'
    allowed_domains = ['politico.eu']
    start_urls = ['https://www.politico.eu/','https://www.politico.eu/brussels/', 'https://www.politico.eu/tag/german-politics/', 'https://www.politico.eu/tag/french-politics/',
                  'https://www.politico.eu/tag/british-politics/', 'https://www.politico.eu/tag/migration/', 'https://www.politico.eu/tag/elections-in-europe/',
                  'https://www.politico.eu/tag/defense/', 'https://www.politico.eu/tag/foreign-policy/', 'https://www.politico.eu/europe-poll-of-polls/',
                  'https://www.politico.eu/continent/', 'https://www.politico.eu/tag/eu-recovery-plan/', 'https://www.politico.eu/special-reports/',
                  'https://www.politico.eu/section/agriculture/', 'https://www.politico.eu/section/brexit/', 'https://www.politico.eu/section/competition/',
                  'https://www.politico.eu/section/cybersecurity/', 'https://www.politico.eu/section/energy/', 'https://www.politico.eu/section/financial-services/',
                  'https://www.politico.eu/section/health-care/', 'https://www.politico.eu/section/mobility/', 'https://www.politico.eu/section/sustainability/',
                  'https://www.politico.eu/section/technology/', 'https://www.politico.eu/section/trade/', 'https://www.politico.eu/section/trade-uk/',
                  'https://www.politico.eu/telescope-hub/', 'https://www.politico.eu/tag/eu-in-africa/', 'https://www.politico.eu/tag/global-policy-lab/',
                  'https://www.politico.eu/changemakers/', 'https://www.politico.eu/energy-visions-hub/', 'https://www.politico.eu/policy-guide/',
                  'https://www.politico.eu/blogs/the-coming-wars/', 'https://www.politico.eu/author/paul-taylor/', 'https://www.politico.eu/author/nathalie-tocci/',
                  'https://www.politico.eu/author/mujtaba-rahman/', 'https://www.politico.eu/tag/declassified/']
    def __init__(self):
        super(PoliticoEu_Spider, self).__init__(name='politico_eu')
        self.page=0
    rules = (
             Rule(LinkExtractor(allow=r'https://www.politico.eu/article/.*'),   callback='parse_item', follow=True),
             Rule(LinkExtractor(allow=r'https://www.politico.eu/.*/page/.*'), callback='parse_item', follow=True)
             )

    def parse_item(self, response):
        time.sleep(random.uniform(0.2, 0.8))
        if 'article' in response.url:
            item = VpnTxtItem()
            item['url'] = response.url
            item['status'] = 1
            item["creat_time"] = time.time()
            try:
                item['keyword']='|'.join([tag.strip() for tag in response.xpath("//div[@class='tags__tags']/a//text()").extract()])
            except Exception:
                item['keyword']=''
            try:
                item['title']=response.xpath("//h1[@class='article-meta__title']/text()").extract_first().strip()
                item['content']=''.join(response.xpath("//div[@class='article__content']/p//text()").extract())
            except Exception :
                item['title']=None
            if item['title'] is not None and len(item['content']) >= 50:
                self.page += 1
                print(time.strftime('%Y.%m.%d-%H:%M:%S'),'第',self.page,'条抓取成功,url:', item['url'])
                yield item
    def close(spider, reason):
        print('scrapy-arstechnica抓取完成,共抓取:',spider.page,'条数据')
        ##self.crawler.engine.close_spider(self, "关闭spider")
        #scrapy crawl politico_eu
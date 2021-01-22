import scrapy,re,time,random
from ..items import VpnTxtItem


class ArstechnicaSpider(scrapy.Spider):
    name = 'arstechnica'
    allowed_domains = ['arstechnica.com']
    start_urls = ['http://arstechnica.com/']

    def parse(self, response):
        category_res=response.xpath("//nav[@id='header-nav-primary']//li/a/@href").extract()
        for category_url in category_res:
            yield scrapy.Request(response.urljoin(category_url),callback=self.category_parse)

    def category_parse(self,response):
        info_url_list = response.xpath("//section[@class='with-xrail']//li[@class='tease article ']/a/@href").extract()
        for info_url in info_url_list:
            time.sleep(random.uniform(0.2,0.8))
            yield scrapy.Request(response.urljoin(info_url),callback=self.info_parse)
        next_url=response.xpath("//a[@class='load-more' or @class='left']/@href").extract_first()
        yield scrapy.Request(response.urljoin(next_url), callback=self.category_parse)

    def info_parse(self,response):
        item=VpnTxtItem()
        try:
            item["keyword"] = re.findall('"keywords":"(.*?)"', response.text)[0]
        except Exception:
            item["keyword"]=''
        try:
            content = ''
            item["title"]   =response.xpath("//meta[@property='og:title']/@content").extract_first()
            txt_list = response.xpath("//div[@class='article-content post-page']//p//text()").extract()
            for txt in txt_list:
                content+=txt.strip()
            item["content"]=content
        except Exception:
            item["title"]=''
            item["content"] = ''
        item["url"]=response.url
        item["creat_time"] = time.time()
        item["status"] = 1
        yield item
import scrapy


class NationalpostSpider(scrapy.Spider):
    name = 'nationalpost'
    allowed_domains = ['https://nationalpost.com/']
    start_urls = ['http://https://nationalpost.com//']

    def parse(self, response):
        pass

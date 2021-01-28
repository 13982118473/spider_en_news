import scrapy,time,random,re,json
from ..items import VpnTxtItem

class NationalpostSpider(scrapy.Spider):
    name = 'nationalpost'
    allowed_domains = ['nationalpost.com']
    start_urls = ['https://nationalpost.com/category/news/?more=news']
    def __init__(self):
        super(NationalpostSpider, self).__init__(name='nationalpost')
        self.page=0
        print('scrapy-nationalpost抓取启动')
    def parse(self, response):
        category_list=response.xpath("//div[contains(@class,'list feed-section__content feed-section__content--category')]//div[@class='article-card__content']/a/@href").extract()
        for category_url in category_list:
            time.sleep(random.uniform(0.2, 0.8))
            yield scrapy.Request(response.urljoin(category_url),callback=self.info_parse)
        # 翻页解析
        next_url = response.xpath("//a[@rel='next']/@href").extract_first()
        yield scrapy.Request(response.urljoin(next_url), callback=self.parse)

    def info_parse(self,response):
        item=VpnTxtItem()
        item['url']=response.url
        item['status']=1
        item["creat_time"] = time.time()
        try:
            keyword_list = re.findall('"tags":( \[.*?\])', response.text)[0].strip()
            item["keyword"]='|'.join(json.loads(keyword_list))
        except Exception:
            item["keyword"] = ''
        try:
            item["title"] = response.xpath("//h1/text()").extract_first()
        except Exception:
            item["title"]=''
        try:
            item["content"] = ''.join(response.xpath("//section[@class='article-content']/p//text()").extract())
            self.page+=1
            print('第',self.page,'条抓取成功,url:',item['url'])
            yield item
        except Exception:
            print(response.url,'抓取失败!!')

    def close(spider, reason):
        print('scrapy-arstechnica抓取完成,共抓取:',spider.page,'条数据')





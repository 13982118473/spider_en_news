import requests,time,json,scrapy,urllib3,random
from ..items import GetKeywordItem
from scrapy.downloadermiddlewares import retry
urllib3.disable_warnings()

class GetKeyword(scrapy.Spider):
    name = 'get_keyword'
    allowed_domains = ['google.com','google.com.hk']
    custom_settings = {
        'User-Agent':'Mozilla/5.0 (Linux; Android 7.0; SM-G930V Build/NRD90M) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.125 Mobile Safari/537.36',
        'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'Accept-Language':'en;q=0.8',
        'referer':'https://www.google.com.hk/'
    }
    item = GetKeywordItem()
    proxy=None
    def __init__(self,keyword_start='',*args, **kwargs):
        super(GetKeyword, self).__init__(name='get_keyword',*args, **kwargs)
        self.keyword_start=keyword_start
        if keyword_start == '':
            raise ValueError('请输入正确的启动指令及参数!!如:scrapy crawl get_keyword -a keyword_start=key1,key2,key3')
        self.args_list = self.keyword_start.split(',')
        for args in self.args_list:
            self.start_urls.append('https://www.google.com/search?q={}'.format(args))
        self.keyword=[]
        print('Scrapy-GetKeyword抓取启动')

    def start_requests(self):
        # 如果无代理,只获取接口
        if self.proxy is not None:
            for start_url in self.start_urls:
                try:
                    yield scrapy.Request(start_url,callback=self.parse,meta={"proxy": self.proxy},errback=self.errback)
                except Exception:pass
        else:
            print('未检查到代理IP,准备获取接口......')
            for args in self.args_list:
                print(time.strftime('%Y.%m.%d-%H:%M:%S'),'正在获取:', args)
                time.sleep(1)
                yield scrapy.Request('https://www.google.com.hk/complete/search?q={}&cp=1&client=psy-ab&xssi=t&gs_ri=gws-wiz&hl=en&authuser=0'.format(args), callback=self.api_parse)

    def parse(self,response):
        if response.status != 429:
            key_wd=[]
            arg=response.url.split('=')[1]
            try:
                date_str=requests.get('https://www.google.com.hk/complete/search?q={}&cp=1&client=psy-ab&xssi=t&gs_ri=gws-wiz&hl=en&authuser=0'.format(arg),verify=False,headers=self.custom_settings,timeout=10).content.decode('raw_unicode-escape').replace(")]}'\n","")
                date_list = json.loads(date_str)
                for date in date_list[0]:
                    key = date[0].replace('<b>', '').replace('</b>', '')
                    if key not in self.keyword and 'www.' not in key:
                        self.keyword.append(key)
                        key_wd.append(key)
            except Exception:pass
            g_key = response.xpath("//div[@class='s75CSd']/span/text()").extract()
            for key in g_key:
                if key not in self.keyword and 'www.' not in key:
                    self.keyword.append(key)
                    key_wd.append(key)
            for key2 in key_wd:
                yield scrapy.Request('https://www.google.com.hk/complete/search?q={}&cp=1&client=psy-ab&xssi=t&gs_ri=gws-wiz&hl=en&authuser=0'.format(key2),callback=self.api_parse)
                print(time.strftime('%Y.%m.%d-%H:%M:%S'),'正在获取:', key2)
        else:
            print('代理错误,状态码:',response.status)

    def parse_2(self,response):
        key_wd = []
        arg = response.url.split('=')[1]
        try:
            date_str = requests.get('https://www.google.com.hk/complete/search?q={}&cp=1&client=psy-ab&xssi=t&gs_ri=gws-wiz&hl=en&authuser=0'.format(arg), verify=False, headers=self.custom_settings, timeout=10).content.decode('raw_unicode-escape').replace(")]}'\n", "")
            date_list = json.loads(date_str)
            for date in date_list[0]:
                key = date[0].replace('<b>', '').replace('</b>', '')
                if key not in self.keyword and 'www.' not in key:
                    self.keyword.append(key)
                    key_wd.append(key)
        except Exception:
            pass
        g_key = response.xpath("//div[@class='s75CSd']/span/text()").extract()
        for key in g_key:
            if key not in self.keyword and 'www.' not in key:
                self.keyword.append(key)
                key_wd.append(key)

        for key2 in key_wd:
            yield scrapy.Request('https://www.google.com/search?q={}'.format(key2), callback=self.parse_3,errback=self.errback)
            print(time.strftime('%Y.%m.%d-%H:%M:%S'),'正在获取:', key2)

    def parse_3(self,response):
        key_wd = []
        arg = response.url.split('=')[1]
        try:
            date_str=requests.get('https://www.google.com.hk/complete/search?q={}&cp=1&client=psy-ab&xssi=t&gs_ri=gws-wiz&hl=en&authuser=0'.format(arg),verify=False,headers=self.custom_settings,timeout=10).content.decode('raw_unicode-escape').replace(")]}'\n","")
            date_list = json.loads(date_str)
            for date in date_list[0]:
                key = date[0].replace('<b>', '').replace('</b>', '')
                if key not in self.keyword and 'www.' not in key:
                    self.keyword.append(key)
                    key_wd.append(key)
        except Exception:pass
        g_key = response.xpath("//div[@class='s75CSd']/span/text()").extract()
        for key in g_key:
            if key not in self.keyword and 'www.' not in key:
                self.keyword.append(key)
                key_wd.append(key)
        for key2 in key_wd:
            yield scrapy.Request('https://www.google.com/search?q={}'.format(key2), callback=self.parse_4,errback=self.errback)
            print(time.strftime('%Y.%m.%d-%H:%M:%S'), '正在获取:', key2)

    def parse_4(self,response):
        key_wd = []
        arg = response.url.split('=')[1]
        try:
            date_str = requests.get('https://www.google.com.hk/complete/search?q={}&cp=1&client=psy-ab&xssi=t&gs_ri=gws-wiz&hl=en&authuser=0'.format(arg), verify=False, headers=self.custom_settings, timeout=10).content.decode('raw_unicode-escape').replace(")]}'\n", "")
            date_list = json.loads(date_str)
            for date in date_list[0]:
                key = date[0].replace('<b>', '').replace('</b>', '')
                if key not in self.keyword and 'www.' not in key:
                    self.keyword.append(key)
                    key_wd.append(key)
        except Exception:
            pass
        g_key = response.xpath("//div[@class='s75CSd']/span/text()").extract()
        for key in g_key and 'www.' not in key:
            if key not in self.keyword:
                self.keyword.append(key)
                key_wd.append(key)
    def errback(self,failure):
        print('-----错误',failure)
    def close(self, reason):
        print(time.strftime('%Y.%m.%d-%H:%M:%S'), '抓取结束')


#如果无代理,只获取接口
    def api_parse(self,response):
        key_wd=[]
        count_number=len(self.args_list)
        date_str=response.body.decode('raw_unicode-escape').replace(")]}'\n", "")
        date_list = json.loads(date_str)
        for date in date_list[0]:
            key = date[0].replace('<b>', '').replace('</b>', '')
            if key not in self.keyword and 'www.' not in key:
                self.keyword.append(key)
                key_wd.append(key)
        for key2 in key_wd:
            if len(self.keyword) >= random.randint(count_number*850-count_number*250,count_number*1000+count_number*200):
                keyword = self.keyword
                self.item['keyword_start'] = self.keyword_start
                self.item['keyword_result'] = ','.join(keyword)
                self.item['keyword_sum'] = len(keyword)
                self.item['status'] = 1
                self.item['creat_time'] = time.time()
                yield self.item
                self.crawler.engine.close_spider(self)
            else:
                print(time.strftime('%Y.%m.%d-%H:%M:%S'), '正在获取:', key2)
                time.sleep(random.uniform(0.001,0.2))
                yield scrapy.Request('https://www.google.com.hk/complete/search?q={}&cp=1&client=psy-ab&xssi=t&gs_ri=gws-wiz&hl=en&authuser=0'.format(key2), callback=self.api_parse)
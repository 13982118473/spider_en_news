安装:
    环境:
        python3.6
    包管理工具:
        pip3
    安装包(pip3 install 包名):
        scrapy (linux安装scrapy 出现错误请参照: https://blog.csdn.net/chitian6393/article/details/100726695或者百度自行更改!!!(一般会报错,需安装 Twisted 和 VS ++)
        lxml
        pymongo
        

文件说明:
    vpn_txt:项目根目录
        --vpn_txt(爬虫目录)
            --middlewares.py (爬虫中间件)
            --pipelines.py   (爬虫管道,自定义存储)
            --settings.py    (爬虫设置,并发数,延迟)
            --items.py       (数据模型)
            --spiders        (爬虫规则目录)
                arstechnica.py (https://www.arstechnica.com/爬取规则)
                cbc.py          (https://www.cbc.com/爬取规则)
                napost.py       (https://www.napost.com/爬取规则)
                politico        (https://www.politico.com/爬取规则)
                verge.py        (https://www.verge.com/爬取规则)
                get_keyword.py  (google关键字爬取规则)

项目说明:
    本项目为crawlab上运行scrapy爬虫
    在./vpn_txt/settings.py文件里,将 crawlab入库管道: {'crawlab.pipelines.CrawlabMongoPipeline': 888} 添加到: ITEM_PIPELINES 里
    上传到crawlab后:
        定义为:scrapy爬虫
        去重选择:覆盖方式,去重字段:title
        日志等级:WARNING

新闻文章启动命令:
    scrapy crawl {spider_name}

Google关键字启动命令:
    scrapy crawl get_keyword -a keyword_start=key1,key2,key3 

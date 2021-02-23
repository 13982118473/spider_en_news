项目说明:
    本项目为crawlab上运行scrapy爬虫,包含:海外新闻文章抓取,Google关键抓取
    在./vpn_txt/settings.py文件里,将 crawlab入库管道: {'crawlab.pipelines.CrawlabMongoPipeline': 888} 添加到: ITEM_PIPELINES 里


安装:
    环境:
        python3.6
    包管理工具:
        pip3
    安装包(pip3 install 包名):
        requirements.txt


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


新闻文章:
    启动命令:
        scrapy crawl {spider_name}
    上传到crawlab后:
        定义为:scrapy爬虫
        去重选择:覆盖方式,去重字段:title
    运行时:
        scrapy爬虫:选择爬虫名
        日志等级:WARNING

Google关键字:
    启动命令:
        scrapy crawl get_keyword -a keyword_start=key1,key2,key3 
    上传到crawlab后:
        定义为:scrapy爬虫
        去重选择:覆盖方式,去重字段:keyword_start
    运行时:
        scrapy爬虫:get_keyword
        日志等级:WARNING
        参数:-a keyword_start=key1,key2,key3 ...(key至少1个)
    

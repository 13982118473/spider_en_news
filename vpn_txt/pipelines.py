# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
from config import sql_date
import pymongo,time,logging

class VpnTxtPipeline:
    def open_spider(self, spider):
        # self.conn = pymongo.MongoClient('mongodb://{}:{}@{}:{}/?authSource={}'.format(sql_date["user"],sql_date["passwd"], sql_date["host"],sql_date["port"],sql_date["authSource"]))
        # self.db=self.conn[sql_date["datebase_name"]]
        # self.page_num=0
        logging.warning('启动爬虫')
    def process_item(self, item, spider):
        # #检查数据库是否已有该数据
        # if self.db[sql_date["set_name"]].count({'title': item['title']}) ==0:
        #     #字数设置
        #     if len(item['content'])>=50:
        #         self.db[sql_date["set_name"]].insert_one(dict(item))
        #         self.page_num+=1
        #         print('第',self.page_num,'条入库成功')
        #     else:pass
        return item

    def close_spider(self, spider):
        #self.conn.close()
        # logging.warning('爬虫关闭,共爬取到:'+str(self.page_num)+'条数据')
        print('********爬取完毕********')
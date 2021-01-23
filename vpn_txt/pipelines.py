# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
from config import sql_date
import pymongo

class VpnTxtPipeline:
    def open_spider(self, spider):
        self.conn = pymongo.MongoClient('mongodb://{}:{}@{}:{}/?authSource={}'.format(sql_date["user"],sql_date["passwd"], sql_date["host"],sql_date["port"],sql_date["authSource"]))
        self.db=self.conn[sql_date["datebase_name"]]
        self.page_num=0
    def process_item(self, item, spider):
        self.db[sql_date["set_name"]].insert_one(dict(item))
        self.page_num+=1
        print('第',self.page_num,'条入库成功')
        return item

    def close_spider(self, spider):
        self.mongo_py.close()
        print('********爬取完毕********')

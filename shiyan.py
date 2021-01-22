import requests,pymongo,re,random,time
from lxml import etree
from config import sql_date
# headers={'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36'
#         ,'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
#          'Accept-Language': 'zh-CN,zh;q=0.9',}
# a=requests.get('https://arstechnica.com/gaming/2021/01/gaming-the-system-how-gamestop-stock-surged-1500-in-nine-months/').content.decode()
# # print(a)
# d=etree.HTML(a)
# url=d.xpath("//div[@class='article-content post-page']//p//text()")
# print(url)
#conn = pymongo.MongoClient('mongodb://{}:{}@{}:{}/?authSource={}'.format("tiupuqg9erb64koe","ckhrde3cqe7ck817","154.212.112.247","17027","admin"))
# conn = pymongo.MongoClient('mongodb://{}:{}@{}:{}/?authSource={}'.format(sql_date["user"],sql_date["passwd"], sql_date["host"],sql_date["port"],sql_date["authSource"]))
#
# db=conn.vpn_txt
# db.hl.insert_one()
time.sleep(random.uniform(0.5,1.2))
import requests,pymongo,re,random,time,json
from lxml import etree
#from config import sql_date
# headers={'User-Agent':'Mozilla/5.0 (Linux; Android 7.0; SM-G930V Build/NRD90M) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.125 Mobile Safari/537.36',
#          'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
#          'Accept-Language': 'zh-CN,zh;q=0.9',}
# #s=requests.Session()
# a=requests.get('https://www.politico.eu/',headers=headers).content.decode()
# d=etree.HTML(a)
# url=d.xpath("//ul[@id='header__explore']//ul[@class='sub-menu']/li/a/@href")
# print(url)
# a=[]
# for u in url:
#     if 'www.' in u:
#         a.append(u)
#     else:
#         if u[-1] =='/':
#             a.append('https://www.politico.eu'+u)
#         else:
#             a.append('https://www.politico.eu'+u+'/')
# print(a)

# a=requests.get('https://www.cbc.ca/news/entertainment/elliot-page-emma-portner-divorce-1.5888967').content.decode()
# print(a)
# d=etree.HTML(a)
# url=d.xpath("//meta[@name='cXenseParse:cbc-keywordsSubject']/@content")
# print(url)
#conn = pymongo.MongoClient('mongodb://{}:{}@{}:{}/?authSource={}'.format("tiupuqg9erb64koe","ckhrde3cqe7ck817","154.212.112.247","17027","admin"))
# conn = pymongo.MongoClient('mongodb://{}:{}@{}:{}/?authSource={}'.format(sql_date["user"],sql_date["passwd"], sql_date["host"],sql_date["port"],sql_date["authSource"]))

# db=conn.vpn_txt
# db.hl.insert_one()
# time.sleep(random.uniform(0.5,1.2))
# print(time.strftime('%Y.%m.%d-%H:%M:%S'))

# w='ewffewf,aaaa,bbbb'.split(',')
# print(w[0])

# if a is  None:
#     print(2)

# 'https://www.google.com/search?q=gitgithub&start=30'
# a='lol'
# print(a.split(','))
# a=['time out market miami parking','time out market miami instagram','time out market miami best food','time out market miami brunch','time out market miami vegan']
# print(','.join(a))
# txt_list=[1,2,3,4,'This article is from gggrrg']
# if 'This article is from' in txt_list[-1]:
#     txt_list.pop(-1)
# print(txt_list)

a=[
    'https://sg.news.yahoo.com/',
    'https://sg.finance.yahoo.com/',
    'https://sg.style.yahoo.com/',
    'https://sg.yahoo.com/',
   ]
for aa in a:
    print(aa.replace('https:','').replace('/',''))
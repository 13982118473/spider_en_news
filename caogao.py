import pymongo
#连接mongod本地的服务
#conn = pymongo.MongoClient('mongodb://{}:{}@{}:{}/?authSource={}'.format("tiupuqg9erb64koe","ckhrde3cqe7ck817","154.212.112.247","17027","admin"))
mongo_py=pymongo.MongoClient('127.0.0.1',27017)

#建立新数据库
db=mongo_py['vpn_txt']
#连接数据库
# db = conn.vpn_txt
# print(db.stats())

# #建立表
biao = db['shiyan']
# a={'sex':"男"}
# biao.insert_one(a)
#
# k = db.collection_names(include_system_collections=True)  # 返回当前库下所有的集合名
# print(k)

# #建立数据：
# # a= {"name":'张三','age':50},
# b=[{"name":'张三','age':50},
#    {"name":'李四','age':51},
#    {"name":'王五','age':48}]
#
# #给表插入一个数据：
# a={'sex':"男"}
# biao.insert_one(a)
#
# #插入多个
# biao.insert_many(b)
#
# #删除一个：
# biao.delete_one({"name":'王五'})
# #删除多个：
# biao.delete_many({"name":'王五'})
#
# #修改一个
# biao.update({"name":'李四'},{'$set':{"name":'王五五'}})
# #修改多个
# biao.update_many({"name":'李四'},{'$set':{"name":'王五五'}})
#
# #查询：
# data = biao.find()
# for i in data:
#     print(i)
# #关闭数据库
# mongo_py.close()

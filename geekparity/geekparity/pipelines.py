# -*- coding: utf-8 -*-
from pymongo import MongoClient
from geekparity.settings import MONGODB_HOST,MONGODB_PORT
from geekparity.spiders.wangyi_spider import WangyiSpider
from geekparity.spiders.xiaomi_spider import XiaomiSpider
# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html


class GeekparityPipeline(object):
    def process_item(self, item, spider):
        client = MongoClient(host=MONGODB_HOST, port=MONGODB_PORT)
        db = None
        if isinstance(spider,WangyiSpider):
            # 插入数据到MongoDB
            db = client.wangyi
        elif isinstance(spider,XiaomiSpider):
            db = client.xiaomi
        projects = db.projects
        # 注意这里不能直接插入item,MongoDB在尝试添加或者设置_id，但是如果定义item的时候没有定义这个字段，那么就会提示KeyError
        projects.insert_one(item)
        # projects.insert_one(dict(item))
        # print("插入一条数据编号为：{0}".format(rs.inserted_id))
        return item

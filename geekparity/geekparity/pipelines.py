# -*- coding: utf-8 -*-
from pymongo import MongoClient
from geekparity.settings import MONGODB_HOST,MONGODB_PORT
from geekparity.spiders.wangyi_spider import WangyiSpider
from geekparity.spiders.xiaomi_spider import XiaomiSpider
from geekparity.items import CommentItem,ProjectItem
# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html


class GeekparityPipeline(object):

    def __init__(self):
        self.client = MongoClient(host=MONGODB_HOST, port=MONGODB_PORT)

    def process_item(self, item, spider):
        # 插入数据到MongoDB
        client = self.client
        db = None
        collection = None
        db = client.geekparity
        # if isinstance(spider,WangyiSpider):
        #     db = client.wangyi
        # elif isinstance(spider,XiaomiSpider):
        #     db = client.xiaomi

        if isinstance(item,ProjectItem):
            collection = db.projects
        elif isinstance(item,CommentItem):
            collection = db.comments
            # 注意这里不能直接插入item,MongoDB在尝试添加或者设置_id，但是如果定义item的时候没有定义这个字段，那么就会提示KeyError
        collection.insert(item)
        # collection.insert_one(dict(item))
        # print("插入一条数据编号为：{0}".format(rs.inserted_id))
        return item

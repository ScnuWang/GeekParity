# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class ProjectItem(scrapy.Item):
    # MongoDB主键
    _id = scrapy.Field()
    # 原始产品编号
    original_id = scrapy.Field()
    # 一级分类编号
    # category_id = scrapy.Field()
    # 二级分类编号
    # superCategory_id = scrapy.Field()
    # 产品名称
    project_name = scrapy.Field()
    # 产品价格
    project_price = scrapy.Field()
    # 产品地址
    project_url = scrapy.Field()
    # 产品简介
    project_desc = scrapy.Field()
    # 产品销售商
    project_platform = scrapy.Field()
    # 产品评分
    project_score = scrapy.Field()
    # 产品图片
    project_picUrl = scrapy.Field()
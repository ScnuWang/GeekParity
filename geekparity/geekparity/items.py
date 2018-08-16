# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy

# 产品数据
class ProjectItem(scrapy.Item):
    # MongoDB主键
    _id = scrapy.Field()
    # 原始产品编号
    original_id = scrapy.Field()
    # 产品归属平台  (网易：1；小米：2)
    website_id = scrapy.Field()
    # 一级分类编号
    # category_id = scrapy.Field()
    # 二级分类编号
    # superCategory_id = scrapy.Field()
    # 产品名称
    project_name = scrapy.Field()
    # 标签列表
    tags = scrapy.Field()
    # 设置关键字的人 默认值：Geekview
    tags_user = scrapy.Field()
    # 设置关键字的时间
    tags_time = scrapy.Field(serializer=str)
    # 关键字状态 0：未分词或分词异常 1：已分词
    tags_status = scrapy.Field()
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
    # 更新时间
    last_updated = scrapy.Field(serializer=str)

# 产品评论数据
class CommentItem(scrapy.Item):
    _id = scrapy.Field()
    # 产品归属平台  (小米：1；网易：2)
    website_id = scrapy.Field()
    # 产品编号
    project_id = scrapy.Field()
    # 评论人
    comment_user = scrapy.Field()
    # 产品评论
    comment_content = scrapy.Field()
    # 评论时间
    comment_time = scrapy.Field()
    # 更新时间
    last_updated = scrapy.Field(serializer=str)
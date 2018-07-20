import scrapy,json,requests
from scrapy.loader import ItemLoader
from geekparity.items import ProjectItem,CommentItem
from datetime import datetime
class WangyiSpider(scrapy.Spider):
    # 运行时调用这个name的值
    name = 'wangyi'
    start_urls=[
        # 居家大分类
        'http://you.163.com/item/list?categoryId=1005000',
        # 鞋包配饰
        'http://you.163.com/item/list?categoryId=1008000',
        # 服饰
        'http://you.163.com/item/list?categoryId=1010000',
        # 电器
        'http://you.163.com/item/list?categoryId=1043000',
        # 洗护
        'http://you.163.com/item/list?categoryId=1013001',
        # 饮食
        'http://you.163.com/item/list?categoryId=1005002',
        # 餐厨
        'http://you.163.com/item/list?categoryId=1005001',
        # 婴童
        'http://you.163.com/item/list?categoryId=1011000',
        # 文体
        'http://you.163.com/item/list?categoryId=1019000',
        # 特色区
        'http://you.163.com/item/list?categoryId=1065000',
    ]

    def parse(self, response):
        result = str(response.text)

        # 截取数据
        json_data = result[result.find('json_Data')+10 : result.find('};\n</script>')+1]
        # print("------------------>"+json_data)
        # 所有获取分类列表已经每一类下面的产品数据
        categoryItemList = json.loads(json_data)['categoryItemList']
        for categoryItem in categoryItemList:
            # 分类名称
            # categoryName = categoryItem['category']['name']
            # 分类编号
            # categoryId = categoryItem['category'][' id']
            # 父分类编号
            # superCategoryId = categoryItem['category'][' superCategoryId']
            # 产品列表
            projectsList = categoryItem['itemList']
            # print("------------------>" ,projectsList)
            for project in projectsList:
                id = str(project['id'])
                project_url = 'http://you.163.com/item/detail?id=' + id
                # print("------------------>", project_url)
                # 这里如果不添加yield关键字，回调parse_project方法失败
                yield scrapy.Request(project_url,callback=self.parse_project)

    def parse_project(self,response):
        result = str(response.text)
        # print("------------------>", result)
        # 截取数据
        json_data = result[result.find('var JSON_DATA_FROMFTL = ')+24: result.find('var JSON_DATA = ')-9]
        json_data = json_data.replace('\'',"\"")
        project_data = json.loads(json_data)['item']
        project = ProjectItem()
        original_id = str(response.url.split('=')[1])
        project['original_id'] = original_id
        project['project_name'] = project_data['name']
        project['project_price'] = project_data['counterPrice']
        project['project_url'] = response.url
        project['project_desc'] = project_data['simpleDesc']
        project['project_picUrl'] = project_data['primaryPicUrl']
        project['project_platform'] = '网易严选'
        project['project_score'] = json.loads(json_data)['commentGoodRates']
        project['last_updated'] = datetime.now()
        yield project
        # print("==================>", project)
        # 处理评论列表
        # 评论地址
        project_comment_url = 'http://you.163.com/xhr/comment/listByItemByTag.json?itemId='+original_id+'&tag=%E5%85%A8%E9%83%A8&size=30&page=1&orderBy=0'
        totalPage = json.loads(requests.get(project_comment_url).text)['data']['pagination']['totalPage']
        # 限定最多抓取120条
        if totalPage > 5 : totalPage = 5
        for page_num in range(1,totalPage):
            comment_url = 'http://you.163.com/xhr/comment/listByItemByTag.json?itemId='+original_id+'&tag=%E5%85%A8%E9%83%A8&size=30&page='+str(page_num)+'&orderBy=0'
            yield scrapy.Request(comment_url, callback=self.parse_comment)

    # 解析评论数据，有可能没有评论，有可能评论很多，有些达到几万条，而且不可能每次都抓取全部，所以，抓取前120条就够了
    def parse_comment(self,response):
        comment_data = json.loads(response.text)['data']['result']
        for comment in comment_data:
            comment_item = CommentItem()
            comment_item['website_id'] = 1
            comment_item['project_id'] = comment['itemId']
            comment_item['comment_user'] = comment['frontUserName']
            comment_item['comment_content'] = comment['content']
            comment_item['comment_time'] = comment['createTime']
            comment_item['last_updated'] = datetime.now()
            yield comment_item

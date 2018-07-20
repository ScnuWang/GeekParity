import scrapy,json,urllib
from scrapy.http import FormRequest
from geekparity.items import ProjectItem

class XiaomiSpider(scrapy.Spider):
    name = 'xiaomi'
    # start_urls = ['https://youpin.mi.com/app/shopv3/pipe',]
    def start_requests(self):
        # form = dict({"uClassList":{"model":"Homepage","action":"BuildHome","parameters":{"id":"446"}}})
        encode_body = 'data=%7B%22uClassList%22%3A%7B%22model%22%3A%22Homepage%22%2C%22action%22%3A%22BuildHome%22%2C%22parameters%22%3A%7B%22id%22%3A%22446%22%7D%7D%7D'
        # FormRequest封装了urllib.parse.quote ,将请求参数编码之后，放进body中,使用默认的headers
        yield FormRequest(url='https://youpin.mi.com/app/shopv3/pipe',method='POST',body=encode_body,callback=self.parse)

    def parse(self, response):
        # 获取列表数据
        data = json.loads(response.text)['result']['uClassList']['data']
        for categoryitem in data:
            # 获取有效分类列表数据
            if categoryitem['item_type'] == 6:
                category = categoryitem['content']
                category_name = category['name']
                # print(category_name)
                # 解析每一类下面的产品数据
                if categoryitem['data'] is not None:
                    for project_data in categoryitem['data']:
                        gid = project_data['gid']
                        form = '{"detail":{"model":"Shopv2","action":"getDetail","parameters":{"gid":%s}},"comment":{"model":"Comment","action":"getList","parameters":{"goods_id":%s,"orderby":"1","pageindex":"0","pagesize":3}},"activity":{"model":"Activity","action":"getAct","parameters":{"gid":%s}}}' % (gid, gid, gid)
                        encode_body = 'data=' + urllib.parse.quote(form)
                        # yield FormRequest(url='https://youpin.mi.com/app/shop/pipe', method='POST',body=encode_body, callback=lambda response:self.parse_project(response,gid))
                        yield FormRequest(url='https://youpin.mi.com/app/shop/pipe', method='POST',body=encode_body, callback=self.parse_project,meta={'gid':gid})
                        # 异常：使用lambda传参，会出现，gid 与响应的gid不一样， 暂不知道原因？

    def parse_project(self, response):
        data = json.loads(response.text)['result']['detail']['data']
        # if gid == 101415:
        #     print(data)
        gid = str(response.meta['gid'])
        try:
            good = data['good']
            project = ProjectItem()
            # gid = str(response.meta['gid'])
            project['original_id'] = gid
            project['project_name'] = good['name']
            project['project_price'] = int(good['market_price']) * 0.01
            project['project_url'] = 'https://youpin.mi.com/detail?gid='+gid
            project['project_desc'] = good['summary']
            project['project_picUrl'] = good['pic_url']
            project['project_platform'] = '小米有品'
            form = '{"overView":{"model":"Product","action":"CommentIndexV2","parameters":{"gid":%s}},"list":{"model":"Product","action":"CommentListOnly","parameters":{"index_type":0,"gid":%s,"pindex":1,"psize":10,"tag_name":null}}}' % (gid,gid)
            encode_body = 'data=' + urllib.parse.quote(form)

            # 注意这里处理参数传递的方式使用lambda传递 获取产品评分
            return FormRequest(url='https://youpin.mi.com/app/shopv3/pipe', method='POST', body=encode_body,callback=self.parse_comment,meta={'project':project})
        except KeyError : pass
        else:
            print("产品出现异常：==============", gid)
            # 商品已下架  100860   102626   101568

    def parse_comment(self,response):
        project = response.meta['project']
        project['project_score'] = json.loads(response.text)['result']['overView']['data']['positive_rate']
        return project
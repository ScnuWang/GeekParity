1. 你在这里看到的是Scrapy的跟踪链接机制：当你在回调方法中产生一个Request时，Scrapy会安排发送该请求并注册一个回调方法，以便在该请求完成时执行。

2. 由于历史原因，Scrapy保存数据到文交时，如果文件存在不会清除之前的数据，会直接连接在之前的数据后面直接添加

3. 调试：scrapy shell "URL地址" ，这里有点类似Django的shell工具

4. 如果是Ajax请求，那么通过response.body获取的结果里面是没有ajax请求的数据的

5. 获取response的返回结果时，使用response.text,使用response.body得到的结果会出现中文乱码

6. 由于数据库使用的是MongoDB，所以在定义item时候，要定义_id字段，否则会提示不支持_id字段

7. 向回调函数传参：通过request.meta['item'] = item 

8. 在整个解析过程中，只需要返回一次item，pipeline就能接收到，但是yield item之后，后续对item的操作将对pipeline无效

9. 给回调函数传参的两种方式：
    - meta['key'] = value,取值 response.meta['key']
    - callback = lambda response : self.callback_def(response,args)
    > lambda表达式，通常是在需要一个函数，但是又不想费神去命名一个函数的场合下使用，也就是指匿名函数。
    
    > Python允许你定义一种单行的小函数。定义lambda函数的形式如下（lambda参数：表达式）lambda函数默认返回表达式的值。你也可以将其赋值给一个变量。lambda函数可以接受任意个参数，包括可选参数，但是表达式只有一个。
    
10. 异常1： 使用lambda传参，会出现，gid 与响应结果数据的gid不一样， 暂不知道原因？

11. 异常2： pymongo.errors.AutoReconnect: localhost:27017: [WinError 10048] 通常每个套接字地址(协议/网络地址/端口)只允许使用一次。

12. 默认json.loads不能处理单引号的json字符串，可通过先json.loads(json.dumps(json_str))

13. 写一个装饰器，被装饰的函数捕捉KeyError异常，处理方式为pass或者打印异常项目信息

14. scrapy默认的抓取任务开始结束时间是采用的标准UTC时区的时间，可通过修改scrapy/extensions/corestats.py中的spider_opened和spider_closed方法设置本地时间，但是这样不太好，直接修改框架的源码了，没有可移植性。

15. 如果CrawlerProcess处理多个spider，某一个出现问题那就需要检查这个spider单独执行是否有问题

16. 入库之前给产品添加标签

17. 定时：scrapyd
18. 分布式：scrapy-redis

19. 时间处理，如果直接存放字符串到数据库，那么在Django应用中取出的时候过滤识别不出来是datatime类型
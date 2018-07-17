1. 你在这里看到的是Scrapy的跟踪链接机制：当你在回调方法中产生一个Request时，Scrapy会安排发送该请求并注册一个回调方法，以便在该请求完成时执行。

2. 由于历史原因，Scrapy保存数据到文交时，如果文件存在不会清除之前的数据，会直接连接在之前的数据后面直接添加

3. 调试：scrapy shell "URL地址" ，这里有点类似Django的shell工具

4. 如果是Ajax请求，那么通过response.body获取的结果里面是没有ajax请求的数据的

5. 获取response的返回结果时，使用response.text,使用response.body得到的结果会出现中文乱码

6. 由于数据库使用的是MongoDB，所以在定义item时候，要定义_id字段，否则会提示不支持_id字段
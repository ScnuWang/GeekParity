from scrapy.cmdline import execute

if __name__ == '__main__':
    # 命令单词之间要有空格
    # execute('scrapy crawl wangyi'.split())  # 等效于execute('scrapy,crawl,wangyi'.split(,))
    # 默认crawl 只能执行一个spider，源码crawl.py 第54行
    # execute('scrapy crawl xiaomi'.split())
    execute('scrapy crawlextend'.split())
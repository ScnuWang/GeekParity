from scrapy import cmdline


if __name__ == '__main__':
    cmdline.execute('scrapy crawl wangyi'.split())
    cmdline.execute('scrapy crawl xiaomi'.split())
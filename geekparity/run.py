import multiprocessing

from apscheduler.schedulers.blocking import BlockingScheduler
from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings
from geekparity.spiders.xiaomi_spider import XiaomiSpider
from geekparity.spiders.wangyi_spider import WangyiSpider

sched = BlockingScheduler()

def crawl():
    process = CrawlerProcess(get_project_settings())
    process.crawl(XiaomiSpider)
    process.crawl(WangyiSpider)
    process.start()

@sched.scheduled_job("interval",seconds=60*15)
def run():
    process = multiprocessing.Process(target=crawl)
    process.start()


if __name__ == '__main__':
    sched.start()



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
    # process.crawl(WangyiSpider)
    process.start()

# @sched.scheduled_job("interval",seconds=15*60)
@sched.scheduled_job("cron",hour='*/1')
# @sched.scheduled_job("cron",minute='*/3')
def run():
    process = multiprocessing.Process(target=crawl)
    process.start()


if __name__ == '__main__':
    sched.start()



from twisted.internet import reactor
from scrapy.crawler import CrawlerRunner
from scrapy.utils.log import configure_logging
from scrapy.utils.project import get_project_settings
from geekparity.spiders.xiaomi_spider import XiaomiSpider
from geekparity.spiders.wangyi_spider import WangyiSpider

from apscheduler.schedulers.twisted import TwistedScheduler

configure_logging({'LOG_FORMAT': '%(levelname)s: %(message)s'})

def crawlxiaomi():
    runner = CrawlerRunner(get_project_settings())
    runner.crawl(XiaomiSpider)
    runner.crawl(WangyiSpider)
    d = runner.join()
    d.addBoth(lambda _: reactor.stop())


if __name__ == '__main__':
    sched = TwistedScheduler()
    sched.add_job(crawlxiaomi,'cron',hour=17,minute=25)
    sched.start()

    try:
        reactor.run()
    except Exception:
        pass
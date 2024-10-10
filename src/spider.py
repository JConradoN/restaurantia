from scrapy.crawler import CrawlerProcess
from ifood_spider import IfoodSpider

def run_spider():
    process = CrawlerProcess(settings={
        'FEEDS': {
            'data/restaurants.json': {
                'format': 'json',
                'encoding': 'utf8',
                'store_empty': False,
                'indent': 4,
            },
        },
    })
    process.crawl(IfoodSpider)
    process.start()
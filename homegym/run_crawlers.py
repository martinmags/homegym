import scrapy
from scrapy.crawler import CrawlerProcess
from spiders.rogue_barbell_spider import RogueBarbellSpider

# Run spider
process = CrawlerProcess()
process.crawl(RogueBarbellSpider)
process.start()

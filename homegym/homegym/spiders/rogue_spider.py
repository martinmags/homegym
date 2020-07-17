import scrapy

# Daemon script to do continuous scheduled scraping, queue bots

# Split Scraping to barbell, bench, plates, racks/cages
class RogueSpider(scrapy.Spider):
  name = 'rogue'
  start_urls = ['']

  def parse(self, response):
    pass
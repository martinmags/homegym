# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy

class HomegymItem(scrapy.Item):
    name = scrapy.Field()
    photo = scrapy.Field()
    link = scrapy.Field()      
    brand = scrapy.Field()     
    price = scrapy.Field()
    category = scrapy.Field()  
    condition = scrapy.Field()
    available = scrapy.Field() 
    tags = scrapy.Field()      

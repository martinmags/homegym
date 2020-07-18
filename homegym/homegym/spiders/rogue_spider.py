import scrapy
import chompjs
from ..items import HomegymItem


# Daemon script to do continuous scheduled scraping, queue bots

# Split Scraping to barbell, bench, plates, racks/cages
class RogueSpider(scrapy.Spider):
  name = 'rogue'
  page_number = 1
  start_urls = ['https://www.roguefitness.com/weightlifting-bars-plates/barbells?p={}'.format(page_number)]

  def parse(self, response):
    # Extract All Barbell Data (name, availability, photo, price)
    all_barbells = response.css(".item")
    for barbell in all_barbells:
      product_link = barbell.css("div.product-image-cont a::attr(href)").get()
      product_details = {
        'product_name': barbell.css("div.product-image-cont a::attr(title)").get(),
        'product_photo': barbell.css("div.product-image-cont img::attr(src)").get(),
        'product_price': barbell.css("span.price::text").get(),
      }
      yield scrapy.Request(product_link, callback = self.parse_stock, meta={'product_details': product_details})
    
  
  def parse_stock(self, response):
    item = HomegymItem()
    product_details = response.meta['product_details']

    item['product_name'] = product_details['product_name']
    item['product_price'] = product_details['product_price']
    item['product_photo'] = product_details['product_photo']

    ### Parse the stock availability ###
    # Out of Stock"
    # "Notify Me"
    
    # # Process Data
    # javascript = response.css('script::text').get()[19]
    # data = chompjs.parse_js_object(javascript)
    # stock = data['attributes']['80']['options']

    # # Process ids
    # option_ids = []
    # for p in stock:
    #   option_ids.append(p['id'])

    # # Extract stock status
    # for p, id in zip(stock, option_ids):
    #   print(p['additional_options'][id]['isInStock'])


    yield item
    


    # item['product_title'] = product_title
    # item['product_price'] = product_price
    # yield item
    # barbell_names
    # barbell_avails
    # barbell_photos
    # barbell_prices


    
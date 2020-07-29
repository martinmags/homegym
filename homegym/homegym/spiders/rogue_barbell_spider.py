import scrapy
from ..items import HomegymItem
# TODO: Daemon script to do continuous scheduled scraping, queue bots
# TODO: Create django RESTful API endpoints for barbell, plate, rack, bench, accessory, bell 

# TODO: Create RoguePlateSpider
# TODO: Create RogueRackSpider
# TODO: Create RogueBenchSpider
# TODO: Create RogueAccessorySpider
# TODO: Create RogueBellSpider (Kettlebells, dumbbells)

# TODO: [LOW PRIO] Append tags to item['tags']

# Split Scraping to barbell, bench, plates, racks/cages
class RogueBarbellSpider(scrapy.Spider):
  name = 'rogue_barbell'
  page_number = 1
  start_urls = ['https://www.roguefitness.com/weightlifting-bars-plates/barbells?p={}'.format(page_number)]

  def parse(self, response):
    # Extract links
    all_barbells = response.css(".item")
    for barbell in all_barbells:
      name = barbell.css("div.product-image-cont a::attr(title)").get().strip()
      if 'Bar' in name:
        details = {
          'name': name,
          'photo': barbell.css("div.product-image-cont img::attr(src)").get(),
          'link' : barbell.css("div.product-image-cont a::attr(href)").get(),
          'price': barbell.css("span.price::text").get().strip(),
          'category': 'Barbell',
          'condition': 'Retail'
        }
        yield scrapy.Request(details['link'], callback = self.parse_stock, meta={'details': details})
    
    if RogueBarbellSpider.page_number <= 3:
      RogueBarbellSpider.page_number += 1
      next_page = 'https://www.roguefitness.com/weightlifting-bars-plates/barbells?p={}'.format(RogueBarbellSpider.page_number)
      yield response.follow(next_page, callback = self.parse)
    
    # Deals [Boneyard Bars, Grab Bag Bars, etc.]
    next_page = 'https://www.roguefitness.com/deals#deal_type[]=rogue_boneyard&cat[]=4667&order=position-asc&p=1&limit=40'
    yield response.follow(next_page, callback = self.parse)
    
  
  def parse_stock(self, response):
    item = HomegymItem()
    details = response.meta['details']
    variants = response.css('.grouped-item')
    # Set brand
    if '</a>' in response.css(".data-table tr td").get():
      brand = response.css(".data-table tr td a::text").get().strip()
    else:
      brand = response.css(".data-table tr td::text").get().strip()
    
    if variants:
      for variant in variants:
        # Set name
        if variants.css(".item-name::text").get():
          item['name'] = variant.css(".item-name::text").get().strip()
        else:
          item['name'] = details['name']
        item['photo'] = details['photo']
        item['link'] = details['link']
        item['brand'] = brand,
        item['price'] = variant.css(".price::text").get().strip()
        item['category'] = details['category']
        item['condition'] = details['condition']
        item['available'] = variant.css(".item-qty").get() is not None
        yield item
    else:
      item['name']  = details['name']
      item['photo'] = details['photo']
      item['link'] = details['link']
      item['brand'] = brand
      item['price'] = details['price']
      item['category'] = details['category']
      item['condition'] = details['condition']
      item['available'] = response.css("#qty").get() is not None
      yield item


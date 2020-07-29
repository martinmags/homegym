# homegym

A web app that tracks websites to help you get the best deals on your home gym equipment. 

### Dev Prerequisites

Install all dependencies
```
pip install -r requirements.txt
```

### Dev Commands

Enter virtual environment
```
source venv/bin/activate
```

Run Scrapy program in ./homegym/homegym
```
scrapy crawl rogue 
```

Output scrapy program into a json
```
scrapy crawl rogue -o test.json
```

# Features

- [] User will be able to search a product by name and see a list of products in-stock on the retail market
  - [] RogueFitness
  - [] RepFitness
  - [] FringeSports
  - [] TitanFitness
  - [] AmericanBarbell
- [] User will be able to search a product by name and see a list of products in-stock on the used market
  - [] FB Marketplace
  - [] Letgo
  - [] Ebay
  - [] OfferUp
- [] Users will be able to setup alerts to products to receive emails or browser notifications.
- [] Users will be able to sort search results by the following:
  - [] Category type (barbell, bench, cage/rack, accessories, etc.)
  - [] Lowest Price
  - [] In-stock
- [] Users will be able to filter search results by the following:
  - [] Price Range
  - [] Brand
  - [] Used or Retail
- [] Users will be able to see a restock graph and see predicted restock dates based on historical data.

# Technology

* Database: Undecided
* Web Framework: Flask
* Front End: HTML, CSS, JS
* Javascript
* scrapy
* ...

# DB Schema
BARBELL, PLATE, RACK, BENCH, BELL, ACCESSORY{
  id          SMALLSERIAL
  name        TEXT
  photo       TEXT
  link        TEXT  
  brand       TEXT  
  price       MONEY
  category    TEXT
  condition   TEXT
  available   BOOLEAN
  tags        TEXT[]  
  updated_at  TIMESTAMPTZ 
}
## Authors

* Software-Developer: **Martin Magsombol**
* Product-Designer: **Martha Magsombol**

## License

TODO




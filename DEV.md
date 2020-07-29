# Developer Documentation

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

### DB Schema

```
BARBELL, PLATE, RACK, BENCH, BELL, ACCESSORY{
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
```

### Architecture

RESTful Backend
```
-> [Scrapy] Scrape data
-> [Scrapy] Item Containers  
-> [Scrapy] Pipeline
-> [PostgreSQL] Persistant data
-> [Django RESTful] Expose JSON data at endpoints
```

Clientside 
```
-> [Fetch/Axios] Fetch API endpoints
-> [HTML/CSS/JS] Display data
```
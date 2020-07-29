### GOAL:
  Install psycopg2 (python sdk for postgresql)
### ACTION:
  pip install psycopg2
### ISSUE:
  ERROR: Command errored out with exit status 1:
  ...
  ld: library not found for -lssl
  clang: error: linker command failed with exit code 1 (use -v to see invocation)
  error: command 'xcrun' failed with exit status 1
### SOLUTION:
  run 'pip install psycopg2-binary' instead
### REFERENCE:
  (?) https://stackoverflow.com/questions/58660146/error-installing-psycopg2-python-3-7-on-macos-10-15

### VERSIONS:
  Python 3.7.3
  psycopg2-binary==2.8.5
### GOAL:
  Trying to insert scraped data from scrapy item into postgresql table
### ACTION:
  (1) curr.execute("""INSERT INTO table (col1) VALUES (?)""", (item['val1']))
  (also tried...)
  (2) curr.execute("""INSERT INTO table (col1) VALUES (%s)""", (item['val1]))
### ISSUE:
  (1) ERROR: syntax error at or near ")" LINE 1: INSERT INTO table (col1) VALUES (?);
  (2) TypeError: not all arguments converted during string formatting
### SOLUTION:
  Need to use a tuple and %s syntax instead
  entry = (item['val1], )
  curr.execute("""INSERT INTO table (col1, col2) VALUES (%s)""", (entry))
### REFERENCE:
  https://stackoverflow.com/questions/21524482/psycopg2-typeerror-not-all-arguments-converted-during-string-formatting


### VERSIONS:
  Python 3.7.3
  psycopg2-binary==2.8.5
### GOAL:
  Handle duplicates from scraper data;
  Only update timestamp and available columns in table whenever a duplicate is seen
### ACTION:
  self.conn.rollback()
### ISSUE:
  It prevented errors, but it does not update timestamp and available columns in table whenever a duplicate is seen
### SOLUTION:
  entry = (item['name'], item['photo'], item['link'], item['brand'], item['price'], item['category'], item['condition'], item['available'], item['available'], datetime.now())
  self.curr.execute("""
    INSERT INTO barbell (name, photo, link, brand, price, category, condition, available) 
    VALUES (%s,%s,%s,%s,%s,%s,%s,%s)
    ON CONFLICT (name)
    DO UPDATE SET (available, updated_at) = (%s,%s);
    """, (entry)
### REFERENCE:
  Upsert Psycopg2 Single Update Issue: https://github.com/mozilla/http-observatory/issues/298
  Upsert: https://www.postgresql.org/docs/9.5/sql-insert.html
  Upsert EX: https://wiki.postgresql.org/wiki/What%27s_new_in_PostgreSQL_9.5#INSERT_..._ON_CONFLICT_DO_NOTHING.2FUPDATE_.28.22UPSERT.22.29
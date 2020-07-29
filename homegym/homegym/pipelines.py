# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import psycopg2
from datetime import datetime

class HomegymPipeline:
  def __init__(self):
    # Initialize Connection
    self.conn = psycopg2.connect(
      host = "localhost",
      port = 5432,
      dbname = "homegym",
      user = "postgres",
      password = "0neS0y!"
    )

    # Create Cursor
    self.curr = self.conn.cursor()
    self.create_tables()

  def create_tables(self):
    ### Create tables
    # Create barbell table
    # Create plate table
    # Create rack table
    # Create bench table
    # Create accessory table
    # Create bell table
    try:
      self.curr.execute("""
        CREATE TABLE IF NOT EXISTS barbell(
          name        TEXT NOT NULL,
          photo       TEXT NOT NULL,
          link        TEXT NOT NULL,
          brand       TEXT NOT NULL,
          price       MONEY NOT NULL,
          category    TEXT NOT NULL,
          condition   TEXT NOT NULL,
          available   BOOLEAN NOT NULL,
          tags        TEXT[],
          updated_at  TIMESTAMPTZ NOT NULL DEFAULT NOW(),
          PRIMARY KEY(name)
        );
      """)
      self.conn.commit()
    except psycopg2.Error as e:
      print("ERROR:", e)

  def process_item(self, item, spider):
    # Add/Update barbell in table
    try:
      entry = (item['name'], item['photo'], item['link'], item['brand'], item['price'], item['category'], item['condition'], item['available'], item['available'], datetime.now())
      self.curr.execute("""
        INSERT INTO barbell (name, photo, link, brand, price, category, condition, available) 
        VALUES (%s,%s,%s,%s,%s,%s,%s,%s)
        ON CONFLICT (name)
        DO UPDATE SET (available, updated_at) = (%s,%s);
        """, (entry)
      )
      self.conn.commit()
    except psycopg2.Error as e:
      print("ERROR:", e)

    return item

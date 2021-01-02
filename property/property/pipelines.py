# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter

from sqlalchemy.orm import sessionmaker
from .models import Items, db_connect, create_items_table

class PropertyPipeline:
    def __init__(self):
        engine = db_connect()
        create_items_table(engine)
        self.Session = sessionmaker(bind=engine)

    # def process_item(self, item, spider):
    #     return item
    
    def process_item(self, item, spider):
        session = self.Session()
        item = Items(**item)

        try:
            session.add(item)
            session.commit()
        except:
            session.rollback()
            raise
        finally:
            session.close()

        return item

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class PropertyItem(scrapy.Item):
    title = scrapy.Field()
    link = scrapy.Field()
    price = scrapy.Field()
    address = scrapy.Field()
    code = scrapy.Field()
    location = scrapy.Field()
    operation = scrapy.Field()
    _type = scrapy.Field()
    date = scrapy.Field()
    thumb = scrapy.Field()
    

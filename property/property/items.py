# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class PropertyItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    title = scrapy.Field()
    link = scrapy.Field()
    address = scrapy.Field()
    code = scrapy.Field()
    profile = scrapy.Field()
    date = scrapy.Field()
    price = scrapy.Field()

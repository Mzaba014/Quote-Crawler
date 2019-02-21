# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class Item(scrapy.Item):
    author = scrapy.Field()
    text = scrapy.Field()
    tags = scrapy.Field()
    last_updated = scrapy.Field(serializer=str)

    # name = scrapy.Field()

# -*- coding: utf-8 -*-
"Honestbee.ph item data design"

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class HonestbeeItem(scrapy.Item):
    "Honestbee.ph item class"
    # define the fields for your item here like:
    # name = scrapy.Field()
    cat = scrapy.Field()
    subcat = scrapy.Field()
    url = scrapy.Field()
    imgsrc = scrapy.Field()
    pricesave = scrapy.Field()
    price = scrapy.Field()
    title = scrapy.Field()
    desc = scrapy.Field()

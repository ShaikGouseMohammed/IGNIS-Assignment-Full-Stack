import scrapy

class NoberoItem(scrapy.Item):
    category = scrapy.Field()
    title = scrapy.Field()
    price = scrapy.Field()
    MRP = scrapy.Field()
    available_skus = scrapy.Field()
    fit = scrapy.Field()
    fabric = scrapy.Field()
    neck = scrapy.Field()
    sleeve = scrapy.Field()
    pattern = scrapy.Field()
    length = scrapy.Field()
    description = scrapy.Field()

    pass

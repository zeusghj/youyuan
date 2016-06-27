# -*- coding: utf-8 -*-


from scrapy import Item, Field

class YouyuanItem(Item):
    uid     = Field()
    url     = Field()
    name    = Field()
    age     = Field()
    address = Field()
    xueli   = Field()
    xinzi   = Field()

    #详细信息 url
    detailUrl = Field()


class UserDetailItem(Item):
    uid       = Field()
    
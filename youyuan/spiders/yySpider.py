#!/usr/env/python
# -*- coding:utf-8 -*-

from scrapy import Spider
from youyuan.items import YouyuanItem
from scrapy.selector import Selector

class yySpider(Spider):
    name = "yySpider"
    allowed_domains = ["youyuan.com"]
    start_urls = ["http://www.youyuan.com/find/beijing/mm18-18/advance-0-0-0-0-0-0-0/p1/",
                  "http://www.youyuan.com/find/beijing/mm18-18/advance-0-0-0-0-0-0-0/p2/",
                  "http://www.youyuan.com/find/beijing/mm18-18/advance-0-0-0-0-0-0-0/p3/",
                  "http://www.youyuan.com/find/beijing/mm18-18/advance-0-0-0-0-0-0-0/p4/",
                  "http://www.youyuan.com/find/beijing/mm18-18/advance-0-0-0-0-0-0-0/p5/"
                  ]

    def parse(self, response):

        print response.url

        items = []

        liResults = Selector(response).xpath('//ul[@class="mian search_list"]/li/dl/dd')

        for li in liResults:
            item = YouyuanItem()

            other          = (li.xpath('.//font/text()').extract())
            ageandaddress  = other[0].strip()
            xueliandxinzi  = other[1].strip()
            item['name']   = (li.xpath('.//a[@target="_blank"]/strong/text()').extract())[0]
            item['url']    = (li.xpath('.//a[@class="sayHiBtnP hello"]/@data_usericon').extract())[0]
            item['uid']    = (li.xpath('.//a[@class="sayHiBtnP hello"]/@data_userid').extract())[0]
            item['age']    = (ageandaddress.split('|')[0]).strip()
            item['address']= (ageandaddress.split('|')[1]).strip()
            item['xueli']  = (xueliandxinzi.split('|')[0]).strip()
            item['xinzi']  = (xueliandxinzi.split('|')[1]).strip()
            item['detailUrl'] = 'http://www.youyuan.com' + (li.xpath('.//a[@target="_blank"]/@href').extract())[0]

            items.append(item)

            yield item
        # return items
        # for x in range(0, items.__len__()):
        #     items[x] = str(items[x])
        # strdata = ''
        #
        # strdata = strdata.join(items)
        # print strdata
        #
        # data = open('youyuandata', 'wb')
        # data.write(strdata)
        # data.close()



#!/usr/env/python
# -*- coding:utf-8 -*-

from scrapy import Spider
from youyuan.items import YouyuanItem, UserDetailItem
from scrapy.selector import Selector
from scrapy import Request
import re

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

        dest = response.url.split("/")[3]

        if dest == "find":

            items = []

            liResults = Selector(response).xpath('//ul[@class="mian search_list"]/li/dl/dd')

            for li in liResults:
                item = YouyuanItem()

                other          = (li.xpath('.//font/text()').extract())
                ageandaddress  = other[0].strip()
                xueliandxinzi  = other[1].strip()
                item['nickame']   = (li.xpath('.//a[@target="_blank"]/strong/text()').extract())[0]
                item['url']    = (li.xpath('.//a[@class="sayHiBtnP hello"]/@data_usericon').extract())[0]
                item['uid']    = (li.xpath('.//a[@class="sayHiBtnP hello"]/@data_userid').extract())[0]
                item['age']    = (ageandaddress.split('|')[0]).strip()
                item['address']= (ageandaddress.split('|')[1]).strip()
                item['xueli']  = (xueliandxinzi.split('|')[0]).strip()
                item['xinzi']  = (xueliandxinzi.split('|')[1]).strip()
                item['detailUrl'] = 'http://www.youyuan.com' + (li.xpath('.//a[@target="_blank"]/@href').extract())[0]

                items.append(item)

                yield Request(item['detailUrl'], callback=self.parse)

        else:

            item = UserDetailItem()

            item['uid'] = (Selector(response).xpath('/html/body/div[2]/div/dl/dd/div[2]/a[1]/@data_userid').extract())[0]
            item['url'] = (Selector(response).xpath('//dl[@class="personal_cen"]/dt/img/@src').extract())[0]
            item['nickame'] = (Selector(response).xpath('//dl[@class="personal_cen"]/dd/div/strong/text()').extract())[0]

            ageandcity = (Selector(response).xpath('//dl[@class="personal_cen"]/dd/p/text()').extract())[0]
            acs = re.split("\s+", ageandcity)
            item['age'] = acs[1]
            item['address'] = acs[0]

            tags = []
            hobys = (Selector(response).xpath('//ol[@class="hoby"]/li'))
            for hoby in hobys:
                tag = ((hoby.xpath('./text()').extract())[0]).strip()
                tags.append(tag)
            item['tags'] = tags

            #图片展示
            photos = []
            photosUrl = Selector(response).xpath('//*[@id="photo"]/div/ul/li[@class="smallPhoto"]')
            for pto in photosUrl:
                ptoUrl = (pto.xpath('./@data_url_full').extract())[0]
                photos.append(ptoUrl);
            item['smallPhotos'] = photos

            #内心独白
            item['dubai'] = ((Selector(response).xpath('/html/body/div[@class="pre_data"]/ul[@class="requre"]/li[1]/p/text()').extract())[0]).strip()

            #详细资料
            olMessages1 = Selector(response).xpath('/html/body/div[4]/ul/li[2]/div/ol[1]')
            item['jiguan']  = (olMessages1.xpath('./li[1]/span/text()').extract())[0]
            item['weight']  = (olMessages1.xpath('./li[2]/span/text()').extract())[0]
            item['xueli']   = (olMessages1.xpath('./li[3]/span/text()').extract())[0]
            item['xinzi']   = (olMessages1.xpath('./li[4]/span/text()').extract())[0]
            item['getBaby'] = (olMessages1.xpath('./li[5]/span/text()').extract())[0]
            item['sexType'] = (olMessages1.xpath('./li[6]/span/text()').extract())[0]
            item['tongju']  = (olMessages1.xpath('./li[7]/span/text()').extract())[0]

            olMessages2 = Selector(response).xpath('/html/body/div[4]/ul/li[2]/div/ol[2]')
            item['marriage']  = (olMessages2.xpath('./li[1]/span/text()').extract())[0]
            item['height']  = (olMessages2.xpath('./li[2]/span/text()').extract())[0]
            item['work'] = (olMessages2.xpath('./li[3]/span/text()').extract())[0]
            item['house'] = (olMessages2.xpath('./li[4]/span/text()').extract())[0]
            item['yidiLove']  = (olMessages2.xpath('./li[5]/span/text()').extract())[0]
            item['foreSex'] = (olMessages2.xpath('./li[6]/span/text()').extract())[0]
            item['meili']  = (olMessages2.xpath('./li[7]/span/text()').extract())[0]

            #征友条件
            olCondition1 = Selector(response).xpath('/html/body/div[4]/ul/li[3]/div/ol[1]')
            item['op_city']  = (olCondition1.xpath('./li[1]/span/text()').extract())[0]
            item['op_height']  = ((olCondition1.xpath('./li[2]/span/text()').extract())[0]).strip().replace(' ','')
            item['op_income'] = ((olCondition1.xpath('./li[3]/span/text()').extract())[0]).strip()

            olCondition2 = Selector(response).xpath('/html/body/div[4]/ul/li[3]/div/ol[2]')
            item['op_age']  = ((olCondition2.xpath('./li[1]/span/text()').extract())[0]).strip().replace(' ','')
            item['op_xueli']  = ((olCondition2.xpath('./li[2]/span/text()').extract())[0]).strip()

            yield item




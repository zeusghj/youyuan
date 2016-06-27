# -*- coding: utf-8 -*-

# Scrapy settings for youyuan project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#     http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html
#     http://scrapy.readthedocs.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'youyuan'

SPIDER_MODULES = ['youyuan.spiders']
NEWSPIDER_MODULE = 'youyuan.spiders'

MONGODB_SERVER = "localhost"
MONGODB_PORT = 27017
MONGODB_DB = "youyuan"
MONGODB_COLLECTION = "user"


ITEM_PIPELINES = {
   'youyuan.pipelines.YouyuanPipeline': 1,
}

DOWNLOAD_DELAY = 1
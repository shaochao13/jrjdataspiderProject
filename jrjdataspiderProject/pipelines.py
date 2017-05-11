# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

import pymongo
from scrapy.conf import settings
from .checkpipeline import check_spider_pipeline


class JrjdataspiderprojectPipeline(object):

    def __init__(self):

        connection = pymongo.MongoClient(host=settings['MONGODB_SERVER'],port=settings['MONGODB_PORT'])
        db = connection[settings['MONGODB_DB']]
        self.connection = db[settings['MONGODB_COLLECTION']]

    def open_spider(self, spider):
        print('open')

    def close_spider(self, spider):
        print('close')

    @check_spider_pipeline
    def process_item(self, item, spider):
        if len(item['items']) > 0:
            for i in item['items']:
                self.connection.insert(dict(i))
        return item

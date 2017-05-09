# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html


class JrjdataspiderprojectPipeline(object):

    def open_spider(self, spider):
        print('open')

    def close_spider(self, spider):
        print('close')

    def process_item(self, item, spider):
        print('+'*10)
        # print(item)
        return item

# -*- coding: utf-8 -*-

from scrapy.exceptions import DropItem
import functools

def check_spider_pipeline(process_item):
    @functools.wraps(process_item)
    def wrapper(self, item, spider):

        if self.__class__.__name__ in spider.pipeline:
            print("OK")
            print(item,spider)
            return process_item(self, item, spider)

    return wrapper
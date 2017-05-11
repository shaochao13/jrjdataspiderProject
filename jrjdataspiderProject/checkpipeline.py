# -*- coding: utf-8 -*-

from scrapy.exceptions import DropItem
import functools

def check_spider_pipeline(process_item_method):
    @functools.wraps(process_item_method)
    def wrapper(self, item, spider):

        if self.__class__.__name__ in spider.pipeline:
            print("OK")
            return process_item_method(self, item, spider)

    return wrapper
# -*- coding: utf-8 -*-

import scrapy
import re
import json
from jrjdataspiderProject.items import CityItem


class CityspiderSpider(scrapy.Spider):
    """跑一次就OK。"""

    pipeline = ['CityDataSpiderPipeline',]
    name = "citySpider"
    allowed_domains = ["jrj.com.cn"]
    start_urls = ['http://bankpro.jrj.com.cn/inc/city.js']

    def parse(self, response):

        return CityItem()


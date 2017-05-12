# -*- coding: utf-8 -*-
import scrapy
from jrjdataspiderProject.items import BankItem


class BankinfospiderSpider(scrapy.Spider):
    """用于获取银行列表数据"""
    pipeline = ['BankinfoPipeline']
    name = "bankinfoSpider"
    allowed_domains = ["jrj.com.cn"]
    start_urls = ['http://bankpro.jrj.com.cn/data.shtml']

    def parse(self, response):
        spans = response.xpath('//div[@id="yhmc_id"]/span')
        # items = []
        for span in spans:
            item = BankItem()
            item['_id'] = span.xpath("@data-value").extract_first()
            content_title = span.xpath("b/@title").extract_first()
            if len(content_title) == 0:
                content_title = span.xpath("b/text()").extract_first()
            content_title = content_title if len(content_title) > 0 else ""
            item['bankName'] = content_title
            yield item


# -*- coding: utf-8 -*-
import scrapy
from scrapy.http import Request
from jrjdataspiderProject.items import JrjdataspiderprojectItem,JrjdataspiderprojectItems
import re
import json

class BankproSpider(scrapy.Spider):
    name = "bankpro"
    allowed_domains = ["jrj.com.cn"]
    start_urls = ['http://bankpro.jrj.com.cn/json/f.jspa?size=50&pn=1&t={"st":"0","xsdq":"-1,-1","sort":"sell_org_date","order":"desc","wd":""}']

    def parse(self, response):
        body = response.body
        pat = r'var bps=(.*)'
        regex = re.compile(pat)
        rtn = regex.findall(body)[0]
        ob = json.loads(rtn)
        status = ob.get(u'success', False)
        if status == True:
            page_count = ob.get(u'page').get(u'pc')
            self.page_count = int(page_count)

        if self.page_count > 0:
            for i in range(1, self.page_count + 1):
                url = u'http://bankpro.jrj.com.cn/json/f.jspa?size=50&pn='+ str(i) +'&t={"st":"0","xsdq":"-1,-1","sort":"sell_org_date","order":"desc","wd":""}';
                yield Request(url=url, callback=self.nextParse)


    def nextParse(self, response):
        body = response.body
        pat = r'var bps=(.*)'
        regex = re.compile(pat)
        rtn = regex.findall(body)[0]
        ob = json.loads(rtn)
        status = ob.get(u'success', False)
        if status == True:
            bankProductList = ob.get(u'bankProductList', [])
            items = JrjdataspiderprojectItems()
            items['items'] = []
            if len(bankProductList) > 0:
                for im in bankProductList:
                    item = JrjdataspiderprojectItem()
                    item['bank_Id'] = im.get(u'bank_Id', None)
                    item['bank_Name'] = im.get(u'bank_Name', None)
                    item['days'] = im.get(u'days', None)
                    item['end_Date'] = im.get(u'end_Date', None)
                    item['entr_Curncy_Name'] = im.get(u'entr_Curncy_Name', None)
                    item['entr_Curncy_Type'] = im.get(u'entr_Curncy_Type', None)
                    item['entr_Min_Curncy'] = im.get(u'entr_Min_Curncy', None)
                    item['inc_Score'] = im.get(u'inc_Score', None)
                    item['inner_Code'] = im.get(u'inner_Code', None)
                    item['liq_Score'] = im.get(u'liq_Score', None)
                    item['mat_Actu_Yld'] = im.get(u'mat_Actu_Yld', None)
                    item['months'] = im.get(u'months', None)
                    item['multiple'] = im.get(u'multiple', None)
                    item['prd_Max_Yld'] = im.get(u'prd_Max_Yld', None)
                    item['prd_Max_Yld_De'] = im.get(u'prd_Max_Yld_De', None)
                    item['prd_Sname'] = im.get(u'prd_Sname', None)
                    item['prd_Type'] = im.get(u'prd_Type', None)
                    item['rist_Score'] = im.get(u'rist_Score', None)
                    item['sell_End_Date'] = im.get(u'sell_End_Date', None)
                    item['sell_Org_Date'] = im.get(u'sell_Org_Date', None)
                    item['star'] = im.get(u'star', None)
                    item['state'] = im.get(u'state', None)
                    item['stk_Score'] = im.get(u'stk_Score', None)
                    item['row'] = im.get(u'row', None)
                    items['items'].append(item)
            yield items



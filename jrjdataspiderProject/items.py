# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy

class JrjdataspiderprojectItems(scrapy.Item):
    items = scrapy.Field()

class JrjdataspiderprojectItem(scrapy.Item):
    bank_Id = scrapy.Field()
    bank_Name = scrapy.Field()
    days = scrapy.Field()
    end_Date = scrapy.Field()
    entr_Curncy_Name = scrapy.Field()
    entr_Curncy_Type = scrapy.Field()
    entr_Min_Curncy = scrapy.Field()
    inc_Score = scrapy.Field()
    inner_Code = scrapy.Field()
    liq_Score = scrapy.Field()
    mat_Actu_Yld = scrapy.Field()
    months = scrapy.Field()
    multiple = scrapy.Field()
    prd_Max_Yld = scrapy.Field()
    prd_Max_Yld_De = scrapy.Field()
    prd_Sname = scrapy.Field()
    prd_Type = scrapy.Field()
    rist_Score = scrapy.Field()
    sell_End_Date = scrapy.Field()
    sell_Org_Date = scrapy.Field()
    star = scrapy.Field()
    state = scrapy.Field()
    stk_Score = scrapy.Field()
    row = scrapy.Field()





# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy

class JrjdataspiderprojectItems(scrapy.Item):
    items = scrapy.Field()

class JrjdataspiderprojectItem(scrapy.Item):
    bank_Id = scrapy.Field() #银行ID
    bank_Name = scrapy.Field() #银行名称
    days = scrapy.Field() #管理期(天)
    end_Date = scrapy.Field()
    entr_Curncy_Name = scrapy.Field() #委托货币
    entr_Curncy_Type = scrapy.Field()
    entr_Min_Curncy = scrapy.Field()
    inc_Score = scrapy.Field()
    inner_Code = scrapy.Field() # 产品ID
    liq_Score = scrapy.Field()
    mat_Actu_Yld = scrapy.Field()  #到期收益率
    months = scrapy.Field()
    multiple = scrapy.Field() #与同期储蓄比
    prd_Max_Yld = scrapy.Field()
    prd_Max_Yld_De = scrapy.Field() #预期收益率
    prd_Sname = scrapy.Field() #产品名称
    prd_Type = scrapy.Field()
    rist_Score = scrapy.Field()
    sell_End_Date = scrapy.Field() #停售日
    sell_Org_Date = scrapy.Field() #发行日
    star = scrapy.Field()
    state = scrapy.Field() #产品状态(0-在售，1-预售，2-停售)
    stk_Score = scrapy.Field() #综合评分
    row = scrapy.Field()

class CityItem(scrapy.Item):
    prov_Name = scrapy.Field()
    city_Name = scrapy.Field()
    prov_Id = scrapy.Field()
    city_Id = scrapy.Field()


class BankItem(scrapy.Item):
    _id = scrapy.Field()
    bankName = scrapy.Field()





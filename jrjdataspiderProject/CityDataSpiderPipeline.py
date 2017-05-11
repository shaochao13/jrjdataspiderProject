# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

import pymongo
from scrapy.conf import settings
from .checkpipeline import check_spider_pipeline
import json


class CityDataSpiderPipeline(object):

    def __init__(self):

        connection = pymongo.MongoClient(host=settings['MONGODB_SERVER'],port=settings['MONGODB_PORT'])
        db = connection[settings['MONGODB_DB']]
        self.connection = db[settings['CITYDATA_COLLECTION']]

    def open_spider(self, spider):
        print('open')

    def close_spider(self, spider):
        print('close')

    @check_spider_pipeline
    def process_item(self, item, spider):
        print("CityDataSpiderPipeline")
        txt = '''[
{"prov_Name":"安徽省","city_Name":"安庆市","prov_Id":"34","city_Id":"08"}
,{"prov_Name":"安徽省","city_Name":"马鞍山市","prov_Id":"34","city_Id":"05"}
,{"prov_Name":"安徽省","city_Name":"合肥市","prov_Id":"34","city_Id":"01"}
,{"prov_Name":"安徽省","city_Name":"安徽省","prov_Id":"34","city_Id":"00"}
,{"prov_Name":"安徽省","city_Name":"淮南市","prov_Id":"34","city_Id":"04"}
,{"prov_Name":"安徽省","city_Name":"淮北市","prov_Id":"34","city_Id":"06"}
,{"prov_Name":"安徽省","city_Name":"六安市","prov_Id":"34","city_Id":"15"}
,{"prov_Name":"安徽省","city_Name":"滁州市","prov_Id":"34","city_Id":"11"}
,{"prov_Name":"安徽省","city_Name":"亳州市","prov_Id":"34","city_Id":"16"}
,{"prov_Name":"安徽省","city_Name":"芜湖市","prov_Id":"34","city_Id":"02"}
,{"prov_Name":"安徽省","city_Name":"阜阳市","prov_Id":"34","city_Id":"12"}
,{"prov_Name":"北京市","city_Name":"北京市","prov_Id":"11","city_Id":"00"}
,{"prov_Name":"北京市","city_Name":"市辖区","prov_Id":"11","city_Id":"01"}
,{"prov_Name":"福建省","city_Name":"莆田市","prov_Id":"35","city_Id":"03"}
,{"prov_Name":"福建省","city_Name":"龙岩市","prov_Id":"35","city_Id":"08"}
,{"prov_Name":"福建省","city_Name":"南平市","prov_Id":"35","city_Id":"07"}
,{"prov_Name":"福建省","city_Name":"宁德市","prov_Id":"35","city_Id":"09"}
,{"prov_Name":"福建省","city_Name":"三明市","prov_Id":"35","city_Id":"04"}
,{"prov_Name":"福建省","city_Name":"福建省","prov_Id":"35","city_Id":"00"}
,{"prov_Name":"福建省","city_Name":"厦门市","prov_Id":"35","city_Id":"02"}
,{"prov_Name":"福建省","city_Name":"漳州市","prov_Id":"35","city_Id":"06"}
,{"prov_Name":"福建省","city_Name":"福州市","prov_Id":"35","city_Id":"01"}
,{"prov_Name":"福建省","city_Name":"泉州市","prov_Id":"35","city_Id":"05"}
,{"prov_Name":"甘肃省","city_Name":"天水市","prov_Id":"62","city_Id":"05"}
,{"prov_Name":"甘肃省","city_Name":"甘肃省","prov_Id":"62","city_Id":"00"}
,{"prov_Name":"甘肃省","city_Name":"嘉峪关市","prov_Id":"62","city_Id":"02"}
,{"prov_Name":"甘肃省","city_Name":"兰州市","prov_Id":"62","city_Id":"01"}
,{"prov_Name":"广东省","city_Name":"揭阳市","prov_Id":"44","city_Id":"52"}
,{"prov_Name":"广东省","city_Name":"广州市","prov_Id":"44","city_Id":"01"}
,{"prov_Name":"广东省","city_Name":"肇庆市","prov_Id":"44","city_Id":"12"}
,{"prov_Name":"广东省","city_Name":"梅州市","prov_Id":"44","city_Id":"14"}
,{"prov_Name":"广东省","city_Name":"深圳市","prov_Id":"44","city_Id":"03"}
,{"prov_Name":"广东省","city_Name":"韶关市","prov_Id":"44","city_Id":"02"}
,{"prov_Name":"广东省","city_Name":"中山市","prov_Id":"44","city_Id":"20"}
,{"prov_Name":"广东省","city_Name":"广东省","prov_Id":"44","city_Id":"00"}
,{"prov_Name":"广东省","city_Name":"惠州市","prov_Id":"44","city_Id":"13"}
,{"prov_Name":"广东省","city_Name":"东莞市","prov_Id":"44","city_Id":"19"}
,{"prov_Name":"广东省","city_Name":"珠海市","prov_Id":"44","city_Id":"04"}
,{"prov_Name":"广东省","city_Name":"江门市","prov_Id":"44","city_Id":"07"}
,{"prov_Name":"广东省","city_Name":"清远市","prov_Id":"44","city_Id":"18"}
,{"prov_Name":"广东省","city_Name":"汕头市","prov_Id":"44","city_Id":"05"}
,{"prov_Name":"广东省","city_Name":"湛江市","prov_Id":"44","city_Id":"08"}
,{"prov_Name":"广东省","city_Name":"佛山市","prov_Id":"44","city_Id":"06"}
,{"prov_Name":"广西壮族自治区","city_Name":"南宁市","prov_Id":"45","city_Id":"01"}
,{"prov_Name":"广西壮族自治区","city_Name":"柳州市","prov_Id":"45","city_Id":"02"}
,{"prov_Name":"广西壮族自治区","city_Name":"桂林市","prov_Id":"45","city_Id":"03"}
,{"prov_Name":"广西壮族自治区","city_Name":"广西壮族自治区","prov_Id":"45","city_Id":"00"}
,{"prov_Name":"贵州省","city_Name":"遵义市","prov_Id":"52","city_Id":"03"}
,{"prov_Name":"贵州省","city_Name":"贵州省","prov_Id":"52","city_Id":"00"}
,{"prov_Name":"贵州省","city_Name":"贵阳市","prov_Id":"52","city_Id":"01"}
,{"prov_Name":"海南省","city_Name":"海南省","prov_Id":"46","city_Id":"00"}
,{"prov_Name":"海南省","city_Name":"海口市","prov_Id":"46","city_Id":"01"}
,{"prov_Name":"河北省","city_Name":"张家口市","prov_Id":"13","city_Id":"07"}
,{"prov_Name":"河北省","city_Name":"保定市","prov_Id":"13","city_Id":"06"}
,{"prov_Name":"河北省","city_Name":"沧州市","prov_Id":"13","city_Id":"09"}
,{"prov_Name":"河北省","city_Name":"唐山市","prov_Id":"13","city_Id":"02"}
,{"prov_Name":"河北省","city_Name":"邯郸市","prov_Id":"13","city_Id":"04"}
,{"prov_Name":"河北省","city_Name":"承德市","prov_Id":"13","city_Id":"08"}
,{"prov_Name":"河北省","city_Name":"廊坊市","prov_Id":"13","city_Id":"10"}
,{"prov_Name":"河北省","city_Name":"河北省","prov_Id":"13","city_Id":"00"}
,{"prov_Name":"河北省","city_Name":"衡水市","prov_Id":"13","city_Id":"11"}
,{"prov_Name":"河北省","city_Name":"邢台市","prov_Id":"13","city_Id":"05"}
,{"prov_Name":"河北省","city_Name":"石家庄市","prov_Id":"13","city_Id":"01"}
,{"prov_Name":"河北省","city_Name":"秦皇岛市","prov_Id":"13","city_Id":"03"}
,{"prov_Name":"河南省","city_Name":"鹤壁市","prov_Id":"41","city_Id":"06"}
,{"prov_Name":"河南省","city_Name":"济源市","prov_Id":"41","city_Id":"90"}
,{"prov_Name":"河南省","city_Name":"开封市","prov_Id":"41","city_Id":"02"}
,{"prov_Name":"河南省","city_Name":"郑州市","prov_Id":"41","city_Id":"01"}
,{"prov_Name":"河南省","city_Name":"三门峡市","prov_Id":"41","city_Id":"12"}
,{"prov_Name":"河南省","city_Name":"河南省","prov_Id":"41","city_Id":"00"}
,{"prov_Name":"黑龙江省","city_Name":"大庆市","prov_Id":"23","city_Id":"06"}
,{"prov_Name":"黑龙江省","city_Name":"鹤岗市","prov_Id":"23","city_Id":"04"}
,{"prov_Name":"黑龙江省","city_Name":"哈尔滨市","prov_Id":"23","city_Id":"01"}
,{"prov_Name":"黑龙江省","city_Name":"黑龙江省","prov_Id":"23","city_Id":"00"}
,{"prov_Name":"黑龙江省","city_Name":"齐齐哈尔市","prov_Id":"23","city_Id":"02"}
,{"prov_Name":"黑龙江省","city_Name":"牡丹江市","prov_Id":"23","city_Id":"10"}
,{"prov_Name":"湖北省","city_Name":"武汉市","prov_Id":"42","city_Id":"01"}
,{"prov_Name":"湖北省","city_Name":"十堰市","prov_Id":"42","city_Id":"03"}
,{"prov_Name":"湖北省","city_Name":"咸宁市","prov_Id":"42","city_Id":"12"}
,{"prov_Name":"湖北省","city_Name":"宜昌市","prov_Id":"42","city_Id":"05"}
,{"prov_Name":"湖北省","city_Name":"鄂州市","prov_Id":"42","city_Id":"07"}
,{"prov_Name":"湖北省","city_Name":"襄阳市","prov_Id":"42","city_Id":"06"}
,{"prov_Name":"湖北省","city_Name":"孝感市","prov_Id":"42","city_Id":"09"}
,{"prov_Name":"湖北省","city_Name":"荆州市","prov_Id":"42","city_Id":"10"}
,{"prov_Name":"湖北省","city_Name":"黄石市","prov_Id":"42","city_Id":"02"}
,{"prov_Name":"湖北省","city_Name":"湖北省","prov_Id":"42","city_Id":"00"}
,{"prov_Name":"湖南省","city_Name":"株洲市","prov_Id":"43","city_Id":"02"}
,{"prov_Name":"湖南省","city_Name":"湖南省","prov_Id":"43","city_Id":"00"}
,{"prov_Name":"湖南省","city_Name":"长沙市","prov_Id":"43","city_Id":"01"}
,{"prov_Name":"湖南省","city_Name":"湘潭市","prov_Id":"43","city_Id":"03"}
,{"prov_Name":"湖南省","city_Name":"衡阳市","prov_Id":"43","city_Id":"04"}
,{"prov_Name":"湖南省","city_Name":"岳阳市","prov_Id":"43","city_Id":"06"}
,{"prov_Name":"吉林省","city_Name":"长春市","prov_Id":"22","city_Id":"01"}
,{"prov_Name":"吉林省","city_Name":"延边朝鲜族自治州","prov_Id":"22","city_Id":"24"}
,{"prov_Name":"吉林省","city_Name":"松原市","prov_Id":"22","city_Id":"07"}
,{"prov_Name":"吉林省","city_Name":"辽源市","prov_Id":"22","city_Id":"04"}
,{"prov_Name":"吉林省","city_Name":"四平市","prov_Id":"22","city_Id":"03"}
,{"prov_Name":"吉林省","city_Name":"吉林省","prov_Id":"22","city_Id":"00"}
,{"prov_Name":"江苏省","city_Name":"无锡市","prov_Id":"32","city_Id":"02"}
,{"prov_Name":"江苏省","city_Name":"南通市","prov_Id":"32","city_Id":"06"}
,{"prov_Name":"江苏省","city_Name":"镇江市","prov_Id":"32","city_Id":"11"}
,{"prov_Name":"江苏省","city_Name":"扬州市","prov_Id":"32","city_Id":"10"}
,{"prov_Name":"江苏省","city_Name":"苏州市","prov_Id":"32","city_Id":"05"}
,{"prov_Name":"江苏省","city_Name":"盐城市","prov_Id":"32","city_Id":"09"}
,{"prov_Name":"江苏省","city_Name":"泰州市","prov_Id":"32","city_Id":"12"}
,{"prov_Name":"江苏省","city_Name":"江苏省","prov_Id":"32","city_Id":"00"}
,{"prov_Name":"江苏省","city_Name":"南京市","prov_Id":"32","city_Id":"01"}
,{"prov_Name":"江苏省","city_Name":"连云港市","prov_Id":"32","city_Id":"07"}
,{"prov_Name":"江苏省","city_Name":"淮安市","prov_Id":"32","city_Id":"08"}
,{"prov_Name":"江苏省","city_Name":"徐州市","prov_Id":"32","city_Id":"03"}
,{"prov_Name":"江苏省","city_Name":"常州市","prov_Id":"32","city_Id":"04"}
,{"prov_Name":"江苏省","city_Name":"宿迁市","prov_Id":"32","city_Id":"13"}
,{"prov_Name":"江西省","city_Name":"上饶市","prov_Id":"36","city_Id":"11"}
,{"prov_Name":"江西省","city_Name":"江西省","prov_Id":"36","city_Id":"00"}
,{"prov_Name":"江西省","city_Name":"赣州市","prov_Id":"36","city_Id":"07"}
,{"prov_Name":"江西省","city_Name":"吉安市","prov_Id":"36","city_Id":"08"}
,{"prov_Name":"江西省","city_Name":"抚州市","prov_Id":"36","city_Id":"10"}
,{"prov_Name":"江西省","city_Name":"景德镇市","prov_Id":"36","city_Id":"02"}
,{"prov_Name":"江西省","city_Name":"宜春市","prov_Id":"36","city_Id":"09"}
,{"prov_Name":"江西省","city_Name":"九江市","prov_Id":"36","city_Id":"04"}
,{"prov_Name":"江西省","city_Name":"萍乡市","prov_Id":"36","city_Id":"03"}
,{"prov_Name":"江西省","city_Name":"新余市","prov_Id":"36","city_Id":"05"}
,{"prov_Name":"江西省","city_Name":"南昌市","prov_Id":"36","city_Id":"01"}
,{"prov_Name":"辽宁省","city_Name":"朝阳市","prov_Id":"21","city_Id":"13"}
,{"prov_Name":"辽宁省","city_Name":"辽宁省","prov_Id":"21","city_Id":"00"}
,{"prov_Name":"辽宁省","city_Name":"鞍山市","prov_Id":"21","city_Id":"03"}
,{"prov_Name":"辽宁省","city_Name":"盘锦市","prov_Id":"21","city_Id":"11"}
,{"prov_Name":"辽宁省","city_Name":"沈阳市","prov_Id":"21","city_Id":"01"}
,{"prov_Name":"辽宁省","city_Name":"营口市","prov_Id":"21","city_Id":"08"}
,{"prov_Name":"辽宁省","city_Name":"辽阳市","prov_Id":"21","city_Id":"10"}
,{"prov_Name":"辽宁省","city_Name":"大连市","prov_Id":"21","city_Id":"02"}
,{"prov_Name":"辽宁省","city_Name":"抚顺市","prov_Id":"21","city_Id":"04"}
,{"prov_Name":"辽宁省","city_Name":"本溪市","prov_Id":"21","city_Id":"05"}
,{"prov_Name":"辽宁省","city_Name":"丹东市","prov_Id":"21","city_Id":"06"}
,{"prov_Name":"辽宁省","city_Name":"铁岭市","prov_Id":"21","city_Id":"12"}
,{"prov_Name":"辽宁省","city_Name":"阜新市","prov_Id":"21","city_Id":"09"}
,{"prov_Name":"辽宁省","city_Name":"锦州市","prov_Id":"21","city_Id":"07"}
,{"prov_Name":"辽宁省","city_Name":"葫芦岛市","prov_Id":"21","city_Id":"14"}
,{"prov_Name":"内蒙古自治区","city_Name":"锡林郭勒盟","prov_Id":"15","city_Id":"25"}
,{"prov_Name":"内蒙古自治区","city_Name":"巴彦淖尔市","prov_Id":"15","city_Id":"08"}
,{"prov_Name":"内蒙古自治区","city_Name":"包头市","prov_Id":"15","city_Id":"02"}
,{"prov_Name":"内蒙古自治区","city_Name":"内蒙古自治区","prov_Id":"15","city_Id":"00"}
,{"prov_Name":"内蒙古自治区","city_Name":"乌兰察布市","prov_Id":"15","city_Id":"09"}
,{"prov_Name":"内蒙古自治区","city_Name":"呼和浩特市","prov_Id":"15","city_Id":"01"}
,{"prov_Name":"内蒙古自治区","city_Name":"呼伦贝尔市","prov_Id":"15","city_Id":"07"}
,{"prov_Name":"内蒙古自治区","city_Name":"乌海市","prov_Id":"15","city_Id":"03"}
,{"prov_Name":"内蒙古自治区","city_Name":"兴安盟","prov_Id":"15","city_Id":"22"}
,{"prov_Name":"内蒙古自治区","city_Name":"赤峰市","prov_Id":"15","city_Id":"04"}
,{"prov_Name":"内蒙古自治区","city_Name":"通辽市","prov_Id":"15","city_Id":"05"}
,{"prov_Name":"内蒙古自治区","city_Name":"鄂尔多斯市","prov_Id":"15","city_Id":"06"}
,{"prov_Name":"宁夏回族自治区","city_Name":"宁夏回族自治区","prov_Id":"64","city_Id":"00"}
,{"prov_Name":"宁夏回族自治区","city_Name":"吴忠市","prov_Id":"64","city_Id":"03"}
,{"prov_Name":"宁夏回族自治区","city_Name":"石嘴山市","prov_Id":"64","city_Id":"02"}
,{"prov_Name":"宁夏回族自治区","city_Name":"银川市","prov_Id":"64","city_Id":"01"}
,{"prov_Name":"青海省","city_Name":"西宁市","prov_Id":"63","city_Id":"01"}
,{"prov_Name":"青海省","city_Name":"青海省","prov_Id":"63","city_Id":"00"}
,{"prov_Name":"全国","city_Name":"全国","prov_Id":"10","city_Id":"00"}
,{"prov_Name":"山东省","city_Name":"山东省","prov_Id":"37","city_Id":"00"}
,{"prov_Name":"山东省","city_Name":"东营市","prov_Id":"37","city_Id":"05"}
,{"prov_Name":"山东省","city_Name":"烟台市","prov_Id":"37","city_Id":"06"}
,{"prov_Name":"山东省","city_Name":"济宁市","prov_Id":"37","city_Id":"08"}
,{"prov_Name":"山东省","city_Name":"莱芜市","prov_Id":"37","city_Id":"12"}
,{"prov_Name":"山东省","city_Name":"济南市","prov_Id":"37","city_Id":"01"}
,{"prov_Name":"山东省","city_Name":"青岛市","prov_Id":"37","city_Id":"02"}
,{"prov_Name":"山东省","city_Name":"淄博市","prov_Id":"37","city_Id":"03"}
,{"prov_Name":"山东省","city_Name":"德州市","prov_Id":"37","city_Id":"14"}
,{"prov_Name":"山东省","city_Name":"泰安市","prov_Id":"37","city_Id":"09"}
,{"prov_Name":"山东省","city_Name":"聊城市","prov_Id":"37","city_Id":"15"}
,{"prov_Name":"山东省","city_Name":"枣庄市","prov_Id":"37","city_Id":"04"}
,{"prov_Name":"山东省","city_Name":"潍坊市","prov_Id":"37","city_Id":"07"}
,{"prov_Name":"山东省","city_Name":"临沂市","prov_Id":"37","city_Id":"13"}
,{"prov_Name":"山东省","city_Name":"日照市","prov_Id":"37","city_Id":"11"}
,{"prov_Name":"山东省","city_Name":"威海市","prov_Id":"37","city_Id":"10"}
,{"prov_Name":"山东省","city_Name":"菏泽市","prov_Id":"37","city_Id":"17"}
,{"prov_Name":"山西省","city_Name":"朔州市","prov_Id":"14","city_Id":"06"}
,{"prov_Name":"山西省","city_Name":"山西省","prov_Id":"14","city_Id":"00"}
,{"prov_Name":"山西省","city_Name":"晋城市","prov_Id":"14","city_Id":"05"}
,{"prov_Name":"山西省","city_Name":"阳泉市","prov_Id":"14","city_Id":"03"}
,{"prov_Name":"山西省","city_Name":"运城市","prov_Id":"14","city_Id":"08"}
,{"prov_Name":"山西省","city_Name":"晋中市","prov_Id":"14","city_Id":"07"}
,{"prov_Name":"山西省","city_Name":"长治市","prov_Id":"14","city_Id":"04"}
,{"prov_Name":"山西省","city_Name":"太原市","prov_Id":"14","city_Id":"01"}
,{"prov_Name":"陕西省","city_Name":"安康市","prov_Id":"61","city_Id":"09"}
,{"prov_Name":"陕西省","city_Name":"宝鸡市","prov_Id":"61","city_Id":"03"}
,{"prov_Name":"陕西省","city_Name":"西安市","prov_Id":"61","city_Id":"01"}
,{"prov_Name":"陕西省","city_Name":"陕西省","prov_Id":"61","city_Id":"00"}
,{"prov_Name":"上海市","city_Name":"市辖区","prov_Id":"31","city_Id":"01"}
,{"prov_Name":"上海市","city_Name":"上海市","prov_Id":"31","city_Id":"00"}
,{"prov_Name":"四川省","city_Name":"宜宾市","prov_Id":"51","city_Id":"15"}
,{"prov_Name":"四川省","city_Name":"乐山市","prov_Id":"51","city_Id":"11"}
,{"prov_Name":"四川省","city_Name":"南充市","prov_Id":"51","city_Id":"13"}
,{"prov_Name":"四川省","city_Name":"成都市","prov_Id":"51","city_Id":"01"}
,{"prov_Name":"四川省","city_Name":"眉山市","prov_Id":"51","city_Id":"14"}
,{"prov_Name":"四川省","city_Name":"泸州市","prov_Id":"51","city_Id":"05"}
,{"prov_Name":"四川省","city_Name":"绵阳市","prov_Id":"51","city_Id":"07"}
,{"prov_Name":"四川省","city_Name":"德阳市","prov_Id":"51","city_Id":"06"}
,{"prov_Name":"四川省","city_Name":"四川省","prov_Id":"51","city_Id":"00"}
,{"prov_Name":"四川省","city_Name":"攀枝花市","prov_Id":"51","city_Id":"04"}
,{"prov_Name":"天津市","city_Name":"市辖区","prov_Id":"12","city_Id":"01"}
,{"prov_Name":"天津市","city_Name":"天津市","prov_Id":"12","city_Id":"00"}
,{"prov_Name":"西藏自治区","city_Name":"西藏自治区","prov_Id":"54","city_Id":"00"}
,{"prov_Name":"西藏自治区","city_Name":"拉萨市","prov_Id":"54","city_Id":"01"}
,{"prov_Name":"香港特别行政区","city_Name":"香港特别行政区","prov_Id":"81","city_Id":"00"}
,{"prov_Name":"新疆维吾尔自治区","city_Name":"新疆维吾尔自治区","prov_Id":"65","city_Id":"00"}
,{"prov_Name":"新疆维吾尔自治区","city_Name":"乌鲁木齐市","prov_Id":"65","city_Id":"01"}
,{"prov_Name":"新疆维吾尔自治区","city_Name":"克拉玛依市","prov_Id":"65","city_Id":"02"}
,{"prov_Name":"云南省","city_Name":"云南省","prov_Id":"53","city_Id":"00"}
,{"prov_Name":"云南省","city_Name":"昆明市","prov_Id":"53","city_Id":"01"}
,{"prov_Name":"浙江省","city_Name":"台州市","prov_Id":"33","city_Id":"10"}
,{"prov_Name":"浙江省","city_Name":"绍兴市","prov_Id":"33","city_Id":"06"}
,{"prov_Name":"浙江省","city_Name":"嘉兴市","prov_Id":"33","city_Id":"04"}
,{"prov_Name":"浙江省","city_Name":"宁波市","prov_Id":"33","city_Id":"02"}
,{"prov_Name":"浙江省","city_Name":"衢州市","prov_Id":"33","city_Id":"08"}
,{"prov_Name":"浙江省","city_Name":"舟山市","prov_Id":"33","city_Id":"09"}
,{"prov_Name":"浙江省","city_Name":"温州市","prov_Id":"33","city_Id":"03"}
,{"prov_Name":"浙江省","city_Name":"浙江省","prov_Id":"33","city_Id":"00"}
,{"prov_Name":"浙江省","city_Name":"杭州市","prov_Id":"33","city_Id":"01"}
,{"prov_Name":"浙江省","city_Name":"金华市","prov_Id":"33","city_Id":"07"}
,{"prov_Name":"浙江省","city_Name":"湖州市","prov_Id":"33","city_Id":"05"}
,{"prov_Name":"浙江省","city_Name":"丽水市","prov_Id":"33","city_Id":"11"}
,{"prov_Name":"重庆市","city_Name":"重庆市","prov_Id":"50","city_Id":"00"}
,{"prov_Name":"重庆市","city_Name":"市辖区","prov_Id":"50","city_Id":"01"}
,{"prov_Name":"重庆市","city_Name":"县","prov_Id":"50","city_Id":"02"}
]'''
        cities = json.loads(txt)

        # for city in cities:
        #     self.connection.insert(city)

        return item
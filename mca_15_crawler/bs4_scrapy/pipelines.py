# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

import csv
from bs4 import BeautifulSoup
from mca_15_crawler import bs4_scrapy
class Mca15CrawlerPipeline(object):

    def process_item(self, item, spider):
       price = []
       names = []
       soup=BeautifulSoup(str(item['record']))
       list = soup('p', 'row')
       for attr in list:
          for hit in attr.findAll(('span'),{'class':'price'}):
            if hit.contents:
                price.append(hit.contents[0].strip())
            for hit in attr.findAll(('a'),{'class':'hdrlnk'}):
                if hit.contents:
                    names.append(hit.contents[0].strip())

       item['record'] = tuple(zip(names[0::2],price[0::2]))
       return item

class CsvWriterPipeline(object):

    def __init__(self):
        self.csvwriter = csv.writer(open(bs4_scrapy.settings.csv_file_path, 'wb'), dialect='excel')

    def process_item(self , item , spider):
        self.csvwriter.writerow(('name','price'))
        self.csvwriter.writerows(item['record'])
        return item


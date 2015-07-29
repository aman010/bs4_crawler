__author__ = 'geek'
from scrapy.spiders import CrawlSpider
from scrapy.http import Request

from mca_15_crawler.bs4_scrapy.items import Mca15CrawlerItem


class crawler(CrawlSpider):
    name="mca_crawler"
    allowed_domains = ['craigslist.org/']
    pro = "search/mca"
    start_urls_base = "http://chicago.craigslist.org/%s"

    def start_requests(self):
            yield Request(self.start_urls_base % self.pro)

    ##recurring over selector to get a defined xpath

    ##or writting a rule
    #Rule(
     #   LinkExtractor(allow=('search/mca')),callback='parse_item'
    #)

    def chunk(self,l , n):
        for i in xrange(0 , len(l) , n):
            yield l[i:i+n]




    def parse(self,response):
        item = Mca15CrawlerItem()
        item['record'] = response.xpath('.//p[@class="row"]').extract()
        return item







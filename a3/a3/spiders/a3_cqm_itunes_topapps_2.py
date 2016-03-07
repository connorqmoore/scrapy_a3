# -*- coding: utf-8 -*-
import scrapy
import time
from scrapy.selector import Selector
from a3.items import A3Item
from scrapy import Item, Field, Request

class A3CqmItunesTopapps2Spider(scrapy.Spider):
    name = "a3-cqm-itunes-topapps-2"
    start_urls = (
        ['https://www.apple.com/itunes/charts/free-apps/']
    )

    def parse(self, response):
        selection = Selector(response)
        names = response.xpath("//ul/li/a[1]/img/@src")
        count = 1
        for name in names:
            item = A3Item()
            base_path = "//ul/li[" + str(count) + "]"
            item['name'] = response.xpath(base_path + "/h3/a/text()").extract()
            item['category'] = response.xpath(base_path + "/h4/a/text()").extract()
            item['link'] = response.xpath(base_path + "/a[@class='more']/@href").extract()
            item['img'] = response.xpath(base_path + "/a/img/@src").extract()
            count += 1
            time.sleep(5)
            yield Request(str(item['link'][0]), meta={'item': item}, callback=self.parse_2)

    def parse_2(self, response):
        item = response.meta['item']
        item['num'] = response.xpath("//div[@class='rating'][1]/span[@class='rating-count']/text()").extract()
        item['rating'] = response.xpath("//span[@itemprop='ratingValue']/text()").extract()
        response.meta['item'] = item
        time.sleep(5)
        yield response.meta['item']
    		
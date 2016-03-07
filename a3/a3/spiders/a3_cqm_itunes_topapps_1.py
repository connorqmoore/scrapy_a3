# -*- coding: utf-8 -*-
import scrapy
from scrapy.selector import Selector
from a3.items import A3Item

class A3CqmItunesTopapps1Spider(scrapy.Spider):
    name = "a3-cqm-itunes-topapps-1"
    allowed_domains = ["https://www.apple.com/itunes/charts/free-apps/"]
    start_urls = (
        'https://www.apple.com/itunes/charts/free-apps/',
    )

    def parse(self, response):
		selection = Selector(response)
		ans = []
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
			ans.append(item)
		return ans
    		
# -*- coding: utf-8 -*-
import scrapy


class Spider1Spider(scrapy.Spider):
    name = "spider1"
    allowed_domains = ["https://www.apple.com/itunes/charts/free-apps/"]
    start_urls = (
        'http://www.https://www.apple.com/itunes/charts/free-apps//',
    )

    def parse(self, response):
        pass

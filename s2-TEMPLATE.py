from scrapy import Item, Field, Request

class PeopleItem( Item ):
    name      = Field()
    url       = Field()
    first     = Field()
    last      = Field()

from scrapy.spiders import Spider

class S2(Spider):
    name = 's2'
    #allowed_domains
    start_urls = ["file:main.html"]
    def parse(self, response):
        names = response.xpath('????')
        ans=[]
        for name in names:
            item = PeopleItem()
            item['name'] = name.xpath('????').extract()
            item['url'] = name.xpath('????')[0].extract()
            # may have to process the URL
            req = Request(item['url'], callback=self.parse_2)
            req.meta['foo'] = item
            #ans.append(item)            
            return req

    def parse_2(self, response):
        it = response.meta['foo']
        first = response.xpath('????').extract()
        last = response.xpath('????').extract()
        it['first'] = first
        it['last'] = last
        return it       




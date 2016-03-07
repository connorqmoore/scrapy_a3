from scrapy import Item, Field, Request

class PeopleItem( Item ):
    name      = Field()
    url       = Field()
    first     = Field()
    last      = Field()

from scrapy.spiders import Spider

class S1(Spider):
    name = 's1'
    #allowed_domains
    start_urls = ["file:main.html"]
    def parse(self, response):
        names = response.xpath('????')
        ans=[]
        for name in names:
            item = PeopleItem()
            item['name'] = name.xpath('????').extract()
            item['url'] = name.xpath('????')[0].extract()
            ans.append(item)            
        return ans



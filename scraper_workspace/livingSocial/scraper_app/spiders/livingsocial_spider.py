from scrapy.spider import BaseSpider
from scraper_app.items import LivingSocialDeal
from scrapy.selector import HtmlXPathSelector
from scrapy.contrib.loader import XPathItemLoader
from scrapy.contrib.loader.processor import Join, MapCompose

class LivingSocialSpider (BaseSpider) :
    '''
    Spider for regularly updated  livingsocial.com  site, Raleigh Page
    '''
    name = "livingsocial"
    allowed_domains = ["livingsocial.com"]
    start_urls = ["https://www.livingsocial.com/cities/45-raleigh"]
    deals_list_xpath = '//li[@dealid]'

    item_fields =  {
            'title': './/span[@itemscope]/meta[@itemprop="name"]/@content',
            'link': './/a/@href',
            'location': './/a/div[@class="deal-details"]/p[@class="location"]/text()',
            'original_price': './/a/div[@class="deal-prices"]/div[@class="deal-strikethrough-price"]/div[@class="strikethrough-wrapper"]/text()',
            'price': './/a/div[@class="deal-prices"]/div[@class="deal-price"]/text()',
            'end_date':'.//span[@itemscope]/meta[@itemprop="availabilityEnds"]/@content'
            }

    def parse (self, response) :
        selector =  HtmlXPathSelector(response)

        #iterate over deals
        for deal in selector.select(self.deals_list_xpath) :
            loader = XPathItemLoader(LivingSocialDeal(), selector=deal)

            #define processor
            # renove whitespace
            loader.default_input_processor =  MapCompose(unicode.strip)
            loader.default_output_processor = Join()

            #iterate over fields and add xpaths to the loader
            for field,xpath in self.item_fields.iteritems() :
                loader.add_xpath(field, xpath)
            yield loader.load_item()


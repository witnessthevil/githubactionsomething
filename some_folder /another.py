import scrapy

from scrapy.crawler import CrawlerProcess

class first_spider(scrapy.Spider):
    name = "first spider"
    start_urls = ["https://scrapy.org/"]

    def parse(self, response, **kwargs):
        
        json = {
            "target" : response.xpath('//div[@class="block-left"]/p[3]/text()').get()
        }

        yield json



process = CrawlerProcess()
process.crawl(first_spider)
process.start()
import scrapy
from scrapy.crawler import CrawlerProcess
from scrapy.http import Request
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import Rule
#https://patents.google.com/patent/JP5522034B2/en
#https://patents.google.com/patent/US11521379B1/en
#https://patents.google.com/patent/US10723456B2/en
#https://patents.google.com/patent/JP2017148926A/en
#https://patents.google.com/patent/EP3246526B1/en
#https://patents.google.com/patent/CN117597217A/en
#https://patents.google.com/patent/CN107102644B/en
#https://patents.google.com/patent/CN113341958B/en
#https://patents.google.com/patent/US10776688B2/en
#https://patents.google.com/patent/US10564633B2/
#https://patents.google.com/patent/US9849595B2/en
#https://patents.google.com/patent/US10733512B1/en
#https://patents.google.com/patent/CN110109426B/enV

#https://patents.google.com/patent/US10559384B2/en
#https://patents.google.com/patent/WO2019243767A1/en
#https://patents.google.com/patent/CN203726272U
#https://patents.google.com/patent/DE10350801A1/en
#https://patents.google.com/patent/US11918208B2/en

class PatentSpider(scrapy.Spider):
    name = "patent"
    allowed_domains = ["patents.google.com"]
    start_urls = [
        "https://patents.google.com/patent/US9110456B2/en",
    ]
    rules = [Rule(LinkExtractor(allow='scholar/'), callback='parse', follow=False)]

    custom_settings = {
        'DOWNLOAD_DELAY': 0.01,
        'RANDOMIZE_DOWNLOAD_DELAY': True,
        'CONCURRENT_REQUESTS': 200,
        'AUTOTHROTTLE_ENABLED': True,
        #'HTTPCACHE_ENABLED': True,
        #'HTTPCACHE_EXPIRATION_SECS': 86400,
        #'HTTPCACHE_DIR': 'httpcache'
    }

    def parse(self, response):
        self_link = response.request.url
        title = response.css('span[itemprop="title"]::text').get().strip()
        #abstract = response.css('meta[name="description"]').xpath('@content').get().strip()
        abstract = response.css('meta[name="DC.description"]').xpath('@content').get().strip()
        number = response.css('title::text').get().split("-")[0].rstrip()
        publication_date = response.css('meta[name="DC.date"]').xpath('@content').get()
        inventors = response.css('dd[itemprop="inventor"]::text').getall()
        follow_links = response.xpath('//tbody/tr/td/a/@href').extract()
        current_assignee = response.css('dd[itemprop="assigneeCurrent"]::text').get().strip()
        status = response.css('span[itemprop="status"]::text').get().strip()
        yield {
            'self_link': self_link,
            'title': title,
            'abstract': abstract,
            'publication_number': number,
            'date': publication_date,
            'inventors': inventors,
            'current_assignee': current_assignee,
            'status': status
        }

        for link in follow_links:
            yield Request(url=response.urljoin(link), callback=self.parse)

def start_scraping():
    process = CrawlerProcess(settings={
        "FEEDS": {
            "output3.csv ": {"format": "csv"}
        }
    })
    process.crawl(PatentSpider)
    process.start()

if __name__ == "__main__":
    start_scraping()

import scrapy

class RecruitSpider(scrapy.spiders.Spider):
    name = "tencent"
    allowed_domains = ["hr.tencent.com"]
    start_urls = [
        "http://hr.tencent.com/position.php?&start=0#a"
    ]

    def parse(self, response):
        for sel in response.xpath('//*[@class="even"]'):
            name = sel.xpath('./td[1]/a/text()').extract()[0]
            detailLink = sel.xpath('./td[1]/a/@href').extract()[0]
            catalog = sel.xpath('./td[2]/text()').extract()[0]
            recruitNumber = sel.xpath('./td[3]/text()').extract()[0]
            workLocation = sel.xpath('./td[4]/text()').extract()[0]
            publishTime = sel.xpath('./td[5]/text()').extract()[0]
            print name, detailLink, catalog,recruitNumber,workLocation,publishTime
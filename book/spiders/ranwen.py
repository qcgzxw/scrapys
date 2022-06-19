import scrapy
from book.items import BookItem


class Ranwen(scrapy.Spider):
    name = "ranwen"
    allowed_domains = ["www.ranwen.com"]
    start_urls = (
        'https://www.ranwen.com/html/41/41996/',
    )

    def parse(self, response):
        for urlLists in response.xpath('//div[@class="listmain"]/dl/dd/a/@href').extract():
            yield scrapy.Request(response.urljoin(urlLists), callback=self.parse_article)

    def parse_article(self, response):
        item = BookItem()
        item['title'] = response.xpath('//div[@id="book"]/div[@class="content"]/h1/text()').extract()
        item['content'] = response.xpath('//div[@id="book"]/div[@class="content"]/div[@id="content"]/text()').extract()
        item['url'] = response.url
        yield item

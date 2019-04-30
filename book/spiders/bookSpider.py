import scrapy
from book.items import BookItem


class BookSpider(scrapy.Spider):
    name = "biqudao"
    allowed_domains = ["biqudao.com"]
    start_urls = (
        'https://m.biqudao.com/bqge98325/all.html',
    )

    def parse(self, response):
        for urlLists in response.xpath('//div[@id="chapterlist"]/p/a/@href').extract():
            yield scrapy.Request(response.urljoin(urlLists), callback=self.parse_article)

    def parse_article(self, response):
        item = BookItem()
        item['title'] = response.xpath('//header["class=top"]/span/text()').extract()
        item['content'] = response.xpath('//div["id=chaptercontent"]/p').extract()[1]
        item['url'] = response.url
        yield item
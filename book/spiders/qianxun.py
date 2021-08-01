import re

import scrapy
from book.items import BookItem


class Qianxun(scrapy.Spider):
    name = "qianxun"
    allowed_domains = ["www.qianxuntxt.com"]
    start_urls = (
        'https://www.qianxuntxt.com/xiaoshuo11304/',
    )

    def parse(self, response):
        for url in response.xpath('//div[@id="list"]/dl/dd/a/@href').extract():
            yield scrapy.Request(response.urljoin(url), callback=self.parse_article)

    def parse_article(self, response):
        item = BookItem()
        item['url'] = response.url
        item['title'] = response.xpath('//div["id=bookname"]/h1/text()').extract()
        item['content'] = response.xpath('//div[@id="content"]/div[1]/text()').extract()
        # <script>document.getElementById("000").innerHTML = "content2";</script>
        js_inner_content = re.findall(
            r'innerHTML\s*=\s*"(.*?)"',
            response.xpath("//body//script[4]/text()").extract()[0]
        )
        if len(js_inner_content) > 0:
            content2 = scrapy.Selector(text="<div>" + js_inner_content[0] + "</div>")
            item['content'][0] += content2.xpath("//div/text()").extract()[0]

        yield item
        next_page = response.xpath('//div[@class="bottem2"]/a[last()]/text()').extract()[0]
        if next_page == "下一页":
            next_page_url = response.xpath('//div[@class="bottem2"]/a[last()]/@href').extract()[0]
            yield scrapy.Request(response.urljoin(next_page_url), callback=self.parse_article)

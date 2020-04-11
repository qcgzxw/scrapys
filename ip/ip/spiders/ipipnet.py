# -*- coding: utf-8 -*-
import scrapy
from ..items import IpItem
from urllib.parse import quote


class IpipnetSpider(scrapy.Spider):
    name = 'ipipnet'
    allowed_domains = ['whois.ipip.net']
    start_urls = ['https://whois.ipip.net/search/GOOGLE%20LLC']

    def __init__(self, keyword=None, *args, **kwargs):
        super(IpipnetSpider, self).__init__(*args, **kwargs)
        if keyword:
            if '%' not in keyword:
                keyword = quote(keyword)
            keyword = keyword.upper()
            self.start_urls = ['https://whois.ipip.net/search/%s' % keyword]

    def parse(self, response):
        for urlLists in response.xpath('//table[@class="table"]/tr/td/a/@href').extract():
            yield scrapy.Request(response.urljoin(urlLists), callback=self.parse_ip_list)

    def parse_ip_list(self, response):
        item = IpItem()
        item['title'] = response.xpath('//div[@class="address-header"]/div/h2/a/text()').extract()
        item['ipv4_list'] = response.xpath('//div[@id="pills-ipv4"]/div/table/tr/td/a/text()').extract()
        item['ipv6_list'] = response.xpath('//div[@id="pills-ipv6"]/div/table/tr/td/a/text()').extract()
        item['url'] = response.url
        yield item
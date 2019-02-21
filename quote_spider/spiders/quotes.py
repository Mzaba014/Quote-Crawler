# -*- coding: utf-8 -*-
from __future__ import absolute_import
import scrapy


class QuotesSpider(scrapy.Spider):
    name = 'quotes'
    allowed_domains = ["quotes.toscrape.com"]
    start_urls = ['http://quotes.toscrape.com/']

    def parse(self, response):
        # quotes_with_nls = response.xpath('//*[@class="quote"]/span/text()').extract()
        quotes = response.xpath('//*[@class="quote"]')

        for quote in quotes:
            text = quote.xpath('.//*[@class="text"]/text()').extract_first()
            author = quote.xpath('.//*[@itemprop="author"]/text()').extract_first()
            tags = quote.xpath('.//*[@class="tag"]/text()').extract()

            yield {
                'Author': author,
                'Text': text,
                'Tags': tags
            }

        next_page_url = response.xpath('//*[@class="next"]/a/@href').extract_first()
        absolute_next_page_url = response.urljoin(next_page_url)
        yield scrapy.Request(absolute_next_page_url)

    # h1_tag = response.xpath('//h1/a/text()').extract_first()
    # tags = response.xpath('//*[@class="tag-item"]/a/text()').extract()

    # yield {'h1_tag': h1_tag, 'tags': tags}
    # response.xpath('//h2/text()').extract()

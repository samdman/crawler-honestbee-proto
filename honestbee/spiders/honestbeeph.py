# -*- coding: utf-8 -*-
import scrapy
from scrapy.spiders import CrawlSpider
from honestbee.items import HonestbeeItem

# scrapy genspider honestbeeph
class HonestbeephSpider(scrapy.Spider):
    name = 'honestbeeph'
    allowed_domains = ['www.honestbee.ph']
    # get urls to crawl
    with open("urls_" + name + ".txt", "rt") as f:
        start_urls = [url.strip() for url in f.readlines()]

    def parse(self, response):
        url = response.url.split("/")
        cat = url[len(url) - 3]
        subcat = url[len(url) - 1]
        #get all items
        for item_link in response.css('.XaRs403S_a6U7-8Wfu_c3 > ._21fv8iCnSiWMpLxNvsklkl::attr(href)').extract():            
            yield scrapy.Request(url='https://www.honestbee.ph' + item_link + '&c=' + cat + '&sc=' + subcat, callback=self.parse_detail_page)

    def parse_detail_page(self, response):
        #get details of item
        urlraw = response.url.split("&")
        url = urlraw[0]
        cat = urlraw[len(urlraw) - 2].split("=")[1]
        subcat = urlraw[len(urlraw) - 1].split("=")[1]

        imgsrc = response.css('.SU-D_DP7-GqGytUNJLSt3 > img::attr(src)').extract()[0]
        title = response.css('._3wTYS6kFJF4Lmjm8wYSHVD::text').extract()[0].strip()
        price = response.css('.MzukkdaYqGeiEjEA4OIMN > span::text').extract()[0]
        desc = response.css('._45xiT1wQN0YS9fB9XH2pt::text').extract()[0]

        item = HonestbeeItem()
        item['cat'] = cat
        item['subcat'] = subcat
        item['imgsrc'] = imgsrc
        item['title'] = title
        item['price'] = price
        item['desc'] = desc
        item['url'] = url
        yield item

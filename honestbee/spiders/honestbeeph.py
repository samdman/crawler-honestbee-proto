# -*- coding: utf-8 -*-
"Honestbee.ph crawler module"
import scrapy
from honestbee.items import HonestbeeItem

# scrapy genspider honestbeeph
class HonestbeephSpider(scrapy.Spider):
    "Honestbee.ph crawler class"
    name = 'honestbeeph'
    allowed_domains = ['www.honestbee.ph']
    # get urls to crawl
    with open("urls_" + name + ".txt", "rt") as uline:
        start_urls = [url.strip() for url in uline.readlines()]

    def parse(self, response):
        url = response.url.split("/")
        cat = url[len(url) - 3]
        subcat = url[len(url) - 1]
        #get all items
        for item_link in response.css('.XaRs403S_a6U7-8Wfu_c3 > ._21fv8iCnSiWMpLxNvsklkl::attr(href)').extract():
            yield scrapy.Request(url='https://www.honestbee.ph' + item_link + '&c=' + cat + '&sc=' + subcat, callback=self.parse_detail_page)

    def parse_detail_page(self, response):
        "Honestbee.ph crawler details parsing"
        #get details of item
        urlraw = response.url.split("&")
        url = urlraw[0]
        cat = urlraw[len(urlraw) - 2].split("=")[1]
        subcat = urlraw[len(urlraw) - 1].split("=")[1]

        imgsrc = response.css('.SU-D_DP7-GqGytUNJLSt3 > img::attr(src)').extract()[0]
        title = response.css('._3wTYS6kFJF4Lmjm8wYSHVD::text').extract()[0].strip()
        price = response.css('.MzukkdaYqGeiEjEA4OIMN > span::text').extract()[0]
        priceorig = response.css('del._2y5V1t6eyCHUXg6r3rhm2Z > span::text').extract()
        pricesave = ""
        if priceorig:
            pricesave = price
            price = priceorig[0]
        desc = response.css('._45xiT1wQN0YS9fB9XH2pt::text').extract()[0]

        item = HonestbeeItem()
        item['cat'] = cat
        item['subcat'] = subcat
        item['imgsrc'] = imgsrc
        item['title'] = title
        item['pricesave'] = pricesave
        item['price'] = price
        item['desc'] = desc
        item['url'] = url
        yield item

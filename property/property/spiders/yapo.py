import scrapy
from datetime import datetime


URLS = [
    'https://www.yapo.cl/maule/comprar?ca=8_s&l=0&w=1&cmn=141&ret=5&pe=3&ss=4', #terreno en talca
    'https://www.yapo.cl/maule/comprar?ca=8_s&l=0&w=1&cmn=141&ret=2&ps=2&pe=3' #casa en talca
]

# Departamento providencia
class YapoSpider(scrapy.Spider):
    name = 'yapo'
    start_urls = URLS

    def parse(self, response):
        for item in response.css('.listing_thumbs'):
            title = item.css('td.thumbs_subject > a ::text').extract_first().lower()
            if "busco" in title:
                return 
            yield {
                'title': title,
                'link': item.css('td.thumbs_subject > a ::attr(href)').extract_first(),
                'price': self.get_price(item.css('td.thumbs_subject > span.price ::text').extract_first()),
                'address': '',
                'code': item.xpath('@id').extract_first(),
                'location': item.css('span.commune ::text').extract_first(),
                'operation': response.url.split("/")[4].split("?")[0],
                '_type': self.get_type(response),
                'date': '',
                'thumb':self.get_thumb(item.css('.link_image > img ::attr(src)').extract_first()),
                'site': self.name
            }

        next_page = response.css('span.nohistory:last-child > a ::attr(href)').extract_first()
        if next_page:
            yield scrapy.Request(response.urljoin(next_page), callback=self.parse)

    def get_type(self, response):
        if response.request.url == URLS[0]:
            return "parcela"
        else:
            return "casa"


    def get_price(self, price):
        price = price.replace(".", "")
        price = price.replace(",", "")
        price = price.strip()

        if "UF" in price:
            price = int(price.replace("UF", ""))*29057
        else:
            price = int(price.replace("$", ""))

        return price

    def get_thumb(self, thumb):
        return thumb if 'transparen' not in thumb else None
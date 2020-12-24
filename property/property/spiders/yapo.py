import scrapy
from datetime import datetime

# Departamento providencia
class YapoSpider(scrapy.Spider):
    name = 'yapo'
    start_urls = [
        'https://www.yapo.cl/maule/comprar?ca=8_s&l=0&w=1&cmn=141&ret=5&pe=3&ss=4', #terreno en talca
    ]

    def parse(self, response):
        for item in response.css('.listing_thumbs'):
            yield {
                'title': item.css('td.thumbs_subject > a ::text').extract_first(),
                'link': item.css('td.thumbs_subject > a ::attr(href)').extract_first(),
                'price': item.css('td.thumbs_subject > span.price ::text').extract_first().strip(),
                'address': '',
                'code': item.xpath('@id').extract_first(),
                'profile': 'personas',
                'location': item.css('span.commune ::text').extract_first(),
                'operation': response.url.split("/")[4].split("?")[0],
                '_type': 'departamento' if response.url[-1] == '1' else 'casa',
                'date': datetime.today().strftime('%d %m %y %H:%M:%S'),
                'thumb':item.css('.link_image > img ::attr(src)').extract_first(),
                'site': self.name
            }

        next_page = response.css('span.nohistory:last-child > a ::attr(href)').extract_first()
        if next_page:
            yield scrapy.Request(response.urljoin(next_page), callback=self.parse)
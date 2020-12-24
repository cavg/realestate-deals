import scrapy


class TopSpider(scrapy.Spider):
    name = 'top'
    allowed_domains = ['toppropiedades.cl']
    start_urls = ['https://www.toppropiedades.cl/resultado?id_operacion=2&id_categoria=25&id_ciudad=137']

    def parse(self, response):
        for item in response.css('li.shown'):
            yield { 
                'title': item.css('a::attr(title)').extract_first(),
                'link': "https://www.toppropiedades.cl/%s" % item.css('a::attr(href)').extract_first(),
                'price': item.css('div.box').extract_first(),
                'address': item.css('div.nu_address_text::text').extract_first(),
                'code': '',
                'profile': '',
                'location': '',
                'operation': '',
                '_type': '',
                'date': datetime.today().strftime('%d %m %y %H:%M:%S'),
                'thumb':item.css('img.w100::attr(src)').extract_first(),
                'site': 'toppropiedades.cl'
            }

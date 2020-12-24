import scrapy
from datetime import datetime
import urllib

class NuroaSpider(scrapy.Spider):
    name = 'nuroa'
    allowed_domains = ['nuroa.cl']
    start_urls = ['https://www.nuroa.cl/venta/casa-talca?order=1&way=2&max_price=30000000&min_price=2500000&time_span=15']

    def parse(self, response):
        for item in response.css('.nu_row'):
            thumb = item.css('img.nu_list_image::attr(src)').extract_first()
            yield { 
                'title': item.css('h3.nu_list_title > a::text').extract_first(),
                'link': urllib.request.urlopen(item.css('h3.nu_list_title > a::attr(href)').extract_first()).geturl(),
                'price': item.css('span[itemprop="price"]::attr(content)').extract_first(),
                'address': item.css('div.nu_address_text::text').extract_first(),
                'code': item.css('::attr(id)').extract_first().replace('nu_flat_',''),
                'profile': '',
                'location': '',
                'operation': '',
                '_type': '',
                'date': datetime.today().strftime('%d %m %y %H:%M:%S'),
                'thumb':thumb if 'no_image.png' not in thumb else '',
                'site': item.css('p.nu_partner_footer::text').extract_first()
            }
        # next_page = response.css('span.nohistory:last-child > a ::attr(href)').extract_first()
        # if next_page:
        #     yield scrapy.Request(response.urljoin(next_page), callback=self.parse)

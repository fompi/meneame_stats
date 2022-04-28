# -*- coding: utf-8 -*-
from re import findall
from scrapy.loader import ItemLoader
import scrapy
from meneame_crawler.items import NewsLoader

class MeneameBaseSpider(scrapy.Spider):
    allowed_domains = ['old.meneame.net']

    def parse(self, response):

        for selector in response.xpath('.//*[@class="news-summary"]'):
            loader = NewsLoader(selector=selector)

            loader.add_xpath('index', './/h2/a/@class', re='l:(.*)')
            loader.add_xpath('noticia', './/h2/a/text()')
            loader.add_xpath('link_noticia', './/h2/a/@href')
            loader.add_xpath('web', './/*[@class="showmytitle"]//text()')
            loader.add_xpath('usuario', './/*[@class="news-submitted"]/a/text()')
            loader.add_xpath('id_usuario', './/*[@class="news-submitted"]/a/@class', re='tooltip u:(.*)')
            loader.add_xpath('fecha_envio', './/*[@class="ts visible" and starts-with(@title, "enviado:")]/@data-ts')
            loader.add_xpath('fecha_publicacion', './/*[@class="ts visible" and starts-with(@title, "publicado:")]/@data-ts')
            loader.add_xpath('meneos', './/*[@class="votes"]/a/text()')
            loader.add_xpath('clicks', './/*[@class="clics"]/span/text()')
            loader.add_xpath('comentarios', './/a[@class="comments"]/@data-comments-number')
            loader.add_xpath('votos_positivos', './/div[@class="news-details-data-up"]//*[@class="positive-vote-number"]/text()')
            loader.add_xpath('votos_anonimos', './/div[@class="news-details-data-up"]//*[@class="anonymous-vote-number"]/text()')
            loader.add_xpath('votos_negativos', './/div[@class="news-details-data-up"]//*[@class="negative-vote-number"]/text()')
            loader.add_xpath('karma', './/div[@class="news-details-data-up"]//*[@class="karma-number"]/text()')
            loader.add_xpath('sub', './/div[@class="news-details-data-up"]//*[@class="subname"]/text()')
            loader.add_xpath('extracto', './/*[@class="news-content"]/text()')
            yield loader.load_item()

        sig_pag = response.xpath('.//*[contains(text(), "siguiente »")]/@href').extract_first()
        abs_sig_pag = response.urljoin(sig_pag)

        if len(findall(r'\d+', sig_pag)) == 1:
            self.logger.info('Following to pag ' + findall(r'\d+', sig_pag)[0])
            yield response.follow(abs_sig_pag)
        else:
            self.logger.critical(
                'Critical error extracting index from "%s" on %s' % (sig_pag, response.url)
            )

class PortadaSpider(MeneameBaseSpider):
    name = 'portada'
    start_urls = ['https://old.meneame.net/']

class DescartadasSpider(MeneameBaseSpider):
    name = 'descartadas'
    start_urls = ['https://old.meneame.net/queue?meta=_discarded']

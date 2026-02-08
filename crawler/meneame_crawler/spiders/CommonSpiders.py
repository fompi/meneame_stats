# -*- coding: utf-8 -*-
from re import findall
import scrapy
from meneame_crawler.items import NewsLoader

class MeneameBaseSpider(scrapy.Spider):
    allowed_domains = ['www.meneame.net']

    def parse(self, response):

        for selector in response.xpath('.//*[@class="news-summary"]'):
            loader = NewsLoader(selector=selector)

            loader.add_xpath('index', './/h2/a/@class', re=r'l:(\d+)')
            loader.add_xpath('noticia', './/h2/a/text()')
            loader.add_xpath('link_noticia', './/h2/a/@href')
            loader.add_xpath('web', './/*[@class="showmytitle"]//text()')
            loader.add_xpath('usuario', './/*[@class="news-submitted"]/a[contains(@href, "/history")]/text()')
            loader.add_xpath('id_usuario', './/*[@class="news-submitted"]/a/@class', re=r'tooltip u:(\d+)')
            loader.add_xpath('fecha_envio', './/*[contains(@class, "ts") and contains(@class, "visible") and starts-with(@title, "enviado:")]/@data-ts')
            loader.add_xpath('fecha_publicacion', './/*[contains(@class, "ts") and contains(@class, "visible") and starts-with(@title, "publicado:")]/@data-ts')
            loader.add_xpath('meneos', './/*[@class="votes"]/a/text()')
            loader.add_xpath('clicks', './/*[@class="clics"]/span/text()')
            loader.add_xpath('comentarios', './/a[contains(@class, "comments")]/@data-comments-number')
            loader.add_xpath('votos_positivos', './/div[@class="news-details-data-up"]//*[@class="positive-vote-number"]/text()')
            loader.add_xpath('votos_anonimos', './/div[@class="news-details-data-up"]//*[@class="anonymous-vote-number"]/text()')
            loader.add_xpath('votos_negativos', './/div[@class="news-details-data-up"]//*[@class="negative-vote-number"]/text()')
            loader.add_xpath('karma', './/div[@class="news-details-data-up"]//*[@class="karma-number"]/text()')
            loader.add_xpath('sub', './/div[@class="news-details-data-up"]//*[@class="subname"]/text()')
            loader.add_xpath('extracto', './/*[@class="news-content"]/text()')
            yield loader.load_item()

        sig_pag = response.xpath('.//a[contains(text(), "siguiente")]/@href').extract_first()
        if sig_pag:
            page_nums = findall(r'\d+', sig_pag)
            if len(page_nums) == 1:
                self.logger.info('Following to pag ' + page_nums[0])
                yield response.follow(response.urljoin(sig_pag))
            else:
                self.logger.critical(
                    'Critical error extracting index from "%s" on %s' % (sig_pag, response.url)
                )

class MeneameSpider(MeneameBaseSpider):
  name = 'meneame'
  start_urls = []
  custom_settings = {}

  def __init__(self, status=None, limit=1, *args, **kwargs):

    super(MeneameSpider, self).__init__(*args, **kwargs)

    if status == 'trash':
      self.start_urls.append('https://www.meneame.net/queue?meta=_discarded')
    elif status == 'portada':
      self.start_urls.append('https://www.meneame.net/')
    elif status == 'pending':
      self.start_urls.append('https://www.meneame.net/queue')
        # or .../shakeit.php?meta=_open ?

#    if limit.isnumeric() and int(limit) > 0:
#      self.limit = int(limit)
#      self.custom_settings['DEPTH_LIMIT'] = self.limit
#      self.crawler.settings.overrides.settings.set('DEPTH_LIMIT', 1)
#      #self.custom_settings.update({'DEPTH_LIMIT': self.limit})
#    elif limit is False:
#      self.custom_settings['DEPTH_LIMIT'] = 0
#    else:
#      self.custom_settings['DEPTH_LIMIT'] = 1
#      self.crawler.settings.overrides.settings.set('DEPTH_LIMIT', 1)

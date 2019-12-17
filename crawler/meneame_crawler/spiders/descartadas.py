# uncompyle6 version 3.6.0
# Python bytecode 3.5 (3351)
# Decompiled from: Python 3.7.4 (default, Oct  4 2019, 06:57:26) 
# [GCC 9.2.0]
# Embedded file name: D:\Programacion\Python\meneame_crawler\meneame_crawler\spiders\descartadas.py
# Compiled at: 2017-12-04 10:22:10
# Size of source mod 2**32: 4484 bytes
import scrapy

class DescartadasSpider(scrapy.Spider):
    name = 'descartadas'
    allowed_domains = ['meneame.net']
    start_urls = ['https://www.meneame.net/queue?meta=_discarded']

    def parse(self, response):

        def extraer(field):
            if field:
                pass
            else:
                field = ''
            return field

        news = response.xpath('.//*[@class="news-summary"]')
        for new in news:
            try:
                index = extraer(new.xpath('.//h2/a/@class').extract_first())
                index = extraer(index.replace('l:', ''))
            except:
                index = ''
            else:
                try:
                    noticia = extraer(new.xpath('.//h2/a/text()').extract_first())
                    noticia = extraer(noticia.replace('"', '-').replace("'", '-').replace(';', ','))
                except:
                    noticia = ''
                else:
                    try:
                        link_n = extraer(new.xpath('.//h2/a/@href').extract_first())
                        link_n = link_n + ' '
                    except:
                        link_n = ''
                    else:
                        try:
                            web = extraer(new.xpath('.//*[@class="showmytitle"]//text()').extract_first())
                        except:
                            web = ''
                        else:
                            try:
                                user = extraer(new.xpath('.//*[@class="news-submitted"]/a/text()').extract_first())
                            except:
                                user = ''
                            else:
                                try:
                                    id_user = extraer(new.xpath('.//*[@class="news-submitted"]/a/@class').extract_first())
                                    id_user = extraer(id_user.replace('tooltip u:', ''))
                                except:
                                    id_user = ''
                                else:
                                    try:
                                        f_envio = extraer(new.xpath('.//*[@class="ts visible"]/@data-ts').extract()[0::2][0])
                                    except:
                                        f_envio = ''
                                    else:
                                        try:
                                            f_pub = extraer(new.xpath('.//*[@class="ts visible"]/@data-ts').extract()[1::2][0])
                                        except:
                                            f_pub = ''
                                        else:
                                            try:
                                                meneos = extraer(new.xpath('.//*[@class="votes"]/a/text()').extract_first())
                                            except:
                                                meneos = ''
                                            else:
                                                try:
                                                    clicks = extraer(new.xpath('.//*[@class="clics"]/text()').extract_first())
                                                    clicks = extraer(clicks.replace(' ', '').replace('clics', ''))
                                                except:
                                                    clicks = ''
                                                else:
                                                    try:
                                                        coment = extraer(new.xpath('.//*[@class="comments"]/text()')[1::2][0].extract())
                                                        coment = extraer(coment.replace(' ', '').replace('comentarios', ''))
                                                    except:
                                                        coment = ''
                                                    else:
                                                        try:
                                                            v_pos = extraer(new.xpath('.//*[@class="votes-up"]/span/strong/text()')[1::2][0].extract())
                                                        except:
                                                            v_pos = ''
                                                        else:
                                                            try:
                                                                v_anom = extraer(new.xpath('.//*[@class="wideonly votes-anonymous"]/span/strong/text()')[1::2][0].extract())
                                                            except:
                                                                v_anom = ''
                                                            else:
                                                                try:
                                                                    v_neg = extraer(new.xpath('.//*[@class="votes-down"]/span/strong/text()')[1::2][0].extract())
                                                                except:
                                                                    v_neg = ''
                                                                else:
                                                                    try:
                                                                        karma = extraer(new.xpath('.//*[@class="karma-value"]/text()')[1::2][0].extract())
                                                                        karma = extraer(karma.replace(' ', ''))
                                                                    except:
                                                                        karma = ''
                                                                    else:
                                                                        try:
                                                                            seccion = extraer(new.xpath('.//*[@class="subname"]/text()')[1::2][0].extract())
                                                                            seccion = extraer(seccion.replace(' ', ''))
                                                                        except:
                                                                            seccion = ''
                                                                        else:
                                                                            try:
                                                                                extracto = extraer(new.xpath('.//*[@class="news-content"]/text()').extract_first())
                                                                                extracto = extraer(extracto.replace(';', ',').replace('"', '-').replace("'", '-'))
                                                                            except:
                                                                                extracto = ''
                                                                            else:
                                                                                yield {'index': index, 
                                                                                 'noticia': noticia, 
                                                                                 'link_noticia': link_n, 
                                                                                 'web': web, 
                                                                                 'usuario': user, 
                                                                                 'id_usuario': id_user, 
                                                                                 'fecha_envio': f_envio, 
                                                                                 'fecha_publicacion': f_pub, 
                                                                                 'meneos': meneos, 
                                                                                 'clicks': clicks, 
                                                                                 'comentarios': coment, 
                                                                                 'votos_positivos': v_pos, 
                                                                                 'votos_anonimos': v_anom, 
                                                                                 'votos_negativos': v_neg, 
                                                                                 'karma': karma, 
                                                                                 'sub': seccion, 
                                                                                 'extracto': extracto}

        sig_pag = response.xpath('.//*[contains(text(), "siguiente »")]/@href').extract_first()
        abs_sig_pag = response.urljoin('http://meneame.net/queue' + sig_pag)
        yield scrapy.Request(abs_sig_pag)
# okay decompiling spiders/__pycache__/descartadas.cpython-35.pyc

# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy

class MeneameCrawlerItem(scrapy.Item):
	index = scrapy.Field()
	noticia = scrapy.Field()
	link_noticia = scrapy.Field()
	web = scrapy.Field()
	usuario = scrapy.Field()
	id_usuario = scrapy.Field()
	fecha_envio = scrapy.Field()
	fecha_publicacion = scrapy.Field()
	meneos = scrapy.Field()
	clicks = scrapy.Field()
	comentarios = scrapy.Field()
	votos_positivos = scrapy.Field()
	votos_anonimos = scrapy.Field()
	votos_negativos = scrapy.Field()
	karma = scrapy.Field()
	sub = scrapy.Field()
	extracto = scrapy.Field()


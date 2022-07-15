# -*- coding: utf-8 -*-
from scrapy.loader import ItemLoader
from itemloaders.processors import TakeFirst, MapCompose
import scrapy

class NewsItem(scrapy.Item):
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

class NewsLoader(ItemLoader):
    default_item_class = NewsItem
    default_output_processor = TakeFirst()

    noticia_in = MapCompose(str.strip)

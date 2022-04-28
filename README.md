## Background

https://www.meneame.net/m/Visualdata/analizando-noticias-portada

## Running

### Crawler (scrapy)

```
$ cd crawler
$ scrapy crawl portada -O ../portada.csv
```

Para las descartadas:
```
$ scrapy crawl descartadas -O descartadas.csv
```

### Analisis (R)

```
$ Rscript -e "rmarkdown::render('analisis.Rmd')"
```

This will generate *analisis.html*; to ensemble only the graphics execute:

```
$ Rscript analisis.R
````

## Other

- https://www.meneame.net/m/Meneantes/meneo-proporciones-pequeno-analisis-sobre-diseno-beta-lab-net-1
- https://www.meneame.net/m/tecnolog%C3%ADa/archivo-yaml-toda-portada-meneame-desde-principio-hasta-18-07
- https://www.meneame.net/story/analisis-top-20-usuarios-meneame

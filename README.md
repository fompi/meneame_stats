## Background

https://www.meneame.net/m/Visualdata/analizando-noticias-portada

## Running

```
# Crawl data into CSV file
$ cd crawler
$ scrapy crawl meneame -a status=portada -s DEPTH_LIMIT=0 -o portada.csv 

# Build analytics report
$ Rscript -e "rmarkdown::render('../analisis.Rmd')"

```

This will generate *analisis.html*

## Other

- https://www.meneame.net/m/Meneantes/meneo-proporciones-pequeno-analisis-sobre-diseno-beta-lab-net-1
- https://www.meneame.net/m/tecnolog%C3%ADa/archivo-yaml-toda-portada-meneame-desde-principio-hasta-18-07
- https://www.meneame.net/story/analisis-top-20-usuarios-meneame

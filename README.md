# meneame_stats

Analisis estadistico de las noticias publicadas en [meneame.net](https://www.meneame.net/).

Articulo original: [Analizando noticias de portada](https://www.meneame.net/m/Visualdata/analizando-noticias-portada)

## Crawler

El crawler para extraer datos de meneame.net se encuentra en un repositorio separado:

**[fompi/meneame_crawler](https://github.com/fompi/meneame_crawler)**

## Analisis

El fichero `analisis.Rmd` contiene un informe en R Markdown con:

- Distribucion de fuentes (dominios mas frecuentes)
- Actividad por usuario
- Evolucion temporal de publicaciones
- Tiempo medio de envio a portada
- Distribucion de votos, karma y comentarios
- Nubes de palabras de titulares

### Uso

```bash
# Generar el informe de analisis (requiere R y las dependencias)
Rscript -e "rmarkdown::render('analisis.Rmd')"
# Produce: analisis.html
```

## Estructura del proyecto

```
.
├── analisis.Rmd           # Informe estadistico en R
└── analisis-2017.html     # Informe generado (datos 2017)
```

## Enlaces relacionados

- https://www.meneame.net/m/Meneantes/meneo-proporciones-pequeno-analisis-sobre-diseno-beta-lab-net-1
- https://www.meneame.net/m/tecnolog%C3%ADa/archivo-yaml-toda-portada-meneame-desde-principio-hasta-18-07
- https://www.meneame.net/story/analisis-top-20-usuarios-meneame

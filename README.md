# meneame_stats

Crawler y analisis estadistico de las noticias publicadas en [meneame.net](https://www.meneame.net/).

Articulo original: [Analizando noticias de portada](https://www.meneame.net/m/Visualdata/analizando-noticias-portada)

## Requisitos

- [Nix](https://nixos.org/download/) (gestor de paquetes)

No hace falta instalar Python, Scrapy ni R manualmente. El `flake.nix` proporciona todo el entorno.

## Inicio rapido

```bash
# Entrar al entorno de desarrollo
nix develop

# Crawlear la portada completa (todas las paginas)
cd crawler
scrapy crawl meneame -a status=portada -s DEPTH_LIMIT=0 -o portada.csv

# Generar el informe de analisis
Rscript -e "rmarkdown::render('../analisis.Rmd')"
# Produce: analisis.html
```

## Crawler

Spider de [Scrapy](https://scrapy.org/) que extrae noticias de meneame.net via scraping HTML.

### Uso

```bash
cd crawler
scrapy crawl meneame -a status=<STATUS> [-s DEPTH_LIMIT=<N>] -o <archivo.csv>
```

### Parametros

| Parametro | Valores | Descripcion |
|-----------|---------|-------------|
| `status` | `portada` | Noticias publicadas en portada |
| | `pending` | Noticias pendientes (cola) |
| | `trash` | Noticias descartadas |
| `DEPTH_LIMIT` | `0` | Sin limite (todas las paginas) |
| | `N` | Maximo N paginas de profundidad (por defecto: 5) |

### Campos extraidos

El CSV resultante usa `;` como delimitador y contiene:

| Campo | Descripcion | Ejemplo |
|-------|-------------|---------|
| `index` | ID de la noticia en meneame | `4144459` |
| `noticia` | Titulo | `5 veces que la termodinamica...` |
| `link_noticia` | URL de la fuente original | `https://aulaquest.com/...` |
| `web` | Dominio de la fuente | `aulaquest.com` |
| `usuario` | Nombre del usuario que la envio | `M.Rajoy.` |
| `id_usuario` | ID numerico del usuario | `79902` |
| `fecha_envio` | Timestamp unix del envio | `1770452296` |
| `fecha_publicacion` | Timestamp unix de la publicacion | `1770508202` |
| `meneos` | Numero de votos positivos (meneos) | `33` |
| `clicks` | Numero de clics | `461` |
| `comentarios` | Numero de comentarios | `13` |
| `votos_positivos` | Votos positivos de usuarios registrados | `24` |
| `votos_anonimos` | Votos de usuarios anonimos | `9` |
| `votos_negativos` | Votos negativos | `1` |
| `karma` | Karma de la noticia | `391` |
| `sub` | Categoria/sub | `ciencia` |
| `extracto` | Extracto/descripcion de la noticia | `Desde demonios que abren...` |

### Configuracion

La configuracion del crawler esta en `crawler/meneame_crawler/settings.py`. Valores relevantes:

- **AutoThrottle** activado: delay inicial de 5s, maximo 60s, concurrencia 1.0
- **robots.txt** respetado
- **CSV delimiter**: `;`

## Analisis

El fichero `analisis.Rmd` contiene un informe en R Markdown con:

- Distribucion de fuentes (dominios mas frecuentes)
- Actividad por usuario
- Evolucion temporal de publicaciones
- Tiempo medio de envio a portada
- Distribucion de votos, karma y comentarios
- Nubes de palabras de titulares

## Estructura del proyecto

```
.
├── flake.nix                        # Entorno nix (Python + Scrapy)
├── analisis.Rmd                     # Informe estadistico en R
├── analisis-2017.html               # Informe generado (datos 2017)
└── crawler/
    ├── scrapy.cfg
    └── meneame_crawler/
        ├── settings.py              # Configuracion de Scrapy
        ├── items.py                 # Modelo de datos (NewsItem)
        ├── my_project_csv_item_exporter.py  # Exportador CSV personalizado
        └── spiders/
            └── CommonSpiders.py     # Spider principal
```

## Enlaces relacionados

- https://www.meneame.net/m/Meneantes/meneo-proporciones-pequeno-analisis-sobre-diseno-beta-lab-net-1
- https://www.meneame.net/m/tecnolog%C3%ADa/archivo-yaml-toda-portada-meneame-desde-principio-hasta-18-07
- https://www.meneame.net/story/analisis-top-20-usuarios-meneame

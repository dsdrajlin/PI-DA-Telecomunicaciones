<img src="./assets/logo_super.png">

<h1 align="center"><b> Super: Radiografía del mercado de telecomunicaciones </b></h1>
<hr>

## Tabla de contenidos  <!-- omit in toc -->
- [Introducción](#introducción)
- [Análisis general](#análisis-general)
- [Análisis particular](#análisis-particular)
- [KPIs](#kpis)
  - [Variación en el acceso a Internet](#variación-en-el-acceso-a-internet)
  - [Tasa de Conversión](#tasa-de-conversión)
- [Stack tecnológico](#stack-tecnológico)
- [Archivos](#archivos)


## Introducción
Como Analista de Datos, fui contratado por __[Super](https://es.wikipedia.org/wiki/Super_(empresa))__, una destacada empresa de telecomunicaciones en Argentina. Fundada en 1985 en la provincia de Mendoza con el propósito inicial de ofrecer acceso a la __televisión por cable__, Super ha experimentado un crecimiento significativo. A lo largo de los años, se ha expandido a más de 100 ciudades y 14 provincias en todo el país.

Además de su expansión geográfica, Super ha diversificado su gama de servicios, incorporando el acceso a Internet en 1999. Siendo pionera en este ámbito, la empresa adoptó la tecnología de __Cablemódem__, aprovechando la infraestructura de televisión por cable para ofrecer servicios de Internet de banda ancha.

A partir de 2010, Super ha respondido a las nuevas tecnologías al introducir el servicio de Acceso a Internet a través de __Fibra óptica__. Esta tecnología, basada en cables de fibra óptica, ofrece ventajas significativas, como velocidades de transmisión más altas, mayor confiabilidad y seguridad en comparación con el cablemódem.

En julio de 2018, Super anunció una inversión sustancial de aproximadamente 400 millones de dólares para expandir su red de fibra óptica ([Fuente](https://www.infobae.com/sociedad/2018/07/17/la-compania-de-television-por-cable-e-internet-supercanal-tiene-nuevos-duenos/)). Este movimiento estratégico ha conducido a una migración casi completa hacia la fibra óptica, marcando el abandono de la tecnología de Cablemódem en la mayoría de las ciudades. A día de hoy, el principal ingreso de Super proviene de la Fibra óptica, seguido de la TV por cable. Estos servicios se ofrecen tanto de forma conjunta como separada.

Este proyecto tiene como objetivo principal analizar los datos actuales de Super, centrándose en los siguientes aspectos:
* Evaluar la situación a nivel nacional y provincial de los servicios de __TV por cable__ e __Internet__.
* Reevaluar la ventaja de invertir en __Fibra óptica__ en comparación con __Cablemódem__, respaldándose en datos concretos.
* Identificar __oportunidades para la mejora__ y el crecimiento continuo.
Desarrollar __Key Performance Indicators (KPIs)__ para monitorizar el cumplimiento de los objetivos de la empresa.

## Análisis general
En este sección, describiremos un panorama general de la situación de acceso a Internet en Argentina.
Para cumplir con los análisis propuestos, se trabajó, en principio con los datasets disponibilizados por el Ente Nacional de Comunicaciones (__[ENACOM](https://www.enacom.gob.ar/)__).

Otras fuentes destacadas de información fueron:
* __[Portal de Datos del Gobierno Argentino](https://datos.gob.ar/)__
* Instituto Nacional de Estadísticas y Censos de la República Argentina (__[INDEC](https://www.indec.gob.ar/)__)
* __[Speedtest Global Index](https://www.speedtest.net/global-index)__
* Cámara Argentina de Internet (__[Cabase](https://www.cabase.org.ar/en/home/)__)

Según ENACOM, __la penetración de Internet ha crecido sostenidamente__. Cuando se mide el número de accesos cada 100 hogares, este era de 49.55 en el primer trimestre de 2014 y aumentó a 77.21 en el cuarto trimestre de 2022. Según el [Informe de Cabase](https://app.powerbi.com/view?r=eyJrIjoiYzNmNjIzZGYtMGFjZS00MzExLTk4YTgtZDJjZjg4MGFmNGJlIiwidCI6ImUxMzMxMmI2LTRkOTMtNDMyOC05NjkxLTA1ZTc3ODNiMGVhMSIsImMiOjR9) a agosto de 2023, __el 85,5% de los hogares cuentan con acceso a Internet fijo__. Este fenómeno, aunque con velocidades distintas, se evidencia para todas las provincias. Según el mencionado informe, el 71% de los hogares con Internet fijo están concentrados en Buenos Aires, Capital Federal, Córdoba, Santa Fe y Mendoza, las 5 jurisdicciones más pobladas según el INDEC. 

El análisis de los rangos de velocidades de bajada revela que en 2014, la mayoría de los accesos eran inferiores a 10 Mbps, mientras que solo una minoría superaba los 30 Mbps. A finales de 2022, con la mayor disponibilidad de tecnologías más rápidas y asequibles, se ha observado una tendencia al aumento de las conexiones con velocidades más altas. Según el mencionado informe de Cabase, el __47.34% de los hogares tiene una velocidad de conexión superior a 50 Mbps__. Considerando lo expuesto, resulta fundamental para aquellas empresas que quieran expandir su mercado ofrecer velocidades más altas.

Según la última información disponibilzada por ENACOM, la velocidad media de bajada estaba en alrededor de 70 Mbps para el último trimestre de 2022. [Speedtest](https://www.speedtest.net/global-index/argentina?fixed#market-analysis) señala que el proveedor de Internet fijo con mayor velocidad en Argentina es "Movistar" con una mediana de velocidad de 92.83 Mbps para el Q4-2022 y una mediana de 102.55 Mbps para el Q3-2023. Surge del análisis y también de esta fuente, grandes diferencias entre distintas provincias.

En consonancia con lo anterior, la __banda ancha se ha impuesto__ frente a la banda angosta por su alta velocidad, capacidad de transmitir múltiples flujos de datos simultáneamente y conectividad permanente.

Dentro de las tecnologías de banda ancha, hay 2 que son las más destacadas de los últimos tiempos: __Cablemódem__ y __Fibra óptica__. Cablemódem apareció antes y es de fácil instalación porque usa la misma estructura que la que proveía la TV por Cable. La Fibra óptica es más reciente, alcanza mayores velocidades de bajada y es la que ha ganado terreno más rápidamente. En estos puntos nos detendremos con más detalle al hacer el análisis particular para Super.

## Análisis particular
A pesar de que Super tuvo sus inicios como una empresa de TV por cable, las nuevas tecnologías y cambios en los patrones de consumo de sus clientes, impulsados por el auge de plataformas de streaming y gaming (fuente: [Forbes Argentina](https://www.forbesargentina.com/negocios/gaming-streaming-industrias-impulsan-uso-internet-exportaciones-argentina-n36828)), la llevaron a reorientarse hacia el servicio de Internet fijo. En la actualidad, aproximadamente el 7% de sus ingresos proviene del servicio de TV por cable, mientras que el 80% proviene del servicio de Internet y el 13% se deriva de clientes con paquetes combinados.

Los datos respaldan la decisión de la empresa: al medir la penetración del servicio como el número de accesos por cada 100 habitantes, se observa un crecimiento de menos del 4% en el periodo 2020-2022, alcanzando un máximo de 16.55 en el último trimestre de 2022. En contraste, al aplicar la misma métrica al acceso a Internet fijo, se registra un aumento del 23.97% en el mismo periodo, con un pico en el último trimestre de 2022 de 24.15 accesos por cada 100 habitantes. Además, aunque con velocidades dispares, estas tendencias se replican en las provincias: un __crecimiento prácticamente estancado en el acceso a TV por cable__ y un __crecimiento sostenido en el acceso a Internet fijo__.

En cuanto a las tecnologías de banda ancha, __Cablemódem y Fibra óptica han experimentado un notable crecimiento en los últimos años__. Aunque Cablemódem, al haber aparecido antes, tiene una mayor participación en el mercado, la Fibra óptica ha mostrado un crecimiento excepcional, especialmente desde 2018. Al último trimestre de 2022, el 53.87% de los accesos correspondían a Cablemódem, el 27.31% a Fibra óptica y el 18.82% a otras tecnologías. Si la tendencia actual persiste, es plausible que la Fibra óptica alcance una posición dominante en el mercado.

Para identificar zonas con oportunidad de crecimiento se tomaron en cuenta 3 factores clave:
* __Población:__ Aquellas provincias más pobladas ofrecen un mercado más extenso al cual acceder.
* __Penetración de la fibra óptica:__ En las provincias donde la penetración aún es baja, existe un mayor potencial para expandirse.
* __Geografía:__ Dado que la oferta de servicios de fibra óptica requiere el desarrollo de una red física, orientarse hacia provincias cercanas inicialmente ayuda a reducir los costos de infraestructura.

Para un análisis más detallado se sugiere consultar [EDA_Super.ipynb](EDA_Super.ipynb). No obstante, podemos afirmar que, basándonos en estos criterios, las provincias que representan oportunidades de crecimiento a corto plazo son:
* Capital Federal
* Santiago Del Estero
* Corrientes
* Entre Rios
* Misiones
* Chaco
* Formosa

## KPIs
Los __KPIs (Key Performance Indicator)__ son métricas específicas y cuantificables utilizadas para medir el rendimiento de una organización, un proceso o una actividad en relación con sus objetivos estratégicos. Estos indicadores son esenciales para evaluar el éxito o el progreso hacia metas establecidas y permiten a las empresas tomar decisiones informadas basadas en datos concretos.

En este proyecto trabajaremos con 2 KPIs. Dado que el negocio está buscando expandirse y captar nuevos mercados, su selección ha sido realizada con el fin de evaluar el cumplimiento de dicho objetivo. Hemos establecido provincias particulares en las que nos interesa enfocarnos; ambos KPIs estarán definidos por provincia y por periodos trimestrales, lo que nos permitirá evaluar continuamente su cumplimiento.

### Variación en el acceso a Internet
Consideremos la siguiente métrica:

`VAI = ((Nuevo acceso - Acceso actual) / Acceso actual) * 100`

Donde:
* "Nuevo acceso" se refiere al número de hogares con acceso a Internet después del próximo trimestre.
* "Acceso actual" se refiere al número de hogares con acceso a Internet en el trimestre actual.

Nuestro KPI consiste en "aumentar en un 2% el acceso al servicio de internet para el próximo trimestre, cada 100 hogares, por provincia". Haremos el seguimiento de nuestro KPI con la métrica VAI.

### Tasa de Conversión
Consideremos la siguiente métrica:

`TC = (Número de conversiones / Número de contactos) * 100`

Donde:
* "Número de conversiones" se refiere al número de clientes que contratan el servicio de Fibra óptica, medido al final del trimestre.
* "Número de contactos" se refiere al número de clientes que contactan a un representante para solicitar información sobre el servicio, medido al final del trimestre.

Nuestro KPI consiste en "alcanzar una tasa de conversión del 2% para final del trimestre, por provincia". Haremos el seguimiento de nuestro KPI con la métrica TC.

## Stack tecnológico
El proyecto se desarrolló en Python, haciendo uso de las siguientes bibliotecas y herramientas:

- **Manipulación y Análisis de Datos:** `pandas` | `numpy`
- **Visualización de Datos:** `matplotlib` | `seaborn` | `plotly` | `geopandas`
- **Operaciones en Archivos y Directorios:** `requests` | `shutil`
- **Operaciones Científicas y Análisis de Datos:** `math` | `scipy` | `scikit-learn`

## Archivos
* __[EDA_preliminar.ipynb:](EDA_preliminar.ipynb)__ Análisis exploratorio inicial de la situación de acceso a Internet en Argentina.
* __[EDA_Super.ipynb:](EDA_Super.ipynb)__ Análisis exploratorio con enfásis en las preguntas de negocio y objetivos especificos de Super.
* __[funciones.py:](funciones.py)__ Funciones de uso común.
* __[Datasets:](Datasets/)__ Carpeta con los archivos usados para el análisis.
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
Como Analista de Datos, he sido contratado por [Super](https://es.wikipedia.org/wiki/Super_(empresa), una destacada empresa de telecomunicaciones en Argentina. La empresa fue fundada en 1985 en la provincia de Mendoza, con el objetivo de brindar acceso a TV por cable. Desde entonces, Super ha experimentado un crecimiento significativo, expandiéndose a más de 100 ciudades y 14 provincias del país.

Además de su expansión geográfica, Super ha diversificado su oferta, incorporando el servicio de Acceso a Internet en 1999. Entre las pioneras en el ámbito, la empresa adoptó la tecnología de Cablemódem, aprovechando la infraestructura de televisión por cable para ofrecer servicios de internet de banda ancha.

A partir de 2010, Super ha respondido a las nuevas tecnologías al introducir el servicio de Acceso a Internet a través de Fibra óptica. Esta tecnología, basada en cables de fibra óptica, proporciona ventajas como velocidades de transmisión más altas, mayor confiabilidad y seguridad en comparación con el cablemódem.

En julio de 2018, Super anunció una inversión sustancial de aproximadamente 400 millones de dólares para expandir su red de fibra óptica ([Fuente](https://www.infobae.com/sociedad/2018/07/17/la-compania-de-television-por-cable-e-internet-supercanal-tiene-nuevos-duenos/)). Este movimiento estratégico ha llevado a la migración casi completa a la fibra óptica, marcando el abandono de la tecnología de Cablemódem en la mayoría de las ciudades. Al día de hoy, su principal ingreso lo constituye la Fibra óptica, seguido de la TV por cable. Estos servicios se venden en forma conjunta o separada.

Este proyecto tiene como objetivo principal analizar los datos actuales de Super, con foco en:
* Evaluar la situación nacional y provincial de los servicios de TV por cable e Internet.
* Reevaluar la ventaja de invertir en Fibra óptica frente a Cablemódem, respaldándose en datos concretos.
* Identificar oportunidades para la mejora y el crecimiento continuo.
* Desarrollar Key Performance Indicators (KPIs) para monitorear el cumplimiento de los objetivos de la empresa.


## Análisis general
En este sección, describiremos un panorama general de la situación de acceso a Internet en Argentina.
Para cumplir con los análisis propuestos, se trabajó en principio con los datasets disponibilizados por el Ente Nacional de Comunicaciones ([ENACOM](https://www.enacom.gob.ar/)).

Otras fuentes destacadas de información fueron:
* [Portal de Datos del Gobierno Argentino](https://datos.gob.ar/)
* Instituto Nacional de Estadísticas y Censos de la República Argentina ([INDEC](https://www.indec.gob.ar/))
* [Speedtest Global Index](https://www.speedtest.net/global-index)
* Cámara Argentina de Internet ([Cabase](https://www.cabase.org.ar/en/home/))

Según ENACOM, la penetración de Internet ha crecido sostenidamente. Cuando se mide el número de accesos cada 100 hogares, este era de 49,55 en el primer trimestre de 2014 y aumentó a 77,21 en el cuarto trimestre de 2022. Según el [Informe de Cabase](https://app.powerbi.com/view?r=eyJrIjoiYzNmNjIzZGYtMGFjZS00MzExLTk4YTgtZDJjZjg4MGFmNGJlIiwidCI6ImUxMzMxMmI2LTRkOTMtNDMyOC05NjkxLTA1ZTc3ODNiMGVhMSIsImMiOjR9) a Agosto de 2023, el 85,5% de los hogares cuentan con acceso a Internet fijo. Este fenómeno, aunque con velocidades distintas, se evidencia para todas las provincias. Según el mencionado informe, el 71% de los hogares con Internet fijo están concentrados en Buenos Aires, Capital Federal, Córdoba, Santa Fe y Mendoza, las 5 jurisdicciones más pobladas según el INDEC. 

Del análisis de los rangos de velocidades de bajada, se observa que en 2014 la mayoría de los accesos eran inferiores a 10 Mbps, mientras que solo una minoría superaba los 30 Mbps. A finales de 2022, con la mayor disponibilidad de tecnologías más rápidas y asequibles, se ha observado una tendencia al aumento de las conexiones con velocidades más altas. Según el mencionado informe de Cabase, el 47.34% de los hogares tiene una velocidad de conexión superior a 50 Mbps. Considerando lo expuesto, resulta fundamental para aquellas empresas que quieran expandir su mercado ofrecer velocidades más altas.

Según la última información disponibilzada por ENACOM, la velocidad media de bajada estaba en alrededor de 70 Mbps para el último trimestre de 2022. [Speedtest](https://www.speedtest.net/global-index/argentina?fixed#market-analysis) señala que el proveedor de Internet fijo con mayor velocidad en Argentina es "Movistar" con una mediana de velocidad de 92.83 Mbps para el Q4-2022 y una mediana de 102.55 Mbps para el Q3-2023. Surge del análisis y también de esta fuente, grandes diferencias entre distintas provincias.

En consonancia con lo anterior, la banda ancha se ha impuesto frente a la banda angosta por su alta velocidad, capacidad de transmitir múltiples flujos de datos simultaneamente y conectividad permanente.

Dentro de las tecnologías de banda ancha, hay 2 que son las mas destacadas de los últimos tiempos: Cablemodem Y Fibra óptica. Cablemodem apareció antes, y es de fácil instalación y porque usaba la misma estructura que la que proveía la TV por Cable. Fibra óptica es más reciente, alcanza mayores velocidades de bajada y es la que ha ganado terreno más rápido. En estos puntos nos detendremos con más detalle al hacer el análisis particular para Super.

## Análisis particular
Si bien Super nació como una empresa de TV por cable, las nuevas tecnologías y cambios en los patrones de consumo de sus clientes ([plataformas de streaming y gaming](https://www.forbesargentina.com/negocios/gaming-streaming-industrias-impulsan-uso-internet-exportaciones-argentina-n36828)), la llevaron a reorientarse al servicio de internet fijo. Hoy en día, solo cerca del 7% de sus ingresos provienen del servicio de TV por Cable, 80% del servicio de internet y 13% de cleintes con paquetes combinados.

Los datos sostienen la decisión de la empresa: cuando se mide la penetracción del servicio como número de accesos cada 100 habitantes, se verifica que este creció menos del 4% en el periodo 2020-2022, con un máximo de 16.55 en el último trimestre de 2022. Al considerar la misma métrica para el acceso a Internet fijo, el aumento fue de 23.97% en el mismo periodo, con un máximo en el último trimestre de 2022 de 24.15 accesos cada 100 habitantes. Además, aunque con velocidades dispares, las mismas tendencias se observaron en las provincias: casi estancamiento del acceso a TV por Cable y crecimiento de Internet fijo.

Respecto a las tecnologías de banda ancha, Cablemodem y Fibra óptica son las que más han crecido en los últimos años. Cablemodem apareció antes por lo que aún domina el mercado pero Fibra óptica es la que ha crecido a mayor velocidad, sobretodo desde 2018. Al último trimestre de 2022, del total de los accesos, 53.87% corresponden a Cablemodem, 27.31% a Fibra óptica y 18.82% a otras tecnologías. De sostenerse la tendencia actual, sería esperable que Fibra óptica tome la posición dominante en el mercado.

Para identificar zonas con oportunidad de crecimiento se tomaron en cuenta 3 factores:
* __Población:__ aquellas provincias más pobladas tienen un mercado más grande al cuál acceder.
* __Penetración de la fibra óptica:__ en aquellas provincias donde la penetración aún es baja, hay mas potencial para expandirse.
* __Geografía:__ dado que ofrecer servicios de fibra óptica requieren el desarrollo de una red física, el orientarse a provincias cercanas aminora en principio los costos de infraestructura.

Para un análisis en mayor profundidad se sugiere consultar [EDA_Super.ipynb](EDA_Super.ipynb), pero podemos afirmar, que con base a estos criterios, aquellas provincias que representan oportunidades de crecimiento en el más corto plazo son:
* Capital Federal
* Santiago Del Estero
* Corrientes
* Entre Rios
* Misiones
* Chaco
* Formosa

## KPIs
Los __KPIs__ (Key Performance Indicator) son métricas específicas y cuantificables utilizadas para medir el rendimiento de una organización, un proceso o una actividad en relación con sus objetivos estratégicos. Estos indicadores son esenciales para evaluar el éxito o el progreso hacia metas establecidas y permiten a las empresas tomar decisiones informadas basadas en datos concretos.

En este proyecto trabajaremos con 2 KPIs. Dado que el negocio está buscando expandirse y captar nuevos mercados, su selección ha sido relizada en pos de evaluar el cumplimiento de dicho objetivo. Dado que hemos establecido provincias particulares en las que nos interesa enfocarnos, ambos estarán definidas por provincia, además de estar definidas por periodos trimestrales, para ir evaluando su cumplimiento.

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
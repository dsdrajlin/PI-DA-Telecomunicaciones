# Análisis del Mercado de Telecomunicaciones para "Super".

## Introducción
Como Analista de Datos, he sido contratado por Super (anteriormente conocida como [Supercanal](https://es.wikipedia.org/wiki/Super_(empresa))), una destacada empresa de telecomunicaciones en Argentina. La empresa fue fundada en 1985 en la provincia de Mendoza, con el objetivo de brindar acceso a TV por cable. Desde entonces, Super ha experimentado un crecimiento significativo, expandiéndose a más de 100 ciudades y 14 provincias del país.

Además de su expansión geográfica, Super ha diversificado su oferta, incorporando el servicio de Acceso a Internet en 1999. Entre las pioneras en el ámbito, la empresa adoptó la tecnología de Cablemódem, aprovechando la infraestructura de televisión por cable para ofrecer servicios de internet de banda ancha.

A partir de 2010, Super ha respondido a las nuevas tecnologías al introducir el servicio de Acceso a Internet a través de Fibra óptica. Esta tecnología, basada en cables de fibra óptica, proporciona ventajas como velocidades de transmisión más altas, mayor confiabilidad y seguridad en comparación con el cablemódem.

En julio de 2018, Super anunció una inversión sustancial de aproximadamente 400 millones de dólares para expandir su red de fibra óptica ([Fuente](https://www.infobae.com/sociedad/2018/07/17/la-compania-de-television-por-cable-e-internet-supercanal-tiene-nuevos-duenos/)). Este movimiento estratégico ha llevado a la migración casi completa a la fibra óptica, marcando el abandono de la tecnología de Cablemódem en la mayoría de las ciudades.

Este proyecto tiene como objetivo principal analizar los datos actuales de Super, con foco en:
* Evaluar la situación nacional y provincial de los servicios de TV por cable e Internet.
* Reevaluar la ventaja de invertir en Fibra óptica frente a Cablemódem, respaldándose en datos concretos.
* Identificar oportunidades para la mejora y el crecimiento continuo.
* Desarrollar Key Performance Indicators (KPIs) para monitorear el cumplimiento de los objetivos de la empresa en este dinámico mercado de telecomunicaciones.



## Análisis general
Contexto de internet en el pais y hallazgos

## Análisis particular
Exploración en particular y conclusiones

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

## Archivos
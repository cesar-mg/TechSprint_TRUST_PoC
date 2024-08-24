[![Quality Gate Status](https://sonarcloud.io/api/project_badges/measure?project=EL-BID_data-repository-Mapainversiones&metric=alert_status)](https://sonarcloud.io/summary/new_code?id=EL-BID_data-repository-Mapainversiones)


# data-Mapainversiones
MapaInversiones es una plataforma que fomenta la transparencia del gasto, las inversiones y las contrataciones públicas en América Latina y el Caribe mediante la integración y visualización de datos públicos. Las diferentes instancias de MapaInversiones implementadas en los países generan conjuntos de datos abiertos para que los ciudadanos y organizaciones interesadas puedan realizar sus análisis propios basados en esta información. Este repositorio en https://github.com/EL-BID/data-Mapainversiones es una capacidad de la solución que permite acceder y descargar de manera agrupada los conjuntos de datos abiertos de las plataformas de los países relacionados.

## Usage

The scripts work with python 3.5+. To install the requirements, run:

```bash
pip install -r scripts/requirements.txt
```

In order to run full load
```
python scripts/full_load.py
```

Extracted datasets will be copied from client bucket to r2 `air` bucket

In order to increment load
```
python scripts/increment_load.py
```

To create `toc` and `datapackage.json`, please use help functions in `process.py`

## Metadata
### Package descriptor sample


```json
{
  "hash": "7d1af14084147c32ef3b53e2c9418d0e",
  "profile": "data-package",
  "name": "presupuesto-pry",
  "title": "Presupuesto",
  "country": "PRY",
  "contributors": [
    {
      "title": "Hacienda",
      "email": "",
      "path": "",
      "role": "author",
      "organization":""
    }
  ],
  "sources": [
    {
      "title": "Presupuesto",
      "path": "",
      "email": ""
    }
  ],
  "resources": []
}

```

### Resource descriptor with tableschema sample

```json
{
  "dialect": {
    "caseSensitiveHeader": false,
    "delimiter": ",",
    "doubleQuote": true,
    "header": true,
    "lineTerminator": "\r\n",
    "quoteChar": "\"",
    "skipInitialSpace": false
  },
  "encoding": "utf-8",
  "format": "csv",
  "hash": "54755420f612237c5345b7870571948c",
  "name": "proyectos",
  "path": "https://air.portaljs.com/opendata/DOM/MAPAINVDB/OPENDATA/PROYECTOS/CSV/2024/06/19/PROYECTOS.CSV",
  "toc": "https://air.portaljs.com/opendata/DOM/MAPAINVDB/OPENDATA/PROYECTOS/toc_PROYECTOS.csv",
  "profile": "tabular-data-resource",
  "schema": {
    "fields": [
      {
        "format": "default",
        "name": "IdProyecto",
        "type": "integer"
      },
      {
        "format": "default",
        "name": "codigosnip",
        "type": "integer"
      } ...
    ],
    "missingValues": [
      ""
    ]
  }
}
```

### Table of content

`toc` - table of content file is used to show all resources with their dates in csv format.

`path` in resource descriptor shows the latest resource

It is part of resource descriptor in the following structure

```CSV
year, URL
2024-05-01, path_to_resource
2024-05-06, path_to_resource
``` 
### Raw data

Raw data is added into resource descriptor section as `source` attribute with the following fields.
``` json
"sources": [
  {
    "name": "PARTIDAS_DE_GASTO",
    "url": "https://mapainversionesanalytics.blob.core.windows.net/sourceraw/DOM/HACIENDA/PARTIDAS_DE_GASTO/CSV/2024/05/01/mh_partidas_de_gasto.csv",
    "description_url": "https://docs.google.com/spreadsheets/d/1L2X8LZWSr9EseLdXPIwij-LkwwJieAxDWbdq3I1MYtM/edit?gid=2117212777#rangeid=558022531"
  }
]
```

### Translations

description_translations field is applied to the following attributes:
* package_title
* package_description
* resource_title
* resource_description
* schema -> description

```
"description_translations": {
  "es": "Código que identifica un subprograma dentro de un programa."
}
```


## Data
### Paraguay datasets - total 3 datasets with 7 resources
|Country|Package name|Resource name|Owner|
|-|-|-|-|
PRY|investment-projects-pry| paraguay-investment-projects|SNIP|
PRY|investment-projects-pry|investment-projects-budget-execution|SNIP|
PRY|investment-projects-pry|investment-projects-components|SNIP|
PRY| general-budget-pry| general-budget | Hacienda |
PRY|general-budget-pry|general-budget-indicators| Hacienda |
PRY|national-development-plan-pry|budget-by-entity|Secretaría Técnica de Planificación|
PRY|national-development-plan-pry| indicators |Secretaría Técnica de Planificación|


### Dominican Republic datasets - total 3 datasets with 11 resources
|Country|Package name|Resource name|Owner|
|-|-|-|-|
DOM|investment-projects-dom|investment-projects|SNIP|
DOM|general-budget-information-on-investment-dom| presupuesto-de-inversion| Hacienda |
DOM|general-budget-information-on-investment-dom| procesos-de-compras|Hacienda / DGCP|
DOM|general-budget-information-on-investment-dom| contratos-de-compras|Hacienda / DGCP|
DOM|general-budget-information-on-investment-dom| presupuesto-relacionado-a-proyectos-de-inversion|Hacienda / SNIP|
DOM|emergency-processes-and-contracts-and-budget-dom| procurement-process|Hacienda / SNIP|
DOM|emergency-processes-and-contracts-and-budget-dom| procurement-process-item-level|Hacienda / SNIP|
DOM|emergency-processes-and-contracts-and-budget-dom| contract|Hacienda / SNIP|
DOM|emergency-processes-and-contracts-and-budget-dom| contract-item-level|Hacienda / SNIP|
DOM|emergency-processes-and-contracts-and-budget-dom| suppliers|Hacienda / SNIP|
DOM|emergency-processes-and-contracts-and-budget-dom| budget|Hacienda / SNIP|


### Argentina datasets - total 1 dataset with 3 resources
|Country|Package name|Resource name|Owner|
|-|-|-|-|
ARG|investment-projects-and-works-arg|spatial-data-works|Secretary of Public Works of the Ministry of Economy of the Argentine Republic|
ARG|investment-projects-and-works-arg|investment-projects|Secretary of Public Works of the Ministry of Economy of the Argentine Republic|
ARG|investment-projects-and-works-arg|datos-ESPACIALES|Secretary of Public Works of the Ministry of Economy of the Argentine Republic|

### Jamaica Republic datasets - total 1 dataset with 1 resources
|Country|Package name|Resource name|Owner
|-|-|-|-|
JAM|investment-projects-jam|investment-projects|Project Bank - Ministry of Finance & the Public Service Jamaica|


### Honduras Republic datasets - total 1 dataset with 3 resources
|Country|Package name|Resource name|Owner
|-|-|-|-|
HON|investment-projects-hnd|public-investment|Secretary of Finance of Honduras (SEFIN) / Regulatory Office of Contracting and Acquisitions of the State of Honduras (ONCAE)|
HON|investment-projects-hnd|general-budget|Secretary of Finance of Honduras (SEFIN) / Regulatory Office of Contracting and Acquisitions of the State of Honduras (ONCAE)|
HON|investment-projects-hnd|thematic-budgets|Secretary of Finance of Honduras (SEFIN) / Regulatory Office of Contracting and Acquisitions of the State of Honduras (ONCAE)|

### Panama Republic datasets - total 1 dataset with 2 resources
|Country|Package name|Resource name|Owner
|-|-|-|-|
PAN|investment-projects-pan|investment-projects|Ministry of Economy and Finance of Panama (MEF)
PAN|investment-projects-pan|presupuesto|Ministry of Economy and Finance of Panama (MEF)

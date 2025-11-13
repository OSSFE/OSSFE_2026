---
title: 'FAIR and Flexible: Fusion Data Mapping with TokaMap and libTokaMap'
authors:
  - name: Jonathan Hollocombe
    affiliations:
      - UKAEA
  - name: Adam Parker
    affiliations:
      - UKAEA
  - name: Stephen Dixon
    affiliations:
      - UKAEA
license: CC-BY-4.0
exports:
  - format: pdf
    template: ../../template
site:
  hide_toc: false
---

Fusion data scientists spend the majority of their time preparing data — cleaning, transforming, and converting it between formats — rather than analysing it and extracting new insights. This process requires scientists to convert data between different formats and structures, usually via a manual and error-prone process.

The TokaMap project aims to establish a generic and open infrastructure for FAIR data mappings, with an initial focus on fusion energy research. TokaMap provides a self-describing, FAIR-compliant representation of data mappings, embedding the information to transform data between different formats and serialisations. This enables data mappings that require less time to write and maintain, can be run in different tools without modification, and can be openly shared between experiments.

The mappings schema is detailed in the TokaMap repository, with documentation detailing how to create TokaMap mappings for fusion experiments alongside tools for validation and verification of the mappings.

Alongside the TokaMap schema, we have also created a reference implementation available in the libTokaMap repository, providing an open source mechanism to use the TokaMap scheme in practice. This is a C++ library focused on providing a performant and extensible tool that can use TokaMap mapping files to transform fusion data in a variety of different workflow settings. LibTokaMap also has a Python wrapper which can be installed via pip, and allows for injection of Python data sources into the underlying C++ library, allowing for a pure Python mapping environment.

The talk will provide details of TokaMap and libTokaMap; details of the schema, how to create your own mappings, and how to run these mappings either in Python or by integrating libTokaMap into your own infrastructure. The tutorial will go into further details, provide a hands-on opportunity for people to create mappings and leverage the power of the TokaMap schema, and allow people to provide feedback to steer the TokaMap schema going forwards.

# Repository
https://github.com/ukaea/tokamap & https://github.com/ukaea/libtokamap


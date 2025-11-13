---
title: 'SimDB: A tool to manage IMAS simulations'
authors:
  - name: Deepak Maroo
    affiliations:
      - ITER Organization
  - name: Olivier Hoenen
    affiliations:
      - ITER Organization
  - name: Jonathan Hollocombe
    affiliations:
      - UKAEA
  - name: Simon Pinches
    affiliations:
      - ITER Organization
license: CC-BY-4.0
exports:
  - format: pdf
    template: ../../template
site:
  hide_toc: false
---

The Integrated Modelling & Analysis Suite (IMAS) developed by ITER is a software eco-system composed of three software layers which the ITER Organization (IO) is progressively making available under open-source licences. The first layer, called the Data Dictionary (or DD, available at  https://github.com/iterorganization/IMAS-Data-Dictionary), is the machine-agnostic data model that describes data and systems in a tokamak with a set of Interface Data Structures (IDS) and strives to be a community-wide data standard. The second layer is composed of several general-purpose tools and libraries to interact with data that respect the DD standard: from APIs for data access and manipulation in a given programming language (e.g. in Python https://github.com/iterorganization/IMAS-Python) to scripts and tools for data visualization (e.g. https://github.com/iterorganization/IMAS-ParaView). The third layer comprises the integrated physics modelling software and data analysis pipelines that produce results following the IMAS data standard.

As more and more simulation packages are interfaced to IMAS, a tool has been developed to allow building and searching through databases of such simulations. This tool, called SimDB (https://github.com/iterorganization/SimDB), was recently made open-source, together with its web-based user interface (https://github.com/iterorganization/SimDB-Dashboard). This poster will present SimDB’s core client-server architecture, and its integration with other open-source software that comprise the IMAS eco-system. The typical workflow for ingesting new simulations will be described by taking examples from the ITER scenarios database. Finally, we will list ongoing plans and share thoughts on making standardized simulation metadata openly accessible.

# Repository
https://github.com/iterorganization/SimDB and https://github.com/iterorganization/SimDB-Dashboard


---
title: 'Open-source MDSplus and Trends in Fusion Data'
authors:
  - name: Joshua Stillerman
    affiliations:
      - MIT Plasma Science and Fusion Center
  - name: Timothy Heidcamp
    affiliations:
      - MIT Plasma Science and Fusion Center
  - name: Stephen Lane-Walsh
    affiliations:
      - MIT Plasma Science and Fusion Center
  - name: Fernando Santoro
    affiliations:
      - MIT Plasma Science and Fusion Center
  - name: Mark Winkel
    affiliations:
      - MIT Plasma Science and Fusion Center
license: CC-BY-4.0
exports:
  - format: pdf
    template: ../../template
site:
  hide_toc: false
github: 'https://github.com/OSSFE/OSSFE_2026'
---

Abstract
MDSplus has long served as a cornerstone for managing scientific data in magnetic fusion research. As experiments evolve and the community moves toward steady-state devices and eventual power plants, user requirements are shifting dramatically in scale and character. Discharge lengths are growing and plant operations generate ever larger volumes of continuous data. Researchers increasingly expect portable, cloud-friendly archives that support rich annotation, adherence to FAIR principles, and machine-learning pipelines.


This evolution demands fundamental shifts in how fusion data systems are architected, with power plant operations expected to produce predominantly continuous operational data punctuated by periodic and event driven diagnostic measurement bursts. Meeting these needs will require a data system that supports wall-clock–based storage, incremental storage and analysis workflows, rapid retrieval of both continuous plant signals and event-driven data, and web-based tools that enable collaborative access and visualization across distributed research environments.


This paper discusses early design efforts to extend open-source MDSplus in response to these emerging demands. We outline key system requirements and present initial prototypes focusing on web-based data display and device configuration, and wall-clock data storage as testbeds for these capabilities. The technical approaches being explored within the open-source MDSplus framework demonstrate potential pathways for creating flexible, future-ready data infrastructure that can accommodate both current experimental needs and the requirements of commercial fusion energy systems.


By aligning development with the evolving needs of fusion facilities and the broader scientific community, this work contributes to ongoing discussions about scalable, sustainable data management strategies essential for fusion energy's transition from research to power generation.


# Repository
https://github.com/MDSplus/mdsplus


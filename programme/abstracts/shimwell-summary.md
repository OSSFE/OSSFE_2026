---
title: 'Summary of V&V efforts for OpenMC'
authors:
  - name: J. Shimwell
    affiliations:
      - Proxima Fusion
license: CC-BY-4.0
exports:
  - format: pdf
    template: ../../template
site:
  hide_toc: false
github: 'https://github.com/OSSFE/OSSFE_2026'
---


Accurate neutronics simulations of fusion reactors are essential for both performance assessment and safety analysis.
Such simulations provide key insights into safety considerations, including radiation dose and material damage, as well as performance metrics such as blanket heating and tritium production.
Confidence in particle transport simulations is therefore critical to the design and operation of fusion devices.
Extensive, reproducible, and transparent verification and validation (V&V) activities are central to building trust in the predictive capability of neutronics software.
In fission environments, V&V of neutronics codes is well established, supported by a wealth of experimental data.
Criticality experiments, in particular, provide highly precise benchmarks for comparing simulations with measurements, with reactivity determined to within a few parts per million (pcm).
By contrast, V&V of neutronics codes for fusion environments remains less developed.
The higher-energy neutrons produced in deuterium–tritium (DT) fusion are less accessible, and available sources are not characterized to the same accuracy as those used in fission experiments.
Although neutron transport in fission and fusion shares many fundamental similarities, the broader energy spectrum of fusion neutrons leads to a wider range of nuclear reactions and transmutation products, requiring dedicated validation.
This is especially relevant for DT fusion, where 14.1 MeV neutrons can induce numerous threshold reactions absent in fission reactors.
This report summarizes current and ongoing V&V efforts for OpenMC in fusion contexts and outlines recommendations for future work.

# Repository
https://github.com/fusion-energy/openmc-v-and-v


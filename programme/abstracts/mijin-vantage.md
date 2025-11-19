---
title: 'VANTAGE-Reactions - a library for treating reactive physics in performance-portable particle codes built with NESO-Particles'
authors:
  - name: S. Mijin
    affiliations:
      - UKAEA
  - name: S. Gadgil
    affiliations:
      - UKAEA
  - name: W. Saunders
    affiliations:
      - UKAEA
  - name: O. Samant
    affiliations:
      - UKAEA
  - name: M. Hardman
    affiliations:
      - UKAEA
  - name: M. Kryjak
    affiliations:
      - UKAEA
  - name: J. Cook
    affiliations:
      - UKAEA
license: CC-BY-4.0
exports:
  - format: pdf
    template: ../../template
site:
  hide_toc: false
github: 'https://github.com/OSSFE/OSSFE_2026'
---

In many particle code use cases the simulated particles undergo transformations related to various atomic or molecular processes, which can range from exciting internal degrees of freedom to the production of one or more new particles. For fusion, a use case of major interest is the modeling of neutral particle dynamics in the tokamak exhaust, where plasma-neutral interactions tend to dominate. Recent research highlights in particular the role of molecular processes in diverted plasmas[1,2]. 

To this end, we have developed VANTAGE-Reactions - a library based on the performance-portable particle framework NESO-Particles, where we provide tools to treat 0D reactive plasma-neutral interaction physics, such as atomic and molecular interactions, as well as surface processes. In this contribution we will present the design of the library, choices of supported algorithms, as well as initial library benchmarking results as well as progress with coupling to the Hermes-3[3] finite volume plasma code. 


[1] A. S. Kukushkin et al., “Role of molecular effects in divertor plasma recombination,” Nuclear Materials and Energy, vol. 12, pp. 984–988, 2017, doi: 10.1016/j.nme.2016.12.030.
[2] K. Verhaegh et al., “Spectroscopic investigations of detachment on the MAST Upgrade Super-X divertor,” Nuclear Fusion, vol. 63, no. 1, Jan. 2023, doi: 10.1088/1741-4326/aca10a.
[3] B. Dudson et al., “Hermes-3: Multi-component plasma simulations with BOUT++,” Computer Physics Communications, vol. 296, p. 108991, Mar. 2024, doi: 10.1016/j.cpc.2023.108991.


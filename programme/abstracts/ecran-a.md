---
title: 'A Transformer Neural Operator Surrogate for Coupled Neutron-Photon Transport in Fusion Blanket Design'
authors:
  - name: Zara Ercan
    affiliations:
      - Zenithon AI
  - name: Hong Chul Nam
    affiliations:
      - ETH Zurich
  - name: Hrishikesh Viswanath
    affiliations:
      - Perdue University
  - name: Abetharan Antony
    affiliations:
      - Zenithon AI
license: CC-BY-4.0
exports:
  - format: pdf
    template: ../../template
site:
  hide_toc: false
github: 'https://github.com/OSSFE/OSSFE_2026'
---

Coupled neutron-photon transport simulations underpin design decisions in fusion, including blanket thermal management, tritium breeding optimization, and magnet shielding verification in MCF devices. However, Monte Carlo methods such as OpenMC require substantial computational resources—often billions of particle histories—to achieve converged mesh tallies in geometrically complex configurations. This computational burden severely limits design iteration during early-stage scoping and multidisciplinary optimization workflows requiring rapid evaluation of thermal source terms for downstream CFD coupling.

We present a transformer-based neural operator trained on high-fidelity OpenMC simulations that maps radial-build design parameters of an ARC-class tokamak to (i) spatially-resolved volumetric heating and tritium production rate fields queryable at arbitrary continuous coordinates, and (ii) integrated quantities including neutron-photon leakage flux at the blanket-tank boundary—a proxy metric for magnet shielding performance that avoids the prohibitive cost of deep-penetration tallies within superconducting coils. The architecture leverages attention mechanisms to capture long-range spatial correlations in the radiation transport problem while maintaining resolution invariance across varying mesh densities.

The surrogate achieves high accuracy (< 10% relative error) across spatial fields and integrated boundary currents while delivering inference 10000x speedups compared to converged Monte Carlo calculations. This tolerance is appropriate for rapid design-space exploration, with final configurations subsequently verified via full-fidelity simulations. We demonstrate application to ARC-like blanket trade studies, enabling real-time evaluation of first-wall, coolant channel, blanket, and vacuum vessel heating distributions that would otherwise require hours to days of Monte Carlo simulation per design point. This work serves as a foundational step toward a geometry-agnostic higher accuracy ML framework for neutron-photon transport, with the goal of enabling rapid surrogate deployment across diverse reactor configurations and nuclear system geometries.


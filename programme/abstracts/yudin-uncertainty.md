---
title: 'Uncertainty Quantification Tools for Lithium Ceramics-based Tritium Breeding Module'
authors:
  - name: Yehor Yudin
    affiliations:
      - Bangor University
  - name: Tom Griffiths
    affiliations:
      - Bangor University
  - name: Tom Smith
    affiliations:
      - Bangor University
  - name: Tessa Davey
    affiliations:
      - Bangor University
  - name: Cillian Cockrell
    affiliations:
      - Bangor University
license: CC-BY-4.0
exports:
  - format: pdf
    template: ../../template
site:
  hide_toc: false
---

In this work, we present a set of software tools for Uncertainty Quantification and Sensitivity Analysis of solid Lithium ceramics-based Tritium breeding module modelling.

This contribution focuses on Finite Element Method modeling of Lithium-based materials on meso- and macroscopic continuum scales for material grains and kernels, suitable for simulating various fusion reactor components, with a specific emphasis on solid-state breeder blanket materials.

A non-intrusive forward uncertainty propagation approach, utilising Polynomial Chaos Expansion and Monte Carlo, is applied to a number of material models, with a particular focus on Lithium-based ceramics.

This provides the functionality to capture uncertainties in tritium trapping and release arising from uncertainties on atomistic scales, neutronics computations, and data, as well as other sources of material properties and engineering conditions, such as gas diffusivity, heat conductivity, and ambient conditions.

We utilise the open-source FEniCSx/DOLFINx FEM library and FESTIM code for materials modelling, and the EasyVVUQ library to perform uncertainty quantification.

Furthermore, an effort to apply the Intrusive Uncertainty Quantification method based on the Stochastic Finite Element Method is presented.

# Repository
https://github.com/YehorYudinIPP/festim_niuq


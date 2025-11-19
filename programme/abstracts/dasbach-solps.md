---
title: 'SOLPS-NN: Neural Networks for Scrape-Off Layer Simulations'
authors:
  - name: Stefan Dasbach
    affiliations:
      - DIFFER
  - name: David vander Mijnsbrugge
    affiliations:
      - DIFFER
  - name: Rick van Schaik
    affiliations:
      - DIFFER
  - name: Sven Wiesen
    affiliations:
      - DIFFER
license: CC-BY-4.0
exports:
  - format: pdf
    template: ../../template
site:
  hide_toc: false
github: 'https://github.com/OSSFE/OSSFE_2026'
---

Managing divertor heat fluxes is a central challenge for tokamak operation. Exhaust modeling codes such as SOLPS-ITER provide the required physical fidelity but are computationally expensive and notoriously difficult to use. To address this, we present SOLPS-NN, a software package that employs neural networks trained on a broad cross-machine SOLPS-ITER database as fast and accessible surrogate models. The package is designed for users without deep learning expertise, enabling rapid exploration of scrape-off layer dynamics.
We benchmark these models against higher-fidelity SOLPS-ITER simulations across different devices and find that they reproduce key plasma behavior with surprising accuracy. Strategies for tailoring the models to specific machines with additional simulations further enhance their predictive power.
Potential applications include scoping of exhaust operational space, coupling to core plasma models for integrated simulations, uncertainty propagation, initialization of SOLPS-ITER runs, and inverse optimization to match target profiles. We also outline future development paths and the challenges of advancing these surrogates toward broader applicability in fusion research.


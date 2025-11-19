---
title: 'Raytrax - an ECRH ray tracer based on JAX'
authors:
  - name: David Straub
    affiliations:
      - Munich University of Applied Sciences HM
  - name: Michael Brookman
    affiliations:
      - Proxima Fusion
  - name: Nikolai Marushchenko
    affiliations:
      - IPP
license: CC-BY-4.0
exports:
  - format: pdf
    template: ../../template
site:
  hide_toc: false
github: 'https://github.com/OSSFE/OSSFE_2026'
---

Raytrax is a new electron cyclotron resonance heating (ECRH) microwave ray tracing code based on the physics approach of TRAVIS. While TRAVIS is implemented in Fortran, Raytrax has been written from scratch in Python leveraging advanced just-in-time compilation and automatic differentiation features provided by JAX. The near-term goal of Raytrax is to provide an accessible, pedagogical implementation of the well-known ray tracing equations that can be used to cross-check other codes' results. The long-term goal is to leverage automatic differentiation to facilitate gradient-based optimization of ECRH heating locations in the conceptual design phase of fusion power plants.

# Repository
github.com/proximafusion/raytrax


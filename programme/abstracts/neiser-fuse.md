---
title: 'FUSE Integrated Modeling Framework for FPP design, Scenario Optimization and Model Validation'
authors:
  - name: T.F. Neiser
    affiliations:
      - General Atomics (GA)
  - name: B.C. Lyons
    affiliations:
      - GA
  - name: O. Meneghini
    affiliations:
      - Proxima Fusion
  - name: T. Slendebroek
    affiliations:
      - UCSD
  - name: J. McClenaghan
    affiliations:
      - GA
  - name: A. Ghiozzi
    affiliations:
      - Aurora Fusion
  - name: G. Avdeeva
    affiliations:
      - GA
  - name: T.B. Cote
    affiliations:
      - GA
  - name: S.S. Denk
    affiliations:
      - GA
  - name: G. Dose
    affiliations:
      - GA
  - name: A. Gupta
    affiliations:
      - GA
  - name: J. Guterl
    affiliations:
      - GA
  - name: N. Shi
    affiliations:
      - GA
  - name: S.P. Smith
    affiliations:
      - GA
  - name: L. Stagner
    affiliations:
      - GA
  - name: D. Weisberg
    affiliations:
      - GA
  - name: M.G. Yoo
    affiliations:
      - GA
  - name: H. Anand
    affiliations:
      - GA
  - name: R. Nazikian
    affiliations:
      - GA
  - name: B. Sammuli
    affiliations:
      - GA
  - name: E. Belli
    affiliations:
      - GA
  - name: J. Candy
    affiliations:
      - GA
license: CC-BY-4.0
exports:
  - format: pdf
    template: ../../template
site:
  hide_toc: false
---

The FUSE integrated-modeling suite is an open-source software with capabilities relevant for fusion pilot plant (FPP) design, scenario optimization and model validation (https://fuse.help). Developed in the Julia programming language, FUSE is fully open-source under the Apache 2.0 license, promoting transparency and collaboration within the fusion research community. Built upon centralized data exchange, FUSE is composed of a collection of independent “actors” each of which reads inputs and writes output to a central, hierarchical data structure based on the IMAS ontology. This facilitates collaboration with public and private sector reactor design and scenario optimization efforts, for example allowing users to bring their own neural network models and actors to plug-and-play in FUSE. The FPP design capability of FUSE hinges on this tight coupling between modular actors that cover the design space from plasma core to the site boundary, allowing fast evaluation of self-consistent design points and minimizing the need for iterative expert evaluations. Scenario optimization benefits from FUSE’s implicit time-dependent modeling capability in both feedforward and feedback modes with controllers, with a Grad-Hogen-like solver in active development. Large database model validation has been carried out with the FUSE framework to identify and deploy the most accurate transport models for reactor design. All of these workflows have been accelerated with neural network representations of equilibrium, MHD stability, pedestal and multi-fidelity transport models. In total, FUSE is prepared to provide digital-twin tools for experimental analysis, predict-first pulse design, and FPP optimization, making it a valuable resource to bring fusion energy to the grid.

# Repository
https://fuse.help


---
title: 'Pellet Fueling: AI-Enhanced Surrogate Model HPI2-NN and Integrated Modelling'
authors:
  - name: A. Panera Alvarez
    affiliations:
      - DIFFER
  - name: E. Geulin
    affiliations:
      - IRFM CEA Cadarache
  - name: F. Koechl
    affiliations:
      - ITER Organization
  - name: P. Lang
    affiliations:
      - IPP Garching
  - name: S. Wiesen
    affiliations:
      - DIFFER
  - name: C. Bourdelle
    affiliations:
      - IRFM CEA Cadarache
license: CC-BY-4.0
exports:
  - format: pdf
    template: ../../template
site:
  hide_toc: false
github: 'https://github.com/OSSFE/OSSFE_2026'
---

Effective core fuelling remains one of the fundamental challenges in magnetically confined fusion plasmas, particularly in reactor-relevant regimes such as those expected in ITER. Among the available strategies, pellet injection has demonstrated the greatest potential for delivering fuel deep into the plasma core [1], where gas puffing is insufficient for effective fueling of reactor-scale plasmas. Nevertheless, the simulation of pellet ablation and deposition is computationally intensive and not particularly well suited for applications requiring fast outputs, such as scenario optimization, real-time control, or digital twin implementations.
In this work, we present HPI2-NN, a machine learning-based surrogate model trained on outputs from the high-fidelity HPI2 pellet code [2,3], which simulates hydrogenic pellet injection in magnetized plasmas. The surrogate is constructed using a comprehensive database of HPI2 simulations spanning WEST, AUG, and ITER conditions, and is capable of reproducing density deposition and thermal profiles, with an average error below 10%, while achieving a speedup of more than four orders of magnitude (from 15 minutes to ~20 ms per evaluation).
A salient aspect of this development is the preprocessing of plasma profile data—electron temperature and density—using Principal Component Analysis (PCA). This allows for dimensionality reduction and efficient encoding of input profiles in a form that the neural network can interpret, while preserving the relevant physics. This feature makes HPI2-NN compatible with both synthetic and experimental data sources and facilitates its use in existing modeling workflows.
The surrogate model is natively integrated within the High Fidelity Pulse Simulator (HFPS) integrated modeling suite, enabling full-discharge simulations that include self-consistent transport, sources, and pellet fuelling physics. Within this framework, HPI2-NN can be invoked as a drop-in substitute (in terms of real time control, and scenario optimization) for the original HPI2 code, allowing for efficient scenario studies without compromising predictive quality. While some validation against experimental WEST discharges is presented, the focus lies on demonstrating the operational readiness of this tool within large-scale integrated modeling and tokamak control.
This talk will also provide a concise yet thorough overview of the physics and operational role of pellet fuelling. We will discuss the technical and computational considerations behind the development of HPI2-NN, its integration into HFPS, and the broader implications for data-driven acceleration of physics-based workflows in fusion science.
References
[1] L.R. Baylor et al. Nucl. Fusion 47 443 (2007).
[2] B. Pégourié, et al. Plasma Physics and Controlled Fusion, vol. 49, p. R87 (2007).
[3] F. Koechl et al., EUROfusion Preprint EFDA-JET-PR (12), 57, (2012).


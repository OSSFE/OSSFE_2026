---
title: 'SLUKE an open-source tool for fast electron heating and current drive in tokamaks'
authors:
  - name: Y. Savoye-Peysson
    affiliations:
      - CEA, IRFM, Saint-Paul-les-Durance Cedex, France
  - name: Joan Decker
    affiliations:
      - EPFL, SCP, CH-1015 Lausanne, Switzerland
license: CC-BY-4.0
exports:
  - format: pdf
    template: ../../template
site:
  hide_toc: false
---

SLUKE is a suite of codes primarily designed to perform first principles calculation of the fast electron distribution driven by radio-frequency waves or a constant electric field in an axi-symmetric magnetic configuration. It is build around the solver LUKE of the linearized bounce-averaged relativistic electron Fokker-Planck equation (1D configuration space, 2D momentum space). Several satellite tools are linked to LUKE, like the multi-wave ray-tracing C3PO and the quantum relativistic non-thermal bremsstrahlung synthetic diagnostic R5X2, allowing direct comparisons with experimental observations. The chain of codes C3PO/LUKE/R5X2 are all linked within the SLUKE environment, which allows to connect them with other numerical tools with a high flexibility, for transport and toroidal MHD equilibrium, antenna coupling. All codes are written in Matlab, while C3PO is written in C language, but encapsulated in Matlab Mex function. The open-source transition is an opportunity to review the codes characteristics  and the considerable physic's work done with these numerical tools, but draw also perspectives of short, medium and long term evolution.


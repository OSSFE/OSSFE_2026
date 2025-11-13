---
title: 'Simulation of MHD plasma equilibria and evolutions by APEC-M code'
authors:
  - name: Alberto Bittesnich
    affiliations:
      - Fusion for energy
  - name: Pietro Testoni
    affiliations:
      - Fusion for Energy
  - name: Alfredo Portone
    affiliations:
      - Fusion for Energy
license: CC-BY-4.0
exports:
  - format: pdf
    template: ../../template
site:
  hide_toc: false
---

APEC is a FEM code developed at Fusion for Energy using ANSYS® APDL to simulate plasma equilibrium and evolution in magnetic confinement fusion machines. It employs an A, V-A nodal formulation to couple axisymmetric plasma equilibrium with 3D eddy current equations in surrounding passive structures. While leveraging ANSYS® features like geometry setup, meshing, and post-processing, APEC's dependence on ANSYS® introduces performance issues, including iteration restarts and repeated matrix factorization, limiting scalability for large models. Additionally, reliance on costly HPC licenses restricts its usability with large models. This work aims to address these challenges by developing an independent, free, scalable, and customizable code to replicate APEC's algorithm and overcome its limitations.


---
title: 'Comparing APIs for semi-Lagrangian and particle-in-cell methods'
authors:
  - name: Nils Schild
    affiliations:
      - Max Planck Institute for Plasma Physics
license: CC-BY-4.0
exports:
  - format: pdf
    template: ../../template
site:
  hide_toc: false
---

Plasma physics simulation codes have become essential tools for advancing research from fusion energy to space plasmas.
A persistent challenge, however, lies in the diversity of numerical and physical methods that are often implemented in isolation, making it difficult to compare results, reuse components, or build on existing work.
By abstracting the details of discretization from shared physics kernels (such as field solvers, collision operators, and boundary conditions), shared APIs can enable researchers to experiment with different algorithms while maintaining consistent physical models.
In this talk, we focus on the open source projects BSL6D and GEMPICX, which implement semi-Lagrangian and particle-in-cell methods to solve various Vlasov systems of strongly magnetized plasmas.
We discuss how aligned APIs lower the barrier for cross-comparisons of plasma simulations using distinct numerical schemes, illustrating the advantages for transparency and reproducibility.
The focus resides on the APIs of datastructures which discretize the various unknowns of the Vlasov systems.

# Repository
https://gitlab.mpcdf.mpg.de/bsl6d/bsl6d


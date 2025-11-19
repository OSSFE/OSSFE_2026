---
title: 'Struphy 3.0 - Using Python for HPC Plasma Modeling'
authors:
  - name: Stefan Possanner
    affiliations:
      - MPI for Plasma Physics
license: CC-BY-4.0
exports:
  - format: pdf
    template: ../../template
site:
  hide_toc: false
github: 'https://github.com/OSSFE/OSSFE_2026'
---

Struphy is an open-source Python package for plasma physics equations designed for high-performance computing (HPC). It is based on vectorization (numpy), parallelization (mpi4py) and compilation (pyccel). The third iteration of the software comes with a re-vamped user interface, a Github repository and new support for Nvidia GPUs via cupy. In this tutorial we will learn how to run various plasma models, such as guiding-center equations, Vlasov-Maxwell equations and MHD equations, and how to change their parameter setup through the new API. We shall show how to load MHD equilibria from third-party packages like DESC and GVEC and how to run test particle simulations in Stellarators. Most exercises will be performed in Jupyter notebooks, provided on the interactive binder interface.

# Repository
https://gitlab.mpcdf.mpg.de/struphy/struphy


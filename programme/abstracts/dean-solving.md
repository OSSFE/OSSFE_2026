---
title: 'Solving fusion problems in FEniCSx'
authors:
  - name: Joseph P. Dean
    affiliations:
      - University of Cambridge
  - name: Chris N. Richardson
    affiliations:
      - University of Cambridge
  - name: Garth N. Wells
    affiliations:
      - University of Cambridge
license: CC-BY-4.0
exports:
  - format: pdf
    template: ../../template
site:
  hide_toc: false
---

Nuclear fusion problems present a wide range of simulation challenges. Whole-system models are often required, with coupling between solid mechanics, fluid dynamics, heat transfer, and electromagnetism. Accurate simulations require advanced numerical schemes that are tailored to the nature of the governing equations in each domain, with robust coupling strategies. To make these high-fidelity simulations viable, scalable algorithms are required that exploit modern parallel high-performance computing architectures, such as GPUs.

FEniCSx is an open-source finite-element framework designed for solving such problems. We present some recent developments to FEniCSx that begin to tackle these challenges, including improved support for multi-physics coupling and GPU acceleration.

# Repository
https://github.com/fenics


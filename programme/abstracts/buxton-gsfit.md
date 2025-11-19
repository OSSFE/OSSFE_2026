---
title: 'GSFit: Grad-Shafranov Fit – A new equilibrium reconstruction code for tokamak plasmas'
authors:
  - name: P.F. Buxton
    affiliations:
      - Tokamak Energy Ltd.
  - name: A. P. K. Prokopyszyn
    affiliations:
      - Tokamak Energy Ltd.
  - name: M. Sertoli
    affiliations:
      - Tokamak Energy Ltd.
  - name: The ST40 Team
    affiliations:
      - Tokamak Energy Ltd.
license: CC-BY-4.0
exports:
  - format: pdf
    template: ../../template
site:
  hide_toc: false
github: 'https://github.com/OSSFE/OSSFE_2026'
---

Equilibrium reconstruction is foundational for all experimental interpretation in tokamaks. The core algorithm used to constrain the Grad-Shafranov equation against diagnostic measurements is well established [1], and has been used in multiple codes such as EFIT [1], EFIT++ [2], and LIUQE [3]. Despite this, an open, flexible, modular, and rigorously validated implementation remains necessary, released under a license compatible with commercial use.

GSFit, developed by Tokamak Energy Ltd. and released under the permissive BSD-3-Clause license, combines Python’s flexibility and ease of use with Rust’s performance and robustness. It supports the full workflow for post-shot equilibrium reconstruction, including magnetics-only operation, passive conductors, kinetic constraints, and flexible degrees of freedom for pressure and poloidal current source functions. We present benchmarks showing excellent agreement with synthetic data produced by ASTRA-SPIDER including transient scenarios with current diffusion and passive conductors, FreeGS, FreeGSNKE, and Fiesta, against established EFIT results. The ultimate evaluation of GSFit’s performance is made against experimental data. Here we compare GSFit with data from ST40’s Thomson Scattering system, soft Xray cameras, midplane line diodes, and visible cameras.

[1] L.L. Lao et. al., Nucl. Fusion, 1985
[2] L. C. Appel, et. al., Comput. Phys. Commun, 2018
[3] J.-M. Moret, et. al., Fusion Eng. Des., 2015


# Repository
https://github.com/tokamak-energy/gsfit


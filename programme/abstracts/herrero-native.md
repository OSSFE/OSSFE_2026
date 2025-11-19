---
title: 'Native OpenMC CSG for Reactor-Scale Fusion Geometry'
authors:
  - name: Rodrigo Herrero
    affiliations:
      - Proxima Fusion
  - name: Jonathan Shimwell
    affiliations:
      - Proxima Fusion
license: CC-BY-4.0
exports:
  - format: pdf
    template: ../../template
site:
  hide_toc: false
github: 'https://github.com/OSSFE/OSSFE_2026'
---

We present an open-source generator of native OpenMC constructive solid geometry (CSG) models for reactor-scale fusion systems. The tool programmatically builds parameterized geometries of major reactor subsystems with an emphasis on detailed winding pack representations. In particular, it resolves the layered unit cell stack (HTS, copper, jackets, plates, etc) needed to support tallies of high-fidelity metrics such as DPA in the HTS and nuclear heating in the stabilizer. By relying on exact CSG region definitions rather than CAD tessellations, the models avoid common robustness issues and substantially reduce turn‑around time for transport studies, enabling plant-scale fidelity with practical runtimes. Using a common CSG description also facilitates cross‑code comparisons (e.g., with MCNP) under identical geometry assumptions.

# Repository
https://github.com/rodrigo-herrero/openmc-csg-fusion-reactor-geometry


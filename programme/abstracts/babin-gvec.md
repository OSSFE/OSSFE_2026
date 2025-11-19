---
title: 'GVEC - a flexible 3D MHD equilibrium solver'
authors:
  - name: Robert Babin
    affiliations:
      - Max Planck Institute for Plasma Physics
  - name: Florian Hindenlang
    affiliations:
      - Max Planck Institute for Plasma Physics
license: CC-BY-4.0
exports:
  - format: pdf
    template: ../../template
site:
  hide_toc: false
github: 'https://github.com/OSSFE/OSSFE_2026'
---

The Galerkin Variational Equilibrium Code (GVEC) is a 3D ideal magnetohydrodynamic (MHD) equilibrium solver, which play a central role in the simulation and modelling of stellarators. Ideal MHD equilibria, while being a simple model of the fusion plasma, serve as the starting point for time dependent MHD, stability and turbulence simulations and are used in stellarator optimization, often within proxies for the actual optimization targets. It is therefore vital to compute MHD equilibria accurately and fast.
GVEC expands on the approach by Hirshman et al. (1983) implemented in VMEC, by using B-Splines for the radial basis, enabling more accurate and smooth solutions, especially near the magnetic axis, with fewer degrees of freedom. The coordinate frame in GVEC is also flexible, e.g. allowing the use of a curve following coordinate frame instead of cylindrical coordinates, extending the computable equilibria to knotted and highly inclined configurations.
GVEC is open source and written in modern fortran, using OpenMP and MPI for parallelization. Python bindings allow convenient installation, pre- and postprocessing.

# Repository
https://gitlab.mpcdf.mpg.de/gvec-group/gvec


---
title: 'The Open FUSION Toolkit: An open-source suite of fusion modeling tools for engineering, analysis, and education'
authors:
  - name: C. Hansen
    affiliations:
      - Columbia University
license: CC-BY-4.0
exports:
  - format: pdf
    template: ../../template
site:
  hide_toc: false
---

The Open FUSION Toolkit [1] is an open-source suite of tools for fusion modeling with a focus on ease of use, tight integration with engineering workflows, and education. The present suite of physics tools include: 1) TokaMaker [2]: a 2D static and time-dependent Grad-Shafranov equilibrium tool designed as an user-friendly and open tool for design, control development and education, 2) ThinCurr [3]: a 3D thin-wall current modeling tool used to study currents in 3D device structures (eg. ports) and as an alternative to fourier-based current potential formulations in stellarator coil optimization, 3) MUG [4]: a 3D linear/nonlinear time-dependent MHD tool for plasma dynamics in arbitrary domains, and 4) Marklin [5]: a 3D force-free, uniform  ideal MHD equilibrium solver. A common core provides capabilities to all tools, including: meshing from CAD models, scalable linear and nonlinear solvers, extensible finite element representations, parallelization via OpenMP+MPI, and 3D visualization. Core functionality is implemented in C/C++/Fortran with Python interfaces for interactive applications and scripting. This talk will present a summary of the toolkit (highlighting applications in each domain) and describe methods to support community adoption including: binary packaging, documentation, and code design.

[1] https://github.com/OpenFUSIONToolkit/OpenFUSIONToolkit
[2] C. Hansen et al., CPC 298 109111 (2024)
[3] C. Hansen et al., CPC 315 109713 (2025)
[4] C. Hansen, PoP 22 042505 (2015)
[5] T. Benedett, NF 61 036022 (2021)

Work supported by US DOE awards DE-SC0019239 and DE-SC0024898 and Commonwealth Fusion Systems, Next Step Fusion, Openstar Technologies, and Realta Fusion

# Repository
https://github.com/OpenFUSIONToolkit/OpenFUSIONToolkit


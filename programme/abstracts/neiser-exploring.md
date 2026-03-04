---
title: 'Exploring fusion power plant trade-offs with FUSE: An open-source multi-objective optimization framework'
authors:
  - name: Tim Slendebroek
    affiliations:
      - Center for Energy Research UCSD
  - name: G. Dose
    affiliations:
      - General Atomics
  - name: A. G. Ghiozzi
    affiliations:
      - General Atomics
  - name: B. C. Lyons
    affiliations:
      - General Atomics
  - name: J. McClenaghan
    affiliations:
      - General Atomics
  - name: O. M. Meneghini
    affiliations:
      - General Atomics
  - name: A. O. Nelson
    affiliations:
      - Columbia University
  - name: T. F. Neiser
    affiliations:
      - General Atomics
  - name: C. Holland
    affiliations:
      - Center for Energy Research UCSD
license: CC-BY-4.0
exports:
  - format: pdf
    template: ../../template
site:
  hide_toc: false
github: 'https://github.com/OSSFE/OSSFE_2026'
---

The FUsion Synthesis Engine (FUSE) is an open-source integrated modeling framework that addresses a critical gap in fusion power plant design: the lack of tools capable of simultaneously optimizing plasma physics, engineering systems, and economics while maintaining self-consistency across all subsystems. We present how FUSE's hierarchical actor system enables systematic exploration of the fusion design space through constrained multi-objective optimization, examining over 200,000 integrated designs to reveal non-intuitive trade-offs between capital cost and operational reliability.

Using FUSE, we demonstrate that positive triangularity (PT) and negative triangularity (NT) tokamak configurations achieve similar economic performance through fundamentally different design philosophies. PT configurations are constrained to larger machines (R₀ > 6.5 m) by the narrow operational window between L-H threshold requirements and power exhaust limits, optimizing through reduced magnetic field (~8 T). NT configurations exploit their ELM-free operation to access compact, high-field designs (R₀ ~ 5.5 m, B₀ > 12 T), revealing unexpected synergies with high-temperature superconductor technology. Recent extensions of this work explore cover the full aspect ratio range from spherical tokamaks to conventional designs, demonstrating FUSE's flexibility in capturing configuration-specific physics while maintaining consistent engineering constraints.

The open-source nature of FUSE enables community-driven development and integration of validated physics models within a parallelizable framework that accelerates design convergence from weeks to hours. We discuss how this open framework facilitates reproducible research, enables rapid testing of emerging technologies, and provides quantitative risk assessment for different power plant pathways. The code and optimization results are publicly available, supporting collaborative advancement of fusion power plant design.

# Repository
https://github.com/ProjectTorreyPines/FUSE.jl


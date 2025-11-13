---
title: 'Automated Design and Optimisation of Stellarators Using Open Source Simulation Codes'
authors:
  - name: S. Sharpe
    affiliations:
      - nTtau Digital LTD
  - name: N. Adepoju
    affiliations:
      - nTtau Digital LTD
  - name: M. Crocker
    affiliations:
      - nTtau Digital LTD
  - name: J. Edwards
    affiliations:
      - nTtau Digital LTD
license: CC-BY-4.0
exports:
  - format: pdf
    template: ../../template
site:
  hide_toc: false
---


This research presents a stellarator optimisation workflow that unifies engineering, physics, and cost considerations into a single automated framework. Stellarator design is inherently complex, with plasma equilibria, coil geometries, and support structures strongly interdependent. Traditional approaches address these elements separately through sequential analyses that are slow, expensive, and unable to capture trade-offs between performance, manufacturability, and overall cost. This work overcomes those limitations by introducing an integrated, high-fidelity workflow that accelerates design and delivers robust, manufacturable solutions.

Using W7-X as a case study, the workflow employs VMEC, REGCOIL, and open-source CAD software to generate an initial stellarator design—including coils, blanket, and shielding—from a starting plasma equilibrium. SIMSOPT is then incorporated into the coil design loop to enable wide exploration of the design space, optimising for coil curvature, length, Bnorm, and coil-coil and coil-plasma spacing. Bayesian optimization techniques are incorporated to improve computational efficiency and reduce the cost of large-scale design exploration. The optimised coil coordinates are coupled with CadQuery to automatically generate 3D CAD models of the coils, which are then used to derive a parametrically defined support structure. Lorentz forces, calculated using a filament-based magnetic field model, are passed to MOOSE to simulate von Mises stress distributions in both the coils and support structure, providing a physics-informed engineering validation of structural integrity.
The workflow delivers coil designs that are geometrically efficient, mechanically robust, and cost-aware. By compressing design timelines, improving fidelity, and reducing manual effort, this optimization workflow offers a scalable pathway for next-generation stellarator development, benefiting fusion researchers, engineers, and industry stakeholders.



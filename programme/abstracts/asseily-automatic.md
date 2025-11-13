---
title: 'Automatic Differentiation for CAD'
authors:
  - name: Max Asseily
    affiliations:
      - Proxima Fusion
  - name: Philipp Jurasic
    affiliations:
      - Proxima Fusion
license: CC-BY-4.0
exports:
  - format: pdf
    template: ../../template
site:
  hide_toc: false
---

Conventional CAD workflows are poorly suited for integration with modern optimization and machine learning methods. We introduce the first fully JAX-compatible, open-source implementation of non-uniform rational B-splines (NURBS), enabling auto-differentiable CAD generation within JAX’s computational graph. By allowing gradients to propagate through curves, surfaces, and geometric operations, our framework supports efficient gradient-based optimization of manufacturable geometries. This capability unlocks computational trade-off studies at high model fidelity, spanning objectives such as obstacle avoidance, plasma confinement quality, coil complexity, thermal and structural loads, and manufacturability. We demonstrate how differentiable CAD can couple seamlessly with physics simulations, equilibrium solvers, and design automation pipelines, providing a scalable foundation for optimization-driven engineering. Applications to stellarator reactor design highlight the potential of auto-differentiable CAD to accelerate discovery in complex engineered systems.


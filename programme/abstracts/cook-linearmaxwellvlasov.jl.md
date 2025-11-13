---
title: 'LinearMaxwellVlasov.jl'
authors:
  - name: J. W. S. Cook
    affiliations:
      - Fourth State Labs Ltd
license: CC-BY-4.0
exports:
  - format: pdf
    template: ../../template
site:
  hide_toc: false
---

LinearMaxwellVlasov.jl is an open-source Julia package that provides comprehensive capability to calculate dielectric and conductivity tensors in the infinite homogeneous plasma limit of the linearized Maxwell-Vlasov set of equations. It offers users cold, warm, kinetic Maxwellian, and arbitrary distribution functions where key integrals fall back to numerical evaluation under circumstances when no analytic expression is available. It is comprehensively tested and used in academia to form the basis of dispersion relation solvers for fast ion physics. Julia's type system allows it go be differentiable for use in other settings, for example where the derivative of conductivity tensors are required. A set of optimizations have been deployed to ensure rapid evaluation of integrals at all levels of distribution function complexity from Maxwellian and Dirac-delta function to coupled parallel and perpendicular wavenumbers.

# Repository
https://github.com/jwscook/LinearMaxwellVlasov.jl


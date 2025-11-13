---
title: 'foamForNuclear: A Modular Multiphysics Platform for Fusion and Fission Applications'
authors:
  - name: Mr. Giovanni Nervi
    affiliations:
      - EPFL
  - name: Dr. Alessandro Scolaro
    affiliations:
      - EPFL
  - name: Prof. Carlo Fiorina
    affiliations:
      - Texas A&M University
  - name: Dr. Mathieu Hursin
    affiliations:
      - EPFL
license: CC-BY-4.0
exports:
  - format: pdf
    template: ../../template
site:
  hide_toc: false
---

The open-source library OpenFOAM has been widely applied in the nuclear field, with dedicated developments ranging from specialized thermal-hydraulics, neutronics and fuel behaviour for fission systems to magnetohydrodynamics, liquid-metal flows and gas dynamics in inertial confinement chambers for fusion. While these efforts demonstrate the versatility of OpenFOAM for nuclear studies, they are often limited to stand-alone solvers or case-specific couplings, which restricts their use in comprehensive multiphysics simulations.

To overcome this limitation, foamForNuclear has been recently introduced, building on years of development of the GeN-Foam and OFFBEAT codes at EPFL and Texas A&M University. The platform merges these efforts into a single, open-source multiphysics environment that provides a general-purpose architecture for coupling arbitrary physics across multiple regions and meshes, while maintaining a modular and extensible design. A key feature of the framework is that it makes it straightforward to integrate a new solver and directly couple it with existing capabilities such as thermal-hydraulics, structural mechanics, or neutronics. This eliminates the need for ad-hoc coupling strategies and allows researchers to build on prior developments without reimplementing the coupling infrastructure.

Although the original libraries were developed specifically for advanced fission applications, an important motivation behind the new architecture was its applicability to fusion. In this contribution, we present the first applications of foamForNuclear to fusion problems, demonstrating its potential in both magnetic confinement and inertial confinement contexts. We also outline future work focused on extending its capabilities by developing new, and leveraging existing, OpenFOAM-based fusion solvers.

# Repository
https://gitlab.com/foam-for-nuclear


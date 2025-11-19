---
title: 'Gysela-X++ - A new C++ Kokkos-based code for gyrokinetic plasma simulations'
authors:
  - name: Virginie Grandgirard
    affiliations:
      - CEA/IRFM, France
  - name: Emily Bourne
    affiliations:
      - EPFL, Switzerland
  - name: Yuuichi Asahi
    affiliations:
      - CEA/MdlS, France
  - name: Julien Bigot
    affiliations:
      - CEA/MdlS, France
  - name: Aakash Dasari
    affiliations:
      - CERFACS, France
  - name: Peter Donnel
    affiliations:
      - CEA/IRFM, France
  - name: Alexander Hoffmann
    affiliations:
      - Max-Planck-IPP, Germany
  - name: Abdelhadi Kara
    affiliations:
      - CEA/IRFM, France
  - name: Philipp Krah
    affiliations:
      - CEA, France
  - name: Etienne Malaboeuf
    affiliations:
      - CINES, France
  - name: Kevin Obrejan
    affiliations:
      - CEA/IRFM, France
  - name: Thomas Padioleau
    affiliations:
      - CEA/MdlS, France
  - name: Pauline Vidal
    affiliations:
      - Max-Planck-IPP, Germany
  - name: Ariel De Vora
    affiliations:
      - CEA, France.
license: CC-BY-4.0
exports:
  - format: pdf
    template: ../../template
site:
  hide_toc: false
github: 'https://github.com/OSSFE/OSSFE_2026'
---

Gyrokinetic simulations are essential for understanding turbulent transport in magnetized plasmas, playing a crucial role in the design and optimization of fusion devices. This presentation introduces Gysela-X++ [1] , a C++ rewrite of the original GYSELA [2] Fortran code, designed to extend its physical capabilities and enhance its portability on exascale architectures. It is built on the Kokkos performance portability framework,  ensuring efficient execution both on CPU and GPU (AMD and NVIDIA) architectures.
As part of this rewrite, we developed Gyselalib++ [3, 4], an open-source library containing all the necessary computational kernels. Gyselalib++ provides mathematical building blocks to construct kinetic or gyrokinetic plasma simulation codes in C++, simulating a distribution function discretized in phase space on a structured grid. Gyselalib++ is not only useful for the fusion community but also addresses a broader audience, as it has been specifically designed to serve as a testbed for the development and benchmarking of new numerical schemes, enabling rapid prototyping and validation of innovative algorithms.
We will discuss the motivations behind this rewrite, the design of this general modular framework based on the core library Gyselalib++, and the performance and scalability gains.

[1] https://gyselax.github.io/gyselalibxx/ 
[2] V. Grandgirard et al., Computer Physics Communications 207 (2016) 35–68.
[3] https://github.com/gyselax/gyselalibxx 
[4] E. Bourne et al., JOSS 2025, https://doi.org/10.21105/joss.08582 


# Repository
https://github.com/gyselax/gyselalibxx/


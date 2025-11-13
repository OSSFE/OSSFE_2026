---
title: 'Using Gkeyll as a self-consistent gyrokinetic predictive tool for tokamak edge turbulence'
authors:
  - name: A.C.D. Hoffmann
    affiliations:
      - Princeton Plasma Physics Laboratory, Princeton, NJ, USA
  - name: T.N. Bernard
    affiliations:
      - General Atomics, San Diego, CA, USA
  - name: M. Francisquez
    affiliations:
      - Princeton Plasma Physics Laboratory, Princeton, NJ, USA
  - name: G.W. Hammett
    affiliations:
      - Princeton Plasma Physics Laboratory, Princeton, NJ, USA
  - name: A. Hakim
    affiliations:
      - Princeton Plasma Physics Laboratory, Princeton, NJ, USA
license: CC-BY-4.0
exports:
  - format: pdf
    template: ../../template
site:
  hide_toc: false
---

This presentation discusses the application of the Gkeyll open-source framework to predictive gyrokinetic turbulence modeling in fusion plasmas. While a companion tutorial introduces the Gkeyll framework in detail, this talk focuses on its capabilities for performing self-consistent, first-principles-based tokamak turbulence simulations. We demonstrate how Gkeyll enables high-fidelity modeling of the tokamak edge and scrape-off layer, moving beyond approaches that rely on empirical inputs and toward a more predictive understanding of plasma behavior.
The core of this work is the self-consistent simulation of plasma turbulence, achieved by solving the full-f, 5D gyrokinetic Boltzmann equation in a global tokamak geometry. We highlight the physics modules that enable this predictive capability, including an adaptive sourcing algorithm and conducting sheath boundary conditions. These allow simulations to be driven by fundamental engineering inputs: magnetic geometry, heating power, and total particle inventory. This approach reduces the reliance on prescribed kinetic profiles, which can be a limiting factor in the predictive power of other models. The open and modular nature of Gkeyll also provides a platform for collaborative development and transparency in simulation methodologies.
This approach is validated against TCV and DIII-D experimental data, showing how simulations can reproduce kinetic profiles and turbulent phenomena. We also illustrate how this predictive tool is used to gain new insights into advanced magnetic configurations like negative triangularity. The optimized GPU implementation of Gkeyll allows these complex simulations to be performed efficiently, making high-resolution, first-principles-based modeling a useful tool for future fusion device design.

# Repository
https://github.com/ammarhakim/gkeyll


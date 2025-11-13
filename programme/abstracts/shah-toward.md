---
title: 'Toward ParaTAN–FESTIM Coupling: An MBSE-Oriented Open-Source Workflow for Neutronics and Tritium Transport in Mirror Fusion Devices'
authors:
  - name: Hitarth Shah
    affiliations:
      - UW Madison
  - name: Benjamin Lindley
    affiliations:
      - UW Madison
license: CC-BY-4.0
exports:
  - format: pdf
    template: ../../template
site:
  hide_toc: false
---

Model-Based Systems Engineering (MBSE) provides a structured framework to formalize requirements, interfaces, and data flows for complex engineering systems. We apply this approach to the development of a mirror-type volumetric neutron source. ParaTAN is an OpenMC-based parametric neutronics tool for mirror devices that enables rapid geometry definition and design-space exploration. A key challenge is linking neutronics outputs with tritium accountancy models in a way that supports traceability and iterative design. We present a coupling between ParaTAN and the FESTIM tritium transport solver. Tritium production fields from OpenMC are mapped into diffusion and retention simulations, allowing systematic evaluation of how design choices affect tritium permeation, retention, and inventory. Framing the coupling within an MBSE architecture moves one step toward a system-level understanding of tritium handling. Even at reduced fidelity, this workflow creates a reproducible open-source pathway for embedding neutronics and tritium modeling into a larger systems framework for mirror fusion development.

# Repository
https://github.com/hitarthrs/paratan


---
title: 'Uncertainty Quantification in Volumetric Neutron Source Neutronics Using OpenMC and the Total Monte Carlo Method with JEFF-4.0'
authors:
  - name: Jin Hun Park
    affiliations:
      - Karlsruhe Institute of Technology
  - name: Roman Afanasenko
    affiliations:
      - Karlsruhe Institute of Technology
  - name: Dieter Leichtle
    affiliations:
      - Karlsruhe Institute of Technology
  - name: Pavel Pereslavtsev
    affiliations:
      - EUROfusion
license: CC-BY-4.0
exports:
  - format: pdf
    template: ../../template
site:
  hide_toc: false
---

This study presents a detailed neutronics simulation of a Volumetric Neutron Source (VNS) using the OpenMC Monte Carlo code together with the JEFF-4.0 nuclear data library. The VNS is considered a key experimental facility for testing and validating structural materials and components relevant to future fusion power plants, such as DEMO, thereby requiring accurate and high-fidelity neutronics simulations to support its design and performance evaluation.
Beyond evaluating standard neutronics parameters, such as reaction rate distributions and energy spectra, this work emphasizes the quantification of uncertainties originating from nuclear data. To this end, the Total Monte Carlo (TMC) method is applied, where nuclear data uncertainties are propagated through large-scale random sampling based on covariance information associated with JEFF-4.0. This latest version of JEFF represents the most recent release of the evaluated nuclear data library, offering broader coverage and improved accuracy compared to its predecessor, JEFF-3.3. However, despite these advancements, a systematic investigation of the uncertainties inherent in JEFF-4.0 has not yet studied.
The combination of OpenMC’s high-performance capabilities and TMC’s rigorous statistical treatment enables a more transparent assessment of the reliability of VNS simulations. The results provide valuable insights into how nuclear data uncertainties impact key observables relevant to fusion-oriented neutron sources, thereby supporting ongoing efforts to establish robust safety margins and optimize experimental designs. Furthermore, this study underlines the broader importance of uncertainty quantification in advancing the predictive capability of neutronics analyses for next-generation nuclear energy systems.


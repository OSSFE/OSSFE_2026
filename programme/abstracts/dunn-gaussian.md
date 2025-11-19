---
title: 'Gaussian Processing Framework for Neutron Generator Diagnostics and Uncertainty Quantification'
authors:
  - name: Collin Dunn
    affiliations:
      - MIT PSFC
  - name: Stefano Segantin
    affiliations:
      - MIT PSFC
  - name: Rémi Delaporte-Mathurin
    affiliations:
      - MIT PSFC
license: CC-BY-4.0
exports:
  - format: pdf
    template: ../../template
site:
  hide_toc: false
github: 'https://github.com/OSSFE/OSSFE_2026'
---

Accurate neutron flux characterization is essential for evaluating the tritium breeding ratio (TBR) in fusion systems. The LIBRA group at MIT operates a tritium breeding platform coupling a lithium-containing molten salt tank with a compact deuterium-tritium (D-T) neutron generator. Here we present an open-source approach to measuring and modeling the angular dependence of the 14.1 MeV neutron flux emitted by the generator.

Neutron flux measurements were performed at multiple polar angles using three complementary diagnostics: niobium activation foils, zirconium activation foils and a diamond detector. A neutron activation foil analysis toolkit was added to the open-source libra-toolbox python package, which includes spectral peak detection, detector efficiency and source rate calculations with corresponding uncertainty evaluations. Furthermore, neutron cross section uncertainties and geometric uncertainties for both the activation foils and diamond detector were evaluated using OpenMC, an open-source Monte Carlo transport code. The results from all detectors and associated uncertainties were propagated and then input into an open-source Gaussian processing framework to extract the post probable flux distribution. 

All aspects of the workflow are open-source ensuring full reproducibility of the analysis from the experimental results. Additionally this workflow can be applied to other neutron generators and adapted to other neutron diagnostics. 


# Repository
https://github.com/LIBRA-project/ngen_characterization


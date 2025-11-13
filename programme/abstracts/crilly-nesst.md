---
title: 'NeSST: Neutron Scattered Spectra Tool'
authors:
  - name: Aidan Crilly
    affiliations:
      - Imperial College London
license: CC-BY-4.0
exports:
  - format: pdf
    template: ../../template
site:
  hide_toc: false
---

Neutron Scattered Spectra Tool[1] (NeSST) is a python library for producing synthetic neutron spectra relevant to nuclear fusion. The tool is primarily focused on inertial fusion, but also has capabilities which are useful for magnetic fusion. NeSST implements literature models for the primary neutron-producing fusion reactions in DT plasmas (DT, DD and TT). It also uses evaluated nuclear data files to calculate scattered spectra, under the single scatter approximation. This is essential in inertial fusion to model the downscatter of neutrons in the target. Scattering is computed using relativistic corrections and the effects of finite temperature and velocity of the scattering medium. Finally, NeSST includes standard diagnostic models for time-of-flight neutron spectral analysis. The code has been used to model experimental data from the OMEGA facility at the Laboratory for Laser Energetics. NeSST makes use of a few other open-source fusion energy projects: python-ENDF[2] and pydress[3].
[1] – https://github.com/aidancrilly/NeSST
[2] – https://github.com/paulromano/endf-python
[3] – https://github.com/jacob-eri/pydress


# Repository
https://github.com/aidancrilly/NeSST


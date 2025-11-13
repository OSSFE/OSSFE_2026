---
title: 'Probabilistic characterisation of neutron spectra with the nFoils package'
authors:
  - name: Louis Butt
    affiliations:
      - University of Birmingham
  - name: Tony Turner
    affiliations:
      - UK Atomic Energy Authority
  - name: Joven Lim
    affiliations:
      - UK Atomic Energy Authority
  - name: Ben Phoenix
    affiliations:
      - University of Birmingham
  - name: Yu-Lung Chiu
    affiliations:
      - University of Birmingham
  - name: Lee Packer
    affiliations:
      - UK Atomic Energy Authority
  - name: Carl Wheldon
    affiliations:
      - University of Birmingham
  - name: David Foster
    affiliations:
      - UK Atomic Energy Authority
  - name: Mark Gilbert
    affiliations:
      - UK Atomic Energy Authority
  - name: Martin Freer
    affiliations:
      - The Faraday Institution
license: CC-BY-4.0
exports:
  - format: pdf
    template: ../../template
site:
  hide_toc: false
---

Modelling an exact neutron spectrum in a neutron facility is challenging. Simulated neutron spectra may be adjusted to reflect outcomes known from validation experiments, but rigorous evaluation of uncertainties is necessary. An experimental neutron spectrum with uncertainty can then be used for the verification and validation of neutron nuclear data, testing diagnostics, and fusion mock-up experiments. Activation foils are frequently used to evaluate and unfold neutron spectra, but uncertainty quantification during evaluation is not always rigorous or transparent. The open-source nFoils Python package has been developed for the probabilistic characterisation of neutron spectra with activation foils, and the methods tested with measurements of a new compact fast neutron source at the Birmingham MC40 Cyclotron Facility. The package includes modules for calculating the activities of foils from gamma spectroscopy results, performing an efficiency calibration for a detector, extracting cross-sections and uncertainties from nuclear data libraries, and comparing experimental results to simulated results. End users can evaluate a neutron spectrum from activation foil gamma spectra by adjusting simple examples, and neutronics developers are welcome to modify the modules to suit their own needs.

# Repository
https://github.com/louisbutt338/nFoils


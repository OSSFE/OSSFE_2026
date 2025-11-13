---
title: 'Extending FLUNED with OpenMC Capabilities for Coupled CFD–Neutronics Simulation of Activated Coolants in Fusion Systems'
authors:
  - name: Marco De Pietri
    affiliations:
      - MIT-PSFC
  - name: Ethan Peterson
    affiliations:
      - MIT-PSFC
license: CC-BY-4.0
exports:
  - format: pdf
    template: ../../template
site:
  hide_toc: false
---

The cooling systems of irradiated components in nuclear fusion installations are often characterized by complex internal fluid-dynamics and neutron fields. Therefore, the simulation of the radioisotopes which are generated and carried through these systems constitutes a multi-physics problem that benefits from the application of coupled CFD and neutronics codes. Coolants considered for future fusion power plants, such as FLiBe, generate, through various nuclear reaction channels, a set of radioisotopes that require tracking for radioprotection purposes. In addition, impurities present in the coolant extend the number of radioisotopes generated from neutron-induced transmutations which can have a significant impact during machine shutdown.
The work presented here introduces a set of developments in the FLUNED code, a CFD-based tool for fluid activation that has been recently validated with experimental data of irradiated water. This code implements a one-way explicit coupling that combines neutronics and CFD simulations to compute the evolution, throughout the same CFD mesh, of the radioisotope concentration.
The new developments couple neutronics data directly from the results of OpenMC simulations. By using the OpenMC depletion module, it is possible to generate reaction rates for arbitrary, user-specified isotopes for use in FLUNED activation calculations. To support this, a workflow was developed that enables the simulation of multiple radioisotopes as passive scalars, produced through single-step transmutations in coolants of arbitrary composition. Previously, FLUNED was hard-coded to operate only with water. Finally, the new advances allow the generation of radiation source models usable by OpenMC for subsequent fixed source MC simulations. In this manner, the work presented enables the practical simulation of nuclear responses from activated coolant in a workflow which is completely open-source.


# Repository
https://github.com/marco-de-pietri/FLUNED-repository


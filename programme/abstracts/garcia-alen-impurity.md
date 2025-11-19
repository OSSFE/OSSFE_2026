---
title: 'Impurity Evolution and Depletion Effects in Breeder Blankets from Reactor Geometry and Material Variations'
authors:
  - name: Luis Garcia
    affiliations:
      - nTtau Digital LTD
  - name: Noe Adepoju
    affiliations:
      - nTtau Digital LTD
  - name: Megan Crocker
    affiliations:
      - nTtau Digital LTD
  - name: Dominic Longhorn
    affiliations:
      - nTtau Digital LTD
  - name: Abinash Manikandan
    affiliations:
      - nTtau Digital LTD
  - name: Max Moreland
    affiliations:
      - nTtau Digital LTD
  - name: Omer Muhammad
    affiliations:
      - nTtau Digital LTD
  - name: Sophie Sharpe
    affiliations:
      - nTtau Digital LTD
  - name: Simon Woodruff
    affiliations:
      - nTtau Digital LTD
license: CC-BY-4.0
exports:
  - format: pdf
    template: ../../template
site:
  hide_toc: false
github: 'https://github.com/OSSFE/OSSFE_2026'
---

This study makes use of open-source neutronics tools to investigate how geometric and material variations influence impurity behaviour and performance in fusion reactors. Impurity buildup is a major challenge for tritium self-sufficiency and long-term activation control in fusion reactors; if left unmanaged, it can reduce tritium production and generate long-lived radioactive materials that worsen operation and waste disposal. Even small changes in wall geometry or material can strongly influence neutron spectra and impurity pathways. Using OpenMC transport framework, simulations  for tokamak, stellarator, and mirror reactor concepts were launched with varied first-wall thicknesses and materials. The study utilises CadQuery for parametric CAD modelling, CAD-to-DAGMC for conversion to DAGMC meshes, and OpenMC for fixed-source transport and depletion. Results show that geometric parameters such as wall thickness and  wall materials shape neutron spectra and tritium breeding ratio (TBR), as these parameters govern neutron multiplication, activation burdens, and impurity transmutation pathways. Detailed tracking of impurity inventories, neutron poisons, and activation products highlights spectrum-dependent sensitivities and their long-term impact on tritium self-sufficiency and licensing. By combining OpenMC with modular open-source tools, this work establishes a flexible framework for cross-concept comparisons, providing fundamental design insights for reactor designers and material scientists for impurity management and material optimisation in distinct fusion energy concepts.



---
title: 'Modeling Permeator Probe for Tritium Concentration in Liquids'
authors:
  - name: Kaelyn Dunnell
    affiliations:
      - MIT PSFC
  - name: James Dark
    affiliations:
      - MIT PSFC
  - name: Huihua Yang
    affiliations:
      - MIT PSFC
  - name: Chiraq Khurana
    affiliations:
      - MIT PSFC
  - name: Remi Delaporte-Mathurin
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

	FESTIM 2 (1) has been newly released to include multi-isotope hydrogen transport, as well as coupling to OpenFOAM (2) and OpenMC (3) codes for thermo-hydraulics and neutronics, respectively. This work demonstrates FESTIM’s multiphysics coupling capabilities by modeling a tritium permeator probe (4), a potential measuring device for tritium concentration in liquid metals and molten salts throughout the fusion fuel cycle. The permeator probe concept relies on a vacuum probe constructed of a hydrogen-permeable membrane, which is inserted into a liquid breeder. Tritium then permeates from the liquid breeder, through the probe membrane to a gas enclosure, where a change in pressure allows us to determine the concentration of tritium in the liquid breeder. All these processes can be simulated in FESTIM. This work thus uses OpenFOAM for fluid mechanics simulations as coupled to FESTIM for tritium transport calculations. Using this study, we are able to optimize the position of the probe relative to the tested breeder to maximize tritium permeation, test the pressurization of the probe as a sensing instrument, and assess the intrusiveness of the probe as creating any change in tritium concentration downstream of the probe placement. 

(1)  Remi Delaporte-Mathurin et al. “FESTIM: An open-source code for hydrogen transport simulations.” International Journal of Hydrogen Energy (Apr 2024), pp.786-802. https://doi.org/10.1016/j.ijhydene.2024.03.184.
(2) Hrvoje Jasak. “OpenFOAM: Open source CFD in research and industry.” International Journal of Naval Architecture and Ocean Engineering (Dec 2009), pp.89-94. https://doi.org/10.2478/IJNAOE-2013-0011.
(3)  Paul Romano et al. “OpenMC: A state-of-the-art Monte Carlo code for research and development.” Annals of Nuclear Energy (Aug 2015), pp.90-97. https://doi.org/10.1016/j.anucene.2014.07.048.
(4) L. Llivia et al. “Development of a hydrogen permeation sensor for future tritium applications.” Fusion Engineering and Design (Aug 2014), pp. 1209-1212. https://doi.org/10.1016/j.fusengdes.2014.04.047.


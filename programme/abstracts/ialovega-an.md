---
title: 'An Integrated Dynamic Modeling Framework for the Tritium Cycle in Inertial Fusion Chamber Materials'
authors:
  - name: Mykola Ialovega
    affiliations:
      - GenF
license: CC-BY-4.0
exports:
  - format: pdf
    template: ../../template
site:
  hide_toc: false
github: 'https://github.com/OSSFE/OSSFE_2026'
---

GenF, a subsidiary of the Thales Group, is pioneering the development and commercialization of direct-drive inertial confinement fusion (ICF) technology in France. A major challenge in fusion power plant design is the reaction chamber, which must integrate the first wall (FW), structural materials, tritium breeding and cooling systems. In ICF reactors, the FW is subjected to pulsed loads of X-rays, energetic ions, and neutrons produced during fusion reactions.

Following ignition, residual fuel ions (deuterium, tritium), fusion product ions (helium) and elements from the ICF target ablator (hydrogen, carbon) interact with chamber materials. These interactions induce sputtering, redeposition, and displacement damage, thereby modifying tritium retention and permeation behavior.

To address these coupled processes, GenF is developing a four-step integrated dynamic model that combines open-source and restricted-access codes. First, the distribution of incident ions is obtained using the CEA-owned code TROLL. Next, the FINGAL module, being developed at GenF, computes energy transfer to neutral gas and impurities. Surface erosion, implantation probabilities, implantation ranges and sub-surface vacancy distributions are then evaluated with SDTrimSP. Finally, the open-source FESTIM code simulates tritium transport, retention, and outgassing in chamber materials.

This integrated framework provides a predictive tool to estimate material lifetime, assess tritium inventory, and support safety evaluations in inertial fusion power plant design.



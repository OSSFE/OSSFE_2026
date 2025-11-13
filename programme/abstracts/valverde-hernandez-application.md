---
title: 'Application of containmentFOAM to calculate suffocation risk during a cryogenic helium leak in the fusion facility IFMIF-DONES '
authors:
  - name: Jaime Valverde-hernandez
    affiliations:
      - Universidad Politécnica de Madrid (UPM)
  - name: Kevin Fernández-Cosials
    affiliations:
      - Universidad Politécnica de Madrid (UPM)
  - name: Stephan Kelm
    affiliations:
      - Forschungszentrum Jülich GmbH
license: CC-BY-4.0
exports:
  - format: pdf
    template: ../../template
site:
  hide_toc: false
---

containmentFOAM is an open-source package, currently available as an add-on to OpenFOAM®-11, whose modelling basis was originally tailored to the needs of containment safety analyses in nuclear power plants. This CFD code combines a high-fidelity representation of the containment thermo-fluid dynamics with a representation of safety systems (PARs, Suppression Pools, rupture foils, etc.)  at the system level. The validation basis of containmentFOAM proves its ability to model buoyancy-driven flows in multi-species gas mixtures, which motivates its application to other disciplines such as industrial hydrogen safety or the safety analysis of future fusion facilities.
In this work, an application case of containmentFOAM to the fusion facility IFMIF-DONES is presented. In particular, the code has been used to evaluate the suffocation risk related to a cryogenic helium leak inside the facility. The modelling has been validated using data from a similar experiment performed at CERN. A soft coupling is applied between Melcor for-fusion and containmentFOAM to calculate the sudden vaporization of liquid helium with MELCOR, and then pass the massflowrate to the CFD, and thus, calculate the advection-diffusion into the large enclosure. The results have been taken into account to provide for safety measures in the facility. 


# Repository
https://iffgit.fz-juelich.de/containmentfoam_developers/containmentfoam_of6


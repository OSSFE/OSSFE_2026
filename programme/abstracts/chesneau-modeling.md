---
title: 'Modeling an Inertial Fusion Reactor system using CoSApp, an open-source Python library.'
authors:
  - name: Hugo Chesneau
    affiliations:
      - GenF
  - name: Mykola Ialovega
    affiliations:
      - GenF
  - name: Florian Condamine
    affiliations:
      - GenF
  - name: Hervé Besaucèle
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

GenF is developing a system model of an Inertial Fusion Reactor (IFR) using CoSApp (Collaborative System Approach), an open-source Python library. CoSApp represents subsystems as modular components that can be interconnected and exchange information (inputs/outputs). This versatile library enables the design of complex systems by solving nonlinear equations imposed by the system and its subsystems. It also supports time-dependent simulations and offers standardized interfaces such as FMU/FMI.
Our goal is to leverage CoSApp’s capabilities to design and select the optimal operating point, informed by state-of-the-art numerical modeling and future experiments. As we address the challenges of inertial fusion reactors, we gradually refine the model by increasing its complexity.
As stated, the library includes time-dependent solvers to simulate operational scenarios, complementing static design. For example, the reactor model features a time-dependent fuel cycle. Directly optimizing the simulation provides insights, among others information, into the required startup tritium inventory and tritium breeding ratio.
Beyond engineering and physical considerations, the model integrates a cost estimation module, enabling direct evaluation of the levelized cost of electricity for any given design. As the model evolves, we aim to approach a digital twin of the IFR.


# Repository
https://gitlab.com/cosapp/cosapp


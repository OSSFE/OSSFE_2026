---
title: 'TRICYS: An Open-Source Architecture for Tool-Coupled Tritium Fuel Cycle Simulation'
authors:
  - name: Xiaokang Zhang
    affiliations:
      - Institute of Plasma Physics, Hefei Institutes of Physical Sciences, Chinese Academy of Sciences, Hefei 230031, China
  - name: Long Gui
    affiliations:
      - Institute of Energy, Hefei Comprehensive National Science Center, Hefei 230031, China
  - name: Chuan Jin
    affiliations:
      - University of Science and Technology of China, Hefei 230026, China
  - name: Yan Lan
    affiliations:
      - Institute of Plasma Physics, Hefei Institutes of Physical Sciences, Chinese Academy of Sciences, Hefei 230031, China
  - name: Shikun Zhang
    affiliations:
      - University of Science and Technology of China, Hefei 230026, China
  - name: Zihao Zhu
    affiliations:
      - University of Science and Technology of China, Hefei 230026, China
  - name: Yiming Lv
    affiliations:
      - Institute of Energy, Hefei Comprehensive National Science Center, Hefei 230031, China
  - name: Shanliang Zheng
    affiliations:
      - Institute of Plasma Physics, Hefei Institutes of Physical Sciences, Chinese Academy of Sciences, Hefei 230031, China
license: CC-BY-4.0
exports:
  - format: pdf
    template: ../../template
site:
  hide_toc: false
github: 'https://github.com/OSSFE/OSSFE_2026'
---

Coupling a fusion tritium fuel cycle (TFC) model to heterogeneous external tools remains a practical bottleneck: subsystem models are developed in different ecosystems (process simulation, Modelica, multiphysics), data interfaces drift over time, and results become difficult to reproduce or verify—especially under large parameter scans. We present TRICYS (TRitium Integrated CYcle Simulation), an Apache-2.0 open-source and configuration-driven platform for end-to-end TFC modeling and analysis that treats co-simulation and data exchange as first-class capabilities. TRICYS supports multi-fidelity workflows, combining a fast 0D / system-dynamics fuel-cycle layer with high-fidelity external sub-models, including Aspen Plus (process units), OpenModelica (component/system dynamics via OMPython), and COMSOL-based multiphysics modules. A scenario is defined via JSON/YAML configuration; TRICYS orchestrates execution, tracks inputs/outputs, and produces structured run artifacts suitable for review and reruns. To maintain credibility in integrated studies, TRICYS performs plant-wide mass-conservation and inventory-closure checks, enabling regression detection as models evolve. We demonstrate TRICYS on a CFEDR representative tokamak fuel-cycle scenario, showing how tool-coupled studies can be performed reproducibly across design variants and operational assumptions, while retaining transparent provenance. The workflow integrates automated analysis outputs and optional lightweight AI-assisted reporting to help summarize results without obscuring underlying data. The project follows open-source engineering practices, including continuous integration for formatting and quality gates.

# Repository
https://github.com/asipp-neutronics/tricys


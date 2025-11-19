---
title: 'NuPlant: Accelerating Fusion Power Plant Design and Optimisation with AI-Driven Multiphysics and Cost Modelling'
authors:
  - name: Muhammad Omer
    affiliations:
      - nTtau Digital
  - name: Simon Woodruff
    affiliations:
      - nTtau Digital
  - name: Dominic Longhorn
    affiliations:
      - nTtau Digital
  - name: Sophie Sharpe
    affiliations:
      - nTtau Digital
  - name: Abinash Manikandan
    affiliations:
      - nTtau Digital
  - name: Luis Garcia
    affiliations:
      - nTtau Digital
  - name: Noe Adepoju
    affiliations:
      - nTtau Digital
  - name: Megan Crocker
    affiliations:
      - nTtau Digital
  - name: Max Moreland
    affiliations:
      - nTtau Digital.
license: CC-BY-4.0
exports:
  - format: pdf
    template: ../../template
site:
  hide_toc: false
github: 'https://github.com/OSSFE/OSSFE_2026'
---

This study presents NuPlant, a Python-based generative design and optimisation tool developed for fusion power plants, covering components from the first wall to the site boundary. Fusion plant design is a multi-scale challenge, with interdependent requirements across plasma-facing components, blanket and shielding systems, magnets, reactor halls, and site infrastructure. Traditional approaches rely on sequential engineering loops and high-fidelity simulations that are time-intensive, computationally expensive, and often unable to efficiently explore wide design spaces. NuPlant addresses these limitations by integrating physics-informed simulations, surrogate modelling, and multi-objective optimisation into an automated, end-to-end workflow. The methodology combines parametric geometry generation, meshing, and multiphysics simulations—including electromagnetic, neutronics, thermal, and structural mechanics—together with cost modelling. Surrogate models are trained on simulation outputs to predict key performance and design metrics such as Tritium Breeding Ratio (TBR), displacements per atom (DPA), first-wall heating, coil spacing and curvature, electromagnetic loads, component stresses, and reactor cost. These models enable rapid exploration of the design space within seconds. Multi-objective optimisation is then applied to identify Pareto-optimal solutions, balancing performance, efficiency, cost, and manufacturability. NuPlant operates at multiple scales, from component-level design to system-level reactor configuration and full site planning. The results show that NuPlant can reduce design timelines from months to hours while maintaining accuracy sufficient for early-stage decision-making. It generates manufacturable, code-compliant, and cost-aware outputs across plant, component, and site levels. By providing a scalable and modular optimisation framework, NuPlant supports fusion researchers, engineers, and project developers in accelerating progress toward economically viable and technically robust fusion power plant designs.


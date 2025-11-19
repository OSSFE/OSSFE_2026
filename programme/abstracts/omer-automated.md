---
title: 'Automated Design and Cost Estimation of Fusion Power Plant Buildings Using a Python Framework'
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
  - name: and Megan Crocker
    affiliations:
      - nTtau Digital
license: CC-BY-4.0
exports:
  - format: pdf
    template: ../../template
site:
  hide_toc: false
github: 'https://github.com/OSSFE/OSSFE_2026'
---

This study presents a Python-based workflow that automates the preliminary design and costing of fusion power plant buildings. Building costs are among the major cost drivers in fusion power plant design, and it is therefore critical to estimate them accurately. Current costing models rely on top-down or percentage-based methods, which systematically over-estimate costs, resulting in inflated capital requirements and reduced confidence in the economic viability of fusion projects. Traditional approaches are also manual, fragmented, and dependent on expert judgment, making them time-intensive and inflexible when evaluating diverse fusion concepts. An integrated and automated tool that applies a bottoms-up approach—estimating costs from first principles by deriving material quantities, structural requirements, and layout rules—to translate reactor design parameters into realistic building layouts and accurate cost estimates is therefore essential.The methodology implements the ARPA-E Costing Tool cost category 21 within a Python framework. Based on input parameters such as reactor power, fuel type and other plant characteristics, the tool generates preliminary requirements for building types, sizes, and layouts. Building sizes are then automatically fine-tuned to fulfil all necessary functional requirements. Structural design rules for concrete and steel, derived from Eurocode and ACI handbooks, are embedded to estimate the quantities of concrete and reinforcement required for each structural element. Building costs are automatically processed, with a bill of materials for every element.The results demonstrate that the workflow can generate scalable building layouts and high-fidelity cost estimates calibrated against NETL references. It reduces manual effort, accelerates design iteration, and provides traceable outputs for early-stage planning. This work enables fusion researchers, engineers, and project developers to accurately estimate infrastructure costs, make informed design decisions, and rapidly optimise fusion power plant



---
title: 'ConStellaration: A dataset of QI-like stellarator plasma boundaries and optimization benchmarks'
authors:
  - name: Santiago A. Cadena
    affiliations:
      - Proxima Fusion
  - name: Andrea Merlo
    affiliations:
      - Proxima Fusion
  - name: Emanuel Laude
    affiliations:
      - Proxima Fusion
  - name: Alexander Bauer
    affiliations:
      - Proxima Fusion
  - name: Atul Agrawal
    affiliations:
      - Proxima Fusion
  - name: Maria Pascu
    affiliations:
      - Proxima Fusion
  - name: Marija Savtchouk
    affiliations:
      - Proxima Fusion
  - name: Enrico Guiraud
    affiliations:
      - Proxima Fusion
  - name: Lukas Bonauer
    affiliations:
      - Proxima Fusion
  - name: Stuart Hudson
    affiliations:
      - Proxima Fusion
  - name: Markus Kaiser
    affiliations:
      - Proxima Fusion
license: CC-BY-4.0
exports:
  - format: pdf
    template: ../../template
site:
  hide_toc: false
github: 'https://github.com/OSSFE/OSSFE_2026'
---

Stellarators are magnetic confinement devices under active development to deliver steady-state carbon-free fusion energy. Their design involves a high-dimensional, constrained optimization problem that requires expensive physics simulations and significant domain expertise. Recent advances in plasma physics and open-source tools have made stellarator optimization more accessible. However, broader community progress is currently bottlenecked by the lack of standardized optimization problems with strong baselines and datasets that enable data-driven approaches, particularly for quasi-isodynamic (QI) stellarator configurations, considered as a promising path to commercial fusion due to their inherent resilience to current-driven disruptions. Here, we release an open dataset of diverse QI-like stellarator plasma boundary shapes, paired with their ideal magnetohydrodynamic (MHD) equilibria and performance metrics. We generated this dataset by sampling a variety of QI fields and optimizing corresponding stellarator plasma boundaries. We introduce three optimization benchmarks of increasing complexity: (1) a single-objective geometric optimization problem, (2) a "simple-to-build" QI stellarator, and (3) a multi-objective ideal-MHD stable QI stellarator that investigates trade-offs between compactness and coil simplicity. For every benchmark, we provide reference code, evaluation scripts, and strong baselines based on classical optimization techniques. Finally, we show how learned models trained on our dataset can efficiently generate novel, feasible configurations without querying expensive physics oracles. By openly releasing the dataset along with benchmark problems and baselines, we aim to lower the entry barrier for optimization and machine learning researchers to engage in stellarator design and to accelerate cross-disciplinary progress toward bringing fusion energy to the grid.

# Repository
https://github.com/proximafusion/constellaration


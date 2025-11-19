---
title: 'Machine learning algorithm coupled with multi-objective optimization for radiation shielding in fusion reactor application'
authors:
  - name: M. Di Giacomo
    affiliations:
      - ATG Science & Engineering S.L., Plaza Ernest Lluch i Martin 5, Barcelona 08019, Spain
  - name: A. Cubi
    affiliations:
      - Fusion for Energy, Josep Pla 2, Barcelona 08019, Spain
  - name: M. Campos
    affiliations:
      - ATG Science & Engineering S.L., Plaza Ernest Lluch i Martin 5, Barcelona 08019, Spain
  - name: D. Laghi
    affiliations:
      - Fusion for Energy, Josep Pla 2, Barcelona 08019, Spain
  - name: A. Bittesnich
    affiliations:
      - ATG Science & Engineering S.L., Plaza Ernest Lluch i Martin 5, Barcelona 08019, Spain
  - name: A. Kolsek
    affiliations:
      - Fusion for Energy, Josep Pla 2, Barcelona 08019, Spain
  - name: M. Fabbri
    affiliations:
      - Fusion for Energy, Josep Pla 2, Barcelona 08019, Spain
  - name: A. Portone
    affiliations:
      - Fusion for Energy, Josep Pla 2, Barcelona 08019, Spain
license: CC-BY-4.0
exports:
  - format: pdf
    template: ../../template
site:
  hide_toc: false
github: 'https://github.com/OSSFE/OSSFE_2026'
---

This work focuses on the development of a robust computational methodology for the design and optimization of shielding cabinets in nuclear fusion applications. The approach integrates multi-objective genetic algorithms (GA), machine learning (ML), and, optionally, physics-informed neural networks (PINNs) that can be employed by the user when available datasets are limited for the application. The methodology systematically explores and evaluates multi-layer shielding configurations using realistic materials, with MCNP neutronics simulations providing key physical outputs for model training and validation. While the primary emphasis is on shielding cabinet design, the framework is structured to be extensible to other fusion system challenges, including, e.g., tritium breeding ratio (TBR) optimization, magnet shielding optimization, and additional engineering parameters. The modular and adaptable nature of the workflow enables future expansion to a wide range of fusion reactor applications. This methodology is intended for use in the preliminary design phase, as it relies on simplified models and simulations; it is not recommended for more advanced, detailed design studies. Ongoing work is focused on validating the PINN models and optimizing the ML architecture and its integration with the GA workflow, with the ultimate goal of supporting the development of an intelligent agent capable of interacting via natural language to recommend optimal shielding designs based on user requirements. The Shield4Fusion (S4F) workflow is being developed as an open source tool and will be made publicly available on GitHub to support collaborative research and practical application in the fusion community.


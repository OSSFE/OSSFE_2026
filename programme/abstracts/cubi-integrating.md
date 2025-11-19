---
title: 'Integrating complex MCNP models into the Gitronics workflow: the ITER E-Lite use case'
authors:
  - name: Alvaro Cubi
    affiliations:
      - Fusion for Energy
  - name: Marco Fabbri
    affiliations:
      - Fusion for Energy
  - name: Aljaz Kolsek
    affiliations:
      - Fusion for Energy
  - name: Davide Laghi
    affiliations:
      - Fusion for Energy
  - name: Alberto Bittesnich
    affiliations:
      - Fusion for Energy
  - name: Alfredo Portone
    affiliations:
      - Fusion for Energy
license: CC-BY-4.0
exports:
  - format: pdf
    template: ../../template
site:
  hide_toc: false
github: 'https://github.com/OSSFE/OSSFE_2026'
---

Radiation transport models for fusion devices have experienced a significant increase in complexity in the latest years in a trend that is expected to continue in the future. This increase in complexity has exacerbated the challenges of proper version control, traceability and collaboration. Gitronics is a workflow and associated Python package that can manage MCNP models as a collection of smaller, single-responsibility files in a manner analogue to the software development industry employing Git and Gitlab. One of the most complex radiation transport models under development, the ITER E-Lite model has been adapted to the Gitronics workflow. This paper reports the process by which the original monolithic 7 million lines long E-Lite file was divided into hundreds of smaller independent files and organized into a Gitronics project. This new version of the model successfully compiled an MCNP input file that was used and tested in simulations to assess any difference with the original file. The tests show that the geometry representation (i.e., cells, surfaces, material assignment) of the compiled version is statistically identical to the original one confirming the validity of the adaptation and the Gitronics workflow. Significant changes were also made to the Gitronics package to better handle such a complex project efficiently.

# Repository
https://github.com/Fusion4Energy/gitronics


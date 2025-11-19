---
title: 'Automating FLASH Code using Galaxy Workflow'
authors:
  - name: Abinash Manikandan
    affiliations:
      - nTtau Digital Ltd, United Kingdom
  - name: Muhammad Omer
    affiliations:
      - nTtau Digital Ltd, United Kingdom
  - name: Sophie Sharpe
    affiliations:
      - nTtau Digital Ltd, United Kingdom
  - name: Noe Adepoju
    affiliations:
      - nTtau Digital Ltd, United Kingdom
  - name: Megan Crocker
    affiliations:
      - nTtau Digital Ltd, United Kingdom
  - name: Dominic Longhorn
    affiliations:
      - nTtau Digital Ltd, United Kingdom
  - name: Luis Garcia
    affiliations:
      - nTtau Digital Ltd, United Kingdom
  - name: Max Moreland
    affiliations:
      - nTtau Digital Ltd, United Kingdom
  - name: Simon Woodruff
    affiliations:
      - nTtau Digital Ltd, United Kingdom
license: CC-BY-4.0
exports:
  - format: pdf
    template: ../../template
site:
  hide_toc: false
github: 'https://github.com/OSSFE/OSSFE_2026'
---

This study presents an automated workflow that integrates FLASH radiation-hydrodynamics code with the Galaxy platform, thereby automating FLASH to streamline simulation execution. The growing complexity of fusion simulations, with multiple input variations, often leads to lost data, delays, and reduced traceability. Traditional manual setup and execution of FLASH code is slow, isolated, and hinder collaboration. Embedding FLASH within Galaxy overcomes these challenges by providing an automated workflow that ensures transparency, provenance, and reproducibility. The methodology implements FLASH 4.8 within a containerised environment in Galaxy. As a case study, the Magnetized Noh Z-pinch problem—a strong shock test using density and pressure profiles—is simulated. Input files (Makefile, configuration file, runtime parameters, and Fortran sources) are included in an XML wrapper and uploaded as inputs. The tool automatically executes the run and generates results in HDF5 format, which can be visualised with tools such as VisIt. Results are validated against a reference Z-pinch run performed directly in Docker. The results demonstrate that this automated approach reduces manual effort, accelerates design iteration by simplifying repeated runs with varying inputs, and provides a transparent, traceable record of simulations that preserves provenance and supports collaboration across teams. The work will benefit fusion researchers, designers, computational scientists, and code developers, as well as the broader nuclear engineering community.


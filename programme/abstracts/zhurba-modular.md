---
title: 'Modular Tokamak Design and Simulation Open Source Framework'
authors:
  - name: A. Zhurba
    affiliations:
      - Next Step Fusion
  - name: A. Asaturov
    affiliations:
      - Next Step Fusion
  - name: E.N. Khairutdinov
    affiliations:
      - Next Step Fusion
  - name: M.R. Nurgaliev
    affiliations:
      - Next Step Fusion
  - name: G.F. Subbotin
    affiliations:
      - Next Step Fusion
license: CC-BY-4.0
exports:
  - format: pdf
    template: ../../template
site:
  hide_toc: false
github: 'https://github.com/OSSFE/OSSFE_2026'
---

The Digital Replica Builder (DRB) is the first open-source component of Next Step Fusion's Modular Tokamak Design and Simulation Open Source Framework. This tool allows users to draw the tokamak geometry—including the vessel, limiter, blanket, coils, loops, probes, and other elements—and generate their digital representations. This provides a flexible and customizable starting point for tokamak design, simulation, and research.

The DRB is designed as the initial step for tokamak design, creating inputs that can be used with any simulation code. Next Step Fusion, for example, uses these outputs for further modeling with its own NSFsim simulator. While the DRB is already integrated into the Fusion Twin Platform (https://fusiontwin.io), it's also available as a standalone tool that you can deploy from its public repository to GitHub Pages, Cloudflare Pages, or similar hosting.

Key Features of DRB:
Web-based: The DRB does not require any specific hardware or software other than a personal computer and a modern web browser.
Free permissive license: Next Step Fusion distributes the DRB under a permissive license that allows for any use, including commercial. The only requirements are to provide credit to the company and, when possible, suggest changes to the original repository.
Easy-to-use point-and-click interface: The DRB's interface is optimized for point-and-click usage and is enhanced with shortcuts, yet it remains simple and easy to use.
Tokamak components support: The DRB supports the vessel, limiter, blanket, coils, TF coils, loops, probes, passive elements, and plasma shape with customizable drawing functions and a shape inspector.
Import and export: The DRB allows you to export your results as a JSON file and import them back to continue your work.


Fig. 1. Digital Replica Builder user interface using an ITER-like tokamak 1:10 scale.

A separate, fully integrated version of the Digital Replica Builder (DRB) is available within the Fusion Twin Platform at https://fusiontwin.io. This deep integration allows users to save their digital replicas to the cloud, share them with others, and run magnetic equilibrium simulations using the advanced tokamak simulator NSFsim with their newly designed replicas.

# Repository
https://github.com/Next-Step-Fusion/replica-builder/


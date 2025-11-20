---
title: 'FreeGSNKE Pulse Design Tool: in-silico scenario design and control validation for tokamak plasmas'
authors:
  - name: Kamran Pentland
    affiliations:
      - UKAEA: Nicola C Amorisco, UKAEA
  - name: Alasdair Ross
    affiliations:
      - STFC Hartree Centre
  - name: Pedro Cavestany
    affiliations:
      - STFC Hartree Centre
  - name: George Holt
    affiliations:
      - STFC Hartree Centre
  - name: Adriano Agnello
    affiliations:
      - STFC Hartree Centre
  - name: Charlie Vincent
    affiliations:
      - UKAEA
  - name: Graham McArdle
    affiliations:
      - UKAEA
  - name: Tim Nunn
    affiliations:
      - UKAEA
  - name: James Buchanan
    affiliations:
      - UKAEA
  - name: Stan Pamela
    affiliations:
      - UKAEA
license: CC-BY-4.0
exports:
  - format: pdf
    template: ../../template
site:
  hide_toc: false
github: 'https://github.com/OSSFE/OSSFE_2026'
---

I’ll cover continuing progress on FreeGSNKE, a fully open-source Python code for simulating both static and evolutive tokamak plasma equilibria. Alongside existing static forward/inverse and evolutive forward solvers, the FreeGSNKE ecosystem now also includes capabilities for calculating virtual circuits and vertical growth rates. Recent work has focused on equipping FreeGSNKE with a Plasma Control System (PCS) to enable plasma position, shape, and current control. While inspired by the controllers used on the MAST Upgrade tokamak, the framework can be customised to any axisymmetric machine. The resulting FreeGSNKE Pulse Design Tool (FPDT) supports in-silico scenario design, control design, and control validation. We aim to open source this tool as part of the FreeGSNKE ecosystem.

# Repository
https://github.com/FusionComputingLab/freegsnke


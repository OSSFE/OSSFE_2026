---
title: 'An Open-Source Divertor Digital Twin Environment for Fusion Power Plants'
authors:
  - name: Michael I. Battye
    affiliations:
      - University of York
license: CC-BY-4.0
exports:
  - format: pdf
    template: ../../template
site:
  hide_toc: false
---

Digital engineering is reshaping fusion R&D, and the in-development **Divertor Digital Twin Environment (DDTE)** aims to provide an end-to-end, *open-source* workflow that shortens the path from late-stage divertor design to plant operation readiness. The DDTE is organised around three complementary flavours, each deliberately modular so that best-in-class community codes can be swapped in as they mature.

**Design Studio**
Starting from native CAD or equilibrium geometry, the pipeline invokes established mesh generators to create prototype meshes and optimises candidate diagnostics. Material and thermal properties are inserted via OMAS-compatible databases, ready for local or HPC execution.

**Scenario Lab**
3D plasma-surface interaction scenarios are assembled by chaining HEAT, FUSE and, as development continues, edge-SOL solvers such as SOLPS-ITER and HERMES-3. Each run outputs time-resolved temperature, stress and erosion fields annotated with VVUQ metadata, and feeds a prognostics-and-health-management module estimating damage accumulation.

**Twin Console**
A divertor digital twin instance will ingest live diagnostic streams (infrared, thermocouples) and *fuse* sensor data before *assimilating* into an ensemble of scenario predictions through Bayesian state estimation. The console reconciles data gaps and forecasts lifetime & maintenance windows.

Key characteristics are: (i) free and open-source software licensing to encourage broad uptake; (ii) an intuitive GUI with scripting back-ends to assist commercialisation; (iii) active multi-institutional co-design to avoid “reinventing the wheel”; and (iv) easy-click installer *and* pre-built Apptainer deployment that scales from laptops to clusters. Current prototyping milestones are presented together with a roadmap that charts the next steps toward a minimally viable DDTE.


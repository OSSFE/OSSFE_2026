---
title: 'FESTIM V&V efforts on advanced coupled problems'
authors:
  - name: Huihua Yang
    affiliations:
      - Plasma Science and Fusion Center, Massachusetts Institute of Technology, Cambridge, MA 02139, USA
  - name: James Dark
    affiliations:
      - Plasma Science and Fusion Center, Massachusetts Institute of Technology, Cambridge, MA 02139, USA
  - name: Abhishek Saraswat
    affiliations:
      - Plasma Science and Fusion Center, Massachusetts Institute of Technology, Cambridge, MA 02139, USA
  - name: Weiyue Zhou
    affiliations:
      - Plasma Science and Fusion Center, Massachusetts Institute of Technology, Cambridge, MA 02139, USA
  - name: Kevin Woller
    affiliations:
      - Plasma Science and Fusion Center, Massachusetts Institute of Technology, Cambridge, MA 02139, USA
  - name: LIBRA Team
    affiliations:
      - Plasma Science and Fusion Center, Massachusetts Institute of Technology, Cambridge, MA 02139, USA
  - name: Eathan Peterson
    affiliations:
      - Plasma Science and Fusion Center, Massachusetts Institute of Technology, Cambridge, MA 02139, USA
  - name: Remi Delaporte-Mathurin
    affiliations:
      - Plasma Science and Fusion Center, Massachusetts Institute of Technology, Cambridge, MA 02139, USA
license: CC-BY-4.0
exports:
  - format: pdf
    template: ../../template
site:
  hide_toc: false
github: 'https://github.com/OSSFE/OSSFE_2026'
---

Achieving tritium self-sufficiency is a central requirement for fusion energy systems, placing tritium transport and breeding in blanket-relevant materials at the core of blanket design. The LIBRA (Liquid Immersion Blanket: Robust Accountancy) project at MIT will be the first initiative to demonstrate reproducible and scalable tritium breeding in molten salts. Its small-scale counterpart, the BABY (Build A Better Yield blanket) experiment, is providing essential benchmarks for tritium breeding and release in molten salt breeder systems under deuterium-tritium (D-T) irradiation. LIBRA is complemented by HYPERION: a permeation experiment for measuring FLiBe permeability to hydrogen isotopes (protium, deuterium) currently in operation at the MIT Plasma Science and Fusion Center (PSFC). These emerging datasets provide the foundation for validating predictive modeling tools, which, once benchmarked against experiments, can support result interpretation, guide blanket design, and identify further data needs.
[FESTIM (Finite-Element Simulation of Tritium in Materials)] (https://github.com/festim-dev/FESTIM) is an open-source, Python-based finite-element framework for multi-dimension, multi-material, multi-species hydrogen transport. In this work, we validate FESTIM against the HYPERION and LIBRA experiments. We also perform uncertainty and sensitivity analyses on parameters like diffusivity, trapping parameters, and surface reaction kinetics, etc. The simulations show very good agreement with the experimental data, supporting FESTIM as a reliable tool for design exploration and safety assessments of blanket concepts (and other fuel cycle components), and providing guidance for experimental design and operation choices as well as data needs in future studies.

# Repository
https://github.com/festim-dev


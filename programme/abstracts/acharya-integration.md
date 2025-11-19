---
title: ' Integration of Open-Source Fusion Codes into Commercial Design Workflows'
authors:
  - name: Sunil Acharya
    affiliations:
      - Ansys Inc
  - name: Sandeep Medikonda
    affiliations:
      - Ansys Inc
  - name: Vikas Namdeo
    affiliations:
      - Ansys Inc
  - name: Abhishek Chitwar
    affiliations:
      - Ansys Inc
license: CC-BY-4.0
exports:
  - format: pdf
    template: ../../template
site:
  hide_toc: false
github: 'https://github.com/OSSFE/OSSFE_2026'
---

The transition to commercially viable fusion energy necessitates rapid, reliable, and iterative design cycles. Open-source fusion codes offer important, high-fidelity capabilities for core fusion technology, particularly in domains like neutronics transport (e.g., OpenMC, MCNP) and advanced plasma physics. 

Yet, a critical disconnect persists: design engineers in commercial organizations are primarily proficient with proprietary codes that offer production-ready environments for simulating the critical supporting disciplines of thermal, structural, and electromagnetic problems. The reliance on these commercial modeling tools, while necessary for integrated system design, creates friction in incorporating the latest community-validated physics and nuclear research crucial for fusion performance. 

This presentation argues that to meet the validation rigor and iterative speed required for commercialization, engineering firms must implement a hybrid modeling strategy that formally integrates these specialized, transparent open-source fusion codes into their core design workflows. 

We propose a practical software integration framework centered on Python-based scripting and API tools (such as PyAnsys for commercial solver interaction) to manage and automate the seamless data exchange between proprietary CAD/FEA/CFD environments and specialized open-source physics packages. The key strategic pillars of this integration include: 

Data Communication: Allowing flexible yet robust data transfer between open source code for seamless transfer of complex geometry, mesh, and material definitions. 

Workflow Orchestration: Leveraging Python to script end-to-end processes, enabling rapid parametric studies across proprietary and open-source solvers. 

Enhanced V&V: Utilizing open-source codebases for transparent comparison, validation, and sensitivity analysis against proprietary results, significantly reducing technical risk. 

By embracing this paradigm, commercial organizations can move beyond basic proprietary capabilities, create more robust and agile design processes, and accelerate the development of commercially viable fusion power plants. This talk provides a roadmap for engineering managers and software architects looking to harness the synergistic power of commercial stability and open-source innovation. 


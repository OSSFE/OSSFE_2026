---
title: 'Integration of MARTe2 into the General Atomics Plasma Control System for Real-Time Simulink Model Execution and Parameterisation'
authors:
  - name: Edward Jones
    affiliations:
      - UKAEA
  - name: Colin Hogden
    affiliations:
      - UKAEA
  - name: Richard Lucock
    affiliations:
      - UKAEA
  - name: Charlie Boswell
    affiliations:
      - UKAEA
  - name: Hudson Baker
    affiliations:
      - UKAEA
  - name: Graham Jones
    affiliations:
      - UKAEA
  - name: Adam Stephen
    affiliations:
      - UKAEA
  - name: Graham McArdle
    affiliations:
      - UKAEA
  - name: P. A. Figueiredo
    affiliations:
      - DIFFER, Eindhoven University of Technology
  - name: J. T. Veenendaal
    affiliations:
      - DIFFER, Eindhoven University of Technology
license: CC-BY-4.0
exports:
  - format: pdf
    template: ../../template
site:
  hide_toc: false
github: 'https://github.com/OSSFE/OSSFE_2026'
---

This work presents the integration of the MARTe2 real-time framework into the General Atomics Plasma Control System (GA PCS) to enable the offloading of control algorithms from PCS to MARTe2. MARTe2 provides an interoperable, extensible, and configuration-driven environment that avoids the need for direct C or C++ programming, making it well suited for flexible control development. Within this project, a Simulink model has been embedded into the MARTe2 “co-processor” and subsequently incorporated into GA PCS, with full parameterisation consistent with PCS conventions. This allows operators to use one of the main control engineering tools and, to adjust model parameters—or even swap the model itself—directly from the PCS graphical interface on a per-shot basis. To support this integration, modifications and new MARTe2 features were developed. Notably, a UDP Source was implemented as a real-time thread blocker that flushes packet buffers and ensures only the latest data is processed, accounting for the higher operating frequency of PCS while maintaining synchronous operation. Additionally, a SimulinkWrapper GAM was extended to permit dynamic reset and modification of models and parameters without halting MARTe2 execution. Together, these developments demonstrate a practical path for incorporating advanced models into PCS through MARTe2, enhancing flexibility, usability, and real-time capability.

# Repository
https://github.com/ukaea/marte2-components


---
title: 'Deep Learning–Based Surrogate Models and RL Control for Extreme Vacuum Environments in Fusion Research'
authors:
  - name: Guillermo Rodríguez-Llorente
    affiliations:
      - HI Iberia & Universidad Carlos III & Gregorio Millán Barbany Institute
  - name: Galo Gallardo Romero
    affiliations:
      - HI Iberia
  - name: Rodrigo Morant Navascués
    affiliations:
      - HI Iberia
  - name: Nikita Khvatkin Petrovsky
    affiliations:
      - HI Iberia
  - name: Anderson Sabogal
    affiliations:
      - IFMIF-DONES Spain
  - name: Roberto Gómez-Espinosa Martín
    affiliations:
      - HI Iberia
license: CC-BY-4.0
exports:
  - format: pdf
    template: ../../template
site:
  hide_toc: false
---

Progress in nuclear fusion is tightly bound to the research of materials that can endure extreme irradiation environments. To evaluate these materials, the IFMIF-DONES facility is being developed as a high-power particle accelerator, with the MuVacAS prototype reproducing the vacuum conditions of its final beam-line segment. Precise regulation of argon pressure inside the ultra-high vacuum chamber is crucial in this setup. This work presents a fully data-driven approach for autonomous pressure control. A Deep Learning Surrogate Model, trained on operational data, emulates the dynamics of the argon injection system and replaces the prototype with a safe simulator. Within this environment, a Deep Reinforcement Learning agent learns a control policy that maintains pressure within strict limits despite disturbances.Then the validation is donde by the deployment of the agent in real prototype. The implementation relies exclusively on open-source tools, even the control system, ensuring transparency, reproducibility, and accessibility. The results demonstrate that combining surrogate modeling and reinforcement learning enables intelligent control strategies for next-generation fusion energy facilities.


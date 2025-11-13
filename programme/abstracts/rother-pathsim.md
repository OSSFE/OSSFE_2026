---
title: 'PathSim: An Open-Source Python Framework for Dynamic System Simulation in Fusion Energy Applications'
authors:
  - name: Milan Rother
    affiliations:
      - Independent
license: CC-BY-4.0
exports:
  - format: pdf
    template: ../../template
site:
  hide_toc: false
---

PathSim is an open-source Python simulation framework designed for block-based dynamic system modeling as an open source replacement for Simulink or Aspen. The framework addresses the need for native Python simulation tools supporting signal flow diagram paradigms, enabling seamless integration with the broader scientific computing ecosystem used in fusion research.
PathSim implements advanced numerical integration methods including high-order implicit solvers, making it suitable for the stiff differential equations commonly encountered in fusion system modeling. The framework's modular architecture enables easy extension with domain-specific blocks for fusion applications, including fuel cycle modeling, plasma control systems, and tritium transport analysis.
A key feature of PathSim is its event handling system that can detect state-dependent events during simulation and dynamically modify or restart system components at runtime. This capability is essential for modeling complex fusion systems where discrete events such as operational mode changes impact system behavior.
Current applications include residence time modeling for chemical process flows in fusion reactor fuel cycles. The framework's extensible design facilitates integration with existing fusion simulation codes and finite element models, supporting unified multi-physics simulations and co-simulation workflows. PathSim's Python foundation enables coupling with machine learning frameworks and modern data analysis tools increasingly used in fusion research.
PathSim is freely available under an open-source license, providing the fusion community with a flexible platform for developing specialized simulation capabilities while leveraging robust numerical foundations.


# Repository
https://github.com/milanofthe/pathsim


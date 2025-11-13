---
title: 'The FEniCS Finite Element framework: introduction and applications in nuclear fusion simulations'
authors:
  - name: Massimiliano Leoni
    affiliations:
      - Proxima Fusion
license: CC-BY-4.0
exports:
  - format: pdf
    template: ../../template
site:
  hide_toc: false
---

In this talk we present FEniCS, a powerful and versatile framework for the solution of general Partial Differential Equations via the Finite Element method.
We will start from a gentle introduction to how to solve the "Hello world" of PDEs, the Poisson equation, to then turn to applications of FEniCS to some real-world problems that we faced, and successfully tackled, at Proxima Fusion, where we use FEniCS to automate large scale analyses of stellarator candidates, as well as study components' reactions to a variety of different conditions or quickly evaluate possible designs to filter out the most promising ones.
Thanks to the flexibility of the Finite Element method, and of the software framework that we use, we can easily write customized solvers for simulations spanning a wide range of physical domains, from thermal diffusion to structural mechanics, from particle transport to electromagnetism, both in n-dimensional space and on domains with codimension greater than zero.
Although it's written in C++ for maximum performance, FEniCS offers a Python interface that makes it easy to encapsulate and integrate solvers with existing tools as part of an external workflow, be it an optimization loop, an orchestrator for a parameter scan, or other pipelines.

# Repository
https://github.com/FEniCS


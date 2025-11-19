---
title: 'Tutorial: an introduction to the Gkeyll simulation framework for both research and education'
authors:
  - name: James Juno
    affiliations:
      - PPPL
  - name: Ammar Hakim
    affiliations:
      - PPPL
  - name: Jonathan Gorard
    affiliations:
      - Princeton University
  - name: Manaure Francisquez
    affiliations:
      - PPPL
  - name: Antoine Hoffmann
    affiliations:
      - PPPL
  - name: Tess Bernard
    affiliations:
      - General Atomics
  - name: Gregory Hammett
    affiliations:
      - PPPL
  - name: Akash Shukla
    affiliations:
      - University of Texas Austin
  - name: Jonathan Roeltgen
    affiliations:
      - University of Texas Austin
  - name: Dingyun Liu
    affiliations:
      - Princeton University
  - name: Maxwell Rosen
    affiliations:
      - Princeton University
  - name: Grant Johnson
    affiliations:
      - Princeton University
  - name: Jason TenBarge
    affiliations:
      - Princeton University
  - name: Sarah Conley
    affiliations:
      - Bates College
  - name: Petr Cagas
    affiliations:
      - Moravian Instruments
  - name: Kolter Bradshaw
    affiliations:
      - Princeton University
  - name: John Rodman
    affiliations:
      - University of Rochester
license: CC-BY-4.0
exports:
  - format: pdf
    template: ../../template
site:
  hide_toc: false
github: 'https://github.com/OSSFE/OSSFE_2026'
---

The Gkeyll simulation framework is a general-purpose plasma simulation framework being utilized across the plasma sciences, with particular fusion applications in understanding turbulence and transport in axisymmetric reactor configurations such as tokamaks and mirrors. Not only does the framework provide streamlined capabilities for handling the complexities of kinetic modeling in fusion devices, including field-line-following geometries, coupling to neutral particles through Gkeyll’s Boltzmann solver, and a variety of application-specific physics modules such as radiation and sheath boundary conditions, the software stack is sufficiently lightweight yet powerful to also make Gkeyll a useful tool in teaching computational physics. 

As a companion tutorial to a presentation on the full spectrum of fusion modeling capabilities, we will show how to build and run Gkeyll, with an overview of the scripting layer of the code written in the Lua programming language to show how one can instantiate diverse simulations without ever re-compiling the code, as well as our Python post-processing suite that makes the reading of output Gkeyll data and analysis as painless as possible. We will also show how we are utilizing Gkeyll in computational physics classes to provide a template for teaching computational physics in the era of large-language models. We focus in particular on how Gkeyll’s programming API supports a pedagogy for teaching basic software engineering while introducing at least a modest barrier to many coding assistant tools trivializing assignments. In this case, because the Gkeyll framework is sufficiently large and covering plasma applications beyond fusion modeling, with solvers for (general) relativistic fluid and kinetic plasmas for astrophysical applications, these coding assistants can struggle to ingest and learn the full scope of the code. A computational physics class can then focus on just using the methods Gkeyll has for data structures and program flow to learn foundational numerical techniques such as integrating ordinary differential equations and inverting linear systems. We will show example assignments utilized in teaching a computational physics class, how they are completed with Gkeyll, and some AI coding tool output attempting to do the whole assignment with minimal intervention to demonstrate the utility of this approach. 

# Repository
https://github.com/ammarhakim/gkeyll


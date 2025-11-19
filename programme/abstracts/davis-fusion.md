---
title: 'Fusion & Nuclear Engineering at scale'
authors:
  - name: Andrew Davis
    affiliations:
      - UKAEA
  - name: Helen Brooks
    affiliations:
      - UKAEA
  - name: Alex Blair
    affiliations:
      - UKAEA
  - name: Aleks Dubas
    affiliations:
      - UKAEA
  - name: Daniel Mason
    affiliations:
      - UKAEA
  - name: Pratheek Shanthraj
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

As both Gen IV fission and the global fusion community take strides into spaces that have heretofore been unexplored c.f. the high temperature, neutron rich environments they both see, the role of simulation in predicting future performance is critical. If we are to take confident steps in predicting mission critical parameters and material lifetimes; nuclear heating, thermal loading, fatigue failure, neutron induced toughness, change in ductile-to-brittle transition temperature then first principles based approaches are critical as there is no experimental data from which we can build the parameterisations which are historically used. We must rely on models that require no calibration, and furthermore we must reduce the role of assumption in our models, along with boundary conditions as both of these drive and limit emergent phenomena. It is likely that Rumsfeldian known-unknowns and unknown-knowns will emerge due to the interaction between physics in such complex systems as fusion reactors. Therefore simulation systems also must be made which allow for the arbitrary linkage of physics. The limitations mentioned before, i.e. the need to reduce boundary conditions and assumptions drives us to model more and more complete and complex models of the physical system, which drives a focus on software implementations which do not prohibit these requirements.  

At UKAEA in service of this mission, we have been focussed on contributing to various software frameworks which tread a path towards whole device simulation; one without egregious approximation and preserving the detail needed for the purpose of the calculation. We have focussed efforts around producing models of fusion systems which can be input into the MOOSE framework; a framework which scales (depending upon the problem being solved) upto hundreds of thousands of CPUs. However, the world of HPC is migrating to full GPU systems and thus we have started the work of integrating MFEM (a GPU accelerated FE solver from LLNL) as an alternative FE backend to libMesh. Simply moving to a system which enables GPU solves isn’t sufficient, an entire sequence of pipelines of physics; dedicated fluids and neutron transport solves must also be ported, else they will bottleneck performance.  

This talk will cover our journey, including examples of state of the art, its applicability to various fusion analyses and our direction of travel over the foreseeable future.   


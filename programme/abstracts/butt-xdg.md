---
title: 'XDG and the wider CAE ecosystem around OpenMC '
authors:
  - name: Patrick Shriwise
    affiliations:
      - ANL
  - name: Waqar Butt
    affiliations:
      - UKAEA
license: CC-BY-4.0
exports:
  - format: pdf
    template: ../../template
site:
  hide_toc: false
---

XDG (Accelerated Discretized Geometry) [1] is a new API being developed to provide users with a robust set of methods to perform spatial queries against a discretized CAD geometry for particle transport operations in scientific simulations. It has been primarily designed for use with the open-source Monte Carlo particle transport code OpenMC. XDG stands on the shoulders of the Direct Accelerated Geometry Monte Carlo (DAGMC) [2] toolkit and its development team, from which it draws significant guidance and inspiration. Various members of the DAGMC development team are collaborators and contributors to the XDG project. 

Stellerator model loaded into XDG and rendered using GPRT
XDG has been designed with two core principles in mind: high performance ray tracing by leveraging single precision ray tracing kernels as much as possible in a scientific application; as well as a high degree of flexibility and extensibility via a single common API which sits above generic interfaces to various mesh and ray tracing backends. The intent of this library is to act as a superset of DAGMC, providing the same functionality to drop in place but also to act as a platform to push new, more advanced features which were not possible with DAGMC, such as:
Tracklength tallies for LibMesh meshes
The ability to use volumetric mesh as geometry directly in OpenMC
The capability to perform surface tracking for particle transport directly on CAD using GPUs with a non vendor-locked solution.
Currently XDG supports two separate mesh libraries: 
MOAB (Mesh Oriented datABase)
LibMesh 
As well as two separate ray tracing libraries: 
Embree - A high-performance CPU ray tracer developed by Intel 
GPRT - A Vulkan-RT pipeline-based GPU ray tracer  

XDG design architecture 

References:
[1] https://github.com/xdg-org/xdg
[2] Paul P.H. Wilson et al. Acceleration techniques for the direct use of CAD-based geometry in fusion neutronics analysis




# Repository
https://github.com/xdg-org/xdg


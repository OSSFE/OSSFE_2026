---
title: 'Optimisation of STEP Magnetic Configuration and In-vessel Components using the  Bluemira Fusion Power Plant Framework'
authors:
  - name: Georgina Graham
    affiliations:
      - UKAEA
  - name: Mathew Bluteau
    affiliations:
      - UKAEA
  - name: Matti Coleman
    affiliations:
      - UKAEA
  - name: James Cook
    affiliations:
      - UKAEA
  - name: Athoy Nilima
    affiliations:
      - UKAEA
  - name: Jonathan Mathews
    affiliations:
      - UKAEA
  - name: Clair Mould
    affiliations:
      - UKAEA
  - name: Alexander Pearce
    affiliations:
      - UKAEA
  - name: Harry Saunders
    affiliations:
      - UKAEA
  - name: Dario Vaccaro
    affiliations:
      - UKAEA
  - name: Ocean Wong
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

Fusion power plant design and integration requires tools for rapid production and 
investigation of different concept designs. Bluemira is an open-source, Python 3 framework built to enable this process. It makes use of interdisciplinary models and incorporates a range of design activities, each of which is parameterised and automated. The bluemira 
framework can be used to create fusion device workflows - a structured set of design 
procedures, made up of selected system models, with inputs (e.g., configuration file of 
user choices, output from a fixed plasma equilibrium model, etc.) and outputs (e.g.,
field or heat-flux maps, CAD of the integrated components, etc.) chosen to suit a design 
program’s requirements. Workflows can be updated, either by modifying the inputs or 
by adding new features, allowing a rapid, iterative approach to producing a stable and 
converged design. Our STEP (Spherical Tokamak for Energy Production) workflow 
includes both a magnetic configuration design procedure, which considers the plasma 
equilibrium and toroidal and poloidal field coils, and an in-vessel component design
procedure, which includes the first wall and divertor design. In this work, we present an
addition to the STEP workflow of a divertor design and optimisation feature which links 
divertor magnetic flux shaping optimisation, using objective functions that act as 
proxies for divertor target heat-flux reduction, with target placement and angle 
optimisation. This modification allows us to explore how the physical space available to 
the divertor component can be exploited, while also optimising for coilset and first wall 
position, satisfying key engineering constraints, and maintaining the input plasma 
equilibrium. Our objective is to facilitate design flexibility in the divertor region 
for the STEP bluemira workflow and allow quick alterations to be made to and 
investigated for the STEP divertor silhouette design.

# Repository
https://github.com/Fusion-Power-Plant-Framework/bluemira


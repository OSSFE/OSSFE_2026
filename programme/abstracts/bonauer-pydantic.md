---
title: 'Pydantic on Steroids – Managing Reproducible Simulation Data at Scale'
authors:
  - name: Bonauer Lukas
    affiliations:
      - Proxima Fusion
license: CC-BY-4.0
exports:
  - format: pdf
    template: ../../template
site:
  hide_toc: false
---

The ecosystem of scientific simulators uses a plethora of different file formats, with each simulator exposing settings and writing outputs in its own ad-hoc manner. Pydantic is the most widely used data validation library for Python, allowing simple declaration of structured data that can be stored in JSON format.

In order to produce, organize, and analyze simulation data at scale, we have developed a framework built on top of Pydantic that makes interfacing with scientific simulators and numeric data easy. The framework adds support for efficiently storing numpy and JAX arrays in Pydantic models, and also allows saving commonly used types as structured data (such as figures, interactive plots, VTK data, STEP files). It also streamlines interaction with a shared, cloud-based storage system, enabling researchers to write reproducible and easily testable Python code that does not need to concern itself with data serialization.

At Proxima Fusion, we use this framework to define a “shared language” for modelling stellarator designs and analysis outputs, storing over 40 TB of data across 8 million objects, enabling both large-scale use cases for Machine Learning applications as well as rapid iteration on the experimental evaluation of new ideas.

This presentation will describe Proxima Fusion’s data storage framework and how it is used in complex simulation pipelines, diving into the details of how a strong data model accelerates research in computational science.


# Repository
parts of it available here: https://github.com/proximafusion/vmecpp


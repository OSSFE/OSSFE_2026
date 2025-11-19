---
title: 'An ML-based design approach for Fusion Energy components'
authors:
  - name: V. Perumal
    affiliations:
      - UHV3D, Inc. dba CAMINNO
  - name: A. Stein
    affiliations:
      - UHV3D, Inc. dba CAMINNO
  - name: A. Manikandan
    affiliations:
      - UHV3D, Inc. dba CAMINNO
  - name: R. Frye
    affiliations:
      - UHV3D, Inc. dba CAMINNO
license: CC-BY-4.0
exports:
  - format: pdf
    template: ../../template
site:
  hide_toc: false
github: 'https://github.com/OSSFE/OSSFE_2026'
---

Commercialization of fusion technologies—ranging from fusion power plants to fusion-powered propulsion systems—requires advanced design and engineering capabilities that tightly integrate physics, materials, and manufacturing processes. Traditionally, the complexity of design and the complexity of manufacturing have been treated separately due to the limitations of existing digital tools and the processing capability of the human mind. This disconnected approach results in sequential, and often repeated, workflows that increase costs and extend project timelines.
One of the principal cost drivers in fusion systems is the need to design and produce components at scale with the requisite uniformity and performance reliability. Recent advances in advanced manufacturing - such as additive manufacturing techniques and architected materials, demonstrate significant potential but remain limited by process variability and the lack of fully integrated digital frameworks.
In this work, we present a multi-objective design optimization and digital twin framework that employs scientific machine learning (ML)-based process modeling. Our algorithm couples physics-based AI models such as Fourier neural operators (FNOs) and physics-informed neural networks (PINNs) that simulate structural, thermal, fluidic, and electromagnetic behaviors with experimental manufacturing data across multiple fusion-relevant components. These ML surrogates serve as computationally efficient replacements for conventional solvers, enabling real-time predictions of performance and manufacturability. This approach not only accelerates design exploration but also supports adaptive manufacturing control, where feedback from production is used to refine both the digital twin and the physical part simultaneously.
Such integrated frameworks are critical for enabling scalable manufacturing of fusion energy targets, high-performance components for fusion power plants, and novel applications such as fusion-powered propulsion systems. More broadly, this work points toward a path where scientific AI accelerates the co-design of fusion technologies—linking physics, manufacturing, and performance—to reduce costs, shorten timelines, and expand the reach of fusion into energy, aerospace, and defense applications.



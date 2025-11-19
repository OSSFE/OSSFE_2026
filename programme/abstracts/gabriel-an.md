---
title: 'An Open-Source PlasmaPy + Machine Learning Pipeline for Early Anomaly Detection in Fusion Plasmas'
authors:
  - name: Marthen Gabriel
    affiliations:
      - University of York
license: CC-BY-4.0
exports:
  - format: pdf
    template: ../../template
site:
  hide_toc: false
github: 'https://github.com/OSSFE/OSSFE_2026'
---

One of the most important challenges for fusion devices with magnetic confinement is the ability to predict and control disruptions. Preserving reactor components and the stability of the plasma requires early identification of anomalous plasma behavior during disruptive events. In this case ‘disruptive events’ signifies the density or magnetic field of the plasma fluctuations. In this work, the authors combine the PlasmaPy Python library with modern machine learning (ML) techniques for anomaly detection in the context of developing an open-source PlasmaPy enhancement pipeline.
Disruption models outlined, using synthetic plasma diagnostics that were generated and preprocess with PlasmaPy, are derived and analyzed using extracted physics informed features of the plasma. These features are plasma β, gyrofrequency, collisionality and the, Alfvén speed. These features serve as the inputs to unsupervised anomaly detection algorithms like the Isolation Forest and autoencoder-based models to ‘predict’ disruptions in given plasma parameters. Fully in Python, the modular pipeline integrates PlasmaPy to open-sourced ML software packages (for example scikit-learn, PyTorch) to provide complete reproducibility.
In comparison to basic time-series signal features, the use of physics-informed feature space provided by PlasmaPy significantly enhances the performance of anomaly detection. This is especially applicable for the identification of early-warning signatures. The workflow is delivered as Jupyter notebooks and open-source code, allowing fusion researchers to adapt and extend the methodology to experimental datasets from present and future devices.


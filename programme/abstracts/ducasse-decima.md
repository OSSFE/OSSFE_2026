---
title: 'DECIMA: Open-Source AI-assisted analysis of MCNP PTRAC files for neutronics in fusion and fission'
authors:
  - name: F. Almuhisen
    affiliations:
      - French Alternative Energies and Atomic Energy Commission (CEA), Institute for Magnetic Confinement Fusion Research (IRFM), Service for Fusion Plasma Physics (SPPF), GC3I Group, Cadarache, France
  - name: Q. Ducasse
    affiliations:
      - Authority for Nuclear Safety and Radiation Protection (ASNR), Laboratory for Micro-Irradiation, Metrology, and Neutron Dosimetry (LMDN), Cadarache, France
license: CC-BY-4.0
exports:
  - format: pdf
    template: ../../template
site:
  hide_toc: false
---

The Monte Carlo N-Particle code (MCNP) is a reference tool for neutron and photon transport, widely used in reactor physics, shielding, radiological protection, detector development, and fusion neutronics, including tokamaks. Conventional output estimators (e.g. tally results) provide averaged quantities such as fluxes or spectra, whereas PTRAC (Particle Track Output) files record the full history of each simulated particle from source to termination, including primary and secondary interactions. This trajectory-resolved information enables targeted analyses for detectors, plasma diagnostics, and reactor studies, but remains extremely difficult to exploit due to the complexity and size of the files, often containing millions of events.
We present DECIMA (Data Extraction & Contextual Inference for MCNP Analysis), the first open-source framework coupling Large Language Models (LLMs) with a domain-specific Knowledge Graph (KG) for MCNP. Unlike existing open-source tools (e.g. MCNPTools, Easy-PTRAC), DECIMA directly delivers answers to user queries in natural language, no coding skills, no post-processing required. The KG grounds LLM reasoning, reducing hallucinations and ensuring reproducibility. Instead of interacting with raw code, users simply ask questions in English or French, and DECIMA delivers analyzed results by executing the necessary routines through the mcnptools library. This approach accelerates interpretation and enables the discovery of patterns and fine details that are difficult to access with conventional tools.
We will demonstrate DECIMA through a representative use case involving detectors and experimental installations, while emphasizing its broader impact in both fusion and fission applications. By doing so, DECIMA unlocks the full potential of PTRAC data, enabling trajectory-level insights that conventional MCNP outputs alone cannot provide. Future developments include pedagogical modules for training, visual analysis of MCTAL files, and extended query capabilities, positioning DECIMA as a community-driven, extensible open-source framework for advanced neutronics analysis.



# Repository
https://github.com/quentinducasse/decima


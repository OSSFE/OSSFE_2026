---
title: 'Towards Automated Annotation of Tokamak Data Using a Human-In-The-Loop Tagging Platform'
authors:
  - name: M. Field
    affiliations:
      - United Kingdom Atomic Energy Authority (UKAEA)
  - name: S. Jackson
    affiliations:
      - UKAEA
  - name: N. Cummings
    affiliations:
      - UKAEA
  - name: N. Bhatia
    affiliations:
      - UKAEA
  - name: J. Blake
    affiliations:
      - UKAEA
  - name: R. Costa
    affiliations:
      - UKAEA
  - name: P. Sharma
    affiliations:
      - UKAEA
  - name: A. Saleem
    affiliations:
      - UKAEA
  - name: S. Pamela
    affiliations:
      - UKAEA
  - name: A. Gonzalez-Beltran
    affiliations:
      - UKAEA
  - name: N. Bhujel
    affiliations:
      - Science and Technology Facilities Council (STFC)
  - name: S. Khan
    affiliations:
      - STFC.
license: CC-BY-4.0
exports:
  - format: pdf
    template: ../../template
site:
  hide_toc: false
---

Machine Learning (ML) is increasingly being applied in the domains of plasma science and fusion energy research [1], with models supporting a wide range of common tasks, such as event identification or disruption prediction [2]. One such example is the ENEJETIC model [3], which identifies frames from JET camera data which contain UFOs – small fragments of debris ejected from tiles which heat up and glow brightly, before being absorbed into the plasma. These UFOs have been shown to cause disruptions [4], making reliable detection methods essential.

Training high-performing ML models requires large volumes of high quality, labelled data. While tokamaks generate extensive datasets – JET produced 105,929 pulses with more than 10GB of raw data per pulse [5], and MAST produced 30,471 shots with 7GB per shot [6] – much of this data lacks the annotations necessary for effective ML training. Retrospective annotation is both challenging and time consuming, as domain experts often lack the appropriate tools to effectively label historic pulses.

To address this challenge, we have developed a human-in-the-loop annotation platform designed for curating and labelling tokamak diagnostic data. Through an intuitive UI, domain experts can annotate diagnostic traces, with their inputs stored in a database via a REST API. The platform supports multiple data access layers, including UDA, SAL, and TokSearch, and is designed to easily integrate new sources. It allows for the connection of automated annotators which can create predictions on unseen pulses, which can range from classical signal processing techniques to full ML models. This reduces the workload for domain experts, who can focus on refining model predictions rather than labelling from scratch.

We present progress on a new application of this platform to  enable the annotation of anomalies such as UFOs or MARFEs in tokamak camera data. We demonstrate how the platform has been used to expand the training dataset for the ENEJETIC model, and how it can enrich the metadata already available by adding bounding box annotations around the UFOs in each frame. We show how these annotations can be ingested into the model so that the algorithm can not only detect the presence of UFOs in a frame, but also their number, position and size. Furthermore, we show how the platform supports a human-in-the-loop workflow, enabling rapid iteration and improvement of models such as ENEJETIC.

[1]: Anirudh, Rushil, et al. "2022 review of data-driven plasma science." IEEE Transactions on Plasma Science 51.7 (2023): 1750-1838. 
[2]: J Vega, Jesús, et al. "Results of the JET real-time disruption predictor in the ITER-like wall campaigns." Fusion Engineering and Design 88.6-8 (2013)
[3]: Field, Matthew, et al. "Using deep learning for the detection of UFOs within the JET tokamak." Physics of Plasmas 32.4 (2025).
[4]: De Vries, P. C., et al. "Survey of disruption causes at JET." Nuclear fusion 51.5 (2011): 053018.
[5]: Vega, J., et al. "New developments at JET in diagnostics, real-time control, data acquisition and information retrieval with potential application to ITER." Fusion Engineering and Design 84.12 (2009): 2136-2144. 
[6]: Jackson, Samuel, et al. "An open data service for supporting research in machine learning on tokamak data." IEEE Transactions on Plasma Science (2025).



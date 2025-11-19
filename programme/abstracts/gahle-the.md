---
title: 'The IAEA Fusion Data Lake Project - Progress, Prototype, and the Path Ahead'
authors:
  - name: Daljeet Singh Gahle
    affiliations:
      - IAEA
  - name: Matteo Barbarino
    affiliations:
      - IAEA
license: CC-BY-4.0
exports:
  - format: pdf
    template: ../../template
site:
  hide_toc: false
github: 'https://github.com/OSSFE/OSSFE_2026'
---

AI and Big Data applications have a fundamental dependency on data infrastructure that provides appropriate, curated, and unified datasets in line with FAIR data principles, which can be programmatically integrated into development pipelines [1]. To support AI applications in fusion, the IAEA is developing the Fusion Data Lake, a modern and scalable solution for discovering and creating datasets for AI-driven research. The project has three main components:

1. International data catalogue;

2. Medium-term storage with tiered access; and

3. Data federation of experimental research institutions.

This work is part of the wider AI for Fusion Coordinated Research Project (CRP), a five-year initiative launched in 2022, which involves 24 institutions across 11 countries [2].

In the first year of the project, the project concepts, architecture, and regulatory bases were developed and demonstrated in practice by completing the first proof of concept, which developed the data catalogue and federation functionality by integrating UKAEA’s MAST Data Catalog [3]. The platform is structured as a central catalogue that synchronises with data solutions from federation members, while facilitating direct connection to the data from the original source to prevent needless computational overhead in accessing the data. The central platform of the Fusion Data Lake is built in Python using Snowflake for compute and Azure for storage, with both programmatic and webapp user interfaces in development.

Currently, the project is in Phase II of the PoC, which is demonstrating the scalability of the developed approach by integrating the experimental shot catalogues of the Large Helical Device from the Japanese National Institute for Fusion Science [4] and Alcator C-Mod from the Plasma Science and Fusion Center at the Massachusetts Institute of Technology [5]. This further generalises the data solution and demonstrates the value of querying a multimachine catalogue through a unified ontology based on global data standards such as DublinCore and fusion-specific terminology from the IMAS Data Dictionary [6, 7].

This presentation will deliver a high-level overview of the Fusion Data Lake project, including:

● Technical stack, architecture design, and concepts

● Ontological approach of the metadata and data model

● Terms of service and data governance

● Current state of the platform

Illustrating the approach, results, and direction of the work, highlighting the high potential value to the fusion community of increasing the visibility and accessibility of the numerous international experimental data sets.

1. P. Brans, "AI ignites innovation in fusion", ITER Organization, 2025, website https://www.iter.org/node/20687/ai-ignites-innovation-fusion (accessed 5th Sept 2025)

2. AI for Fusion, International Atomic Energy Agency, 2025, website https://nucleus.iaea.org/sites/ai4atoms/ai4fusion/SitePages/AI4F.aspx (accessed 5th Sept 2025)

3. S. Jackson et al. 2025, IEEE Trans. on Plasma Sci., doi: 10.1109/TPS.2025.3583419. https://ieeexplore.ieee.org/document/11128905 4. LHD Experiment Data Repository, National Institute for Fusion Science. [Online]. Available: https://exp.lhd.nifs.ac.jp/opendata/LHD/

5. Trevisan, G. L., Rea, C., & MIT PSFC Disruption Studies Group. (2025). DisruptionPy: An open-source physics-based Scientific Framework for Disruption Analysis of Fusion Plasmas (0.11.0). Zenodo. https://doi.org/10.5281/zenodo.15359587

6. Dublin Core Metadata Initiative Usage Board, DCMI Metadata Terms. Dublin Core Metadata Initiative, Jan. 20, 2020. [Online]. Available: https://www.dublincore.org/specifications/dublin-core/dcmi-terms/ 7. ITER Organization, IMAS Data Dictionary, version 4.0.0. GitHub, 2024. [Online]. Available: https://github.com/iterorganization/IMAS-Data-Dictionary


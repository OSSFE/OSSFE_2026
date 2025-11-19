---
title: 'Bridging Tokamak Physics and Engineering: The PECAN Framework for Disruption and EM Modeling'
authors:
  - name: Lombroni Riccardo
    affiliations:
      - ENN
  - name: Maione Ivan Alessio
    affiliations:
      - KIT
license: CC-BY-4.0
exports:
  - format: pdf
    template: ../../template
site:
  hide_toc: false
github: 'https://github.com/OSSFE/OSSFE_2026'
---

Plasma disruptions pose a major challenge for the safe operation of tokamaks, primarily due to the intense electromagnetic (EM) and heat loads they generate on tokamak components. Accurate EM analysis requires efficient and reliable workflows that can bridge plasma physics and engineering design. The traditional approach relies on a two-step process: first, disruption dynamics are modeled with an equilibrium code (e.g. MAXFEA, DINA, CREATE-NL, etc.), and then the resulting evolution is applied to a 3D electromagnetic solver by means of a number of different techniques. While this workflow is well-established, it still exhibits shortcomings, leaving space for improvement and innovation.
The PECAN project addresses this gap by integrating these two steps into a single, self-consistent framework capable of simultaneously simulating plasma dynamics and 3D EM loads. Unlike cutting-edge physics-oriented codes such as JOREK or M3D-C1, which provide advanced insights but often remain impractical for timely engineering applications, PECAN is tailored to inform and support design decisions across all project stages, from conceptualization to detailed engineering. It maintains acceptable accuracy in plasma physics while drastically reducing computational costs and enables the direct treatment of components with detailed 3D models, providing the resolution required for robust engineering assessment. 
This contribution will present the current status of PECAN development, a framework conceived in the spirit of open-source collaboration. While its primary motivation and main development efforts focus on disruption simulations, PECAN is designed with versatility in mind. Beyond disruptions, possible applications in other areas of tokamak engineering will also be discussed, offering a broader view of the code’s potential utility as an accessible framework for the fusion community.



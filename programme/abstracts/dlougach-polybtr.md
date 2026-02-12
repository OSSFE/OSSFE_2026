---
title: 'PolyBTR code development for neutral beam design workflows'
authors:
  - name: Eugenia Dlougach
    affiliations:
      - Neutral Beam Research
  - name: Fedor Kuyanov
    affiliations:
      - University of Oxford
license: CC-BY-4.0
exports:
  - format: pdf
    template: ../../template
site:
  hide_toc: false
github: 'https://github.com/OSSFE/OSSFE_2026'
---

BTR (Beam TRansmission) code is routinely used for the design and analysis of neutral beam injectors (NBIs), being one of the first physical simulators of the tokamak H&CD subsystem. The code was initially developed in 1995 to support the design and thermal load analysis of NBI beamlines. Neutral beam losses and the resulting transmission efficiency can reduce the total power input to a fusion device; therefore, the target plasma will not achieve the required parameters without appropriate NBI optimization. As such, BTR provides an efficient and flexible numerical tool for fusion engineers and physicists to optimize the NBI efficiency and coupling with the target. The code was first implemented in Turbo Pascal; it was the 1st numerical tool able to trace the entire beam mix, including atoms and ions (‘Beam Transmission with Re-ionization’). By 2005, it had been released for open access after being moved to MS Visual C++. Within 25 years, five major BTR versions have been released, while the most recent (BTR-5) was issued in 2020. All of these require a Windows OS to run.
However, BTR workflow models and structure are similar to the NBI configuration, which consists of a series of components: the ion source, neutralizer, ion and atom collectors, beam dumps, etc. Besides, users often want to choose a set of specific tasks to be solved and organized in a customized workflow. Therefore, the new BTR version is expected to be a collection of multiple blocks, each representing some basic BTR task and/or beamline component. These units can be further integrated into a simple or complex workflow according to the user’s preferences. Unlike the former versions, the new BTR will run on Linux systems. The main features of classical BTR code, such as simplicity, interactivity, and flexibility, will be kept.
For BTR workflow management, we use the Polygraph service initially developed for organizing programming competitions. The service facilitates the design, modification, and execution of complex workflows. BTR’s computational tasks are now represented as isolated blocks with dependencies (“connections”). The user can control the blocks’ resources (time and memory limits). The key feature of Polygraph, distinguishing it from most workflow engines, is support of cycles: each block can be executed multiple times. Another advantage of Polygraph is the automatic parallelization of independent tasks. Finally, workflow blocks can be written in different programming languages and can interact in a highly non-linear manner. The current version of Polygraph correctly executes workflows of arbitrary complexity, verified by unit tests and practical experiments.

# Repository
https://github.com/kuyanov/polygraph


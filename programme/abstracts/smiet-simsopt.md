---
title: 'Simsopt: A flexible framework for stellarator optimisation'
authors:
  - name: Christopher Berg Smiet
    affiliations:
      - École Polytechnique Fédérale de Lausanne
  - name: Matt Landreman
    affiliations:
      - University of Maryland
  - name: Bharat Medasani
    affiliations:
      - Type One Energy
  - name: Misha Padidar
    affiliations:
      - Courant Institute of Mathematical Sciences
  - name: Florian Wechsung
    affiliations:
      - Courant Institute of Mathematical Sciences
  - name: Andrew Giuliani
    affiliations:
      - Courant Institute of Mathematical Sciences
  - name: Rogerio Jorge
    affiliations:
      - University of Wisconsin-Madison
  - name: Ken Hammond
    affiliations:
      - Princeton Plasma Physics Laboratory
  - name: Caoxiang Zhu
    affiliations:
      - University of Science & Technology of China
license: CC-BY-4.0
exports:
  - format: pdf
    template: ../../template
site:
  hide_toc: false
---

A stellarator confines a plasma using a twisting, nonaxisymmetric magnetic field, created by a set of complicated coils. 
The first step in stellarator design is therefore at the interface of two complex optimisation problems: 1) finding the optimal magnetic field according to a list of desirable physics properties, and 2) finding the a set of coils that support said field. 
SIMSOPT is a flexible, extensible, python-based framework for carrying out these optimizations. 
This allows users to easily define new optimisation functions, couple to new plasma equilibrium solvers, and define complicated, multi-stage optimisation problems on the fly. 
Simsopt was involved with many exciting recent developments in stellarator physics, including:  Quasi-symmetric fields that confine virtually all particles [1], realistic coils that generate such fields [2], open databases with hudreds of thousands of stellarator configurations [3], efficient algorithms for single-stage (direct-from-coils) optimization [4,5], and a new family of Stable Quasi-Isodynamic Designs (SQUiDs) [6]. 
As the collaboration that funded its intial development draws to a close, simsopt has become a mature, well-rounded framework with an international community of users and developers. 
We will present the design and devopment philosophy of SIMSOPT and discuss recent notable results, as well as future development directions and challenges. 

[1] Landreman, Matt, and Elizabeth Paul. "Magnetic fields with precise quasisymmetry for plasma confinement." Physical Review Letters 128.3 (2022): 035001.
[2] Wechsung, Florian, et al. "Precise stellarator quasi-symmetry can be achieved with electromagnetic coils." Proceedings of the National Academy of Sciences 119.13 (2022): e2202084119.
[3]Giuliani, Andrew. "Direct stellarator coil design using global optimization: application to a comprehensive exploration of quasi-axisymmetric devices." Journal of Plasma Physics 90.3 (2024): 905900303.
[4] Jorge, Rogerio, et al. "Single-stage stellarator optimization: combining coils with fixed boundary equilibria." Plasma Physics and Controlled Fusion 65.7 (2023): 074003.
[5]Smiet, Christopher Berg, et al. "Efficient single-stage optimization of islands in finite-β stellarator equilibria." Physics of Plasmas 32.1 (2025).
[6] Goodman, Alan G., et al. "Quasi-isodynamic stellarators with low turbulence as fusion reactor candidates." PRX Energy 3.2 (2024): 023010.

# Repository
https://github.com/hiddenSymmetries/simsopt


---
title: 'Stellacode: A New Differentiable Coil Optimization Code for Broader CWS Geometries'
authors:
  - name: Mohamed Aziat
    affiliations:
      - Renaissance Fusion
  - name: Anouk Nicolopoulos-Salle
    affiliations:
      - Renaissance Fusion
license: CC-BY-4.0
exports:
  - format: pdf
    template: ../../template
site:
  hide_toc: false
---

Renaissance Fusion (RF) has systematically leveraged open-source software (OSS) for reactor design and modeling and extends community tools to meet its specific needs and goals. We present Stellacode, a differentiable optimization code for stellarator coil design that solves coil optimization problems using truncated singular value decomposition (TSVD) together with the Tikhonov regularization strategy implemented in the REGCOIL algorithm [1]. In addition, Stellacode supports targeting quadratic functionals of the current density, such as current curvature, thereby mitigating coil complexity and reducing the prevalence of windowpane-like coils. 

Stellacode accommodates a broad range of coil-winding surface (CWS) geometries. Originating as an open-source Python project developed with INRIA [2], it has since evolved substantially and is now integrated into RF internal toolchain. The current version provides expanded geometry support, advanced CWS optimization with engineering constraints, rich visualization, JAX-based differentiable implementations, and multiple solver backends. 

In this poster, we outline the Stellacode algorithm and investigate the impact of using piecewise-cylindrical (PWC) surfaces, rather than conformal surfaces, on current-density solutions to the Biot–Savart inverse problem. We then present benchmark comparisons between Stellacode and the Fortran implementation of REGCOIL. Furthermore, we describe a coil-complexity reduction algorithm and compare coils obtained with and without explicitly targeting current curvature. Finally, we highlight a recent upgrade that accounts for a finite PWC width from which coils are extracted, and we provide preliminary results for multilayer coil configurations. 

Our long-term objective is to release Stellacode back to the OSS community following publication of the associated research and once RF grooved-coil technology on wide HTS foils has been successfully de-risked. 


[1] Matt Landreman. [2017], “An improved current potential method for fast computation of stellarator coil shapes”, Nucl. Fusion 57 046003 

[2] Y. Privat et al. [2022], “Optimal shape of stellarators for magnetic confinement fusion”, Volume 163, July 2022, Pages 231-264. 


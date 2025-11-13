---
title: 'Constraining Equilibria with Toroidal Harmonics in the Bluemira Design Framework'
authors:
  - name: Clair Mould
    affiliations:
      - UKAEA
  - name: Oliver Bardsley
    affiliations:
      - UKAEA
  - name: Matti Coleman
    affiliations:
      - UKAEA
  - name: James Cook
    affiliations:
      - UKAEA
  - name: Georgina Graham
    affiliations:
      - UKAEA
license: CC-BY-4.0
exports:
  - format: pdf
    template: ../../template
site:
  hide_toc: false
---

Bluemira is an integrated design framework for fusion power plants. The design space
of many physics and engineering aspects of a power plant concept can be rapidly
explored using automated workflows. Bluemira workflows include a free-boundary
plasma equilibrium solver with coil optimisation of position and current, that is subject
to geometrical and engineering constraints.

An equilibrium poloidal field configuration has contributions from both the plasma and
the coilset. Normally, when we optimise the coilset contribution, we must also re-solve
the non-linear Grad-Shafranov equation for the equilibrium to find the plasma
contribution. However, we can exploit the premise that the equilibrium solution will not
change if the coilset contribution in the region occupied by the plasma is kept the same
(Bardsley et al., 2024). This means that we do not need to re-solve the Grad-Shafranov
equation, which is advantageous as we can reduce the computational complexity of
the optimisations used in our coilset and divertor magnetic field configuration design.

The magnetic field in a toroidal region can be described by a scalar quantity using
toroidal harmonic functions. In this work, we make use of these functions to describe
the coilset contribution to the equilibrium poloidal magnetic flux within the region
containing the plasma. We then select the most significant harmonics and fix their
amplitudes to create a small (typically about 5 amplitude values) set of constraints to
use while performing coilset optimisation. We explore the use of toroidal harmonic
constraints on both single and double null designs and compare our method to
optimisations using a set of fixed poloidal flux points to constrain the LCFS shape while
re-solving the Grad-Shafranov equation. We present the implementation of the toroidal
harmonic constraint method in the bluemira framework and demonstrate the
advantages of its application on magnetic field design using equilibria from
demonstration power plant concept designs.

# Repository
https://github.com/Fusion-Power-Plant-Framework/bluemira


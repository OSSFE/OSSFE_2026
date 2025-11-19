---
title: 'Integrating the Plasma Edge, Plasma Facing Components, and Blanket Simulations within the MOOSE Framework '
authors:
  - name: Corey DeChant
    affiliations:
      - Idaho National Laboratory
  - name: Grayson Gall
    affiliations:
      - North Carolina State University
  - name: Casey Icenhour
    affiliations:
      - Idaho National Laboratory
  - name: Lin Yang
    affiliations:
      - Idaho National Laboratory
  - name: Mahmoud Eltawila
    affiliations:
      - University of Illinois Urbana-Champaign
  - name: Trevor Franklin
    affiliations:
      - Virginia Commonwealth University
  - name: Masashi Shimada
    affiliations:
      - Idaho National Laboratory
  - name: Guillaume Louis Giudicelli
    affiliations:
      - Idaho National Laboratory
  - name: Logan Harbour
    affiliations:
      - Idaho National Laboratory
  - name: Helen Brooks
    affiliations:
      - United Kingdom Atomic Energy Agency
  - name: Amanda Lietz
    affiliations:
      - North Carolina State University
  - name: April Novak
    affiliations:
      - University of Illinois Urbana-Champaign
  - name: Lane Carasik
    affiliations:
      - Virginia Commonwealth University
  - name: Pierre-Clement Simon
    affiliations:
      - Idaho National Laboratory
license: CC-BY-4.0
exports:
  - format: pdf
    template: ../../template
site:
  hide_toc: false
github: 'https://github.com/OSSFE/OSSFE_2026'
---

Fully coupled multiphysics models of fusion devices are crucial to the goal of achieving fusion power on the grid. These models must incorporate the interconnected phenomena of these devices, including plasma physics, neutronics, first wall interactions, and tritium transport. Currently, there are two main approaches to developing these platforms: (1) loosely coupled, where one couples existing codes and solvers together through input and output parameters and data, and (2) tightly coupled, where one develops the necessary models within a singular, integrated framework. This work focuses on a combination of these approaches for magnetically confined fusion devices by developing within the Multiphysics Object Oriented Simulation Environment (MOOSE) framework. The MOOSE framework allows for both tightly coupled physics, with monolithic solves or Picard fixed-point iterations, and loosely coupled physics, using MOOSE’s MultiApp system. The Software for Advanced Large-scale Analysis of MAgnetic confinement for Numerical Design, Engineering & Research (SALAMANDER) application is the primary MOOSE application for multiphysics fusion device modeling. SALAMANDER integrates, in an open-source application, various existing MOOSE capabilities, such as the heat conduction, solid mechanics and thermal hydraulics modules, with MOOSE-based applications, such as Cardinal (neutronics and computational fluid dynamics) and TMAP8 (Tritium Migration Analysis Program, version 8).

This presentation highlights the development of plasma physics modeling capabilities within MOOSE, including a fluid-based model for the edge region of the plasma and a particle-in-cell (PIC) model for the plasma sheath region. The plasma fluid modeling is an expansion the MOOSE-based application, Zapdos, which was originally formulated to model low-temperature, non-magnetized plasma processes. New additions to Zapdos are based on the Braginskii equations commonly used in fusion edge modeling. The PIC capability is a new addition in SALAMANDER, based on MOOSE’s ray-tracing module, which incorporates the direct simulation Monte Carlo method for collisions. Both methods of plasma modeling have gone through a rigorous verification process and are being validated as they are coupled to existing MOOSE capabilities to model the interactions between the plasma edge, first wall, and the blanket.

# Repository
MOOSE Framework: https://github.com/idaholab/moose, SALAMANDER: https://github.com/idaholab/salamander, Zapdos: https://github.com/shannon-lab/zapdos


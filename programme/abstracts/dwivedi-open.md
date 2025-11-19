---
title: 'Open-Source Molecular Dynamics Framework for High-Velocity Dust Impacts on Tungsten Plasma-Facing Walls'
authors:
  - name: Prashant Dwivedi
    affiliations:
      - Czech Technical University in Prague, Czech Republic
  - name: Tomáš Polcar
    affiliations:
      - University of Southampton, Faculty of Engineering and Physical Sciences, UK
license: CC-BY-4.0
exports:
  - format: pdf
    template: ../../template
site:
  hide_toc: false
github: 'https://github.com/OSSFE/OSSFE_2026'
---

The resilience of plasma-facing components in fusion reactors is critically influenced by high-velocity tungsten (W) dust impacts during transient events such as disruptions and runaway electron terminations. We present a fully open-source molecular dynamics (MD) framework to simulate and analyse W-on-W dust collisions across a broad parameter space: velocities (1–4.5 km/s), projectile sizes (4–10 nm), temperatures (300–3000 K), and incidence angles (0°–75°). Simulations were performed using LAMMPS, with post-processing in OVITO and custom Python scripts to extract crater geometry, dislocation density, ejecta mass, and velocity-resolved atomistic data.

Our results reveal three distinct regimes of impact behavior—deformation, bonding, and disintegration—each governed by kinetic energy and thermomechanical coupling. Crater morphology and volume follow robust dimensionless π-group scaling relations, validated against experimental cratering data from light gas gun tests. Elevated temperatures enhance plastic flow and ejecta, while angular incidence leads to elliptical craters and asymmetric rim growth. Dislocation analysis shows that target orientation significantly affects defect density and crater recovery kinetics.

This work offers a validated, scalable, and extensible modelling toolset for investigating dust–wall interactions in fusion reactors and contributes to predictive design of durable plasma-facing materials under extreme conditions.


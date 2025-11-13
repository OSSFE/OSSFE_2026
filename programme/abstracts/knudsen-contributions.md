---
title: 'Contributions to OpenMC: HexMesh and alpha,n source'
authors:
  - name: Erik B Knudsen
    affiliations:
      - United Neux/University of Gothenburg
license: CC-BY-4.0
exports:
  - format: pdf
    template: ../../template
site:
  hide_toc: false
---

We present our latest contributions to the OpenMC open source software package.
A hexagonal mesh addition.
A source model for simulating the neutron contribution arising from the α,n reaction in the presence of an α-decaying isotope.

Hexagonal meshes have so far been absent in OpenMC. This is a pity, since it blocks OpenMC from use in connection with a set of legacy codes that are defined on a hexagonal grid. In addition it seems counterintuitive not to be able to define a mesh with the same properties as the underlying often hexagonal geometry lattice.

α,n-sources are sometimes used in the scientific community as low maintenance, cheap (relatively) neutron sources. For instance to test instrument concepts, e.g. detectors before developing them fully for large scale facilities. Further, it can be of interest for molten salt reactors, since the reaction may contribute (to a minor extent) to neutron economy, through alpha conversion by the halogen element of the fuel salt.

In both cases we will present the new models together with a few identified use cases.	


# Repository
https://www.github.com:openmc-dev/openmc


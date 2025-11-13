---
title: 'Using open-source tools and platforms to build a multi-tenant development environment for fusion research'
authors:
  - name: Bartłomiej Pogodziński
    affiliations:
      - Poznan Supercomputing and Networking Center
  - name: Daniel Figat
    affiliations:
      - Poznan Supercomputing and Networking Center
license: CC-BY-4.0
exports:
  - format: pdf
    template: ../../template
site:
  hide_toc: false
---

The EUROfusion Standard Software (ESS) initiative within the E-TASC programme defines specifications for developing and delivering robust software for fusion-related computations. To support this effort, the Advanced Computing Hub at PSNC/IPPLM provides a cohesive, multi-tenant development environment for contributors. The platform combines GitLab (source control, CI/CD, and container registry) and an automated documentation pipeline with service monitoring via Grafana, complemented by commercial wiki and issue-tracking solutions. All components are integrated through Keycloak-based single sign-on (SSO) federated with multiple identity providers (IdPs).
The entire stack is provisioned with Terraform and configured with Ansible, adhering to the Infrastructure-as-Code (IaC) paradigm. This approach ensures reproducible deployments, auditable change control, and rapid rollbacks, while simplifying collaboration among administrators and developers. We present the architecture, deployment workflow, and lessons learned from operating this environment within EUROfusion.


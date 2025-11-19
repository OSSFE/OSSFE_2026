---
title: 'A comparison of open source data distribution tools for global data sharing'
authors:
  - name: Stephen Dixon
    affiliations:
      - UKAEA
  - name: Adam Parker
    affiliations:
      - UKAEA
  - name: Jonathan Hollocombe
    affiliations:
      - UKAEA
license: CC-BY-4.0
exports:
  - format: pdf
    template: ../../template
site:
  hide_toc: false
github: 'https://github.com/OSSFE/OSSFE_2026'
---

Fusion datasets can be fragmented across globally distributed experimental facilities, each with different data storage and access systems. This can pose challenges for aggregation of multi-machine datasets and for accessing data on remote, high performance computing (HPC) facilities where analysis may need to be run. 

This talk presents recent efforts to investigate two open source tools for distributing data between multiple experimental facilities and multiple HPC analysis clusters. Some key advantages we were interested in exploring included (i) abstracting site-specific data access routines and adopting a unified interface, (ii) strategies for minimising latency between globally distributed locations, and (iii) scalability beyond manual, ad-hoc data copy operations.

The Pelican Platform[1] and CVMFS[2] are both examples of data distribution services which provide consolidated access interfaces and use caches and data mirrors to reduce latency when accessing multiple, globally distributed data sources. Pelican is a data federation platform which aims to unify access to different kinds of storage APIs (S3, Posix, HTTP) through adaptor services; it uses XRootD[3] for data transfer and includes features for user authorisation and authentication. CVMFS is a CERN-developed data distribution technology widely used in High Energy Physics. Initially focused on sharing open software, CVMFS uses the HTTP protocol for data transfer, has a convenient virtual filesystem interface, and implements an aggressive local caching strategy to improve performance for certain data access patterns. Overall, Pelican is more focused on large-scale data federation while CVMFS has advantages for transparent access to fine-grained data in read-heavy applications. 

We compare these tools against traditional methods such as manual SCP (Secure Copy Protocol) transfers in terms of performance and also highlight the additional features these tools provide which can particularly benefit typical fusion analysis workflows. 

[1] Pelican Platform, https://pelicanplatform.org/
[2] CernVM File System, https://cvmfs.readthedocs.io/en/stable/ 
[3] XRootD, https://xrootd.org/

# Repository
https://github.com/PelicanPlatform/pelican, https://github.com/cvmfs/cvmfs


---
title: 'Energy-Aware Kubernetes: Monitoring and Analyzing Fusion Simulation Power Consumption with Kepler'
authors:
  - name: Shakthi Kannan
    affiliations:
      - Morton Labs AI
  - name: Zach Hynek
    affiliations:
      - Morton Labs AI
license: CC-BY-4.0
exports:
  - format: pdf
    template: ../../template
site:
  hide_toc: false
github: 'https://github.com/OSSFE/OSSFE_2026'
---

Energy usage is important in infrastructure for Fusion companies who want to measure and optimize cost and sustainability when running simulation models. The Kepler (Kubernetes-based Efficient Power Level Exporter) project provides a mechanism to measure power consumption metrics for Kubernetes workloads by leveraging hardware counters, kernel statistics, and machine learning–based models. In this tutorial, we will demonstrate how to deploy and configure Kepler in a Kubernetes cluster, integrate it with observability stacks such as Prometheus and Grafana, and interpret the resulting energy metrics at the node, pod, and container levels. Kepler uses Intel RAPL (Running Average Power Limit) sensors to collect energy data from CPU packages, cores, and memory subsystems to distribute this energy proportionally to workloads based on their CPU time consumption. The readers will be able understand how Kepler enables insights into the energy footprint of containerized applications and supports more efficient, sustainable cloud-native operations for Fusion modeling, simulation experiments and infrastructure deployments.

# Repository
https://github.com/sustainable-computing-io/kepler


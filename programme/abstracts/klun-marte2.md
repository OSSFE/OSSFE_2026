---
title: 'MARTe2 on Low-Performance Platforms: From Inverted Pendulums to Fusion Control'
authors:
  - name: Matej Klun
    affiliations:
      - Cosylab d.d.
  - name: Adam Stephen
    affiliations:
      - UKAEA
license: CC-BY-4.0
exports:
  - format: pdf
    template: ../../template
site:
  hide_toc: false
---


The MARTe2 real-time framework is widely used in fusion research and other scientific domains to implement deterministic, high-performance control and data acquisition systems. Its modular design, multi-platform support, and open-source nature make it a powerful tool for building scalable control architectures. While MARTe2 has traditionally been deployed on high-end hardware, its adaptability also enables use in constrained environments where cost, accessibility, or rapid prototyping are critical.
This work demonstrates MARTe2 on low-performance platforms, through two projects developed together with UKAEA. 
First, synchronized, timestamped data acquisition is achieved with a GPS receiver and Raspberry Pi combined with an STM32 board for ADC sampling, proving that precise timing and deterministic processing are possible even on resource-limited systems. 
Second, the Inverted Pendulum prototype, implemented using MARTe2 on an embedded ARM-based controller(STM32) with modest computational resources, demonstrates real-time regulation of an inherently unstable system. This mirrors the stringent timing and feedback requirements of plasma stabilization, showing that MARTe2 can sustain deterministic performance even on low-cost embedded hardware.
Together, these results validate MARTe2 as a versatile solution bridging low-cost prototyping with advanced fusion control. Its ability to maintain deterministic performance under constrained conditions opens pathways for affordable diagnostics, training, and early-stage development, contributing to the broader Fusionics vision of scalable and modular control for fusion applications.



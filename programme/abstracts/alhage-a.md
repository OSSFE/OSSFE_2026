---
title: 'A software library for robust ELM detection'
authors:
  - name: J. Alhage
    affiliations:
      - Ghent University
  - name: C. Haems
    affiliations:
      - Ghent University
  - name: M. Van Damme
    affiliations:
      - Ghent University
  - name: Y. Zhang
    affiliations:
      - Ghent University
  - name: G. Verdoolaege
    affiliations:
      - Ghent University
license: CC-BY-4.0
exports:
  - format: pdf
    template: ../../template
site:
  hide_toc: false
---

Edge-localized modes (ELMs) are repetitive instabilities in tokamaks where heat and particles are released from the plasma. Various diagnostic signals can be used to detect ELMs, usually involving common workflows, such as conditioning the data by applying filters, locating peaks or regions of interest, combining small events, or dropping insignificant ones. More importantly, these methods have a number of parameters to optimize and need their performance to be measured. We simplified the conception of new ELM detection algorithms by uncoupling these processes. First, several event detection algorithms were implemented and tuned for the specific shape of an ELM peak. These include robust thresholding, novelty detection, one-dimensional convolutional and recurrent neural networks, and object detection methods exploiting feature invariance. Shared pre- and post-processing steps were written as combinable building blocks. Then, the quality of the output was evaluated with interval metrics, which are more appropriate performance indicators than RMSE and distance-to-peak for events that span a duration in timeseries. The training dataset includes more than 10,000 manually labeled ELMs from the JET tokamak, including compound and irregular ones, as the user-exposed functions must identify diverse classes of event behavior with minimal adjustments. Locating ELMs automatically is essential for understanding the conditions that lead to their onset, and for measuring their impact. Moreover, these tools can be adapted to other tokamak events, either in the plasma or in machine components. We have implemented our ELM detection workflow in `elm-detection`, a Python package to robustly mark edge-localized modes.

# Repository
https://github.com/infusion-ugent (WIP)


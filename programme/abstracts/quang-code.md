---
title: 'Code-to-code Comparison of OpenMC and ORIGEN for Isotopic Depletion in Fusion'
authors:
  - name: Son Quang
    affiliations:
      - University of Tennessee
  - name: Jonathan Wing
    affiliations:
      - University of Tennessee
  - name: Nicholas R. Brown
    affiliations:
      - University of Tennessee
  - name: G. Ivan Maldonado
    affiliations:
      - University of Tennessee
license: CC-BY-4.0
exports:
  - format: pdf
    template: ../../template
site:
  hide_toc: false
---

Fusion power plants present material activation challenges that are fundamentally different from fission reactors, and most existing computational isotopic depletion tools have been designed based upon fission-based fuel cycles. This can lead to significant uncertainties when estimating transmutation products, decay heat, and waste management implications for fusion materials. The validation of depletion software dedicated to fusion environments is the motivation for this research, which has the potential to significantly impact the field of nuclear engineering and the future of fusion power plants. In this study, OpenMC, an open-source modern Monte Carlo particle transport code with integrated depletion capability, is applied to model activation and isotopic evolution of structural and blanket materials under fusion-relevant neutron fields. To verify its accuracy, OpenMC results are systematically contrasted against ORIGEN across key metrics, including major activation products, activity, decay heat, and long-lived isotopes. Agreement is generally strong, confirming the reliability of OpenMC for fusion applications, while also highlighting discrepancies traceable to ORIGEN’s fission-oriented libraries and assumptions. By explicitly demonstrating the feasibility and advantages of OpenMC in this context, this work establishes a pathway toward a fusion-focused open-source simulation framework. Such capability is critical for accurate prediction of material performance, long-term radiological inventories, and regulatory decision-making in future fusion power plants. The findings emphasize that developing, validating, and standardizing fusion-specific depletion codes must become a priority for the fusion community.


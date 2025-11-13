---
title: 'RT-GSFit – Real-time Grad-Shafranov Fit'
authors:
  - name: A. P. K. Prokopyszyn
    affiliations:
      - Tokamak Energy Ltd.
  - name: J. Bland
    affiliations:
      - Tokamak Energy Ltd.
  - name: P. F. Buxton
    affiliations:
      - Tokamak Energy Ltd.
  - name: F. Janky
    affiliations:
      - Tokamak Energy Ltd.
  - name: B. Vincent
    affiliations:
      - Tokamak Energy Ltd.
  - name: ST40 Team
    affiliations:
      - Tokamak Energy Ltd.
license: CC-BY-4.0
exports:
  - format: pdf
    template: ../../template
site:
  hide_toc: false
---

Accurate calculation of the magnetic plasma centre and boundary is essential for plasma control in tokamaks. We are developing RT-GSFit [1], a real-time equilibrium reconstruction code designed to calculate the magnetic field configuration with millisecond resolution. The code solves the Grad–Shafranov equation [2, 3], producing solutions consistent with magnetics measurements. 

RT-GSFit is written in C to enable seamless integration with the ST40 Plasma Control System, implemented in MathWorks® Matlab/Simulink [4]. Verification has been performed against analytic equilibria and established offline reconstruction tools such as GSFit [5], showing strong agreement.  

In this presentation, we will provide a detailed explanation of the RT-GSFit architecture, including how the code achieves the speed required for real-time operation and how it is integrated with Simulink. We will also describe our approaches for handling passive elements and mitigating edge cases that can cause equilibrium solvers to fail. 

[1] Tokamak Energy, rtgsfit: Real-Time Grad–Shafranov Fit, GitHub repository, 2025. [Online]. Available: https://github.com/tokamak-energy/rtgsfit 

[2] H. Grad and H. Rubin, “Hydromagnetic Equilibria and Force-Free Fields,” Proc. 2nd United Nations Int. Conf. on the Peaceful Uses of Atomic Energy, vol. 31, p. 190, Geneva: IAEA, 1958. 

[3] V. D. Shafranov, Plasma Equilibrium in a Magnetic Field, Reviews of Plasma Physics, vol. 2, p. 103, New York: Consultants Bureau, 1966. 

[4] The MathWorks, Inc., MATLAB version: 23.2.0 (R2023b), Natick, Massachusetts, United States, 2025. [Online]. Available: https://www.mathworks.com 

[5] Tokamak Energy, gsfit: Grad–Shafranov Fit, GitHub repository, 2025. [Online]. Available: https://github.com/tokamak-energy/gsfit 

# Repository
https://github.com/tokamak-energy/rtgsfit


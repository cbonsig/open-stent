open-stent
==========

Stents are medical implants commonly used to provide support and scaffolding to diseased arteries, veins, or other vessels in the human body. Many stent design can be imagined as a series of deforming beams, wrapped into a cylindrical shape like a spring. Well known structural mechanics formulas can be used to relate deflections of beams to stresses, strains, and forces. Stent Calculator uses these principles to relate stent design inputs like tubing diameter, wall thickness, and strut length, to performance outputs like strength, surface area, mass, contact pressure, and strain. These relationships are especially useful for stents fabricated from superelastic nitinol, which can reach strains of 1-2% with a substantially linear elastic relationship to stress. Because this is an order of magnitude higher than conventional engineering materials, nitinol is particularly well suited to analysis using the tools provided by the Stent Calculator project.

Goals and Motivation of This Project
====================================

This project is intended to bring the collaborative principles of open source to the typically closed and proprietary world of medical device development. NDC has a long history leading development of nitinol stents and similar components, and has also been a leading publisher and educator in the field. Contributing to the open source and creative commons movements is a natural evolution of our commitment to nitinol education. It is our hope that providing these tools and resources in an unlimited way to the community of medical device developers, as well as academic researchers, reviewers, and others, we will inspire a new generation of designers with ideas that will advance the state of the art, and the practice of medicine.

2021 Update
===========

The 2010 version of the Stent Calculator worksheet more complicated than necessary for many applications. An simplified revision, created in 2021, implements the most important features in a Jupyter Notebook. The [Stent Calculator 2021](https://github.com/cbonsig/open-stent/blob/master/stent_calculator_2021/stent_calculator_2021.ipynb) notebook is good starting place. If you don't have Jupyter installed on your own computer, you can access an interactive version on [Google Colab](https://colab.research.google.com/github/cbonsig/open-stent/blob/master/stent_calculator_2021/stent_calculator_2021.ipynb).

The formulas derived in the Jupyter Notebook are implemented in a [Google Sheet](https://docs.google.com/spreadsheets/d/1WNo-heeC47Z9YqaJjs4vi74C_uU2YyMQA8cRFJYoxgw/edit#gid=0). This is a good way to experiment with different design alternatives. Use "File > Make a Copy" to edit in your browser, or "File > Download" to edit on your own computer.

Open Stent Design / Print Edition
=================================
You can buy a nicely bound full color printed version of the Open Stent Design manuscript for about $20 from Amazon. http://www.amazon.com/Open-Stent-Design-expanding-cardiovascular/dp/1481080695

Components of This Project
==========================
This project will be seeded with a set of related resources, as explained below. The initial release of each component will be posted as it becomes available. Craig first presented the project at the Open Source Stent Calculator project at SMST 2010, and it is also discussed at http://www.nitinol.com/nitinol-university/ The components of the project include:

Open Stent Design: open-stent.pdf a draft manuscript that explains the project, provides step-by-step guidance for building a generic stent using Solidworks, and documents all of the formulas used in the Stent Calculator Worksheet.

Open Source Stent Design: Open_Stent_Design_20100611.SLDPRT a generic stent, including native parametrically controlled Solidworks files to generate the geometry in raw, finished, constrained, and expanded forms.

Stent Calculator Worksheet: Stent_Calculator_Worksheet.xls a spreadsheet based calculator designed to predict stent performance as a function of design inputs.

Stent Calculator Python: stent-calculator.py Python code including all formulas from the worksheet.

Open Source Stent FEA: (planned) Abaqus code for analysis of the open source stent, and verification of Stent Calculator.

Licensing
=========
This work is licensed under a Creative Commons Attribution-ShareAlike 3.0 Unported License. Information about the terms of this license can be found at http://creativecommons.org/licenses/by-sa/3.0/

This "CC-BY-SA" license is explained in detail at the link above. Basically, it means that you have my permission to use, share, distribute, and create derivative works, in a commercial or non-commercial setting, with two requirements:
1. Provide attribution, for example: "Derived from Open Stent Design, Craig Bonsignore, Nitinol Devices & Components (NDC), http://nitinol.com"
2. Any derived works are shared under the same terms.

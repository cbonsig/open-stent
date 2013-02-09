open-stent
==========

Stents are medical implants commonly used to provide support and scaffolding to diseased arteries, veins, or other vessels in the human body. Many stent design can be imagined as a series of deforming beams, wrapped into a cylindrical shape like a spring. Well known structural mechanics formulas can be used to relate deflections of beams to stresses, strains, and forces. Stent Calculator uses these principles to relate stent design inputs like tubing diameter, wall thickness, and strut length, to performance outputs like strength, surface area, mass, contact pressure, and strain. These relationships are especially useful for stents fabricated from superelastic nitinol, which can reach strains of 1-2% with a substantially linear elastic relationship to stress. Because this is an order of magnitude higher than conventional engineering materials, nitinol is particularly well suited to analysis using the tools provided by the Stent Calculator project.

Goals and Motivation of This Project
====================================

This project is intended to bring the collaborative principles of open source to the typically closed and proprietary world of medical device development. NDC has a long history leading development of nitinol stents and similar components, and has also been a leading publisher and educator in the field. Contributing to the open source and creative commons movements is a natural evolution of our commitment to nitinol education. It is our hope that providing these tools and resources in an unlimited way to the community of medical device developers, as well as academic researchers, reviewers, and others, we will inspire a new generation of designers with ideas that will advance the state of the art, and the practice of medicine.

Components of This Project
==========================
This project will be seeded with a set of related resources, as explained below. The initial release of each component will be posted as it becomes available. Craig first presented the project at the Open Source Stent Calculator project at SMST 2010, and it is also discussed at NitinolUniversity.com The components of the project include:

Open Stent Design: open-stent.pdf a draft manuscript that explains the project, provides step-by-step guidance for building a generic stent using Solidworks, and documents all of the formulas used in the Stent Calculator Worksheet.

Open Source Stent Design: Open_Stent_Design_20100611.SLDPRT a generic stent, including native parametrically controlled Solidworks files to generate the geometry in raw, finished, constrained, and expanded forms.

Stent Calculator Worksheet: Stent_Calculator_Worksheet.xls a spreadsheet based calculator designed to predict stent performance as a function of design inputs.

Stent Calculator Python: stent-calculator.py Python code including all formulas from the worksheet.

Open Source Stent FEA: (planned) Abaqus code for analysis of the open source stent, and verification of Stent Calculator.

Licensing
=========
The resources provided as part of this project are contributed to the community under copyleft licenses. This means that the materials may be freely redistributed with attribution, and requires any derivative works to carry the same freedoms as the original license. Under these principles, the entire community benefits from its collective wisdom and creativity. We look forward to your contributions!

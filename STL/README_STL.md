# Open Stent STL files

The Open Stent design was developed using SolidWorks 2012; the native files are posted in the parent directory of this repository. The design been ported to Pro/Engineer by @teckna3d; native files for that version can be found at https://github.com/teckna3d/open-stent . Unfortunately, there are as yet no good open source alternative to parametric solid modeling software like SolidWorks and Pro/E. 

.STL is a non-proprietary file format commonly used to represent geometry, especially for 3D printing. This folder contains two .STL exports derived from the original SolidWorks Open_Stent_Design_20100611.SLDPRT file. One represents the stent in its constrained configuration (about 2mm diameter), and the other represents the stent in its expanded configuration (about 8mm diameter). This configuration is typical for peripheral arterial stents. 

This geometry was designed according to the capabilities and constraints of laser micromachining, and not with additive manufacturing techniques in mind. I have not attempted to 3D print these geometries, and I expect that it would be quite challenging to get a good quality result. Scaling up the geometry will probably be helpful, and a creative approach to support material will be essential. These files are saved directly from SolidWorks 2014. Some post-processing using Meshlab, or the mesh processing tool of your choice will probably be necessary.

If you have any success printing these models, derivatives, or similar structures, please drop me a line! 
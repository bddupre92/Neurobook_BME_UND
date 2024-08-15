# Chapter 8: Lab Example 2

## Overview
In this lab example, we will utilize the Image System Engineering Toolbox for Biology, or ISETBio for short. ISETBio is a set of tools for MATLAB that can conduct visual system analysis by providing capabilities to create spectral radiance scenes and model their effects on human optics, eye movements, cone absorptions, retinal cell properties, and more. 

The link to download and install ISETBio from their GitHub can be found here:
[GitHub - isetbio/isetbio: Tools for modeling image systems engineering in the human visual system front end](https://github.com/isetbio/isetbio).

You can learn more about ISETBio from Cottaris et al. [194]. 

As part of this lab, we will reinforce our understanding of the visual system anatomy by creating a plot of cone density in the eye. This will be accomplished by utilizing a tutorial script from the ISETBio toolbox in MATLAB.

## Requirements
- MATLAB
- ISETCam
- ISETBio

## Description
As we learned in the visual system chapter, cones are concentrated in the fovea. The cones are responsible for our color vision but are not very sensitive to light in comparison to rods. For this reason, there is a clever application of our anatomical knowledge during times of darkness. This concentration of cones in the center of our vision essentially creates a centrally focused blind spot at night. Instead of looking directly at an object when it is dark, you can look 5-10 degrees away from the center of gaze and have better light sensitivity, effectively enhancing your night vision. 

Let’s look at a plot of the cone density to effectively illustrate this concept.

Within MATLAB, navigate to the ISETBio tutorial/cones folder. Inside this folder, you can find a `t_conesDensity.m` script file. If you open this, the ISETBio team has succinctly described the function of the script and the source of the data. They use two resources to obtain the cone density estimates: Curcio et al. [170], and Song et al. [171].

The script file is short and to the point. A quick evaluation of the script will show you how the ISETBio toolbox works to obtain the final goal of plotting cone density. The `pos` portion of code specifies the location of some object outward from the fovea in millimeters. The `ang` portion defines the angle of view around the eye in radians. This allows us to plot a full range of the eye map (Fig. 8.10). Then, the distribution of cones from the two research papers above is defined.

Run the script for `t_conesDensity.m` and evaluate the final logarithmic scale plot that is produced.

## Summary
We utilized the ISETBio toolbox in MATLAB to run a basic tutorial that allowed us to visualize the concentration of cones across the retina. This provides us with a basic understanding of how the ISETBio toolbox functions and may guide you in thinking of creative ways to employ this toolbox for your own research goals.

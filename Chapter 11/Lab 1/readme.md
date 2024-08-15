# Chapter 11: Lab Example 1

## Overview
In this chapter, you learned about the Psychophysics Toolbox functions and how they can be used in MATLAB to conduct research. For the laboratory exercise, we will utilize one of these Psychtoolbox functions to perform an auditory test. Of note, the author of this chapter has undergone two tympanoplasty procedures to reconstruct both eardrums. This was a result of complications from ear tubes as an infant. Using the knowledge you gained in this chapter and your newfound understanding of the auditory system, try to look for any abnormal results from the MATLAB hearing test performed by the author. 

## Objective
Use the Psychtoolbox functions in MATLAB to perform a rudimentary hearing test to examine the frequency range that you can detect. Plot the frequency range in MATLAB.

## MATLAB Setup
First, you should already have MATLAB installed on your computer. Next, go to Psychtoolbox and download the Psychtoolbox files:

[Psychtoolbox Download](http://psychtoolbox.org/download.html#installation)

Installing Psychtoolbox is straightforward and installation instructions are also provided in the link above. After downloading the Psychtoolbox folder, path to it in MATLAB and type `SetupPsychtoolbox` in the MATLAB command line. Done!

## MATLAB Code
The MATLAB code for this lab is provided in the file [ExtendedToneReactionTest.m](ExtendedToneReactionTest.m). This function initializes the Psychtoolbox sound driver, generates tones at various frequencies, plays those frequencies at three decibel (dB) ranges, and measures the response.

To run the code:
1. Download the `ExtendedToneReactionTest.m` file.
2. Place it in your MATLAB working directory.
3. Run the function by typing `ExtendedToneReactionTest` in the MATLAB command window.

## Laboratory Results and Discussion
Now, run the code and hit the spacebar (or any key) when you hear a tone. When the author performed this lab, he utilized a high-quality headphone system and listened in a quiet room. Although it should be mentioned the decibel setting in the code is relative to the volume setting of the computer and not reflective of the actual decibel level.  Fig. 11.4 shows the test result from the author. 

The green circles on the graph represent a response, and the red x represents no response. Next, let’s observe the results from a healthy adult female volunteer and compare:

If we look at the frequency and decibel response, there is a notable difference in the higher-frequency range. Notice how the author was unable to hear any 10,000 Hz tones and could only hear the 7,500 Hz tone at 70dB. The female volunteer could hear both frequencies at 50dB and 70 dB.




# Chapter 1: Lab Example 1

## Introduction

This first chapter explains the fundamental principles of the brain, including the neurons, and how they communicate with one another to execute various functions throughout the body. We will take what we have discussed and apply it to a practical engineering tool. In this first lab example, we will use MATLAB. This platform will provide the tools for simulating and analyzing the differences in morphology of different neurons using the TREES Toolbox. This toolbox is comprehensively designed to analyze and visualize neuron morphology structures. In this lab example, we will download the toolbox and generate visuals using the dataset provided to look at the morphology of different neurons. 

## Steps
First, you will need to download MATLAB if you do not already have it; it will become useful not only in the journey of neural engineering in this textbook but in many other instances of your engineering journey. Follow this link to download MATLAB

https://www.mathworks.com/products/matlab/student.html

After downloading MATLAB to your device, you will then need to download the TREES toolbox using this link. 

https://www.mathworks.com/matlabcentral/fileexchange/68886-trees-toolbox

Once on the website, you will download the current version of the TREES toolbox from GitHub. The toolbox comes in the form of a zip file. When the zip file is downloaded onto your device, unzip the toolbox. Other toolboxes recommended for the TREES Toolbox are the Image Processing Toolbox, in polyhedron, and the Statistics and Machine Learning Toolbox, which can be added using the MATLAB Add-On Explorer. 
Now that we have the toolbox, we can explore it in MATLAB. The first step is to unzip the TREES toolbox file and then add the TREES Toolbox to your MATLAB path. You do this by importing the file using the import folder button. Then right-click the file in the Current Folder box and select Add to Path. Once in your MATLAB path, code in >>start_trees in the command window. Another way to start the toolbox is by navigating to the start_trees.m file and clicking run. You will get the red error mes-sage in the second image if you have unsuccessfully uploaded the trees toolbox. You will see the second message in black if you have successfully uploaded it.
Now that the toolbox is loaded into your MATLAB, we will visualize neuron morphology. 

![image](https://github.com/user-attachments/assets/6330fd5e-90d9-4f8c-8ff5-de6f9e47afc8)

![image](https://github.com/user-attachments/assets/c652fb82-3f3e-4600-af44-88c2079b4840)


First, go to the command window and code >>load_tree. Once you have done that, MATLAB will open the Pick a file pop-up box. Navigate to the samples folder, then to the mtr folder. The TREES toolbox saves the morphology files in. mtr format. For this lab, we will select the sample .mtr file and click Open.
Next, to upload the sample as a visual image, code >>fix_tree_UI in the command window. You will be prompted with a pop-up box asking you to upload an input tree to be repaired. Click OK and navigate back to the “sample.mtr” file. You will then be prompted to upload a reference tree and navigate back to the same “sample.mtr” file. Once you have uploaded the input and reference tree, a “fix_tree_UI” pop-up window will open, show-casing the sample.

![image](https://github.com/user-attachments/assets/fc7a2b8a-ecb1-46e8-aa20-ade6b9611713)

![image](https://github.com/user-attachments/assets/8925b40d-5664-478d-9d89-4bbf22b27e2f)

Can you use your knowledge from this chapter to know what morphological structure is being depicted? If you said axon terminals, you are correct! In this sample, we see a visual representation of the axon terminals and a potential number of synaptic connections this sample could make. 

Now, we will upload a new sample. Follow the same steps for the “sample.mtr” file but choose the “hss.mtr” file instead. Remember to upload this as your tree to be repaired and your reference tree. 

![image](https://github.com/user-attachments/assets/63876f2f-486b-41f2-a288-efcef7fb1a21)

Using this file, we can see an example of an entire neuron show-casing all the morphological features. You can use the zoom-in and zoom-out buttons in the top left corner to take a closer look at the different parts of the neuron. 
We can take this image rend-ing one step further by uploading an image stack. 
Navigate to the Load stack button in the right-hand corner. The “Pick a file” po- up menu will open. Navigate to the test folder, stacks folder, and data folder, and click the available stack image.
In this new image rendering, we can see how the morphology of these neurons is situated and what other neurons around it look like. 
This toolbox can also visualize neurons, measure dendritic length, branch points, and surface area of neurons, and conduct statistical analysis on these parameters. 

![image](https://github.com/user-attachments/assets/bc118186-cd0e-4dda-ad20-eca45f9eec4f)

## Other Examples and Resources

Several other examples are available for you to use to keep exploring this toolbox. One type of resource is Hermann Cuntz's free TREES toolbox tutorials on YouTube, which can be accessed using [this link](https://www.youtube.com/@manodelcatan).

For more examples of practical applications of this chapter's content, please visit the book's dedicated GitHub repository page using [this link](https://github.com/bddupre92/Neurobook_BME_UND).

# Chapter 3: Lab Example 2

## Introduction

In this lab example, we will develop our own neural network (NN) to predict injury risk from vehicle crash data using artificial data to simply illustrate how you could apply NNs to your own research. We will generate sample data, build and train the NN, and then test it with input data to evaluate its functionality. To reiterate, this is an entirely fictional dataset meant to illustrate the application of NNs to various research datasets.

## Exercise Instructions

### Step 1: Generate Sample Data

First, we will generate synthetic data to simulate vehicle crash database information. Imagine this data could be any form of information, whether training for images as shown in Fig. 3.20, or a large dataset with a range of variables as in this example. Obviously, the type of network you design will change, but this is meant to be a very basic exercise. For this artificially generated data, we will include vehicle type, crash severity, peak acceleration, and corresponding injury risk. Run the `generate_dataset.py` script to generate artificial data. Feel free to make your own adjustments to this script as well. The generated data is artificially skewed with some variability and noise to introduce realistic trends in data to improve this theoretical model’s prediction accuracy (increased severity leads to increased injury risk) while attempting to include some degree of variability. This is a scatter plot of what our generated dataset looks like:

### Step 2: Write and Execute the Neural Network Training Script

Using the script provided named `train_nn.py`, write and execute the training script for the neural network code. You can see the Keras model is being used here. Additionally, some of the data is normalized within this code as well. As you learned in this chapter, normalization is a key step to ensure that each feature contributes proportionately to the model’s learning process. After executing the training script, we see the following:

As you can see in this screenshot, the model completed 20 epochs and the test loss was 0.4281 with an accuracy of 82.5%. This effectively accomplishes the goal of training a custom neural network from a dataset. We could take this a step further by predicting the injury risk from provided data.

### Step 3: Write and Execute Prediction Code

Let’s re-load the neural network while also having it output a prediction of injury risk from a sedan with a 12mph delta-V (collision severity) and 55g peak acceleration. This can be accomplished by the `predict_nn.py` script. The following output is observed after the model is re-trained:

## Discussion

Based on the trained data, the neural network predicts the injury risk from our sedan of 12mph dV and 55g acceleration to be 64%. This could be likened to the typical logistic regression type analysis typically conducted for these types of datasets. However, even in this simple feed-forward type of neural network we generated, it is clear how many variables could be included to train the network, including data that is non-linear or variable in nature. Neural networks can handle non-linear relationships and complex patterns in the data, unlike logistic regression. Obviously, there can be overfitting concerns and various other considerations already discussed in the chapter. This laboratory example shows a simplistic method for training a feedforward neural network for classification tasks.

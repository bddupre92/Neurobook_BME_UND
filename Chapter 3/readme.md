Brain MRI Age Classification using Deep Learning
This project demonstrates how to classify brain MRI images into different age groups using deep learning. The project leverages the ResNet50 model, pre-trained on ImageNet, for transfer learning. The workflow includes preprocessing MRI data, training the model, evaluating its performance, and visualizing the model's behavior through occlusion sensitivity maps.

Prerequisites
Ensure you have the following packages installed:

bash
Copy code
pip install nibabel tensorflow matplotlib seaborn pandas scikit-learn
Project Structure
Data Loading and Preprocessing

Mount Google Drive: Mount your Google Drive to access the dataset.
Load Participant Data: Load and preprocess participant metadata.
Load MRI Data: Load and preprocess the MRI data from NIfTI files.
Data Augmentation: Apply data augmentation to increase model generalization.
Model Building and Training

Transfer Learning with ResNet50: Use ResNet50 as the base model for feature extraction.
Training the Model: Train the model on the augmented dataset.
Custom Training Progress Bar: Implement a custom progress bar to monitor training.
Evaluation and Visualization

Model Evaluation: Evaluate the model using metrics such as accuracy and confusion matrix.
Occlusion Sensitivity Maps: Visualize which parts of the images contribute most to the model's decisions.
License and Acknowledgments
This code is a recreation of the Matlab Code found at the following link: Brain MRI Age Classification using Deep Learning.

MathWorks Teaching Resources. (2022). Brain MRI Age Classification using Deep Learning (Course Integration Version) [Source code]. GitHub. Retrieved [date you accessed the repository], from https://github.com/MathWorks-Teaching-Resources/Brain-MRI-Age-Classification-using-Deep-Learning.

Copyright (c) 2020, The MathWorks, Inc.

All rights reserved. Redistribution and use in source and binary forms, with or without modification, are permitted provided that the following conditions are met:

Redistributions of source code must retain the above copyright notice, this list of conditions, and the following disclaimer.
Redistributions in binary form must reproduce the above copyright notice, this list of conditions, and the following disclaimer in the documentation and/or other materials provided with the distribution.
In all cases, the software, and all modifications and derivatives of the software shall be licensed to you solely for use in conjunction with MathWorks products and service offerings.
Disclaimer: THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.

# Brain MRI Age Classification using Deep Learning

This project demonstrates how to classify brain MRI images into different age groups using deep learning. It utilizes the ResNet50 model pre-trained on ImageNet for transfer learning. The project is structured to preprocess MRI data, train the model, evaluate its performance, and visualize the model's behavior using occlusion sensitivity maps.

## Prerequisites

Ensure you have the following packages installed:

```bash
pip install nibabel tensorflow matplotlib seaborn pandas scikit-learn

## Project Structure

- **Data Loading and Preprocessing**
  - **Mount Google Drive**: Mount your Google Drive to access the dataset.
  - **Load Participant Data**: Load and preprocess participant metadata.
  - **Load MRI Data**: Load and preprocess the MRI data from NIfTI files.
  - **Data Augmentation**: Apply data augmentation to increase model generalization.

- **Model Building and Training**
  - **Transfer Learning with ResNet50**: Use ResNet50 as the base model.
  - **Training the Model**: Train the model on the augmented dataset.
  - **Custom Training Progress Bar**: Implement a custom progress bar to monitor training.

- **Evaluation and Visualization**
  - **Model Evaluation**: Evaluate the model using accuracy and a confusion matrix.
  - **Occlusion Sensitivity Maps**: Visualize which parts of the images contribute most to the model's decisions.

#License and Acknowledgments

This code is a recreation of the Matlab Code found at the following link: https://github.com/matlab-deep-learning/Brain-MRI-Age-Classification-using-Deep-Learning?tab=License-1-ov-file#readme

MathWorks Teaching Resources. (2022). Brain MRI Age Classification using Deep Learning (Course Integration Version) [Source code]. GitHub. Retrieved [date you accessed the repository], from https://github.com/MathWorks-Teaching-Resources/Brain-MRI-Age-Classification-using-Deep-Learning

Copyright (c) 2020, The MathWorks, Inc. All rights reserved. Redistribution and use in source and binary forms, with or without modification, are permitted provided that the following conditions are met:

Redistributions of source code must retain the above copyright notice, this list of conditions and the following disclaimer.
Redistributions in binary form must reproduce the above copyright notice, this list of conditions and the following disclaimer in the documentation and/or other materials provided with the distribution.
In all cases, the software is, and all modifications and derivatives of the software shall be, licensed to you solely for use in conjunction with MathWorks products and service offerings. THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.

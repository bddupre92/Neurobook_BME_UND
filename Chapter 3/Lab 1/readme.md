# Brain MRI Age Classification using Deep Learning

This project demonstrates how to classify brain MRI images into different age groups using deep learning. It utilizes the ResNet50 model pre-trained on ImageNet for transfer learning. The project is structured to preprocess MRI data, train the model, evaluate its performance, and visualize the model's behavior using occlusion sensitivity maps. This is a Python recreation of the Matlab model linked and cited below. 

## Project structure

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

## Prerequisites

Ensure you have the following packages installed:

```bash
pip install nibabel tensorflow matplotlib seaborn pandas scikit-learn
```

## Instructions
**Mount Google Drive:**

```bash
from google.colab import drive
drive.mount('/content/drive')
```

**Load Participant Data:**
```bash
participant_data_path = '/content/drive/MyDrive/Brain-MRI-Age-Classification-using-Deep-Learning/ds000228-1.1.0-subset/derivatives/participants.tsv'
participant_data = pd.read_csv(participant_data_path, sep='\t')
participant_data['AgeClass'] = pd.cut(participant_data['Age'], bins=[3, 6, 13, np.inf], labels=['Ages3-5', 'Ages7-12', 'Adults'])
Load and Preprocess MRI Data:
```

```bash
mri_data_folder = '/content/drive/MyDrive/Brain-MRI-Age-Classification-using-Deep-Learning/ds000228-1.1.0-subset/derivatives/preprocessed_data'
images, labels = load_2d_slices(mri_data_folder)
```

**Prepare Data for Training:**

```bash
x_train, x_test, y_train, y_test = train_test_split(images, labels_encoded, test_size=0.2, stratify=labels_encoded, random_state=42)
x_train_3ch = resize_and_convert(x_train)
x_test_3ch = resize_and_convert(x_test)
```

**Build and Train the Model:**

```bash
base_model = ResNet50(weights='imagenet', include_top=False, input_shape=(224, 224, 3))
model.fit(train_gen, validation_data=val_gen, epochs=10, callbacks=[CustomProgbar()])
```

**Evaluate the Model:**
```bash
test_gen = datagen.flow(x_test_3ch, y_test, batch_size=32, shuffle=False)
y_pred = np.argmax(model.predict(test_gen), axis=1)
accuracy = accuracy_score(y_test, y_pred)
```

**Visualize Occlusion Sensitivity Maps:**
```bash
view_occlusion_sensitivity_maps(class_label, 3, model, x_test_3ch, y_test, y_pred)
```

**Results**

Accuracy: Achieve and report the accuracy on the test dataset.
Confusion Matrix: Visualize the confusion matrix to understand model performance across classes.
Occlusion Sensitivity Maps: Generate maps to see which parts of the image are most important for the model's classification decisions.

**License**

This code is a recreation of the Matlab Code found at the following link: https://github.com/matlab-deep-learning/Brain-MRI-Age-Classification-using-Deep-Learning?tab=License-1-ov-file#readme

[1] Vijay Iyer (2024). Brain-MRI-Age-Classification-using-Deep-Learning (https://github.com/matlab-deep-learning/Brain-MRI-Age-Classification-using-Deep-Learning/releases/tag/v1.1), GitHub. Retrieved August 14, 2024.

Copyright (c) 2020, The MathWorks, Inc. All rights reserved. Redistribution and use in source and binary forms, with or without modification, are permitted provided that the following conditions are met:

Redistributions of source code must retain the above copyright notice, this list of conditions and the following disclaimer.
Redistributions in binary form must reproduce the above copyright notice, this list of conditions and the following disclaimer in the documentation and/or other materials provided with the distribution.
In all cases, the software is, and all modifications and derivatives of the software shall be, licensed to you solely for use in conjunction with MathWorks products and service offerings. THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.



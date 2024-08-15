
# Chapter 5: Lab Example 1

## Overview
For this laboratory exercise, we will utilize FreeSurfer to process and analyze fMRI data from the OpenfMRI dataset ds000171. This dataset examines how neural processing of emotionally provocative auditory stimuli is altered in depression. The study includes 19 individuals with Major Depressive Disorder (MDD) and 20 never-depressed control participants (ND), who listened to positive and negative emotional musical and nonmusical stimuli during fMRI scanning.

## Dataset Description
- **Title:** Neural Processing of Emotional Musical and Nonmusical Stimuli in Depression
- **Participants:** 19 MDD and 20 ND
- **Tasks:** Music comprehension/production
- **Scanner:** Siemens Skyra 3T

## Objective
The goal of this laboratory exercise is to process, visualize, and compare the brain activity of a control subject and an MDD subject using FreeSurfer and the dataset described above. This exercise will guide you through the steps of downloading the dataset, setting up FreeSurfer, running preprocessing with FreeSurfer, and visualizing the data in Freeview (the FreeSurfer visualization interface).

## Installation and Setup
Now that you have a general idea about this laboratory exercise, let’s get FreeSurfer installed and running. As of the time of writing this book, FreeSurfer 7.4.1 is the current version of the toolbox. We will cover the basic installation on a Windows 11 64-bit OS running on an LG Gram laptop with 16GB of RAM and an integrated graphics card.

### Steps:
1. Install Windows Subsystem for Linux (WSL) using the following command in Windows PowerShell (run as administrator):
   ```bash
   wsl -install
   ```

2. Download and install an X server (e.g., Xming, VcXsrv) to handle graphical visualizations.

3. Open the Ubuntu terminal and download FreeSurfer with:
   ```bash
   wget https://surfer.nmr.mgh.harvard.edu/pub/dist/freesurfer/7.4.1/freesurfer-linux-ubuntu22_amd64-7.4.1.tar.gz
   ```

4. Install FreeSurfer:
   ```bash
   sudo mkdir /usr/local/
   sudo tar -xzvf freesurfer-linux-ubuntu22_amd64-7.4.1.tar.gz -C /usr/local
   ```

5. Set up environment variables:
   ```bash
   export FREESURFER_HOME=/usr/local/freesurfer/
   echo "export FREESURFER_HOME=/usr/local/freesurfer/" >> ~/.bashrc
   source ~/.bashrc
   ```

6. Copy the FreeSurfer license file to your Linux directory:
   ```bash
   cp /mnt/c/Users/your_username/Downloads/license.txt ~/
   echo "export FS_LICENSE=$HOME/license.txt" >> ~/.bashrc
   ```

7. Configure display settings:
   ```bash
   echo "export DISPLAY=:0" >> ~/.bashrc
   source ~/.bashrc
   ```

8. Run Freeview to verify installation:
   ```bash
   freeview
   ```

## Downloading the Dataset
Next, let's proceed to downloading the dataset we want to analyze. You can download or use any data that suits your experiment goals. 

Visit the OpenfMRI data page and download the ds000171 accession number dataset:
[Download OpenfMRI ds000171](https://openfmri.org/dataset/ds000171/)

Extract the folders you downloaded into your WSL home directory:

```bash
mkdir -p ~/openfmri_ds000171/controls
mkdir -p ~/openfmri_ds000171/mdd
tar -xzvf controls.tar.gz -C ~/openfmri_ds000171/controls
tar -xzvf mdd.tar.gz -C ~/openfmri_ds000171/mdd
```

## Preprocessing
If you explore the structure of the data within the controls and MDD folders, you’ll notice several subfolders separating each subject data, and within those, anatomical and functional fMRI data. Let’s work with subject 01 data from both the control and MDD group. Setup a `SUBJECTS_DIR` environment variable:

```bash
export SUBJECTS_DIR=~/openfmri_ds000171
```

Run `recon-all` for the control subject and then for the MDD subject:

```bash
recon-all -s control_sub-01 -i ~/openfmri_ds000171/controls/sub-control01/anat/sub-control01_T1w.nii.gz -all
recon-all -s mdd_sub-01 -i ~/openfmri_ds000171/mdd/sub-mdd01/anat/sub-mdd01_T1w.nii.gz -all
```

Run `qcache` for both subjects to smooth the data:

```bash
recon-all -s control_sub-01 -qcache
recon-all -s mdd_sub-01 -qcache
```

### FS-FAST Preprocessing
Now, you will need to run FS-FAST (FreeSurfer Functional Analysis Stream) preprocessing. FSFAST performs essential preprocessing steps of functional data such as motion correction, slice timing, spatial normalization, and smoothing.

Organize the functional data for FSFAST preprocessing:

```bash
mkdir -p ~/openfmri_ds000171/analysis/control_sub-01/bold/001 
mkdir -p ~/openfmri_ds000171/analysis/control_sub-01/bold/002 
mkdir -p ~/openfmri_ds000171/analysis/mdd_sub-01/bold/001 
mkdir -p ~/openfmri_ds000171/analysis/mdd_sub-01/bold/002
```

Move and rename the functional data files into these directories:

```bash
mv ~/openfmri_ds000171/controls/sub-control01/func/sub-control01_task-music_run-1_bold.nii.gz ~/openfmri_ds000171/analysis/control_sub-01/bold/001/f.nii.gz
mv ~/openfmri_ds000171/controls/sub-control01/func/sub-control01_task-music_run-1_events.par ~/openfmri_ds000171/analysis/control_sub-01/bold/001/
mv ~/openfmri_ds000171/controls/sub-control01/func/sub-control01_task-nonmusic_run-4_bold.nii.gz ~/openfmri_ds000171/analysis/control_sub-01/bold/002/f.nii.gz
mv ~/openfmri_ds000171/controls/sub-control01/func/sub-control01_task-nonmusic_run-4_events.par ~/openfmri_ds000171/analysis/control_sub-01/bold/002/
mv ~/openfmri_ds000171/mdd/sub-mdd01/func/sub-mdd01_task-music_run-1_bold.nii.gz ~/openfmri_ds000171/analysis/mdd_sub-01/bold/001/f.nii.gz
mv ~/openfmri_ds000171/mdd/sub-mdd01/func/sub-mdd01_task-music_run-1_events.par ~/openfmri_ds000171/analysis/mdd_sub-01/bold/001/
mv ~/openfmri_ds000171/mdd/sub-mdd01/func/sub-mdd01_task-nonmusic_run-4_bold.nii.gz ~/openfmri_ds000171/analysis/mdd_sub-01/bold/002/f.nii.gz
mv ~/openfmri_ds000171/mdd/sub-mdd01/func/sub-mdd01_task-nonmusic_run-4_events.par ~/openfmri_ds000171/analysis/mdd_sub-01/bold/002/
```

Create a text file in each session folder containing the subject name that corresponds to the anatomical data processed by `recon-all` earlier:

```bash
echo "control_sub-01" > ~/openfmri_ds000171/analysis/control_sub-01/subjectname
echo "mdd_sub-01" > ~/openfmri_ds000171/analysis/mdd_sub-01/subjectname
```

Run FS-FAST preprocessing:

```bash
export SUBJECTS_DIR=~/openfmri_ds000171/analysis
preproc-sess -s control_sub-01 -fsd bold -stc up -surface fsaverage lhrh -mni305 -fwhm 5 -per-run
preproc-sess -s mdd_sub-01 -fsd bold -stc up -surface fsaverage lhrh -mni305 -fwhm 5 -per-run
```


### First-Level Analysis
Next, we need to conduct the first-level analysis of the data. For simplicity, we are only going to analyze one run for two subjects, one control and one MDD subject.

Set up the analysis for the left hemisphere:

```bash
mkanalysis-sess   -fsd bold -stc up -surface fsaverage lh -fwhm 5   -event-related -paradigm sub-control01_task-music_run-1_events.par -nconditions 3   -spmhrf 0 -TR 3 -refeventdur 16 -nskip 4 -polyfit 2   -analysis control.music.sm05.lh -force -per-run
```

Run the same analysis setup for the MDD subject.

### Creating Contrasts
Create contrasts you are interested in examining:

```bash
mkcontrast-sess -s control_sub-01 -analysis control.music.sm05.lh -contrast combined_music-vs-rest -a 2 -a 3
mkcontrast-sess -s control_sub-01 -analysis control.music.sm05.lh -contrast pos_music-vs-rest -a 2
mkcontrast-sess -s control_sub-01 -analysis control.music.sm05.lh -contrast response-vs-rest -a 1

mkcontrast-sess -s mdd_sub-01 -analysis mdd.music.sm05.lh -contrast combined_music-vs-rest -a 2 -a 3
mkcontrast-sess -s mdd_sub-01 -analysis mdd.music.sm05.lh -contrast pos_music-vs-rest -a 2
mkcontrast-sess -s mdd_sub-01 -analysis mdd.music.sm05.lh -contrast response-vs-rest -a 1
```

Run the analysis:

```bash
selxavg3-sess -s control_sub-01 -analysis control.music.sm05.lh
selxavg3-sess -s mdd_sub-01 -analysis mdd.music.sm05.lh
```

### Visualization and Comparison
After processing, you can visualize the results using Freeview. Open Freeview with the `freeview` command in your terminal. Select "load volume" and locate the “mri” directory of the subject you wish to examine. You can also look at other outputs from recon-all, such as segmentations, surfaces, or masks.

For the major depressive disorder subject, look at the results for their combined music vs baseline (tone). You can see areas of activation in the left hemisphere. If you conducted the analysis of the right hemisphere and subcortical structures, you could examine which internal structures become activated in each subject.

The applications of this tool are extensive in your journey to studying fMRI. From here, you could analyze every control subject and create a statistically robust representation of brain activations during music exposure in comparison to resting state. Or you could proceed to compare the activations of the control subject to the depressive subjects.

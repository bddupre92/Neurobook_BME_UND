In this lab, we will become familiar with EEGLAB, a MATLAB toolbox designed for processing electroencephalography (EEG), magnetoencephalography (MEG), and other electrophysiological data. Distributed under the free BSD license, EEGLAB offers a comprehensive suite of tools for displaying and analyzing EEG data.
# Installation and Main Features
EEGLAB is hosted by the Swartz Center for Computational Neuroscience at UC San Diego. You can download the toolbox from this [link](https://sccn.ucsd.edu/eeglab/index.php ).
We extend our gratitude to UC San Diego for providing this valuable resource.
## Download and Installation
The download and installation process is similar to that of other MATLAB toolboxes:
1.	Visit the EEGLAB download page.
2.	Follow the instructions provided to download the appropriate version for your system.
3.	Unzip the downloaded file to a convenient directory on your computer.
4.	Add the EEGLAB folder to your MATLAB path.
## Running EEGLAB
After installation, you can launch EEGLAB by running the eeglab.m file. To do this:
1.	Open MATLAB.
2.	Navigate to the directory where you unzipped EEGLAB.
3.	Type eeglab in the MATLAB command window and press Enter.
This action should open the EEGLAB graphical user interface (GUI), which will appear as follows:

![image](https://github.com/user-attachments/assets/64ba1bc2-c898-4b02-a51f-23fa5e528bda)

In the following sections of this lab, we will explore the main features of EEGLAB for displaying and processing EEG data. These features include data importing, preprocessing, visualization, and analysis tools that are essential for neuroengineering research.

If you select File- load exisiting dataset and browse to the sample_data folder in the toolbox you will see t EEGLAB is a powerful tool for processing and analyzing EEG data and associated events. While you have the option to import your own EEG data, for this lab, we will work with existing datasets included in the EEGLAB package.
To load a sample dataset, follow these steps:
1.	Go to the File menu.
2.	Select Load existing dataset.
3.	Browse to the sample_data folder within the EEGLAB toolbox directory.
4.	You will see several options of sample datasets to choose from.
These sample datasets will help you familiarize yourself with the features and capabilities of EEGLAB.


In this lab, we will work with the eeglab_data.set sample dataset.

![image](https://github.com/user-attachments/assets/89697482-5360-40b1-b889-3f91c35ce5d8)

As shown, the sample data contains over 30,000 frames per epoch, 32 channels per frame, and 154 events, and it is sampled at 128 Hz, meaning 128 samples per second.

![image](https://github.com/user-attachments/assets/f3e0d0bb-6a8e-4f79-afe2-7ab097f433b4)


##Loading the EEG Data
1.	Select **eeglab_data.set** from the available options.
2.	This dataset contains EEG data with 32 channels, each labeled accordingly.
##Visualizing the Data
Once the data is loaded, EEGLAB allows you to plot all the channels in the time domain to observe different events. In this dataset:
•	Square events are highlighted in green.
•	RT events are highlighted in red.

 ![image](https://github.com/user-attachments/assets/0c9d5187-f596-4d0f-880e-594cc454acab)

##Power Spectral Density
EEGLAB also provides tools to plot the power spectral density (PSD) of the EEG signals. This feature is useful for identifying channels that may be faulty or need to be excluded from the analysis.
![image](https://github.com/user-attachments/assets/4b5720cf-2034-4b5a-b452-88c2752c847c)

 
##Inspecting Specific Channels
You can isolate a specific channel and visualize its properties using the **pop_prop** function. This feature enables detailed inspection of individual channels, facilitating quick and efficient EEG data analysis.

 ![image](https://github.com/user-attachments/assets/f3a5c313-78b1-4741-93e0-9e7ada27b37a)


##Advanced Features
EEGLAB is a robust tool with a variety of advanced features:
•	**Filtering**: EEGLAB allows you to apply frequency-delimited filters to the signals, which helps in isolating specific frequency bands of interest.
•	**Artifact Removal**: You can use independent component analysis (ICA) to remove artifacts from the data.
•	**Event-Related Potentials (ERP)**: EEGLAB enables the extraction and classification of event-related potentials (ERP), which are brain responses directly resulting from specific sensory, cognitive, or motor events. By averaging the responses of all events, you can build a signature waveform distinctive of the response to a specific stimulus.
These basic and advanced tools provided by EEGLAB allow for rapid and in-depth inspection and analysis of EEG data.
 
![image](https://github.com/user-attachments/assets/e68b0413-27d9-4292-8ff3-7ba4edd70a23)

![image](https://github.com/user-attachments/assets/96a44516-0b1b-4f09-8366-9adef3a38301)

EEGLAB provides advanced tools for cleaning EEG data, including the "Clean RawData" and "Artifact Subspace Reconstruction (ASR)" methods. These tools are essential for removing noise and artifacts from EEG recordings, which can otherwise interfere with data analysis and interpretation. By using these tools, you can significantly improve the quality and reliability of your EEG data.
To use the "Clean RawData" tool in EEGLAB, start by ensuring EEGLAB is running and your dataset is loaded. Navigate to the Tools menu, then select Reject data using Clean RawData. This will open a dialog box where you can configure parameters for data cleaning. The default settings are usually sufficient, but you can adjust them based on your dataset's specific needs. Click OK to run the tool, which will process the data and remove segments with high noise levels or artifacts.
For the Artifact Subspace Reconstruction (ASR) tool, again go to the Tools menu and select Reject data using ASR. In the dialog box that appears, configure the key parameters such as the cutoff threshold, which determines the level of artifact removal, and the window length, which defines the length of data segments to be processed. After setting these parameters, click OK to run ASR. This tool will identify and correct artifacts by reconstructing the affected data segments.


 ![image](https://github.com/user-attachments/assets/20b1f086-6ecb-41ab-be0c-80bd4568036d)

Both tools are integral for cleaning EEG data in EEGLAB, effectively removing noise and artifacts to enhance data quality. As shown, the signals in red have been identified as potential rejects from the dataset.
##ERPs
An Event-Related Potential (ERP) is a measured brain response that is the direct result of a specific sensory, cognitive, or motor event. ERPs are derived from electroencephalography (EEG) recordings and are used in cognitive neuroscience, psychology, and other fields to study brain function.

![image](https://github.com/user-attachments/assets/a9a0979d-941b-492c-9996-28308d113321)

 
Figure: Event-related potential in response to a visual stimulus as obtained by averaging the EEG signal of multiple stimulus presentations (S1, S2,… Sn). Originally published in Purves et al. (2008)
###How ERPs are Obtained Based on EEG
1. EEG Recording
Electroencephalography (EEG) involves placing electrodes on the scalp to measure the electrical activity produced by neurons in the brain. The raw EEG signal is a complex mix of electrical activity from multiple sources, including both spontaneous brain activity and responses to specific events.
2. Experimental Design
To obtain ERPs, researchers design experiments where participants are exposed to specific stimuli (e.g., visual, auditory, or tactile). These stimuli are presented at known times and are often repeated many times to obtain reliable measurements.
3. Time-Locking to Events
The EEG data is segmented into epochs, which are time-locked to the onset of the stimuli. Each epoch includes data from a short time window before and after the stimulus.
4. Averaging
Because the EEG signal contains a lot of noise from unrelated brain activity, muscle movements, and external sources, individual epochs are averaged across many trials. This averaging process helps to isolate the consistent brain response to the stimulus, as random noise tends to cancel out, while the signal related to the event remains.
5. Baseline Correction
Before averaging, a baseline correction is often performed. This involves subtracting the mean voltage of a pre-stimulus period (e.g., the time just before the stimulus is presented) from the entire epoch. This helps to correct for any slow drifts in the EEG signal.
6. Resulting ERP Waveforms
The result of averaging and baseline correction is a series of ERP waveforms, which reflect the brain's electrical response to the specific event. These waveforms consist of a series of positive and negative voltage deflections (peaks and troughs) occurring at different latencies (times) after the stimulus.
##Key Components of ERPs
•	Latency: The time between the onset of the stimulus and the occurrence of a particular ERP component (peak or trough). This reflects the timing of neural processes.
•	Amplitude: The magnitude of the voltage change associated with an ERP component, which can indicate the strength of the neural response.
•	Polarity: Whether the ERP component is positive (upwards) or negative (downwards).
•	Topography: The distribution of ERP amplitudes across the scalp, which can provide information about the source of the neural activity.
##Common ERP Components
•	P300: A positive deflection occurring around 300 milliseconds after stimulus onset, often associated with attention and decision-making processes.
•	N400: A negative deflection peaking around 400 milliseconds, related to language processing and semantic incongruence.
•	N170: A negative component occurring around 170 milliseconds, associated with face perception.
##Example of ERP Analysis Process
1.	Record EEG data while a participant performs a task involving repeated stimuli.
2.	Segment the data into epochs around each stimulus presentation.
3.	Apply baseline correction to each epoch.
4.	Average the epochs to obtain the ERP waveform.
5.	Analyze the ERP components to interpret the neural processes involved in the task.
ERPs provide valuable insights into the timing and nature of cognitive processes by allowing researchers to examine the brain's electrical response to specific events in real-time.
EEGLAB includes the extraction and examination of Event-Related Potentials (ERPs). To analyze ERPs using EEGLAB, researchers first import their raw EEG data into the software. They then preprocess the data, which typically involves filtering to remove noise, epoching the continuous EEG data into time segments around the events of interest, and performing baseline correction. Artifact rejection or correction methods are applied to remove noise from non-neural sources such as eye movements or muscle activity. Once clean epochs are obtained, they are averaged to isolate the ERP components related to specific stimuli or tasks. EEGLAB provides various tools for visualizing these ERP waveforms, including plotting the averaged ERP data and topographical maps to examine spatial distributions of the ERP components. Additionally, EEGLAB supports statistical analysis and comparison of ERP components across different experimental conditions. This comprehensive suite of tools within EEGLAB facilitates detailed ERP analysis, helping researchers to interpret the neural mechanisms underlying cognitive processes.

![image](https://github.com/user-attachments/assets/a08042ef-f501-44f4-98c7-48a0612d7055)

References:

EEGLAB: https://sccn.ucsd.edu/eeglab
Delorme, A., & Makeig, S. (2004). EEGLAB: an open source toolbox for analysis of single-trial EEG dynamics including independent component analysis. Journal of neuroscience methods, 134(1), 9–21.
Makeig, S., Westerfield, M., Jung, T. P., Covington, J., Townsend, J., Sejnowski, T. J., & Courchesne, E. (1999). Functionally independent components of the late positive event-related potential during visual spatial attention. Journal of Neuroscience, 19(7), 2665–2680.

# Chapter 2: Lab Example 2

## Overview
This Lab Example will look at the Izhikevich (IZH) Model. The Izhikevich model is a mathematical model of a neuron similar to Hodgkin-Huxley's, and it is designed to replicate a wide variety of spiking and bursting behaviors observed in neurons. Eugene M. Izhikevich first introduced it in 2003 [1] as a more detailed model and alternative to the Hodgkin-Huxley model. In this lab, we will use Simulink to create the IZH model and then look at different firing patterns of a neuron. 

The following system of ordinary differential equations describes the IZH Model:

### The membrane potential equation

![image](https://github.com/user-attachments/assets/26dfc1db-521e-4f03-856a-3be55f50bbdf)


### The recovery variable

![image](https://github.com/user-attachments/assets/fe6872ac-38d0-4086-8e35-ab0f1fca13c4)

### After-spiking resetting condition

![image](https://github.com/user-attachments/assets/406d35f4-8624-4528-89f4-979e388709e9)


## Variables
- **v**
  - Represents the membrane potential of the neuron.
  - Measured in millivolts (mV).
  - The variable indicates the neuron's voltage at any given time.
  - When v reaches a threshold (e.g., 30 mV), the neuron has fired an action potential (spike).

- **u**
  - Represents the membrane recovery variable.
  - It accounts for K+ (potassium) activation and inactivation of Na+ (sodium) ionic currents.
  - Helps in modeling the refractory period of the neuron, during which the neuron is less likely to fire another spike.
  - Influences the rate at which the membrane potential returns to its resting state after a spike.

- **I**
  - Represents the input current to the neuron.
  - Can be thought of as the external stimulus or synaptic input the neuron receives.
  - It influences the neuron's membrane potential and can cause it to reach the threshold to fire a spike.

- **a**
  - Time scale of the recovery variable u.
  - Controls how quickly u responds to changes in v.

- **b**
  - Sensitivity of the recovery variable u to the membrane potential v subthreshold fluctuations.
  - Determines how strongly u is coupled to v.

- **c**
  - After-spike reset value of the membrane potential v.
  - When the membrane potential v reaches the threshold (e.g., 30 mV), it is reset to c.

- **d**
  - After-spike reset increment of the recovery variable u.
  - When the membrane potential v is reset, u is incremented by d.
  - This helps to model the effect of spike-triggered adaptation, where the neuron's excitability is reduced after firing.

## How it works
### Membrane Potential Dynamics:
  - The first equation models the membrane potential dynamics v. It includes a quadratic term 0.04v², a linear term 5v, and constant terms that drive the membrane potential.
  - The term −u represents the inhibitory effect of the recovery variable on the membrane potential.
  - The input current I can depolarize (excite) or hyperpolarize (inhibit) the membrane potential.

### Recovery Variable Dynamics:
  - The second equation describes the dynamics of the recovery variable u. It adjusts u based on the current value of v and the difference between bv and u.
  - The parameter a controls the time scale, while b determines the sensitivity of u to v.

### After-Spike Resetting:
  - When the membrane potential v reaches a threshold (30 mV), it is reset to a lower value c, simulating the neuron firing an action potential.
  - Simultaneously, the recovery variable u is incremented by d, increasing its value to reflect the refractory period where the neuron is less likely to fire again immediately.

By adjusting the parameters a, b, c, and d, the IZH model can replicate various types of neuronal behavior, making it versatile and efficient for simulating neuronal networks. Here is a figure taken from Izhikevich et al. (2003) that shows some of the different types of spiking patterns that the model can replicate.

![image](https://github.com/user-attachments/assets/746863b2-761a-4c2f-9146-ea0c170357f7)

In this lab, we will replicate a YouTube tutorial from MATLAB Ambassador. YouTube is a great resource for tutorials on using different engineering tools.

## Requirements
- Simulink
- MATLAB
- YouTube

## Steps
First, open MATLAB. Then, use this link to find the YouTube page for the video Simulating a Neuron by the MATLAB Ambassador. [YouTube Video](https://www.youtube.com/watch?v=NnZlGC1_I0M)

The video caption includes a link to a Google Drive folder with the files needed to complete this lab. Here is the link as well.
   [Google Drive Folder](https://drive.google.com/drive/folder...)

Once you have the folder open, download the `NeuronParameters.m` file. This MATLAB script will give us our parameters for the variables discussed in the IZH model. Once you download the file, save it and open it in your MATLAB as a new script. You can also double-click the file to open it in MATLAB. Once you open the MATLAB script, click run to ensure no errors.

After this, go back to Google Drive and download the `NeuronVideo2.slxc` file. This is going to be the Simulink model. You can open it two ways. The first way is to double-click on the file and automatically open it in Simulink. The second way is to save the file, navigate to Simulink under the Home tab in MATLAB, click open under the simulation file, and then click the file.

Once you have opened the Simulink file, it should look like this.

 ![image](https://github.com/user-attachments/assets/5f203faf-d4fb-4d18-9e4c-ada57994af9b)
  

## Simulink Model Components Description
Here is a breakdown of the key components of the Simulink model:

### Input Block (I):
- Represents the input current to the neuron.

### Membrane Potential Equation Implementation:
- Blocks calculate 0.04v^2, 5v, and the constants 140 and −u.
- The sum of these components and the input current I gives dv/dt.

### Recovery Variable Equation Implementation:
- Blocks calculate a(bv - u) to determine du/dt.

### Function Block (Fcn):
- Handles the after-spike resetting condition. When v reaches 30 mV, it resets v to c and increments u by d.

### Integrator Blocks:
- Integrate dv/dt and du/dt) to update v and u over time.

### Output Blocks:
- Display the membrane potential v and the recovery variable u.

Now that you have all the files and understand how they work watch the YouTube video where you will model tonic spiking and bursting. Click the scope box to view the neurons' spiking pattern.

Next, we will take this lab further and model more spiking patterns, including inhibition-induced spiking and a resonator. You will first need to return to your Neuron Parameters code in MATLAB and add the following parameters for the variables.
a = -0.02
b = -1
c = -60
d = 8
I = 80

Then, you will need to change T to equal 3. This means that MATLAB will pull the parameters from row three of the parameter’s matrix. Click Run. Then go to Simulink and click Run on your model. You must click Run in MATLAB before running the Simulink model again. You will see the firing pattern here.

![image](https://github.com/user-attachments/assets/2e313247-0a57-4fc0-aba4-7dc0bfa0a875)

Inhibition-Induced Spiking
Inhibition-induced spiking, also known as post-inhibitory rebound speaking, is a phenomenon where a neuron generates action potentials in response to inhibitory input. This behavior is counterintuitive because inhibition typically reduces neuronal activity, yet it can trigger spiking in this case. The mechanism for inhibition-induced spiking involves:

Inhibitory Input: Hyperpolarizes the neuron's membrane potential.
Deactivation of Inward Current: Low threshold calcium channels or hyperpolarization-activated cation channels become deactivated.
Rebound Depolarization: When the inhibitory input is removed, the neuron experiences rebound depolarization. This occurs because the previously de-inactivated ion channel is activated, allowing an influx of positive ions.
Action Potential Generation: Where the rebound depolarization is strong enough, can bring the membrane potential above the threshold and create an action potential.
Inhibition-induced spiking generates rhythmic patterns of activity in circuits responsible for locomotion and respiration. Additionally, this type of firing can help synchronize the activity of neural networks (Chapter 3), contributing to the coordination of the timing of neural processing. This type of firing pattern shows that an inhibitory signal is just as important as excitatory signaling.

Now, let’s enter the following parameters for a resonator:
a = 0.1
b = 0.26
c = -60
d = -1
I = 0

Remember, you must change the T variable in MATLAB to the appropriate row in the matrix you want to pull from and click run on the MATLAB script before running the Simulink model.

![image](https://github.com/user-attachments/assets/d1b85df3-688a-4700-b6af-e8f1ce402078)

The resonator feature occurs during T=0 through T=150. A resonator is a type of neuron that prefers to respond to inputs at certain frequencies. This means that they respond more strongly to inputs at their preferred frequency. Resonator neurons are important in various neural circuits where frequency tuning is essential, such as in the auditory system (Chapter 11), where neurons must respond selectively to specific sound frequencies. They also play roles in motor control and other neural processes that involve rhythmic or periodic activity.

That is the end of this lab example. You are encouraged to research different firing patterns that can be replicated using this model and try to use them in MATLAB and Simulink.

### Acknowledgment
We would like to express our sincere gratitude to the MATLAB Ambassador for creating the instructional YouTube video "Simulating a Neuron". This video has been invaluable in guiding us through implementing and understanding the Izhikevich neuron model using Simulink. The clear explanations and detailed walkthrough provided in the video have greatly enhanced our ability to model various neuronal firing patterns and apply these concepts in our lab exercises.
We also extend our thanks to the community of educators and content creators who continue to share their knowledge and expertise through platforms like YouTube, making advanced learning accessible and engaging for students and professionals worldwide.
Thank you for your contribution to computational neuroscience and educational outreach.

### References
E. M. Izhikevich, “Simple model of spiking neurons,” IEEE Trans. Neural Netw., vol. 14, no. 6, pp. 1569–1572, Nov. 2003, doi: 10.1109/TNN.2003.820440.

MATLAB Ambassador - Italy, Simulating a Neuron with Simulink, (Jun. 24, 2020). Accessed: Aug. 02, 2024. [Online Video]. Available: https://www.youtube.com/watch?v=NnZlGC1_I0M

# Chapter 12: Lab 2

## Overview

In this lab example, we will continue with our Neuron Example in Chapter 2 and focus on modifying parameters for Parkinson’s Disease. We will expand our understanding of the Hodgkin-Huxley (HH) model and how diseases influence the model. Specifically, we will simulate the differences in neural activity between a healthy brain and a brain affected by Parkinson's disease using the HH model. A graphical user interface (GUI) will allow us to input various parameters and observe their impact on the membrane potential of neurons.

## Requirements

- Python (tested with 3.8 and later)
- NEURON (neuron.yale.edu)
- Matplotlib
- Tkinter

## Steps

1. Go to the GitHub repository for this book: [https://github.com/bddupre92/Neurobook_BME_UND](https://github.com/bddupre92/Neurobook_BME_UND).
2. Navigate to Chapter 12 Lab Example 1.
3. Copy and paste the code into a script named `PDNeuronGUI.py`.

## Script Structure

### Define Constants and Parameters:
- `amp_value`: Amplitude of the current.
- `duration_value`: Duration of the current.
- `num_steps_value`: Number of steps in the simulation.
- `dend_nseg_value`: Number of segments in the dendrite.
- `cm_value`: Membrane capacitance.
- `Ra_value`: Axial resistance.
- `gbar_hh_value`: Maximum conductance for sodium, potassium, and leak channels.
- `v_init_value`: Initial membrane potential.

The GUI input will pop up with pre-populated values for everything. Run the initial example before modifying parameters to assess if this is a good starting point for the HH Model.

### Baseline Neural Activity Simulation:
Simulate baseline neural activity with the defined parameters.

### Post-Stimulation Neural Activity Simulation:
Simulate neural activity after modifying the parameters to represent Parkinson's disease.

### Visualization:
Plot the membrane potential for both the healthy and Parkinson's brain models.

## Explanation of the Figures

### Membrane Potential Comparison
- **Healthy Brain**: The membrane potential plot for the healthy brain shows the typical action potential characteristics.
- **Parkinson's Brain**: The membrane potential plot for the Parkinson's brain, modified by changing parameters like dendrite diameter, membrane capacitance, and ion channel conductance, shows how the action potential is affected by Parkinson's disease.

### Key Observations
- The differences in the membrane potential plots illustrate the impact of Parkinson's disease on neural activity.
- The modified parameters in the Parkinson's model result in changes to the amplitude and shape of the action potentials, demonstrating the disease's effect on neuronal excitability.

## Explanation of the Additional Figures

1. **Current vs. Membrane Potential**:
   - This plot shows how different amplitudes of the injected current affect the membrane potential for both healthy and Parkinson's models.
   - By varying the current amplitude, you can observe the threshold behavior and how the neurons respond differently in healthy versus Parkinson's conditions.

2. **Duration vs. Membrane Potential**:
   - This plot shows how the duration of the injected current affects the membrane potential.
   - By varying the duration, you can observe the impact on the action potential duration and how prolonged stimulation influences the neuron's behavior.

## Explanation of the Parameter Sensitivity Plots

1. **Membrane Capacitance (cm) Sensitivity**:
   - Shows how changes in membrane capacitance affect the membrane potential.
   - Higher capacitance can make the neuron less responsive, while lower capacitance makes it more responsive.

2. **Axial Resistance (Ra) Sensitivity**:
   - Illustrates the impact of axial resistance on the membrane potential.
   - Higher resistance slows down signal propagation, while lower resistance speeds it up.

3. **Sodium Conductance (gbar_na) Sensitivity**:
   - Displays how changes in sodium conductance influence the action potential.
   - Higher conductance increases excitability, making it easier to trigger action potentials.

4. **Potassium Conductance (gbar_k) Sensitivity**:
   - Demonstrates the effect of potassium conductance on repolarization.
   - Higher conductance leads to quicker repolarization, shortening the action potential duration.

5. **Leak Conductance (gbar_l) Sensitivity**:
   - Shows how variations in leak conductance affect the membrane potential.
   - Higher leak conductance stabilizes the resting membrane potential but reduces overall excitability.

These sensitivity plots help in understanding the robustness of the model and the significance of each parameter in influencing the membrane potential.

## Suggestions for Parameters to Modify

To explore the impact of different parameters on action potentials, you can modify the following inputs:

1. **Amplitude of Current (nA)**:
   - Higher amplitudes can increase the likelihood of triggering an action potential.
   - Lower amplitudes might not reach the threshold for an action potential.

2. **Duration of Current (ms)**:
   - Longer durations can sustain depolarization, potentially leading to multiple action potentials.
   - Shorter durations might only cause a brief depolarization without reaching the threshold.

3. **Membrane Capacitance (cm)**:
   - Increasing capacitance makes the membrane less responsive to voltage changes, slowing down action potential initiation.
   - Decreasing capacitance makes the membrane more responsive, speeding up action potential initiation.

4. **Axial Resistance (Ra)**:
   - Higher resistance can reduce the speed of signal propagation along the neuron.
   - Lower resistance can increase the speed of signal propagation.

5. **Sodium Conductance (gbar_na)**:
   - Increasing sodium conductance can enhance the neuron's excitability, making it easier to trigger action potentials.
   - Decreasing sodium conductance can reduce excitability.

6. **Potassium Conductance (gbar_k)**:
   - Increasing potassium conductance can lead to quicker repolarization and a shorter action potential duration.
   - Decreasing potassium conductance can prolong repolarization and action potential duration.

7. **Leak Conductance (gbar_l)**:
   - Higher leak conductance can stabilize the resting membrane potential but reduce overall excitability.
   - Lower leak conductance can increase excitability but may make the neuron more prone to spontaneous activity.

8. **Resting Membrane Potential (v_init)**:
   - A more negative resting potential (hyperpolarized) makes it harder to reach the threshold for an action potential.
   - A less negative resting potential (depolarized) makes it easier to reach the threshold.

## What the Output Means

- **Action Potential Amplitude**: Indicates the strength of the neural signal. Changes in amplitude can reflect alterations in ion channel conductance or membrane properties.
- **Action Potential Duration**: Affects the timing and pattern of neural signaling. Prolonged action potentials can indicate issues with ion channel kinetics.
- **Threshold**: The minimum membrane potential required to trigger an action potential. Changes in the threshold can indicate alterations in membrane excitability.
- **Repolarization Phase**: The phase during which the membrane potential returns to the resting state. Alterations in this phase can reflect changes in potassium conductance or other repolarizing mechanisms.

By systematically modifying these parameters, you can gain insights into how different factors contribute to the overall behavior of neurons in both healthy and diseased states. This understanding can help in developing targeted therapies for neurological disorders like Parkinson's disease.

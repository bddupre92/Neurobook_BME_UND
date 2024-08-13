# Chapter 7: Lab Example 2

## Laboratory Exercise: Exploring Electrical Stimulation on Neural Networks Using Python

### Overview

In this lab, we will simulate the effects of electrical stimulation on a neural network using Python. A graphical user interface (GUI) will be created to allow interactive experimentation with various parameters and observe how these changes affect neural activity. This hands-on approach will help students understand the dynamics of neural networks and the impact of different parameters on neural activity.

### Goals of the Lab

- Understand the basic structure and function of a neural network.
- Explore how electrical stimulation affects neural network activity.
- Learn how to create and interact with a GUI for scientific simulations.
- Analyze the impact of different parameters on neural network behavior, including the ratio of inhibitory neurons.

### Requirements

- Python (tested with 3.8 and later)
- Python libraries: `NumPy`, `Matplotlib`, `Tkinter`

### Steps

1. **Setting Up the Environment**
   - Install the necessary Python libraries if not already installed:
     ```bash
     !pip install numpy matplotlib tkinter
     ```

2. **Creating the Neural Network Simulation**
   - Define functions to create the neural network, apply electrical stimulation, and simulate neural activity.
   - Implement a function to simulate neural activity considering both excitatory and inhibitory neurons.

3. **Building the GUI**
   - Create a graphical user interface using Tkinter that allows users to input parameters such as network size, stimulation intensity, number of steps, stimulation position, and the ratio of inhibitory neurons.

4. **Running the Simulation**
   - Users will input the desired parameters and run the simulation through the GUI.
   - The simulation will display initial and final neural network activity using heatmaps.

### Interpretation of Results

- **Initial Neural Network Activity**: Shows the state of the neural network before stimulation, with only the neuron at the stimulation position activated.
- **Neural Network Activity After Stimulation**: Displays how the neural activity spreads from the initially stimulated neuron to its neighbors. The color intensity represents the level of activation, with higher values indicating more activity.

### Key Observations

- **Spread of Activation**: The stimulation spreads from the initially stimulated neuron to its neighbors, creating a pattern of activation influenced by the simulation parameters.
- **Effects of Inhibition**: Inhibitory neurons can significantly alter the pattern of activation, demonstrating how inhibition can dampen neural activity and create more complex patterns.

### Suggestions for Parameters to Modify

1. **Network Size**:
   - **Impact**: Increasing the network size allows for observing how the spread of activation scales with larger networks.
   - **Output**: Larger networks may show more complex patterns of activation and a broader spread of activity.

2. **Stimulation Intensity**:
   - **Impact**: Higher intensity can result in stronger activation spread.
   - **Output**: Increased stimulation intensity can lead to more neurons being activated, resulting in a more widespread and intense pattern of activity.

3. **Number of Steps**:
   - **Impact**: More steps can provide insights into the longer-term effects of stimulation.
   - **Output**: Additional steps allow for observing how the activation evolves over time, potentially showing sustained or diminishing activity.

4. **Stimulation Position**:
   - **Impact**: Changing the position can show the impact of stimulation at different network locations.
   - **Output**: Different stimulation positions can highlight how the network's structure and connectivity influence the spread of activation.

5. **Inhibitory Neurons Ratio**:
   - **Impact**: Varying the ratio of inhibitory neurons affects the balance between excitation and inhibition in the network.
   - **Output**:
     - **Low Ratio (e.g., 0.01)**: Minimal inhibition, broader and more intense spread of activity.
     - **High Ratio (e.g., 0.2)**: Significant inhibition, reduced activity, and more localized pattern of activation.

### Detailed Explanation of the Images

- **Image with Inhibitory Neurons Ratio at 0.01**:
  - **Observation**: The neural network activity after stimulation shows a broad spread of activation.
  - **Interpretation**: With a low ratio of inhibitory neurons, the inhibition is minimal, allowing for more neurons to become activated and maintain higher activity levels across the network.

- **Image with Inhibitory Neurons Ratio at 0.2**:
  - **Observation**: The neural network activity after stimulation is more localized, with reduced overall activity.
  - **Interpretation**: A higher ratio of inhibitory neurons increases the inhibition, damping the spread of activation and resulting in fewer neurons being activated. The overall activity is more subdued and confined to a smaller region.

By adjusting these parameters, students can explore the intricate dynamics of neural networks and understand the delicate balance between excitation and inhibition. This hands-on lab provides valuable insights into the behavior of neural systems and the potential implications for neurostimulation therapies.


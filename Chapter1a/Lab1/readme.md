# Synthetic Neuron Simulation with Arduino

This repository contains the code and instructions for simulating the behavior of a synthetic neuron using an Arduino microcontroller. The simulation is based on the Hodgkin-Huxley model, which describes how action potentials in neurons are initiated and propagated through the movement of ions across the cell membrane.

## Lab Overview

In this lab, you will:
1. Understand the Hodgkin-Huxley model and its application in simulating neuronal behavior.
2. Implement the Hodgkin-Huxley equations in Arduino code.
3. Simulate the behavior of a synthetic neuron and observe the output.
4. Use an oscilloscope to visualize the membrane potential signal.

## Materials Needed

- Arduino microcontroller
- Breadboard and connecting wires
- Resistors and LEDs (optional, for visual representation of the output)
- Computer with Arduino IDE installed
- Oscilloscope

## Key Concepts

### Hodgkin-Huxley Model

The Hodgkin-Huxley model is a set of nonlinear differential equations that describe the ionic mechanisms underlying the initiation and propagation of action potentials in neurons. The model includes variables for membrane potential (`V`), and gating variables (`n`, `m`, and `h`) which represent the probability of ion channels being open or closed.

- **Membrane Potential (`V`)**: The voltage difference across the neuron's membrane.
- **Gating Variables (`n`, `m`, `h`)**: Variables representing the state of potassium (`n`), sodium activation (`m`), and sodium inactivation (`h`) gates.

### Equations

The model is defined by the following key equations:

1. **Membrane Potential (`V`)**: Describes the change in membrane potential over time based on ion conductances and injected current.
2. **Gating Variables (`n`, `m`, `h`)**: Describe the dynamics of the gating variables, which affect the conductance of ion channels.

## Procedure

### Setup the Arduino Environment

1. Connect the Arduino to your computer.
2. Open the Arduino IDE and create a new sketch.

### Initialize Variables and Constants

1. Define initial values for the gating variables (`n1`, `m1`, `h1`) and membrane potential (`V1`).
2. Define constants such as membrane capacitance (`C`), maximum conductances for potassium (`g_k_max`), sodium (`g_Na_max`), and leak channels (`g_L`), and equilibrium potentials for potassium (`E_K`), sodium (`E_Na`), and leak channels (`E_L`).

### Implement the Hodgkin-Huxley Equations

1. Write functions to calculate the derivatives of the gating variables (`n_prime`, `m_prime`, `h_prime`).
2. Update the state of the neuron in the `loop` function by calculating new values for the gating variables and membrane potential.

### Output the Membrane Potential

1. Use the `analogWrite` function to output the membrane potential to pin 3 on the Arduino.
2. Connect pin 3 to the oscilloscope to visualize the signal.

### Connecting the Oscilloscope

1. Connect the ground probe of the oscilloscope to the ground pin on the Arduino.
2. Connect the signal probe of the oscilloscope to pin 3 of the Arduino.
3. Turn on the oscilloscope and set it to the appropriate voltage and time scales to visualize the signal from the Arduino.

## Arduino Code

```cpp
// Synthetic Arduino neuron simulation

// Initial values for gating variables and membrane potential
double n1 = 0.0003;
double m1 = 0.0011;
double h1 = 0.9998;
double V1 = -10;

// Constants for the neuron model
double C = 1;                // Membrane capacitance
double g_k_max = 36;         // Maximum conductance for potassium channels
double g_Na_max = 120;       // Maximum conductance for sodium channels
double g_L = 0.3;            // Conductance for leak channels
double E_K = -12;            // Potassium equilibrium potential
double E_Na = 115;           // Sodium equilibrium potential
double E_L = 10.613;         // Leak equilibrium potential
double d_t = 0.04;           // Time step for the simulation
double I_inj = 10;           // Injected current

// Variables to store the current state of the neuron
double n, m, h, V;
double n_new, m_new, h_new, V_new;

void setup() {
  // Setup code to run once
  pinMode(3, OUTPUT);         // Set pin 3 as output
  Serial.begin(9600);         // Begin serial communication at 9600 baud rate
  
  // Initialize the state variables
  n = n1;
  m = m1;
  h = h1;
  V = V1;
}

void loop() {
  // Main loop for the simulation

  // Calculate the derivatives of the gating variables
  double dn = n_prime(n, -V);
  double dm = m_prime(m, -V);
  double dh = h_prime(h, -V);

  // Update the gating variables
  n_new = n + dn * d_t;
  m_new = m + dm * d_t;
  h_new = h + dh * d_t;

  // Calculate the change in membrane potential
  double dV = 1 / C * (-1 * g_k_max * pow(n, 4) * (V - E_K) 
                     - g_Na_max * pow(m, 3) * h * (V - E_Na) 
                     - g_L * (V - E_L) + I_inj);
  V_new = V + dV * d_t;

  // Output the updated membrane potential to pin 3
  analogWrite(3, V_new + 20);

  // Update the state variables for the next iteration
  n = n_new;
  m = m_new;
  h = h_new;
  V = V_new;
}

// Function to calculate the derivative of the n gating variable
double n_prime(double n, double V) {
  double k_1 = (0.01 * (V + 10)) / (exp((V + 10) / 10) - 1);
  double k_2 = 0.125 * exp(V / 80);
  double dn = k_1 - (k_1 + k_2) * n;
  return dn;
}

// Function to calculate the derivative of the m gating variable
double m_prime(double m, double V) {
  double k_1 = 0.1 * (V + 25) / (exp((V + 25) / 10) - 1);
  double k_2 = 4 * exp(V / 18);
  double dm = k_1 - (k_1 + k_2) * m;
  return dm;
}

// Function to calculate the derivative of the h gating variable
double h_prime(double h, double V) {
  double k_1 = 0.07 * exp(V / 20);
  double k_2 = 1 / (exp((V + 30) / 10) + 1);
  double dh = k_1 - (k_1 + k_2) * h;
  return dh;
}

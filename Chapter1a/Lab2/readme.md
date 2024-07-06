Lab Add-On: Simulating the Action Potential Threshold with a Potentiometer
Overview
In this add-on to the synthetic neuron simulation lab, you will incorporate a potentiometer to dynamically adjust the action potential threshold. This enhancement allows you to explore how changing the threshold affects the neuron's behavior.

Objectives
Integrate a potentiometer into the existing Arduino setup.
Modify the code to read the potentiometer value and use it to adjust the action potential threshold.
Observe the effects of changing the threshold on the membrane potential using an oscilloscope.
Materials Needed
Arduino microcontroller
Breadboard and connecting wires
Potentiometer (10kΩ recommended)
Resistors and LEDs (optional, for visual representation of the output)
Computer with Arduino IDE installed
Oscilloscope
Setup
Connect the Potentiometer:

Connect one outer pin of the potentiometer to the 5V pin on the Arduino.
Connect the other outer pin to the GND pin.
Connect the middle pin (wiper) to an analog input pin on the Arduino (e.g., A0).
Modify the Arduino Code:

Update the Arduino code to read the potentiometer value and use it to adjust the action potential threshold. The potentiometer will simulate the action potential threshold by influencing the injected current (I_inj).

Arduino Code
cpp
Copy code
// Synthetic Arduino neuron simulation with adjustable threshold

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
  // Read the potentiometer value (0-1023)
  int potValue = analogRead(A0);
  
  // Map the potentiometer value to a suitable range for I_inj (e.g., 0 to 20)
  double I_inj = map(potValue, 0, 1023, 0, 20);

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
Connecting the Oscilloscope
Connect the ground probe of the oscilloscope to the ground pin on the Arduino.
Connect the signal probe of the oscilloscope to pin 3 of the Arduino.
Turn on the oscilloscope and set it to the appropriate voltage and time scales to visualize the signal from the Arduino.
Conclusion
By adding a potentiometer to the setup, you can dynamically adjust the action potential threshold and observe how this change affects the neuron's behavior. This enhancement provides a more interactive and hands-on approach to studying the dynamics of neurons and the principles of bioelectricity. Using the oscilloscope allows you to visualize the changes in membrane potential in real-time, further enhancing your understanding of neuronal activity.

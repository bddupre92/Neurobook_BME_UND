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

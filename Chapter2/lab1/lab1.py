import numpy as np
import matplotlib.pyplot as plt

# Define gating variables function
def gating_variables(V, m, h, n):
    # Gating variables
    alpha_m = 0.1 * ((25 - V) / (np.exp((25 - V) / 10) - 1))
    beta_m = 4.0 * np.exp(-V / 18)
    alpha_h = 0.07 * np.exp(-V / 20)
    beta_h = 1.0 / (np.exp((30 - V) / 10) + 1)
    alpha_n = 0.01 * ((10 - V) / (np.exp((10 - V) / 10) - 1))
    beta_n = 0.125 * np.exp(-V / 80)
    
    dm = alpha_m * (1 - m) - beta_m * m
    dh = alpha_h * (1 - h) - beta_h * h
    dn = alpha_n * (1 - n) - beta_n * n
    
    return dm, dh, dn

# Parameters
C_m = 1.0   # Membrane capacitance, in uF/cm^2
g_Na = 120.0  # Maximum conductances, in mS/cm^2
g_K = 36.0
g_L = 0.3
E_Na = 50.0  # Reversal potentials, in mV
E_K = -77.0
E_L = -54.387

# Time vector
t = np.arange(0, 50, 0.01)  # Time, in ms

# External current
I_ext = np.zeros(len(t))
I_ext[1000:4000] = 10  # Inject a current pulse between 10 ms and 40 ms

# Initial values
V = -65.0  # Initial membrane potential, in mV
m = 0.0529  # Initial values for gating variables
h = 0.596
n = 0.3177

# Preallocate vectors for efficiency
V_trace = np.zeros(len(t))
m_trace = np.zeros(len(t))
h_trace = np.zeros(len(t))
n_trace = np.zeros(len(t))

for i in range(len(t)):
    # Record values
    V_trace[i] = V
    m_trace[i] = m
    h_trace[i] = h
    n_trace[i] = n
    
    # Calculate conductances
    g_Na_t = g_Na * m**3 * h
    g_K_t = g_K * n**4
    
    # Calculate currents
    I_Na = g_Na_t * (V - E_Na)
    I_K = g_K_t * (V - E_K)
    I_L = g_L * (V - E_L)
    
    # Update membrane potential
    V += (I_ext[i] - (I_Na + I_K + I_L)) / C_m * 0.01
    
    # Update gating variables using Euler method
    dm, dh, dn = gating_variables(V, m, h, n)
    m += dm * 0.01
    h += dh * 0.01
    n += dn * 0.01

# Plot results
plt.figure(figsize=(10, 8))

plt.subplot(2, 1, 1)
plt.plot(t, V_trace)
plt.title('Membrane Potential')
plt.xlabel('Time (ms)')
plt.ylabel('V_m (mV)')

plt.subplot(2, 1, 2)
plt.plot(t, I_ext)
plt.title('Injected Current')
plt.xlabel('Time (ms)')
plt.ylabel('I_{ext} (\muA/cm^2)')

plt.tight_layout()
plt.show()

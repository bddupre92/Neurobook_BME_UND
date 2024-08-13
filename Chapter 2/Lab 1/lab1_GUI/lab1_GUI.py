import numpy as np
import matplotlib.pyplot as plt
from tkinter import Tk, Label, Entry, Button

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

def simulate():
    # Get user inputs
    C_m = float(C_m_entry.get())
    g_Na = float(g_Na_entry.get())
    g_K = float(g_K_entry.get())
    g_L = float(g_L_entry.get())
    E_Na = float(E_Na_entry.get())
    E_K = float(E_K_entry.get())
    E_L = float(E_L_entry.get())
    pulse_start = int(pulse_start_entry.get())
    pulse_end = int(pulse_end_entry.get())
    pulse_amplitude = float(pulse_amplitude_entry.get())

    # Time vector
    t = np.arange(0, 50, 0.01)  # Time, in ms

    # External current
    I_ext = np.zeros(len(t))
    I_ext[pulse_start*100:pulse_end*100] = pulse_amplitude  # Inject a current pulse between pulse_start ms and pulse_end ms

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

# Create GUI window
root = Tk()
root.title("Hodgkin-Huxley Neuron Model")

# Create labels and entry widgets for user input
Label(root, text="C_m (uF/cm^2):").grid(row=0, column=0)
C_m_entry = Entry(root)
C_m_entry.grid(row=0, column=1)
C_m_entry.insert(0, "1.0")

Label(root, text="g_Na (mS/cm^2):").grid(row=1, column=0)
g_Na_entry = Entry(root)
g_Na_entry.grid(row=1, column=1)
g_Na_entry.insert(0, "120.0")

Label(root, text="g_K (mS/cm^2):").grid(row=2, column=0)
g_K_entry = Entry(root)
g_K_entry.grid(row=2, column=1)
g_K_entry.insert(0, "36.0")

Label(root, text="g_L (mS/cm^2):").grid(row=3, column=0)
g_L_entry = Entry(root)
g_L_entry.grid(row=3, column=1)
g_L_entry.insert(0, "0.3")

Label(root, text="E_Na (mV):").grid(row=4, column=0)
E_Na_entry = Entry(root)
E_Na_entry.grid(row=4, column=1)
E_Na_entry.insert(0, "50.0")

Label(root, text="E_K (mV):").grid(row=5, column=0)
E_K_entry = Entry(root)
E_K_entry.grid(row=5, column=1)
E_K_entry.insert(0, "-77.0")

Label(root, text="E_L (mV):").grid(row=6, column=0)
E_L_entry = Entry(root)
E_L_entry.grid(row=6, column=1)
E_L_entry.insert(0, "-54.387")

Label(root, text="Pulse Start (ms):").grid(row=7, column=0)
pulse_start_entry = Entry(root)
pulse_start_entry.grid(row=7, column=1)
pulse_start_entry.insert(0, "10")

Label(root, text="Pulse End (ms):").grid(row=8, column=0)
pulse_end_entry = Entry(root)
pulse_end_entry.grid(row=8, column=1)
pulse_end_entry.insert(0, "40")

Label(root, text="Pulse Amplitude (\u03BCA/cm^2):").grid(row=9, column=0)
pulse_amplitude_entry = Entry(root)
pulse_amplitude_entry.grid(row=9, column=1)
pulse_amplitude_entry.insert(0, "10.0")

# Button to run simulation
Button(root, text="Simulate", command=simulate).grid(row=10, columnspan=2)

root.mainloop()

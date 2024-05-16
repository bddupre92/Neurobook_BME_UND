import numpy as np
import matplotlib.pyplot as plt
from tkinter import Tk, Label, Entry, Button

def heaviside(x):
    return np.heaviside(x, 1)

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
    C_m_val = float(C_m_entry.get())
    g_Na_val = float(g_Na_entry.get())
    g_K_val = float(g_K_entry.get())
    g_L_val = float(g_L_entry.get())
    E_Na_val = float(E_Na_entry.get())
    E_K_val = float(E_K_entry.get())
    E_L_val = float(E_L_entry.get())
    tau_syn_val = float(tau_syn_entry.get())
    g_syn_val = float(g_syn_entry.get())
    pulse_start_val = int(pulse_start_entry.get())
    pulse_end_val = int(pulse_end_entry.get())
    pulse_amplitude_val = float(pulse_amplitude_entry.get())

    # Reversal potential for synaptic current
    E_syn = 0

    # Time vector
    t = np.arange(0, 100, 0.01)  # Time, in ms

    # External current for neuron 1
    I_ext = np.zeros(len(t))
    I_ext[pulse_start_val*100:pulse_end_val*100] = pulse_amplitude_val

    # Initial values
    V1 = -65.0
    V2 = -65.0
    m1 = 0.0529
    h1 = 0.596
    n1 = 0.3177
    m2 = 0.0529
    h2 = 0.596
    n2 = 0.3177
    s = 0

    # Preallocate vectors for efficiency
    V1_trace = np.zeros(len(t))
    V2_trace = np.zeros(len(t))
    s_trace = np.zeros(len(t))

    for i in range(len(t)):
        V1_trace[i] = V1
        V2_trace[i] = V2
        s_trace[i] = s

        g_Na_t1 = g_Na_val * m1**3 * h1
        g_K_t1 = g_K_val * n1**4
        g_Na_t2 = g_Na_val * m2**3 * h2
        g_K_t2 = g_K_val * n2**4

        I_Na1 = g_Na_t1 * (V1 - E_Na_val)
        I_K1 = g_K_t1 * (V1 - E_K_val)
        I_L1 = g_L_val * (V1 - E_L_val)
        I_syn1 = g_syn_val * s * (V1 - E_syn)

        I_Na2 = g_Na_t2 * (V2 - E_Na_val)
        I_K2 = g_K_t2 * (V2 - E_K_val)
        I_L2 = g_L_val * (V2 - E_L_val)

        V1 += (I_ext[i] - (I_Na1 + I_K1 + I_L1 + I_syn1)) / C_m_val * 0.01
        V2 += (- (I_Na2 + I_K2 + I_L2)) / C_m_val * 0.01

        dm1, dh1, dn1 = gating_variables(V1, m1, h1, n1)
        dm2, dh2, dn2 = gating_variables(V2, m2, h2, n2)
        m1 += dm1 * 0.01
        h1 += dh1 * 0.01
        n1 += dn1 * 0.01
        m2 += dm2 * 0.01
        h2 += dh2 * 0.01
        n2 += dn2 * 0.01

        s += ((1 - s) / tau_syn_val) * heaviside(V1 - -20) - s / tau_syn_val * 0.01

    # Plot results
    plt.figure(figsize=(10, 8))
    plt.subplot(3, 1, 1)
    plt.plot(t, V1_trace)
    plt.title('Membrane Potential of Neuron 1')
    plt.xlabel('Time (ms)')
    plt.ylabel('V_m (mV)')

    plt.subplot(3, 1, 2)
    plt.plot(t, V2_trace)
    plt.title('Membrane Potential of Neuron 2')
    plt.xlabel('Time (ms)')
    plt.ylabel('V_m (mV)')

    plt.subplot(3, 1, 3)
    plt.plot(t, s_trace)
    plt.title('Synaptic Gating Variable')
    plt.xlabel('Time (ms)')
    plt.ylabel('s')

    plt.tight_layout()
    plt.show()

# Create GUI window
root = Tk()
root.title("Hodgkin-Huxley Network Simulation")

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

Label(root, text="Synaptic Conductance (mS/cm^2):").grid(row=7, column=0)
g_syn_entry = Entry(root)
g_syn_entry.grid(row=7, column=1)
g_syn_entry.insert(0, "0.1")

Label(root, text="Synaptic Time Constant (ms):").grid(row=8, column=0)
tau_syn_entry = Entry(root)
tau_syn_entry.grid(row=8, column=1)
tau_syn_entry.insert(0, "10")

Label(root, text="Pulse Start (ms):").grid(row=9, column=0)
pulse_start_entry = Entry(root)
pulse_start_entry.grid(row=9, column=1)
pulse_start_entry.insert(0, "10")

Label(root, text="Pulse End (ms):").grid(row=10, column=0)
pulse_end_entry = Entry(root)
pulse_end_entry.grid(row=10, column=1)
pulse_end_entry.insert(0, "40")

Label(root, text="Pulse Amplitude (\u03BCA/cm^2):").grid(row=11, column=0)
pulse_amplitude_entry = Entry(root)
pulse_amplitude_entry.grid(row=11, column=1)
pulse_amplitude_entry.insert(0, "10")

# Add a button to trigger the simulation
Button(root, text="Simulate", command=simulate).grid(row=12, columnspan=2)

root.mainloop()

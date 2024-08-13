import numpy as np
from neuron import h, gui
import matplotlib.pyplot as plt
from tkinter import Tk, Label, Entry, Button, messagebox

# Create dendrite and soma sections
dend = h.Section(name='dend')
dend.L = 100  # Set the length of the dendrite
dend.diam = 10  # Set the diameter of the dendrite

soma = h.Section(name='soma')
soma.L = 20  # Set the length of the soma
soma.diam = 20  # Set the diameter of the soma

# Connect dendrite to soma
dend.connect(soma(1))

# Insert Hodgkin-Huxley channels
for sec in [soma, dend]:
    sec.insert('hh')

# Function to run simulation for healthy brain model
def run_healthy_simulation(amp_value, duration_value, num_steps_value, dend_nseg_value, cm_value, Ra_value, gbar_hh_value, v_init_value):
    # Set membrane properties
    for sec in [soma, dend]:
        sec.cm = cm_value
        sec.Ra = Ra_value
        for seg in sec:
            seg.hh.gnabar = gbar_hh_value[0]
            seg.hh.gkbar = gbar_hh_value[1]
            seg.hh.gl = gbar_hh_value[2]
    
    # Create stimulation object
    stim = h.IClamp(soma(0.5))  # Apply the stimulation to the soma
    stim.dur = duration_value

    # Recording vectors
    v_vec = h.Vector()  # Membrane potential vector for soma
    t_vec = h.Vector()  # Time stamp vector
    v_vec.record(soma(0.5)._ref_v)
    t_vec.record(h._ref_t)

    # Stimulation parameters
    stim.amp = amp_value

    # Run initial simulation
    h.tstop = duration_value + 10  # Ensure enough time for the stimulation
    h.finitialize(v_init_value)
    h.run()

    # Store results
    return np.array(t_vec), np.array(v_vec)

# Function to run simulation for Parkinson's model
def run_parkinsons_simulation(amp_value, duration_value, num_steps_value, dend_nseg_value, cm_value, Ra_value, gbar_hh_value, v_init_value):
    # Modify the dendrite to simulate Parkinson's (e.g., reduce the diameter)
    dend.diam = 5

    # Set membrane properties
    for sec in [soma, dend]:
        sec.cm = cm_value * 1.2  # Example modification for Parkinson's
        sec.Ra = Ra_value * 1.5  # Example modification for Parkinson's
        for seg in sec:
            seg.hh.gnabar = gbar_hh_value[0] * 0.8
            seg.hh.gkbar = gbar_hh_value[1] * 0.8
            seg.hh.gl = gbar_hh_value[2] * 1.2

    # Create stimulation object
    stim = h.IClamp(soma(0.5))  # Apply the stimulation to the soma
    stim.dur = duration_value

    # Recording vectors
    v_vec = h.Vector()  # Membrane potential vector for soma
    t_vec = h.Vector()  # Time stamp vector
    v_vec.record(soma(0.5)._ref_v)
    t_vec.record(h._ref_t)

    # Stimulation parameters
    stim.amp = amp_value

    # Run initial simulation
    h.tstop = duration_value + 10  # Ensure enough time for the stimulation
    h.finitialize(v_init_value)
    h.run()

    # Restore dendrite properties
    dend.diam = 10

    # Store results
    return np.array(t_vec), np.array(v_vec)

# Function to run simulation based on user input
def run_simulation():
    try:
        amp_value = float(amp_entry.get())
        duration_value = float(duration_entry.get())
        num_steps_value = int(num_steps_entry.get())
        dend_nseg_value = int(nseg_entry.get())
        cm_value = float(cm_entry.get())
        Ra_value = float(Ra_entry.get())
        gbar_na_value = float(gbar_na_entry.get())
        gbar_k_value = float(gbar_k_entry.get())
        gbar_l_value = float(gbar_l_entry.get())
        v_init_value = float(v_init_entry.get())

        gbar_hh_value = [gbar_na_value, gbar_k_value, gbar_l_value]

        # Run healthy and Parkinson's simulations
        t_healthy, v_healthy = run_healthy_simulation(amp_value, duration_value, num_steps_value, dend_nseg_value, cm_value, Ra_value, gbar_hh_value, v_init_value)
        t_parkinsons, v_parkinsons = run_parkinsons_simulation(amp_value, duration_value, num_steps_value, dend_nseg_value, cm_value, Ra_value, gbar_hh_value, v_init_value)

        # Plot results
        plt.figure(figsize=(10, 6))
        plt.plot(t_healthy, v_healthy, label='Healthy Brain', color='blue')
        plt.plot(t_parkinsons, v_parkinsons, label='Parkinson\'s Brain', color='red')
        plt.xlabel('Time (ms)')
        plt.ylabel('Membrane Potential (mV)')
        plt.title('Membrane Potential Comparison')
        plt.legend()
        plt.show()

        # Additional plot: Current vs. Membrane Potential
        currents = np.linspace(amp_value / 10, amp_value * 2, 10)
        plt.figure(figsize=(10, 6))
        for i, current in enumerate(currents):
            t_h, v_h = run_healthy_simulation(current, duration_value, num_steps_value, dend_nseg_value, cm_value, Ra_value, gbar_hh_value, v_init_value)
            t_p, v_p = run_parkinsons_simulation(current, duration_value, num_steps_value, dend_nseg_value, cm_value, Ra_value, gbar_hh_value, v_init_value)
            plt.plot(t_h, v_h, color='blue', alpha=0.1 + 0.9 * (i / len(currents)))
            plt.plot(t_p, v_p, color='red', alpha=0.1 + 0.9 * (i / len(currents)))
        plt.xlabel('Time (ms)')
        plt.ylabel('Membrane Potential (mV)')
        plt.title('Current vs. Membrane Potential')
        plt.show()

        # Additional plot: Duration vs. Membrane Potential
        durations = np.linspace(duration_value / 10, duration_value * 2, 10)
        plt.figure(figsize=(10, 6))
        for i, duration in enumerate(durations):
            t_h, v_h = run_healthy_simulation(amp_value, duration, num_steps_value, dend_nseg_value, cm_value, Ra_value, gbar_hh_value, v_init_value)
            t_p, v_p = run_parkinsons_simulation(amp_value, duration, num_steps_value, dend_nseg_value, cm_value, Ra_value, gbar_hh_value, v_init_value)
            plt.plot(t_h, v_h, color='blue', alpha=0.1 + 0.9 * (i / len(durations)))
            plt.plot(t_p, v_p, color='red', alpha=0.1 + 0.9 * (i / len(durations)))
        plt.xlabel('Time (ms)')
        plt.ylabel('Membrane Potential (mV)')
        plt.title('Duration vs. Membrane Potential')
        plt.show()

        # Parameter Sensitivity Analysis
        def plot_sensitivity(parameter, values, label, default_value):
            plt.figure(figsize=(10, 6))
            for i, value in enumerate(values):
                kwargs = {
                    'amp_value': amp_value,
                    'duration_value': duration_value,
                    'num_steps_value': num_steps_value,
                    'dend_nseg_value': dend_nseg_value,
                    'cm_value': cm_value if parameter != 'cm' else value,
                    'Ra_value': Ra_value if parameter != 'Ra' else value,
                    'gbar_hh_value': gbar_hh_value if parameter not in ['gbar_na', 'gbar_k', 'gbar_l'] else
                    [value if parameter == 'gbar_na' else gbar_hh_value[0],
                     value if parameter == 'gbar_k' else gbar_hh_value[1],
                     value if parameter == 'gbar_l' else gbar_hh_value[2]],
                    'v_init_value': v_init_value
                }
                t_h, v_h = run_healthy_simulation(**kwargs)
                t_p, v_p = run_parkinsons_simulation(**kwargs)
                plt.plot(t_h, v_h, color='blue', alpha=0.1 + 0.9 * (i / len(values)))
                plt.plot(t_p, v_p, color='red', alpha=0.1 + 0.9 * (i / len(values)))
            plt.xlabel('Time (ms)')
            plt.ylabel('Membrane Potential (mV)')
            plt.title(f'{label} Sensitivity')
            plt.show()

        cm_values = np.linspace(cm_value / 2, cm_value * 2, 10)
        Ra_values = np.linspace(Ra_value / 2, Ra_value * 2, 10)
        gbar_na_values = np.linspace(gbar_na_value / 2, gbar_na_value * 2, 10)
        gbar_k_values = np.linspace(gbar_k_value / 2, gbar_k_value * 2, 10)
        gbar_l_values = np.linspace(gbar_l_value / 2, gbar_l_value * 2, 10)

        plot_sensitivity('cm', cm_values, 'Membrane Capacitance (cm)', cm_value)
        plot_sensitivity('Ra', Ra_values, 'Axial Resistance (Ra)', Ra_value)
        plot_sensitivity('gbar_na', gbar_na_values, 'Sodium Conductance (gbar_na)', gbar_na_value)
        plot_sensitivity('gbar_k', gbar_k_values, 'Potassium Conductance (gbar_k)', gbar_k_value)
        plot_sensitivity('gbar_l', gbar_l_values, 'Leak Conductance (gbar_l)', gbar_l_value)

    except ValueError:
        messagebox.showerror("Error", "Invalid input. Please enter numerical values.")

# Create GUI window
root = Tk()
root.title("HH Model Simulation")

# Labels and entries for user input with default values
amp_label = Label(root, text="Amplitude of Current (nA):")
amp_label.grid(row=0, column=0, padx=10, pady=5)
amp_entry = Entry(root)
amp_entry.insert(0, "1")  # Default value
amp_entry.grid(row=0, column=1, padx=10, pady=5)

duration_label = Label(root, text="Duration of Current (ms):")
duration_label.grid(row=1, column=0, padx=10, pady=5)
duration_entry = Entry(root)
duration_entry.insert(0, "5")  # Default value
duration_entry.grid(row=1, column=1, padx=10, pady=5)

num_steps_label = Label(root, text="Number of Steps:")
num_steps_label.grid(row=2, column=0, padx=10, pady=5)
num_steps_entry = Entry(root)
num_steps_entry.insert(0, "5")  # Default value
num_steps_entry.grid(row=2, column=1, padx=10, pady=5)

nseg_label = Label(root, text="Number of Segments (nseg):")
nseg_label.grid(row=3, column=0, padx=10, pady=5)
nseg_entry = Entry(root)
nseg_entry.insert(0, "10")  # Default value
nseg_entry.grid(row=3, column=1, padx=10, pady=5)

cm_label = Label(root, text="Membrane Capacitance (cm):")
cm_label.grid(row=4, column=0, padx=10, pady=5)
cm_entry = Entry(root)
cm_entry.insert(0, "1")  # Default value
cm_entry.grid(row=4, column=1, padx=10, pady=5)

Ra_label = Label(root, text="Axial Resistance (Ra):")
Ra_label.grid(row=5, column=0, padx=10, pady=5)
Ra_entry = Entry(root)
Ra_entry.insert(0, "100")  # Default value
Ra_entry.grid(row=5, column=1, padx=10, pady=5)

gbar_na_label = Label(root, text="Na Conductance (gbar_na):")
gbar_na_label.grid(row=6, column=0, padx=10, pady=5)
gbar_na_entry = Entry(root)
gbar_na_entry.insert(0, "0.12")  # Default value
gbar_na_entry.grid(row=6, column=1, padx=10, pady=5)

gbar_k_label = Label(root, text="K Conductance (gbar_k):")
gbar_k_label.grid(row=7, column=0, padx=10, pady=5)
gbar_k_entry = Entry(root)
gbar_k_entry.insert(0, "0.036")  # Default value
gbar_k_entry.grid(row=7, column=1, padx=10, pady=5)

gbar_l_label = Label(root, text="Leak Conductance (gbar_l):")
gbar_l_label.grid(row=8, column=0, padx=10, pady=5)
gbar_l_entry = Entry(root)
gbar_l_entry.insert(0, "0.0003")  # Default value
gbar_l_entry.grid(row=8, column=1, padx=10, pady=5)

v_init_label = Label(root, text="Resting Membrane Potential (v_init):")
v_init_label.grid(row=9, column=0, padx=10, pady=5)
v_init_entry = Entry(root)
v_init_entry.insert(0, "-65")  # Default value
v_init_entry.grid(row=9, column=1, padx=10, pady=5)

# Button to run simulation
run_button = Button(root, text="Run Simulation", command=run_simulation)
run_button.grid(row=10, columnspan=2, padx=10, pady=10)

# Run GUI
root.mainloop()

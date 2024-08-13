import numpy as np
from neuron import h, gui
import matplotlib.pyplot as plt
from tkinter import Tk, Label, Entry, Button, messagebox

# Function to run simulation based on user input
def run_simulation():
    try:
        amp_value = float(amp_entry.get())
        duration_value = float(duration_entry.get())
        num_steps_value = int(num_steps_entry.get())
        dend_nseg_value = int(nseg_entry.get())

        dend_length_value = float(dend_length_entry.get())
        dend_diam_value = float(dend_diam_entry.get())
        soma_length_value = float(soma_length_entry.get())
        soma_diam_value = float(soma_diam_entry.get())

        # Create dendrite and soma sections
        dend = h.Section(name='dend')
        soma = h.Section(name='soma')

        # Set dendrite and soma sizes
        dend.L = dend_length_value
        dend.diam = dend_diam_value
        soma.L = soma_length_value
        soma.diam = soma_diam_value

        # Connect dendrite to soma
        dend.connect(soma(1))

        # Insert Hodgkin-Huxley channels
        soma.insert('hh')
        for seg in soma:
            seg.hh.gnabar = 0.12  # Sodium conductance in S/cm2
            seg.hh.gkbar = 0.036  # Potassium conductance in S/cm2
            seg.hh.gl = 0.0003    # Leak conductance in S/cm2
            seg.hh.el = -54.3     # Reversal potential in mV

        dend.insert('pas')
        for seg in dend:
            seg.pas.g = 0.001  # Passive conductance in S/cm2
            seg.pas.e = -65    # Leak reversal potential mV

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
        h.finitialize(-65)
        h.run()

        # Plot membrane potential
        plt.figure(figsize=(8, 4))
        plt.plot(t_vec, v_vec)
        plt.xlabel('time (ms)')
        plt.ylabel('mV')
        plt.title('Membrane Potential of Soma')
        plt.show()

        # Plot dendrite activity
        dend_v_vec = h.Vector()  # Membrane potential vector for dendrite
        dend_v_vec.record(dend(0.5)._ref_v)
        plt.figure(figsize=(8, 4))
        for i in np.linspace(amp_value, amp_value * num_steps_value, num_steps_value):
            stim.amp = i
            h.finitialize(-65)
            h.run()
            soma_plot, = plt.plot(t_vec, v_vec, color='black')
            dend_plot, = plt.plot(t_vec, dend_v_vec, color='red')
        plt.legend([soma_plot, dend_plot], ['soma', 'dend'])
        plt.xlabel('time (ms)')
        plt.ylabel('mV')
        plt.title('Comparison of Soma and Dendrite Activity')
        plt.show()

        # Plot effects of nseg on dendritic signal
        plt.figure(figsize=(8, 4))
        ref_v = []
        ref_dend_v = []
        soma_hires_plots = []
        dend_hires_plots = []
        soma_lowres_plots = []
        dend_lowres_plots = []

        # High resolution
        dend.nseg = dend_nseg_value
        for i in np.linspace(amp_value, amp_value * num_steps_value, num_steps_value):
            stim.amp = i
            h.finitialize(-65)
            h.run()
            soma_hires, = plt.plot(t_vec, v_vec, color='blue', linestyle='--')
            dend_hires, = plt.plot(t_vec, dend_v_vec, color='green', linestyle='--')
            soma_hires_plots.append(soma_hires)
            dend_hires_plots.append(dend_hires)
            ref_v_vec = np.zeros_like(v_vec)
            v_vec.to_python(ref_v_vec)
            ref_v.append(ref_v_vec)
            ref_dend_v_vec = np.zeros_like(dend_v_vec)
            dend_v_vec.to_python(ref_dend_v_vec)
            ref_dend_v.append(ref_dend_v_vec)

        # Low resolution
        dend.nseg = 3  # Set low resolution
        err = 0
        idx = 0
        for i in np.arange(amp_value, amp_value * num_steps_value + 0.1, amp_value):
            stim.amp = i
            h.finitialize(-65)
            h.run()
            soma_lowres, = plt.plot(t_vec, v_vec, color='black', linestyle='-')
            dend_lowres, = plt.plot(t_vec, dend_v_vec, color='red', linestyle='-')
            soma_lowres_plots.append(soma_lowres)
            dend_lowres_plots.append(dend_lowres)
            err += np.mean(np.abs(np.subtract(ref_v[idx], v_vec)))
            err += np.mean(np.abs(np.subtract(ref_dend_v[idx], dend_v_vec)))
            idx += 1

        err /= idx
        err /= 2  # Since we have a soma and dend vec
        messagebox.showinfo("Average Error", "Average error: {:.2f}".format(err))

        plt.legend([soma_lowres_plots[0], dend_lowres_plots[0], soma_hires_plots[0], dend_hires_plots[0]],
                   ['soma low-res', 'dend low-res', 'soma hi-res', 'dend hi-res'])
        plt.xlabel('time (ms)')
        plt.ylabel('mV')
        plt.title('Effect of nseg on Dendritic Signal')
        plt.show()

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
nseg_entry.insert(0, "50")  # Default value (set higher for high-resolution)
nseg_entry.grid(row=3, column=1, padx=10, pady=5)

dend_length_label = Label(root, text="Dendrite Length (µm):")
dend_length_label.grid(row=4, column=0, padx=10, pady=5)
dend_length_entry = Entry(root)
dend_length_entry.insert(0, "100")  # Default value
dend_length_entry.grid(row=4, column=1, padx=10, pady=5)

dend_diam_label = Label(root, text="Dendrite Diameter (µm):")
dend_diam_label.grid(row=5, column=0, padx=10, pady=5)
dend_diam_entry = Entry(root)
dend_diam_entry.insert(0, "10")  # Default value
dend_diam_entry.grid(row=5, column=1, padx=10, pady=5)

soma_length_label = Label(root, text="Soma Length (µm):")
soma_length_label.grid(row=6, column=0, padx=10, pady=5)
soma_length_entry = Entry(root)
soma_length_entry.insert(0, "20")  # Default value
soma_length_entry.grid(row=6, column=1, padx=10, pady=5)

soma_diam_label = Label(root, text="Soma Diameter (µm):")
soma_diam_label.grid(row=7, column=0, padx=10, pady=5)
soma_diam_entry = Entry(root)
soma_diam_entry.insert(0, "20")  # Default value
soma_diam_entry.grid(row=7, column=1, padx=10, pady=5)

# Button to run simulation
run_button = Button(root, text="Run Simulation", command=run_simulation)
run_button.grid(row=8, columnspan=2, padx=10, pady=10)

# Run GUI
root.mainloop()

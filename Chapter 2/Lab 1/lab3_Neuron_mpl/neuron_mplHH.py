import matplotlib
matplotlib.use('TkAgg')  # Use the TkAgg backend

from neuron import h, gui
import numpy as np
import matplotlib.pyplot as plt
import mplcursors

# Create a simple network with two Hodgkin-Huxley neurons connected via a synapse
class HHNeuron:
    def __init__(self):
        self.soma = h.Section(name='soma')
        self.soma.insert('hh')

# Create two neurons
neuron1 = HHNeuron()
neuron2 = HHNeuron()

# Connect neuron1 to neuron2 with an excitatory synapse
syn = h.ExpSyn(neuron2.soma(0.5))
syn.tau = 2
syn.e = 0

# Create a NetStim to stimulate neuron1
stim = h.NetStim()
stim.number = 1
stim.start = 5

# Create a NetCon to connect the NetStim to the first neuron
nc_stim = h.NetCon(stim, None)
nc_stim.threshold = 0  # You can adjust the threshold as needed
nc_stim.delay = 1
nc_stim.weight[0] = 0.04

# Create a NetCon to connect neuron1 to neuron2 via the synapse
nc_syn = h.NetCon(neuron1.soma(0.5)._ref_v, syn)
nc_syn.threshold = -20  # Spike detection threshold
nc_syn.delay = 5
nc_syn.weight[0] = 0.04

# Record time, voltage of both neurons, and synaptic current
t = h.Vector().record(h._ref_t)
v1 = h.Vector().record(neuron1.soma(0.5)._ref_v)
v2 = h.Vector().record(neuron2.soma(0.5)._ref_v)
i_syn = h.Vector().record(syn._ref_i)

# Run the simulation
h.finitialize(-65)
h.continuerun(40)

# Plot the results
plt.figure(figsize=(10, 8))

ax1 = plt.subplot(3, 1, 1)
line1, = plt.plot(t, v1, label='Neuron 1')
plt.ylabel('Voltage (mV)')
plt.legend()

ax2 = plt.subplot(3, 1, 2)
line2, = plt.plot(t, v2, label='Neuron 2', color='r')
plt.ylabel('Voltage (mV)')
plt.legend()

ax3 = plt.subplot(3, 1, 3)
line3, = plt.plot(t, i_syn, label='Synaptic Current', color='g')
plt.ylabel('Current (nA)')
plt.xlabel('Time (ms)')
plt.legend()

plt.tight_layout()

# Add hover interactivity
mplcursors.cursor(line1).connect("add", lambda sel: sel.annotation.set_text(f'Time: {sel.target[0]:.2f}, Voltage: {sel.target[1]:.2f}'))
mplcursors.cursor(line2).connect("add", lambda sel: sel.annotation.set_text(f'Time: {sel.target[0]:.2f}, Voltage: {sel.target[1]:.2f}'))
mplcursors.cursor(line3).connect("add", lambda sel: sel.annotation.set_text(f'Time: {sel.target[0]:.2f}, Current: {sel.target[1]:.2f}'))

plt.show()  # Show the plot interactively

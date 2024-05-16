from neuron import h, gui
import numpy as np
from matplotlib import pyplot as plt

# Create sections
soma = h.Section(name='soma')
dend = h.Section(name='dend')

# Topology
dend.connect(soma(1))

# Geometry
soma.L = soma.diam = 12.6157  # microns
dend.L = 200  # microns
dend.diam = 1  # microns

# Biophysics
for sec in h.allsec():
    sec.Ra = 100    # Axial resistance in Ohm * cm
    sec.cm = 1      # Membrane capacitance in micro Farads / cm^2

soma.insert('hh')  # Insert active Hodgkin-Huxley current in the soma
for seg in soma:
    seg.hh.gnabar = 0.12  # Sodium conductance in S/cm2
    seg.hh.gkbar = 0.036  # Potassium conductance in S/cm2
    seg.hh.gl = 0.0003    # Leak conductance in S/cm2
    seg.hh.el = -54.3     # Reversal potential in mV

dend.insert('pas')  # Insert passive current in the dendrite
for seg in dend:
    seg.pas.g = 0.001  # Passive conductance in S/cm2
    seg.pas.e = -65    # Leak reversal potential mV

# Stimulation
stim = h.IClamp(dend(1))
stim.delay = 5
stim.dur = 1
stim.amp = 0.1

# Recording vectors
v_vec = h.Vector()  # Membrane potential vector
t_vec = h.Vector()  # Time stamp vector
v_vec.record(soma(0.5)._ref_v)
t_vec.record(h._ref_t)

# Run simulation
simdur = 25.0
h.tstop = simdur
h.run()

# Plot membrane potential with explanation
plt.figure(figsize=(8, 4))
plt.plot(t_vec, v_vec)
plt.xlabel('time (ms)')
plt.ylabel('mV')
plt.annotate('Membrane potential of soma over time', xy=(0.5, 0.95), xycoords='axes fraction', ha='center')
plt.show()

print("Proceed to vary amplitude of current? (yes/no)")
proceed = input().lower()
if proceed == 'yes':
    # Varying amplitude of the current in a loop with explanation
    step = 0.075
    num_steps = 4
    plt.figure(figsize=(8, 4))
    for i in np.linspace(step, step*num_steps, num_steps):
        stim.amp = i
        h.tstop = simdur
        h.run()
        plt.plot(t_vec, v_vec, color='black')
    plt.xlabel('time (ms)')
    plt.ylabel('mV')
    plt.annotate('Effect of varying amplitude of current on soma', xy=(0.5, 0.95), xycoords='axes fraction', ha='center')
    plt.show()

    print("Proceed to visualize dendrite activity? (yes/no)")
    proceed = input().lower()
    if proceed == 'yes':
        # Visualizing dendrite activity with explanation
        dend_v_vec = h.Vector()  # Membrane potential vector for dendrite
        dend_v_vec.record(dend(0.5)._ref_v)
        plt.figure(figsize=(8, 4))
        for i in np.linspace(step, step*num_steps, num_steps):
            stim.amp = i
            h.tstop = simdur
            h.run()
            soma_plot = plt.plot(t_vec, v_vec, color='black')
            dend_plot = plt.plot(t_vec, dend_v_vec, color='red')
        plt.legend(soma_plot + dend_plot, ['soma', 'dend'])
        plt.xlabel('time (ms)')
        plt.ylabel('mV')
        plt.annotate('Comparison of soma and dendrite activity', xy=(0.5, 0.95), xycoords='axes fraction', ha='center')
        plt.show()

        print("Proceed to test the effects of nseg on dendritic signal? (yes/no)")
        proceed = input().lower()
        if proceed == 'yes':
            # Testing the effects of nseg on dendritic signal with explanation
            plt.figure(figsize=(8, 4))
            ref_v = []
            ref_dend_v = []

            # High resolution
            dend.nseg = 101
            for i in np.linspace(step, step*num_steps, num_steps):
                stim.amp = i
                h.run()
                soma_hires = plt.plot(t_vec, v_vec, color='blue')
                soma_hires = plt.plot(t_vec, dend_v_vec, color='green')
                ref_v_vec = np.zeros_like(v_vec)
                v_vec.to_python(ref_v_vec)
                ref_v.append(ref_v_vec)
                ref_dend_v_vec = np.zeros_like(dend_v_vec)
                dend_v_vec.to_python(ref_dend_v_vec)
                ref_dend_v.append(ref_dend_v_vec)

            # Low resolution
            dend.nseg = 1  # Play with this value. Use odd values.
            err = 0
            idx = 0
            for i in np.arange(step, step*(num_steps+.9), step):
                stim.amp = i
                h.run()
                soma_lowres = plt.plot(t_vec, v_vec, color='black')
                dend_lowres = plt.plot(t_vec, dend_v_vec, color='red')
                err += np.mean(np.abs(np.subtract(ref_v[idx], v_vec)))
                err += np.mean(np.abs(np.subtract(ref_dend_v[idx], dend_v_vec)))
                idx += 1

            err /= idx
            err /= 2  # Since we have a soma and dend vec
            print("Average error = {}".format(err))

            plt.legend(soma_lowres + dend_lowres + soma_hires,
                       ['soma low-res', 'dend low-res', 'soma hi-res', 'dend hi-res'])
            plt.xlabel('time (ms)')
            plt.ylabel('mV')
            plt.annotate('Effect of nseg on dendritic signal', xy=(0.5, 0.95), xycoords='axes fraction', ha='center')
            plt.show()
else:
    print("Exiting...")

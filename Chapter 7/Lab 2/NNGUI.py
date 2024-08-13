import numpy as np
import matplotlib.pyplot as plt
from tkinter import Tk, Label, Entry, Button, messagebox

# Function to create the neural network
def create_neural_network(size):
    return np.zeros((size, size))

# Function to apply electrical stimulation
def apply_stimulation(network, position, intensity):
    x, y = position
    network[x, y] = intensity
    return network

# Function to simulate neural activity
def simulate_activity(network, steps, threshold=1.0):
    for _ in range(steps):
        new_network = np.copy(network)
        for x in range(network.shape[0]):
            for y in range(network.shape[1]):
                if network[x, y] >= threshold:
                    # Activate neighboring neurons
                    if x > 0:
                        new_network[x-1, y] += 0.5 * network[x, y]
                    if x < network.shape[0] - 1:
                        new_network[x+1, y] += 0.5 * network[x, y]
                    if y > 0:
                        new_network[x, y-1] += 0.5 * network[x, y]
                    if y < network.shape[1] - 1:
                        new_network[x, y+1] += 0.5 * network[x, y]
        network = new_network
    return network

# Function to create an advanced neural network with inhibitory neurons
def create_advanced_neural_network(size, inhibitory_ratio=0.2):
    network = np.zeros((size, size))
    inhibitory_neurons = np.random.choice([True, False], size=(size, size), p=[inhibitory_ratio, 1-inhibitory_ratio])
    return network, inhibitory_neurons

# Function to simulate advanced neural activity with inhibitory neurons
def simulate_advanced_activity(network, inhibitory_neurons, steps, threshold=1.0):
    for _ in range(steps):
        new_network = np.copy(network)
        for x in range(network.shape[0]):
            for y in range(network.shape[1]):
                if network[x, y] >= threshold:
                    factor = -0.5 if inhibitory_neurons[x, y] else 0.5
                    # Activate neighboring neurons with inhibition consideration
                    if x > 0:
                        new_network[x-1, y] += factor * network[x, y]
                    if x < network.shape[0] - 1:
                        new_network[x+1, y] += factor * network[x, y]
                    if y > 0:
                        new_network[x, y-1] += factor * network[x, y]
                    if y < network.shape[1] - 1:
                        new_network[x, y+1] += factor * network[x, y]
        network = new_network
    return network

# Function to run the simulation based on user input
def run_simulation():
    try:
        size = int(size_entry.get())
        intensity = float(intensity_entry.get())
        steps = int(steps_entry.get())
        x_pos = int(x_entry.get())
        y_pos = int(y_entry.get())
        inhibitory_ratio = float(inhibitory_ratio_entry.get())

        # Initialize the advanced neural network
        network, inhibitory_neurons = create_advanced_neural_network(size, inhibitory_ratio)

        # Apply stimulation
        stimulation_position = (x_pos, y_pos)
        network = apply_stimulation(network, stimulation_position, intensity)

        # Simulate advanced activity
        advanced_network_activity = simulate_advanced_activity(network, inhibitory_neurons, steps)

        # Plot the initial and final advanced network activity
        plt.figure(figsize=(12, 6))
        plt.subplot(1, 2, 1)
        plt.imshow(network, cmap='hot', interpolation='nearest')
        plt.title('Initial Advanced Neural Network Activity')
        plt.colorbar()

        plt.subplot(1, 2, 2)
        plt.imshow(advanced_network_activity, cmap='hot', interpolation='nearest')
        plt.title('Advanced Neural Network Activity After Stimulation')
        plt.colorbar()

        plt.show()

    except ValueError:
        messagebox.showerror("Error", "Invalid input. Please enter numerical values.")

# Create the GUI window
root = Tk()
root.title("Neural Network Simulation")

# Labels and entries for user input
size_label = Label(root, text="Network Size:")
size_label.grid(row=0, column=0, padx=10, pady=5)
size_entry = Entry(root)
size_entry.insert(0, "10")  # Default value
size_entry.grid(row=0, column=1, padx=10, pady=5)

intensity_label = Label(root, text="Stimulation Intensity:")
intensity_label.grid(row=1, column=0, padx=10, pady=5)
intensity_entry = Entry(root)
intensity_entry.insert(0, "5.0")  # Default value
intensity_entry.grid(row=1, column=1, padx=10, pady=5)

steps_label = Label(root, text="Number of Steps:")
steps_label.grid(row=2, column=0, padx=10, pady=5)
steps_entry = Entry(root)
steps_entry.insert(0, "5")  # Default value
steps_entry.grid(row=2, column=1, padx=10, pady=5)

x_label = Label(root, text="Stimulation X Position:")
x_label.grid(row=3, column=0, padx=10, pady=5)
x_entry = Entry(root)
x_entry.insert(0, "5")  # Default value
x_entry.grid(row=3, column=1, padx=10, pady=5)

y_label = Label(root, text="Stimulation Y Position:")
y_label.grid(row=4, column=0, padx=10, pady=5)
y_entry = Entry(root)
y_entry.insert(0, "5")  # Default value
y_entry.grid(row=4, column=1, padx=10, pady=5)

inhibitory_ratio_label = Label(root, text="Inhibitory Neurons Ratio:")
inhibitory_ratio_label.grid(row=5, column=0, padx=10, pady=5)
inhibitory_ratio_entry = Entry(root)
inhibitory_ratio_entry.insert(0, "0.2")  # Default value
inhibitory_ratio_entry.grid(row=5, column=1, padx=10, pady=5)

# Button to run the simulation
run_button = Button(root, text="Run Simulation", command=run_simulation)
run_button.grid(row=6, columnspan=2, padx=10, pady=10)

# Run the GUI
root.mainloop()

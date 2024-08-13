import numpy as np
import matplotlib.pyplot as plt

# Define the neural network
def create_neural_network(size):
    return np.zeros((size, size))

# Apply electrical stimulation
def apply_stimulation(network, position, intensity):
    x, y = position
    network[x, y] = intensity
    return network

# Simulate neural activity
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

# Initialize the neural network
size = 10
network = create_neural_network(size)

# Apply stimulation
stimulation_position = (5, 5)
stimulation_intensity = 5.0
network = apply_stimulation(network, stimulation_position, stimulation_intensity)

# Simulate activity
steps = 5
network_activity = simulate_activity(network, steps)

# Plot the initial and final network activity
plt.figure(figsize=(12, 6))
plt.subplot(1, 2, 1)
plt.imshow(network, cmap='hot', interpolation='nearest')
plt.title('Initial Neural Network Activity')
plt.colorbar()

plt.subplot(1, 2, 2)
plt.imshow(network_activity, cmap='hot', interpolation='nearest')
plt.title('Neural Network Activity After Stimulation')
plt.colorbar()

plt.show()


# Advanced: Introducing inhibitory neurons and varying connectivity
def create_advanced_neural_network(size, inhibitory_ratio=0.2):
    network = np.zeros((size, size))
    inhibitory_neurons = np.random.choice([True, False], size=(size, size), p=[inhibitory_ratio, 1-inhibitory_ratio])
    return network, inhibitory_neurons

# Simulate advanced neural activity with inhibitory neurons
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

# Initialize the advanced neural network
size = 10
network, inhibitory_neurons = create_advanced_neural_network(size)

# Apply stimulation
stimulation_position = (5, 5)
stimulation_intensity = 5.0
network = apply_stimulation(network, stimulation_position, stimulation_intensity)

# Simulate advanced activity
steps = 5
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

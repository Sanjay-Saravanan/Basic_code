import numpy as np
import matplotlib.pyplot as plt
import threading

# Here is the activation function and its derivative.
sigma = lambda z: 1 / (1 + np.exp(-z))
d_sigma = lambda z: np.cosh(z / 2) ** (-2) / 4


# This function initialises the network with it's structure, it also resets any training already done.
def reset_network(n1=6, n2=7, random=np.random):
    global W1, W2, W3, b1, b2, b3
    W1 = random.randn(n1, 1) / 2
    W2 = random.randn(n2, n1) / 2
    W3 = random.randn(2, n2) / 2
    b1 = random.randn(n1, 1) / 2
    b2 = random.randn(n2, 1) / 2
    b3 = random.randn(2, 1) / 2


# This function feeds forward each activation to the next layer. It returns all weighted sums and activations.
def network_function(a0):
    z1 = W1 @ a0 + b1
    a1 = sigma(z1)
    z2 = W2 @ a1 + b2
    a2 = sigma(z2)
    z3 = W3 @ a2 + b3
    a3 = sigma(z3)
    return a0, z1, a1, z2, a2, z3, a3


# This is the cost function of a neural network with respect to a training set.
def cost(x, y):
    return np.linalg.norm(network_function(x)[-1] - y) ** 2 / x.size


# GRADED FUNCTION

# Fill in all incomplete lines.
# ===YOU SHOULD EDIT THIS FUNCTION===
def J_W1(x, y):
    a0, z1, a1, z2, a2, z3, a3 = network_function(x)
    J = 2 * (a3 - y)
    J = J * d_sigma(z2)
    J = (J.T @ W3).T
    J = J * d_sigma(z2)
    J = J @ a0.T / x.size
    J = J @ a1.T / x.size
    J = J @ a2.T / x.size
    J = J @ a3.T / x.size
    return J


# GRADED FUNCTION

# Compare this function to J_W3 to see how it changes.
# There is no need to edit this function.
def J_W2(x, y):
    # The first two lines are identical to in J_W3.
    a0, z1, a1, z2, a2, z3, a3 = network_function(x)
    J = 2 * (a3 - y)
    # the next two lines implement da3/da2, first σ' and then W3.
    J = J * d_sigma(z3)
    J = (J.T @ W3).T
    # then the final lines are the same as in J_W3 but with the layer number bumped down.
    J = J * d_sigma(z2)
    J = J @ a1.T / x.size
    return J


# Fill in all incomplete lines.
# ===YOU SHOULD EDIT THIS FUNCTION===
def J_b1(x, y):
    a0, z1, a1, z2, a2, z3, a3 = network_function(x)
    J = 2 * (a3 - y)
    J = J * d_sigma(z2)
    J = (J.T @ W3).T
    J = J * d_sigma(z2)
    J = J @ a0.T / x.size
    J = J @ a1.T / x.size
    J = J @ a2.T / x.size
    J = J @ a3.T / x.size
    J = np.sum(J, axis=1, keepdims=True) / x.size
    return J


# As previously, fill in all the incomplete lines.
# ===YOU SHOULD EDIT THIS FUNCTION===
def J_b2(x, y):
    a0, z1, a1, z2, a2, z3, a3 = network_function(x)
    J = 2 * (a3 - y)
    J = J * d_sigma(z2)
    J = (J.T @ W3).T
    J = J * d_sigma(z2)
    J = np.sum(J, axis=1, keepdims=True) / x.size
    return J


def training_data():
    return training_data()


x, y = training_data()
iterations = training_data()
reset_network()

plot_training(x, y, iterations=50000, aggression=7, noise=10)

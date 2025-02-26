import numpy as np
import pandas as pd

# Load the dataset
data = pd.read_csv('dataset/Question2_Dataset.csv')

df = pd.DataFrame(data)

# Normalize features
features = ['X1', 'X2', 'X1^2', 'X1^3', 'X2^2', 'X2^3', 'X1*X2', 'X1^2*X2']
X = df[features]
Y = df['Y'].values.reshape(-1, 1)

# Normalize each feature
means = X.mean()
stds = X.std()
X_normalized = (X - means) / stds

# Add intercept term
X_normalized = np.c_[np.ones(X_normalized.shape[0]), X_normalized.values]

# Initialize parameters
theta = np.zeros(X_normalized.shape[1])
alpha = 0.1
m = len(Y)

# Gradient descent
def compute_cost(X, Y, theta):
    predictions = X.dot(theta)
    errors = predictions - Y
    cost = (1/(2*m)) * np.sum(errors**2)
    return cost

def gradient_descent(X, Y, theta, alpha, iterations):
    costs = []
    for i in range(iterations):
        predictions = X.dot(theta).reshape(-1, 1)
        errors = predictions - Y
        gradients = (1/m) * X.T.dot(errors).flatten()
        theta -= alpha * gradients
        cost = compute_cost(X, Y, theta)
        costs.append(cost)
    return theta, costs

# Run gradient descent for different iterations
iterations_list = [10, 100, 1000]
results = []

for n in iterations_list:
    theta, costs = gradient_descent(X_normalized, Y, theta, alpha, n)
    final_cost = round(costs[-1])
    max_theta = round(np.max(theta))
    results.append((n, final_cost, max_theta))

# Display results
for n, cost, theta_max in results:
    print(f"n={n}: Cost Function = {cost}, Optimal Theta parameter = {theta_max}")
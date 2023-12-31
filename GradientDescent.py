import numpy as np

def gradient_descent(X, y, learning_rate, num_iterations):
    num_samples, num_features = X.shape
    theta = np.zeros(num_features)  # Initialize theta with zeros

    for _ in range(num_iterations):
        # Calculate the predicted values
        y_pred = np.dot(X, theta)

        # Calculate the gradient
        gradient = (1 / num_samples) * np.dot(X.T, (y_pred - y))

        # Update theta using gradient descent equation
        theta -= learning_rate * gradient

    return theta

# Example usage
X = np.array([[1, 3], [2, 4], [5, 1]])
y = np.array([1, 2, 3])

learning_rate = 0.1
num_iterations = 1000

theta = gradient_descent(X, y, learning_rate, num_iterations)
print("Theta:", theta)

#output Theta: [0.5648855  0.19083969]





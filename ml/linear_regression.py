import math
import numpy as np


class LinearRegression1:
    def __init__(self, lr=0.01, epochs=100):
        self.lr = lr
        self.epochs = epochs

    def initialize(self, n_features):
        """initialize weights uniformly in [-1/n, 1/n]"""
        limit = 1 / math.sqrt(n_features)
        self.w = np.random.uniform(-limit, limit, n_features)

    def fit(self, X, y, grad_descent=True):
        # add bias
        X = np.insert(X, 0, 1, axis=1)
        n_features = X.shape[1]
        self.initialize(n_features)
        # mse = np.mean(np.square((y-y_pred)))

        if grad_descent:
            for i in range(self.epochs):
                y_pred = np.matmul(X, self.w)
                grad_w = - 2 / n_features * np.matmul((y - y_pred), X)
                self.w = self.w - self.lr * grad_w
        else:
            # Normal eq.
            self.w = np.linalg.inv(np.matmul(X.T, X)).dot(X.T).dot(y)

    def predict(self, X):
        X = np.insert(X, 0, 1, axis=1)
        return np.matmul(X, self.w)


if __name__ == "__main__":
    try:
        X = np.array([[1, 1], [1, 2], [2, 2], [2, 3]])  # (4,3)
        y = np.dot(X, np.array([1, 2])) + 3  # (4,)
        linreg = LinearRegression1()
        linreg.fit(X, y)
        y_pred = linreg.predict(X)
        print(y)
        print(y_pred)

    except KeyboardInterrupt:
        exit()

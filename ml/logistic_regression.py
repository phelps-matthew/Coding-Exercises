import numpy as np
import random
import math


class LogisticRegression1:
    """Numpy"""

    def __init__(self, epochs=4000, lr=0.01):
        self.epochs = epochs
        self.lr = lr
        self.threshold = 0.5

    def sigmoid(self, x):
        return 1 / (1 + np.exp(-x))

    def initialize(self, n_features):
        """initialize weights uniformly in [-1/sqrt(n), 1/sqrt(n)]"""
        limit = 1 / math.sqrt(n_features)
        self.w = np.random.uniform(-limit, limit, n_features)

    def fit(self, X, y):
        # add bias
        X = np.insert(X, 0, 1, axis=1)
        self.initialize(X.shape[1])
        n_samples = X.shape[0]

        for _ in range(self.epochs):
            y_pred = self.sigmoid(np.matmul(X, self.w))
            grad_w = -1 / n_samples * np.matmul(y - y_pred, X)
            self.w = self.w - self.lr * grad_w

    def predict(self, X):
        X = np.insert(X, 0, 1, axis=1)
        p = self.sigmoid(np.matmul(X, self.w))
        return (p >= 0.5).astype(int)


def numpy_test():
    X = np.array([[1, 2], [1, 1], [2, 3], [2, 1]])  # (4,3)
    y = np.array([0, 0, 1, 1])
    logreg = LogisticRegression1()
    logreg.fit(X, y)
    y_pred = logreg.predict(X)
    print(y)
    print(y_pred)


def python_test():
    pass


if __name__ == "__main__":
    try:
        numpy_test()

    except KeyboardInterrupt:
        exit()

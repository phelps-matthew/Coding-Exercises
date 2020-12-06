import math
import random
import numpy as np


class LinearRegression1:
    """Numpy based linear regression"""

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
                grad_w = -2 / n_features * np.matmul((y - y_pred), X)
                self.w = self.w - self.lr * grad_w
        else:
            # Normal eq.
            self.w = np.linalg.inv(np.matmul(X.T, X)).dot(X.T).dot(y)

    def predict(self, X):
        X = np.insert(X, 0, 1, axis=1)
        return np.matmul(X, self.w)


class LinearRegression2:
    """Pure python linear regression"""

    def __init__(self, lr=0.01, epochs=100):
        self.lr = lr
        self.epochs = epochs

    def initialize(self, n_features):
        """initialize weights uniformly in [-1/n, 1/n]"""
        limit = 1 / math.sqrt(n_features)
        self.w = [random.uniform(-limit, limit) for _ in range(n_features)]

    def matmul(self, A, B):
        print(A, B)
        if isinstance(A[0], (int, float)):
            A = [A]
        if isinstance(B[0], (int, float)):
            B = [B]
        print(len(A[0]), len(B))
        assert len(A[0]) == len(B)
        m = len(A)
        n = len(B[0])
        res = [[] * n for i in range(m)]
        for i in range(m):
            for j in range(n):
                res[i][j] = sum(A[i][k] * B[k][j] for k in range(A[0]))
        return res

    def get_y_pred(self, X):
        return [
            sum(X[i][j] * self.w[j] for j in range(len(self.w))) for i in range(len(X))
        ]

    def get_grad_loss_summand(self, X, y):
        return [sum(y[k] * X[k][i] for k in range(len(y))) for i in range(len(X[0]))]

    def fit(self, X, y):
        """Ignore normal equation since no built-in linear algebra pkg"""
        # add bias
        X = [[1] + row for row in X]
        n_features = len(X[0])
        self.initialize(n_features)

        for i in range(self.epochs):
            y_pred = self.get_y_pred(X)
            delta_y = [y[i] - y_pred[i] for i in range(len(y))]
            grad_w = [
                -2 / n_features * elem
                for elem in self.get_grad_loss_summand(X, delta_y)
            ]
            for i in range(len(self.w)):
                self.w[i] = self.w[i] - self.lr * grad_w[i]

    def predict(self, X):
        X = [[1] + row for row in X]
        return np.matmul(X, self.w)


def numpy_test():
    X = np.array([[1, 1], [1, 2], [2, 2], [2, 3]])  # (4,3)
    y = np.dot(X, np.array([1, 2])) + 3  # (4,)
    linreg = LinearRegression1()
    linreg.fit(X, y)
    y_pred = linreg.predict(X)
    print(y)
    print(y_pred)


def python_test():
    X = [[1, 1], [1, 2], [2, 2], [2, 3]]
    y = [1 * a + 2 * b + 3 for a, b in X]
    linreg = LinearRegression2()
    linreg.fit(X, y)
    y_pred = linreg.predict(X)
    print(y)
    print(y_pred)


if __name__ == "__main__":
    try:
        numpy_test()
        python_test()

    except KeyboardInterrupt:
        exit()

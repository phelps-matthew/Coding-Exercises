"""
Matthew Phelps CS Pratical 6
Notes:
 - MSE is too large, does not reduce after grad descent
"""

import csv
import random
import math
import operator
import pandas as pd
import numpy as np


class Dataloader:
    def __init__(self, path="./USA_Housing.csv", shuffle=True):
        self.data = pd.read_csv(path)
        self.length = len(self.data)
        if shuffle:
            self.data = self.data.sample(frac=1).reset_index(drop=True)
        split_len = int(0.8 * self.length)
        self.drop_address()
        self.feature_len = self.data.shape[1] 
        self.x_train = self.include_bias(self.data.iloc[:split_len, :-1].values)  # income
        self.y_train = self.data.iloc[:split_len, -1].values.reshape(-1, 1)  # price
        self.x_test = self.include_bias(self.data.iloc[split_len:, :-1].values)  # income
        self.y_test = self.data.iloc[split_len:, -1].values.reshape(-1, 1)  # price
        # self.feature, self.label = self.get_feature_label()

    def drop_address(self):
        self.data = self.data.drop(["Address"], axis=1)

    def include_bias(self, x):
        """Add columns of ones to input vector"""
        return np.column_stack((np.ones((len(x), 1)), x))


class LinearRegression:
    def __init__(self, path="./USA_Housing.csv"):
        self.data = Dataloader(path)
        self.x_train = self.data.x_train
        self.y_train = self.data.y_train
        self.x_test = self.data.x_test
        self.y_test = self.data.y_test
        self.weight = np.random.randn(self.data.feature_len, 1)  # transposed

    def get_MSE(self):
        n = len(self.x_train)
        err = 1 / n * np.sum(np.square(self.x_train.dot(self.weight) - self.y_train))
        return err

    def get_gradients(self):
        n = len(self.x_train)
        grads = 2 / n * self.x_train.T.dot(self.x_train.dot(self.weight) - self.y_train)
        return grads

    def _fit(self, epochs=10, lr=0.1):
        for _ in range(epochs):
            grads = self.get_gradients()
            self.weight = self.weight - lr * grads

    def fit(self):
        self._fit()

    def predict_testset(self):
        return self.x_test.dot(self.weight)

    def predict(self, x):
        return x.dot(self.weight)


if __name__ == "__main__":
    lr = LinearRegression()
    print(lr.weight, lr.get_MSE())
    lr.fit()
    print(lr.weight, lr.get_MSE())
    print("MSE:", lr.get_MSE())

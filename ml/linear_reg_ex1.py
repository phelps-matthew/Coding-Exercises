import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import KFold


def error(x, y):
    kf = KFold(n_splits=len(x))
    ols = 0
    for train_idx, test_idx in kf.split(x):
        reg = LinearRegression().fit(x[train_idx], y[train_idx])
        ols += np.square(y[test_idx]-reg.predict(x[test_idx]))
        print(ols)
    return ols


X = np.array([[0], [2], [3]])
y = np.array([[1], [2], [1]])
ols = error(X, y)

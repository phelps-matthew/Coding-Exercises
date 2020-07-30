from sklearn.linear_model import LogisticRegression
from sklearn.datasets import load_iris


X, y = load_iris(return_X_y=True)
print(X)
print(y)
clf = LogisticRegression(random_state=0).fit(X, y)
clf.predict(X[:2, :])
# fmt: off
import ipdb,os; ipdb.set_trace(context=5)  # noqa
# fmt: on
clf.predict_proba(X[:2, :])
clf.score(X, y)

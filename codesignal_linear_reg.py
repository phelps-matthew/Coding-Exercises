from sklearn.linear_model import LinearRegression
import numpy as np

#slope = sum(
#    [(a - mean_A) * (b - mean_B) for a, b in zip(A_train, B_train)]
#) / float(sum([(a - mean_A) ** 2 for a in A_train]))

x = [1,2,3]
y = [1,2,3]

#print(np.array(x).reshape(-1, 1))
lin_model = LinearRegression().fit(np.array(x).reshape(-1, 1), np.array(y).reshape(-1, 1))
print(lin_model.coef_.item())


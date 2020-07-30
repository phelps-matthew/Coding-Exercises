import pandas as pd

fruits = pd.DataFrame(data=[[30, 21]], columns=["Apples", "Bananas"])
d = {"a": [1, 34], "n": [24, 53], "b": [43, 32]}
df2 = pd.DataFrame(d)
print(df2)
ds = pd.Series(d)
print(ds)

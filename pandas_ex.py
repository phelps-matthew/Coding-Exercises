import pandas as pd

fruits = pd.DataFrame(data=[[30, 21]], columns=["Apples", "Bananas"])
d = {"a": [1, 34], "n": [24, 53], "b": [43, 32]}
df2 = pd.DataFrame(d)
# fmt: off
import ipdb,os; ipdb.set_trace(context=5)  # noqa
# fmt: on
print(df2)
ds = pd.Series(d)
print(ds)

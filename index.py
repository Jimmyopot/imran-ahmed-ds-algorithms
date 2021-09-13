import pandas as pd
import numpy as np


df = pd.DataFrame([
    ['1', 'Fares', 32, True],
    ['2', 'Elena', 23, False],
    ['3', 'Steven', 40, True]
])
df.columns = ['id', 'name', 'age', 'decision']
print(df)
print(df.name)


myMatrix = np.array([[11, 12, 13], [21, 22, 23], [31, 32, 33]])
print(myMatrix)
print(type(myMatrix))
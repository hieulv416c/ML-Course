from numpy import nan as NA
import pandas as pd

data = pd.DataFrame([[1., 6.5, 3.],
                     [1., NA, NA],
                     [NA, NA, NA],
                     [NA, 6.5, 3.]])
print(data)

print("-"*10)
cleaned = data.dropna()
print(cleaned)

print("-"*10)
cleaned2 = data.dropna(how='all')
print(cleaned2)

print("-"*10)
cleaned3 = data.dropna(axis=1)
print(cleaned3)

print("-"*10)
cleaned4 = data.dropna(thresh=1)
print(cleaned4)

print("-"*10)
cleaned5 = data.dropna(subset=1)
print(cleaned5)


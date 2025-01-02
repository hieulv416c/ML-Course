from numpy import nan as NA
import pandas as pd

data = pd.DataFrame([[1., 6.5, 3.],
                     [1., NA, NA],
                     [NA, NA, NA],
                     [NA, 6.5, 3.]])
print(data)

print("-"*10)
cleaned=data.fillna(data.mean())
print(cleaned)

print("-"*10)
cleaned2=data.fillna(data.median())
print(cleaned2)

print("-"*10)
cleaned3=data.fillna(data.mode(axis=1))
print(cleaned3)

print("-"*10)
cleaned4=data.fillna(0)
print(cleaned4)
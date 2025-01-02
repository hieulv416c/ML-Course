pip install numpy
pip install pandas
from numpy import nan as NA
import pandas as pd

data = pd.DataFrame([
    [1.,6.5,3.],
    [1.,NA,NA],
    [NA,NA,NA],
    [NA,6.5,3.]
])
print(data)
print ("-"*10)
cleaned = data.dropna()
print(cleaned)
cleaned=data.fillna(data.mean())
print(cleaned)

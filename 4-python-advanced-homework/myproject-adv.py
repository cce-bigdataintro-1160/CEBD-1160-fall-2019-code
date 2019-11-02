#!/usr/bin/env python3

import pandas as pd

df = pd.read_csv(filepath_or_buffer='data/boston/housing.data',
                 sep='\\s+',
                 header=0)

df.columns = ['CRIM', 'ZN', 'INDUS', 'CHAS', 'NOX', 'RM', 'AGE', 'DIS', 'RAD', 'TAX', 'PTRATIO', 'B', 'LSTAT', 'MEDV']

print(df.info())
print(df.describe())
print(df.corr())

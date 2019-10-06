#!/usr/bin/env python3

import numpy as np
import pandas as pd


def pretty_print(name, to_print):
    print(f'{name}:')
    print(f'{to_print}\n\n')

# We finally get to look at Pandas! This is how we create a Series manually. A series is just like a numpy vector but
# now we have labeled fields
orders = pd.Series(data=[300.50, 60, 123.40, 60, np.nan],
                   index=['Customer 1', 'Customer 2', 'Customer 3', 'Customer 4', 'Customer 5'])

# This is how we can print a Series
pretty_print("orders", orders.to_string())

# This is how we can select the first line only
pretty_print("first row of orders", orders.head(n=1))

# This is how we can see the labels of each value
pretty_print("orders indexes", orders.index)

# Pandas can automagically infer the type for a Series by checking all values for us
pretty_print("order types", orders.dtypes)

# Printing the shape of a Series
pretty_print("orders shape", orders.shape)

# Describing a Series
pretty_print("orders description with types", orders.describe())

# Sorting all values in a series
pretty_print("orders sorted values", orders.sort_values())

# Counting occurrences of different values in a series
pretty_print("orders counts of values", orders.value_counts())

# Checking for null elements in a Series
pretty_print("orders check for null elements", orders.isnull())

#!/usr/bin/env python3

import pandas as pd


def pretty_print(name, to_print):
    print(f'{name}:')
    print(f'{to_print}\n\n')


# This is how we create a Series manually. Notice it is a two dimension series, now with lables on both columns and rows
orders = pd.DataFrame(data=[['XB4Z34', 11, 25.50],
                            ['SZA1123', 34, 60],
                            ['P4FF2S', 2, 123.40],
                            ['PL34DS', 10, 1254.23],
                            ['PL34DS', 4, 12.4]],
                      # index=['Customer 1', 'Customer 2', 'Customer 3', 'Customer 4', 'Customer 5'],
                      columns=['Product', 'Qty', 'Price'])

orders.columns = ['Product', 'Qty', 'Price']

# A few basic functions to printing series
pretty_print("Printing an entire dataframe", orders.to_string())
pretty_print("Showing the length of our dataframe(nr rows)", len(orders))
pretty_print("Selecting only the first row of a dataframe", orders.head(n=1))

# Again we have a few methods that can quickly explain the entire dataset shape for us
pretty_print("Show all column names for a dataframe", orders.columns)
pretty_print("Show all index names for a dataframe", orders.index)
pretty_print("Pandas can automagically infer the type for a DataFrame by checking all values for us", orders.dtypes)
pretty_print("Getting the shape of a dataframe", orders.shape)
pretty_print("Summarized info on dataframe", orders.info())
pretty_print("Quick stats on all numeric columns for dataframe", orders.describe())

# A few other advanced functions to check values in a DataFrame
pretty_print("Sorting all rows in the DF by price", orders.sort_values(by='Price'))
pretty_print("Checking for null values on DF", orders.isnull())
pretty_print("Checking n unique values for each column", orders.nunique())

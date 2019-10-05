#!/usr/bin/env python3

import pandas as pd
import matplotlib.pyplot as plt
import os


def pretty_print(name, to_print):
    print(f'{name}:')
    print(f'{to_print}\n\n')

# Make sure to install xlrd with pip3!!!
titanic = pd.read_excel(io='data/titanic/train.xlsx',
                        sheet_name='Sheet1',
                        header=0)

pretty_print("titanic dataframe", titanic.to_string())
pretty_print("titanic columns", titanic.columns)

os.makedirs('plots', exist_ok=True)

# Plotting line chart
plt.plot(titanic['Fare'], color='red')
plt.title('Fare by Index')
plt.xlabel('Index')
plt.ylabel('Fare')
plt.savefig(f'plots/fare_by_index_plot.png', format='png')
plt.clf()

# Plotting histogram
plt.hist(titanic['Survived'], bins=3, color='g')
plt.title('Survived')
plt.xlabel('Survived')
plt.ylabel('Count')
plt.savefig(f'plots/survived_hist.png', format='png')
plt.clf()

# Plotting scatterplot
plt.scatter(titanic['Age'], titanic['Fare'], color='b')
plt.title('Age to Fare')
plt.xlabel('Age')
plt.ylabel('Fare')
plt.savefig(f'plots/age_to_fare.png', format='png')

plt.close()

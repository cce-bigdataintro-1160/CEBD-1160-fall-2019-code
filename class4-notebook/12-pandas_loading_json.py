#!/usr/bin/env python3

import pandas as pd
import matplotlib.pyplot as plt
import os


def pretty_print(name, to_print):
    print(f'{name}:')
    print(f'{to_print}\n\n')


titanic = pd.read_json('data/titanic/train.json')

pretty_print("Titanic dataframe", titanic.to_string())
pretty_print("Titanic dataframe", titanic.columns)
pretty_print("Titanic dataframe", titanic.info())
pretty_print("Titanic dataframe", titanic.describe().to_string())

plt.close()

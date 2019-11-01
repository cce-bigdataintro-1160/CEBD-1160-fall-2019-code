#!/usr/bin/env python3

import os

import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv('data/wine.data',
                 sep=',',
                 header=0)

df.columns = ['class', 'alcohol', 'malic_acid', 'ash', 'alcalinity_of_ash', 'magnesium', 'total_phenols', 'flavanoids',
              'nonflavanoid_phenols', 'proanthocyanins', 'color_intensity', 'hue', 'od280 od315_of_diluted_wines',
              'proline']

os.makedirs('plots/8-matplotlib_multiple_plot_axes', exist_ok=True)

plt.style.use("ggplot")

fig, axes = plt.subplots(1, 1, figsize=(5, 5))

# This time we plot multiple plots on the same axes, to get some perspective on their comparisons
axes.scatter(df['alcohol'], df['total_phenols'], alpha=0.7)
axes.scatter(df['alcohol'], df['color_intensity'], alpha=0.7)
# axes.scatter(df['alcohol'], df['malic_acid'], alpha=0.7)

axes.set_xlabel('Alcohol')
axes.set_ylabel('Total Phenols / Color Intensity')
axes.set_title(f'Alcohol comparisons')
axes.legend()
plt.savefig(f'plots/8-matplotlib_multiple_plot_axes/multiplot_scatter.png', dpi=300)

plt.close()

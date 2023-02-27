# -*- coding: utf-8 -*-
"""
Created on Mon Feb 27 20:20:04 2023

@author: CYNTHIA AWUOR
"""

import matplotlib.pyplot as plt

# data
modules = ['salmon', 'grey', 'brown', 'midnightblue', 'purple', 'orange', 'black',
           'darkorange', 'darkturquoise', 'greenyellow', 'darkolivegreen', 'darkmagenta',
           'orangered4', 'paleturquoise', 'mediumpurple3', 'lightcyan1', 'floralwhite',
           'ivory', 'brown4', 'bisque4']
genes = [3197, 2112, 1354, 888, 866, 588, 359, 278, 199, 199, 187, 186, 151,
         87, 53, 45, 38, 38, 36, 34]
colors  =[(0.98, 0.5, 0.45, 1), (0.5, 0.5, 0.5, 1), (0.6, 0.4, 0.2, 1), (0.1, 0.1, 0.44, 1), (0.5, 0, 0.5, 1), (1, 0.65, 0, 1), (0, 0, 0, 1), (1, 0.55, 0, 1), (0, 0.81, 0.82, 1), (0.68, 1, 0.18, 1), (0.33, 0.42, 0.18, 1), (0.55, 0, 0.55, 1), (0.55, 0.14, 0, 1), (0.69, 0.93, 0.93, 1), (0.58, 0.44, 0.86, 1), (0.88, 1, 1, 1), (1, 0.98, 0.94, 1), (1, 1, 0.94, 1), (0.55, 0.27, 0.07, 1), (0.55, 0.46, 0.36, 1)]
# create bar plot
fig, ax = plt.subplots(figsize=(12, 8))
rects = ax.bar(modules, genes, color=colors, linewidth=1.5)

# set y-axis label
ax.set_ylabel('Genes')

# set title
ax.set_title('Gene Distribution in Modules', fontsize=16)

# set x-axis tick labels
ax.set_xticklabels(modules, rotation=90)

# set background color
ax.set_facecolor('lightgrey')


# add gene values on top of bars
for i, rect in enumerate(rects):
    value = rect.get_height()
    ax.text(i, value + 50, str(value), horizontalalignment='center', color='black', fontsize=10)


# show plot
plt.show()

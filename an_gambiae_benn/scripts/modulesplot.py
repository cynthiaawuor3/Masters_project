# -*- coding: utf-8 -*-
"""
Created on Mon Feb 27 11:47:39 2023

@author: cynthia awuor
"""

import matplotlib.pyplot as plt

# data
modules = ['blue', 'honeydew1', 'grey', 'black', 'darkorange2', 'lightgreen', 'orangered4', 'lightyellow', 'cyan', 'darkred', 'darkturquoise', 'darkorange', 'saddlebrown', 'plum1', 'mediumpurple3', 'lightcyan1', 'ivory', 'bisque4', 'lightpink4', 'coral1', 'antiquewhite4', 'coral2', 'skyblue2', 'yellow4', 'skyblue1', 'orangered3']
genes = [3839, 1312, 935, 925, 710, 632, 615, 440, 191, 149, 142, 134, 109, 86, 85, 77, 75, 72, 62, 48, 47, 44, 39, 38, 34, 31]

colors  =[(0, 0, 1, 1), (0.94, 1, 0.94, 1), (0.5, 0.5, 0.5, 1), (0, 0, 0, 1), (0.93, 0.46, 0, 1), (0.56, 0.93, 0.56, 1), (1, 0.27, 0, 1), (1, 1, 0.88, 1), (0, 1, 1, 1), (0.55, 0, 0, 1), (0, 0.81, 0.82, 1), (1, 0.55, 0, 1), (0.54, 0.27, 0.07, 1), (1, 0.73, 1, 1), (0.58, 0.44, 0.86, 1), (0.88, 1, 1, 1), (1, 1, 0.94, 1), (0.55, 0.46, 0.36, 1), (0.55, 0.35, 0.35, 1), (1, 0.45, 0.34, 1), (0.55, 0.51, 0.48, 1), (0.93, 0.38, 0.25, 1), (0.49, 0.81, 0.94, 1), (0.55, 0.55, 0, 1), (0.53, 0.81, 0.92, 1), (1, 0.17, 0, 1)]
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

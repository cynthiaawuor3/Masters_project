# -*- coding: utf-8 -*-
"""
Created on Mon Feb 27 11:47:39 2023

@author: cynthia awuor
"""

import matplotlib.pyplot as plt

# data
modules = ['antiquewhite4', 'bisque4', 'black', 'blue', 'coral1', 'coral2', 'cyan', 'darkorange', 
           'darkorange2', 'darkred', 'darkturquoise', 'grey', 'honeydew1', 'ivory', 'lightcyan1', 
           'lightgreen', 'lightpink4', 'lightyellow', 'mediumpurple3', 'orangered3', 'orangered4', 
           'plum1', 'saddlebrown', 'skyblue1', 'skyblue2', 'yellow4']
genes = [47, 72, 925, 3839, 48, 44, 191, 134, 710, 149, 142, 935, 1312, 75, 77, 632, 62, 440, 
         85, 31, 615, 86, 109, 34, 39, 38]
colors = [(0.78, 0.61, 0.43, 1.0), (1.0, 0.89, 0.77, 1.0), (0.0, 0.0, 0.0, 1.0), (0.0, 0.0, 1.0, 1.0), (1.0, 0.5, 0.31, 1.0), (1.0, 0.8, 0.56, 1.0), (0.0, 1.0, 1.0, 1.0), (1.0, 0.55, 0.0, 1.0), (1.0, 0.43, 0.0, 1.0), (0.55, 0.0, 0.0, 1.0), (0.0, 0.81, 0.82, 1.0), (0.5, 0.5, 0.5, 1.0), (1.0, 1.0, 0.94, 1.0), (1.0, 1.0, 1.0, 1.0), (0.88, 1.0, 1.0, 1.0), (0.56, 0.93, 0.56, 1.0), (0.73, 0.56, 0.56, 1.0), (1.0, 1.0, 0.88, 1.0), (0.58, 0.44, 0.86, 1.0), (1.0, 0.27, 0.0, 1.0), (0.55, 0.12, 0.0, 1.0), (0.87, 0.63, 0.87, 1.0), (0.55, 0.27, 0.07, 1.0), (0.53, 0.81, 0.98, 1.0), (0.49, 0.75, 0.93, 1.0), (1.0, 0.93, 0.0, 1.0)]

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

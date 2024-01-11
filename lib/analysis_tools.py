
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath('')))
# print(sys.path)
import pandas as pd
import datetime
import matplotlib
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
# import seaborn as sns
import matplotlib.ticker as ticker

from scipy.stats import pearsonr
from pingouin import ancova

def plot_boxes_grade_cats(abt, 
    columns, 
    labels, 
    title, 
    xlabel, 
    ylabel,
    hide_x = False,
    hide_y = False):
    """
    Given an ABT and a list of columns in that ABT,
    plot 
    """
    x_pos_range = np.arange(len(labels)) / (len(labels) - 1)
    x_pos_range



    for i, column in enumerate(columns):

        series_excellent = abt[abt['grade'] >= 8.5][column]
        bp_excellent = plt.boxplot(series_excellent,
                            showfliers=False,
                            patch_artist= True,
                            boxprops = dict(color = 'grey', facecolor = 'white'),
        positions= [i - 0.2])
        for median in bp_excellent['medians']:
            median.set_color('gray')
            
        series_pass = abt[(abt['grade'] >= 5.5) & (abt['grade'] < 8.5)][column]
        bp_pass = plt.boxplot(series_pass,
                            showfliers=False,
                            patch_artist= True,
                            boxprops = dict(color = 'blue', facecolor = 'white'),
        positions= [i])
        for median in bp_pass['medians']:
            median.set_color('blue')
        

        series_fail = abt[abt['grade'] < 5.5][column]
        bp_fail = plt.boxplot(series_fail,
                            showfliers=False,
                            patch_artist=True,
                            boxprops=dict(color='red', facecolor='white'),
        positions= [i + 0.2])
        for median in bp_fail['medians']:
            median.set_color('red')
    plt.xticks(range(0, len(labels)), labels, rotation=90)

    plt.title(title)
    plt.ylabel(ylabel)
    plt.xlabel(xlabel)

    import matplotlib.patches as mpatches

    red_patch = mpatches.Patch(facecolor = 'white', edgecolor='red', label='Failing')
    blue_patch = mpatches.Patch(facecolor = 'white', edgecolor='blue', label='Passing / Good')
    grey_patch = mpatches.Patch(facecolor = 'white', edgecolor='grey', label='Excellent')
    plt.legend([grey_patch, blue_patch, red_patch], ['Excellent', 'Passing / Good', 'Failing'])

    if hide_y:
        plt.yticks([])
    plt.show()
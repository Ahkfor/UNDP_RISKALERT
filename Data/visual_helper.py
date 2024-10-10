import matplotlib.pyplot as plt
import numpy as np


def line_bar_plot(x, y, title, x_label=None, y_label=None, save_path=None, unit=None):
    '''

    :param x: x-axis data
    :param y: y-axis data
    :param title: string
    :param x_label: string
    :param y_label: string
    :return:
    '''
    if unit == 'billion':
        y = [i/10**9 for i in y]

    # Create the plot
    plt.figure(figsize=(10, 6))

    # Bar plot
    plt.bar(x, y, color='skyblue', label='Bar Data', alpha=0.5, width=0.4)

    # Line plot (plotted on the same y-axis)
    plt.plot(x, y, color='r', label='Line Data', linewidth=2.5, marker='o')

    # Titles and labels
    plt.title(title, fontsize=16, fontweight='bold')
    if x_label:
        plt.xlabel(x_label, fontsize=14)
    if y_label:
        plt.ylabel(y_label, fontsize=14)

    if save_path:
        # Save the plot
        plt.savefig(save_path)
        return save_path
    else:
        plt.show()


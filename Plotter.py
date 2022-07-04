import matplotlib
import matplotlib.pyplot as plt
import numpy as np


def plot(data,
         title='',
         y_label='',
         y_grid_base=1,
         y_grid_res=None,
         y_grid_format='{}',
         x_label='',
         x_grid_base=1,
         x_grid_res=None,
         x_grid_format='{}',
         show=True,
         ax=None,
         point_size=1,
         total_x=None):
    if total_x == None:
        total_x = len(data)
    if x_grid_res == None:
        x_grid_res = np.power(10, np.round(np.log10(len(data)))-1)
    if y_grid_res == None:
        y_grid_res = np.power(10, np.round(np.log10(max(data)))-1)
    x_data = [(element / len(data)) * total_x for element in range(len(data))]
    if show:
        plt.scatter(x_data,
                    data,
                    c=range(len(data)),
                    title=title,
                    point_size=point_size)
        ax = plt.gca()
    else:
        ax.scatter(x_data,
                   data,
                   c=range(len(data)),
                   s=point_size)
    ax.yaxis.set_major_formatter(matplotlib.ticker.FuncFormatter(
        lambda val, pos: y_grid_format.format(val / y_grid_base) if val != 0 else '0'
    ))
    ax.yaxis.set_major_locator(matplotlib.ticker.MultipleLocator(base=y_grid_res))
    ax.xaxis.set_major_formatter(matplotlib.ticker.FuncFormatter(
        lambda val, pos: x_grid_format.format(val / x_grid_base) if val != 0 else '0'
    ))
    ax.xaxis.set_major_locator(matplotlib.ticker.MultipleLocator(base=x_grid_res))
    ax.set(title=title, xlabel=x_label, ylabel=y_label)
    if show:
        plt.show()

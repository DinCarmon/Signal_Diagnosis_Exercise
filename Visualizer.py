import json
import csv
import sys
import matplotlib
import matplotlib.pyplot as plt
from matplotlib.pyplot import figure
import numpy as np
import Plotter


def visualize_abs(data, show=True, ax=None, point_size=1):
    data_abs = [abs(element) for element in data]
    Plotter.plot(data_abs,
                 title='abs(signal)',
                 y_label='abs(signal)',
                 show=show,
                 ax=ax,
                 point_size=point_size)


def visualize_phase(data, show=True, ax=None, point_size=1):
    data_phase = [np.angle(element) for element in data]
    Plotter.plot(data_phase,
                 title='phase(signal)',
                 y_label='phase(signal)',
                 y_grid_base=np.pi,
                 y_grid_res=np.pi/2,
                 y_grid_format='{:.0g}$\pi$',
                 show=show,
                 ax=ax,
                 point_size=point_size)

def visualize_abs_fft(data, show=True, ax=None, point_size=1):
    s_fft = np.fft.fft(data)
    s_fft_abs = [abs(element) for element in s_fft]
    Plotter.plot(s_fft_abs,
                 title='FFT(signal)',
                 y_label='FFT(signal)',
                 x_grid_base=np.pi,
                 x_grid_res=np.pi / 2,
                 x_grid_format='{:g}$\pi$',
                 show=show,
                 ax=ax,
                 point_size=point_size,
                 total_x=2 * np.pi)
    return s_fft_abs


def visualize_in_complex_plane(data, point_size=1, show=True, ax=None):
    data_real = [np.real(element) for element in data]
    data_imag = [np.imag(element) for element in data]
    title = "scatter(signal)"
    if show:
        plt.scatter(data_real,
                    data_imag,
                    c=range(len(data)),
                    s=point_size,
                    title=title)
    else:
        ax.scatter(data_real,
                   data_imag,
                   c=range(len(data)),
                   s=point_size)
        ax.set_title(title)
    if show:
        plt.show()


def visualize_total(data,
                    point_size=1,
                    fig_size_inches=(5, 5)):
    fig, axs = plt.subplots(4)
    fig.set_size_inches(fig_size_inches)
    visualize_abs(data, show=False, ax=axs[0], point_size=point_size)
    visualize_phase(data, show=False, ax=axs[1], point_size=point_size)
    visualize_in_complex_plane(data,
                               show=False,
                               point_size=point_size,
                               ax=axs[2])
    visualize_abs_fft(data, show=False, ax=axs[3], point_size=point_size*100)
    plt.show()

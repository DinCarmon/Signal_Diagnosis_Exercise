import json
import csv
import sys
import FileParser
import Visualizer
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import scipy
import scipy.signal

def main():
    s = FileParser.read_file_to_array('mystery_signal.mat')
    #Visualizer.visualize_abs(s)
    #Visualizer.visualize_phase(s)
    #Visualizer.visualize_in_complex_plane(s, point_size=0.2)
    #Visualizer.visualize_total(s, point_size=0.2, fig_size_inches=(18.5, 9))
    #Visualizer.visualize_total(s[:int(len(s)/10000)], point_size=300, fig_size_inches=(18.5, 9))

    print('length of signal is ' + str(len(s)) + " samples")

    s_fft = np.fft.fft(s)
    s_fft_abs = [abs(element) for element in s_fft]
    freq = [2 * np.pi * element / len(s) for element in range(len(s))]
    max_s_fft_abs = max(s_fft_abs)
    print('notable frequencies are:')
    for i in range(len(s)):
        if s_fft_abs[i] >= max_s_fft_abs / 3:
            print(str(freq[i] / np.pi) + "\u03C0")

    frame_size = 8
    s = s[0: len(s) - np.mod(len(s), frame_size)]
    s_frames = np.split(s, len(s) / frame_size)
    num_of_frames = len(s_frames)
    print("num of full frames is " + str(num_of_frames))
    """s_frames_mean = np.mean(s_frames, axis=0)
    s_frames_var = np.var(s_frames, axis=0)
    Visualizer.visualize_total(s_frames_mean, point_size=10, fig_size_inches=(18.5, 9))
    Visualizer.visualize_total(s_frames_var, point_size=10, fig_size_inches=(18.5, 9))
    """

    """s_frames_mean = np.mean(s_frames, axis=1)
    s_frames_var = np.var(s_frames, axis=1)
    Visualizer.visualize_total(s_frames_mean, point_size=1, fig_size_inches=(18.5, 9))
    Visualizer.visualize_total(s_frames_var, point_size=10, fig_size_inches=(18.5, 9))
"""
    """s_frames_mean = np.mean(np.angle(s_frames), axis=1)
    s_frames_var = np.var(np.angle(s_frames), axis=1)
    Visualizer.visualize_total(s_frames_mean, point_size=10, fig_size_inches=(18.5, 9))
    Visualizer.visualize_total(s_frames_var, point_size=10, fig_size_inches=(18.5, 9))"""




    fig = plt.figure(figsize=(18.5, 9))
    f, t, s_spectrogram = scipy.signal.spectrogram(s)
    plt.pcolormesh(t, f, s_spectrogram, shading='gouraud')
    plt.ylabel('Frequency')
    plt.xlabel('Time')
    plt.show()

    plt.xcorr(s, s, usevlines=True, normed=True)
    plt.grid(True)
    plt.show()

if __name__ == '__main__':
    main()

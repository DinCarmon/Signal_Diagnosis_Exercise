import json
import csv
import sys
import numpy as np


def read_file_to_array(file_path):
    file_signal = open(file_path, 'r')
    s = [element for element in csv.reader(file_signal, delimiter=';')][0]
    s = [element.replace(" ", "").replace("i", "j") for element in s]
    s = [complex(element) for element in s]
    return np.array(s)

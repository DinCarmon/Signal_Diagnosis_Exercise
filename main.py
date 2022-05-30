import json
import csv
import sys

def main():
    print('hello world')
    file_signal = open('mystery_signal.mat', 'r')
    s = [element for element in csv.reader(file_signal, delimiter=';')][0]
    s = [element.replace(" ", "").replace("i", "j") for element in s]
    s = [complex(element) for element in s]
    print(s)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()

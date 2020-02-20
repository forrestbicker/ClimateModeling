from matplotlib import pyplot as plt
import numpy as np
from scipy.optimize import curve_fit
from os import listdir
import csv
from matplotlib.ticker import MultipleLocator

in_dir = "/Users/forrestbicker/Documents/Code/Python/WorkInProgress/MTF/data/GRAPHER/RAW/"
out_dir = "/Users/forrestbicker/Documents/Code/Python/WorkInProgress/MTF/data/GRAPHER/OUT/"

def f(x, a, b):
    return(a * x + b)

def func_to_xy(x, y, func, *argv):
    res = 2**8  # resolution of curve
    xrange = max(x) - min(x)

    x = np.array([min(x) + xrange * (i / res) for i in range(res)
                  if f(min(x) + xrange * (i / res), *argv) <= max(y)])
    y = [f(x, *argv) for x in x]
    return([x, y])

def fTok(x):
    return((x - 32) * 5 / 9 + 273.15)

def f_x(x):
    return(x)

def f_y(y):
    # y = y
    # if y == 0:
    #     return 0
    # else:
    #     return(np.log10(y))
    y = fTok(y)
    return(np.log10(y))

in_names = [file for file in listdir(in_dir) if file != ".DS_Store"]
for in_name in in_names:
    in_basename = in_name.split(".")[0]

    in_path = in_dir + in_name
    out_path = out_dir + in_basename + ".jpg"

    with open(in_path, "r") as in_file:
        print("Processing file: " + in_basename)
        in_data = np.array(list(csv.reader(in_file))[1:]).T  # parses csv into 2d array
        x = [f_x(int(x)) for x in in_data[0][1:]][-31:]
        print(x)
        for row in in_data[1::2]:
            y = [f_y(float(y)) for y in row[1:]][-31:]
            plt.scatter(x, y, s=2)

            a, b = curve_fit(f, x, y, maxfev=5000, p0=[10, 5])[0]

            x_fit, y_fit = func_to_xy(x, y, f, a, b)
            plt.plot(x_fit, y_fit, color='#1f3e78', linestyle='-')

            plt.suptitle(row[0], fontname='Times')
            plt.ylabel(in_basename + " (log in)", fontname='Times')
            plt.xlabel('Time (Year)', fontname='Times')

            plt.savefig(out_dir + f'{in_basename}_{row[0]}_IOWA.png')
            plt.cla()
            # plt.Axes.get_xaxis.

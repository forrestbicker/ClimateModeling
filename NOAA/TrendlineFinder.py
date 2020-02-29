import numpy as np
from scipy.optimize import curve_fit
from matplotlib import pyplot as plt
from json import load, dump
from scipy import stats
from sklearn.metrics import r2_score
from collections import defaultdict
from math import exp

in_path = "/Users/forrestbicker/Documents/Code/Python/WorkInProgress/MTF/data/NOAA/OUT/climateNOAA_ALL_Month-Specific.json"
out_dir = "/Users/forrestbicker/Documents/Code/Python/WorkInProgress/MTF/data/NOAA/GRAPHS/"
out_dict = defaultdict(list)
out_path = "/Users/forrestbicker/Documents/Code/Python/WorkInProgress/MTF/data/NOAA/OUT/month-Specific-Predictions.json"

def f(x, a, b, c):
    return(a * x ** 2 + b * x + c)
    # return(
    #     a * n ** x + b
    # )

def func_to_points(f, x, *coeffients):
    x = np.array(x)

    y = [f(x, *coeffients) for x in x]
    return([x, y])

def coeffients_to_eq(*coeffients):
    # a, b, n = coeffients
    # return f"{a:.2f}x^{n:.2f} + {b:.2f}"

    eq = []

    if len(coeffients) > 2:
        for i, coefficent in enumerate(reversed(coeffients[:-2])):
            eq.append(f"{coefficent:.2e}x^{i-1}")

    if len(coeffients) >= 2:
        eq.append(f"{coeffients[1]:.2e}x")

    if len(coeffients) >= 1:
        eq.append(f"{coeffients[0]:.2e}")

    return(" + ".join(eq))

def polyfit(x, y, degree):
    coeffs = np.polyfit(x, y, degree)

    # r-squared
    p = np.poly1d(coeffs)
    # fit values, and mean
    yhat = p(x)                         # or [p(z) for z in x]
    ybar = np.sum(y) / len(y)          # or sum(y)/len(y)
    ssreg = np.sum((yhat - ybar)**2)   # or sum([ (yihat - ybar)**2 for yihat in yhat])
    sstot = np.sum((y - ybar)**2)    # or sum([ (yi - ybar)**2 for yi in y])

    return [coeffs.tolist(), ssreg / sstot]

def curvefit(x, y, f):
    coeffients = curve_fit(f, x, y, maxfev=100000)[0]
    predicted_y = func_to_points(f, x, *coeffients)[1]
    r2 = r2_score(y, predicted_y)
    return [coeffients, r2]

with open(in_path, "r") as in_file:
    in_dict = load(in_file)

for metric in ["tMax", "tAvg", "tMin", "pcp"]:
    for month in in_dict[metric]:
        x = []
        y = []
        for year in in_dict[metric][month]:
            x_year = int(year)
            if x_year >= 1949:
                y_year = []
                for datapoint in in_dict[metric][month][year]:
                    # x.append(int(year))
                    # y.append(datapoint)
                    y_year.append(datapoint)
                y_year = np.average(y_year)

                x.append(x_year)
                y.append(y_year)
        plt.scatter(x, y, s=2)

        key = str(metric) + str(month)


        coeffients, r2 = curvefit(x, y, f)
        # coeffients, r2 = polyfit(x, y, 2)
        print(coeffients, "|" + key, r2)

        x_fit, y_fit = func_to_points(f, range(1949, 2051), *coeffients)

        plt.plot(x_fit, y_fit, color='#1f3e78', linestyle='-')

        title = metric + " " + month
        eq = coeffients_to_eq(*coeffients)

        plt.suptitle(f"{title}\n{eq}\n{r2}", fontname='Times')
        plt.ylabel(metric, fontname='Times')
        plt.xlabel('Time (Year)', fontname='Times')

        plt.savefig(f'{out_dir}{metric}_{month}.png', dpi=576)
        plt.cla()

        for year in range(1949, 2051):
            index = str(year) + "-" + month
            prediction = max(0,f(year, *coeffients))
            out_dict[index].append(prediction)

with open(out_path, "w+") as out_file:
    dump(out_dict, out_file, sort_keys=True, indent=4)




from keras.utils import plot_model
from keras.models import load_model
import matplotlib.pyplot as plt
from json import load, dump
import numpy as np


training_data_path = "/Users/forrestbicker/Documents/Code/Python/WorkInProgress/MTF/data/AI/OUT/MASTER.json"
model_path = "/Users/forrestbicker/Documents/Code/Python/WorkInProgress/MTF/data/AI/NNData/model.hdf5"
in_path = "/Users/forrestbicker/Documents/Code/Python/WorkInProgress/MTF/data/NOAA/OUT/month-Specific-Predictions.json"
out_path = "/Users/forrestbicker/Documents/Code/Python/WorkInProgress/MTF/data/AI/PREDICTIONS/output.json"
csv_path = "/Users/forrestbicker/Documents/Code/Python/WorkInProgress/MTF/data/NOAA/OUT/month-Specific-Predictions.csv"
out_dict = {}


def normalize(arr, min, ptp):
    arr = (arr - min) / ptp
    return arr

with open(training_data_path, "r") as training_data_file:
    training_data_dict = load(training_data_file)

temp = []
pcpt = []

for dataID in training_data_dict:
    temp += training_data_dict[dataID][0][0:3]
    pcpt += [training_data_dict[dataID][0][3]]

temp = np.array(temp)
pcpt = np.array(pcpt)


model = load_model(model_path)

with open(in_path, "r") as in_file:
    in_dict = load(in_file)

in_data = []

for index in in_dict:
    in_data.append(in_dict[index])

in_data = np.array(in_data)

in_data = in_data.T
in_data[0:3] = normalize(in_data[0:3], np.min(temp), np.ptp(temp))
in_data[3] = normalize(in_data[3], np.min(pcpt), np.ptp(pcpt))
in_data = in_data.T

print(in_data.shape)
out_data = model.predict_proba(in_data)

print(out_data)

for i, index in enumerate(in_dict):
    independent_variables = in_dict[index]
    out_dict[index] = [independent_variables, list(out_data[i].astype('float'))]

with open(out_path, "w+") as out_file:
    dump(out_dict, out_file, indent=4)

with open(csv_path, "w+") as csv_path:
    for index in out_dict:
        line = []
        year, month = index.split("-")
        line.append(year)
        line.append(month)
        for i, metric in enumerate(["tMax", "tAvg", "tMin", "pcp"]):
            #     line += np.average(in_dict[metric][month][year])
            line.append(str(out_dict[index][0][i]))
        line.append(str(out_dict[index][1][0]))
        csv_path.write(",".join(line) + "\n")

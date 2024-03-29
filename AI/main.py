from keras.layers import Dense
from keras.layers.core import Dropout
from keras.models import Sequential
from keras.losses import categorical_crossentropy, mean_squared_error
import keras
import numpy as np
from pprint import pprint
from sklearn.preprocessing import normalize
from hyperopt import Trials, STATUS_OK, tpe
from hyperas import optim
from hyperas.distributions import choice, uniform
from json import load, dump
from keras.activations import hard_sigmoid, linear, relu, sigmoid
from keras.optimizers import Adam
import matplotlib.pyplot as plt


def getData():
    def normalize(arr):
        arr = (arr - np.min(arr)) / np.ptp(arr)
        return arr

    def normalizeMASTER(arr):
        arr = arr.T
        arr[0:3] = normalize(arr[0:3])
        arr[3] = normalize(arr[3])
        return arr.T

    in_path = "AI\DATA\MASTER.json"

    with open(in_path, "r") as in_file:
        in_dict = load(in_file)

    x = []
    y = []

    for dataID in in_dict:
        x.append(in_dict[dataID][0])
        y.append(in_dict[dataID][1])

    x = np.array(x).astype('float32')
    y = np.array(y).astype('float32').T[0].T

    x = normalizeMASTER(x)


    x_train = x[0:-1000]
    y_train = y[0:-1000]
    x_val = x[-1000:]
    y_val = y[-1000:]

    return((x_train, y_train, x_val, y_val))

def getModel(x_train, y_train, x_val, y_val):

    # x_train = np.array([[0, 0], [0, 1], [1, 0], [1, 1]], "float32")
    # y_train = np.array([[0.5], [0.5], [0.5], [0.5]], "float32")

    x_dim = len(x_train[0])
    # y_dim = len(y_train[0])
    y_dim = 1
    #       ()      ()
    #       ()      ()
    # ()    ()      ()
    # ()    ()      ()      ()
    # ()    ()      ()      ()
    # ()    ()      ()
    #       ()      ()
    #       ()      ()
    # r     r       s       s
    model = Sequential()

    model.add(Dense(16, input_dim=x_dim, activation=linear))
    model.add(Dense(8, activation=relu))
    model.add(Dropout(0.05))
    model.add(Dense(8, activation=sigmoid))
    # model.add(Dropout(0.2))
    # model.add(Dense(8, activation='sigmoid'))
    model.add(Dense(y_dim, activation=hard_sigmoid))

    model.compile(
        loss=mean_squared_error,
        optimizer=Adam(10**-3),
        metrics=["accuracy"]
    )

    history = model.fit(
        x_train,
        y_train,
        epochs=15,
        verbose=2,
        validation_data=(x_val, y_val)
    )

    with open("history.json", "w+") as out_file:
        out_dict = history.history
        for metric in out_dict:
            contents = out_dict[metric]
            contents = np.array(contents).astype('float')
            out_dict[metric] = list(contents)  # converts to JSON serializable list
        dump(out_dict, out_file)

    return(model)

# print(getData()[-2])

modle = getModel(*getData())
out = modle.predict_proba(getData()[-2]) # test on validation data

modle.save("m.hdf5")

print(out)
np.savetxt("foo.csv", out, delimiter=",")

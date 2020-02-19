from keras.layers import Dense
from keras.layers.core import Dropout
from keras.models import Sequential
from keras.losses import categorical_crossentropy
import keras
import numpy as np
from pprint import pprint
from sklearn.preprocessing import normalize
from hyperopt import Trials, STATUS_OK, tpe
from hyperas import optim
from hyperas.distributions import choice, uniform
from json import load
from keras.activations import hard_sigmoid, relu, sigmoid


def getData():
    def normalizeByCol(arr):
        arr = arr.T
        for i, col in enumerate(arr):
            arr[i] = (col - np.min(col)) / np.ptp(col)

        return arr.T
    in_path = "/Users/forrestbicker/Documents/Code/Python/WorkInProgress/MTF/data/AI/OUT/MASTER.json"

    with open(in_path, "r") as in_file:
        in_dict = load(in_file)

    x = []
    y = []

    for dataID in in_dict:
        x.append(in_dict[dataID][0])
        y.append(in_dict[dataID][1])

    x = np.array(x).astype('float32')
    y = np.array(y).astype('float32')

    x = normalizeByCol(x)
    y = normalizeByCol(y)

    x_train = x[0:-1000]
    y_train = y[0:-1000]
    x_val = x[-1000:]
    y_val = y[-1000:]

    return((x_train, y_train, x_val, y_val))

def model(x_train, y_train, x_val, y_val): 

    # x_train = np.array([[0, 0], [0, 1], [1, 0], [1, 1]], "float32")
    # y_train = np.array([[0.5], [0.5], [0.5], [0.5]], "float32")

    x_dim = len(x_train[0])
    y_dim = len(y_train[0])
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

    model.add(Dense(8, input_dim=x_dim, activation=relu))
    model.add(Dense(16, activation=relu))
    model.add(Dropout({{uniform(0, 1)}}))
    model.add(Dense(16, activation=sigmoid))
    # model.add(Dropout(0.2))
    # model.add(Dense(8, activation='sigmoid'))
    model.add(Dense(y_dim, activation=hard_sigmoid))

    adam = keras.optimizers.Adam(lr={{choice([10**-3, 10**-2, 10**-1])}})
    rmsprop = keras.optimizers.RMSprop(lr={{choice([10**-3, 10**-2, 10**-1])}})
    sgd = keras.optimizers.SGD(lr={{choice([10**-3, 10**-2, 10**-1])}})

    optim_choice = {{choice(['adam', 'sgd', 'rmsprop'])}}
    if optim_choice == 'adam':
        optim = adam
    elif optim_choice == 'rmsprop':
        optim = rmsprop
    else:
        optim = sgd

    model.compile(
        loss='mean_squared_error',
        optimizer=optim,
    )

    model.fit(
        x_train,
        y_train,
        epochs=10,
        verbose=2,
        validation_data=(x_val, y_val)
    )

    loss = model.evaluate(x_val, y_val, verbose=0)
    print('Test accuracy: ', loss)
    return({'loss': loss, 'status': STATUS_OK, 'model': model})

# model(*getData())

# out = model.predict_proba(x_train)

best_run, best_model = optim.minimize(model=model,
                                      data=getData,
                                      algo=tpe.suggest,
                                      max_evals=30,
                                      trials=Trials())

print(best_model)

with open("foo.json", "w+") as outfile:
    dump(best_model, outfile)

# np.savetxt("foo.csv", out, delimiter=",")

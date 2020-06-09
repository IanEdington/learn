import random
import numpy as np
from sklearn.model_selection import train_test_split

def makeTerrainData(n_points=1000):
    # source: https://github.com/udacity/ud120-projects/blob/d4a496143f270f1027ccf789d4764ddb59d90a28/choose_your_own/prep_terrain_data.py
    # make the toy data set
    random.seed(42)
    grade = [random.random() for _ in range(0, n_points)]
    bumpy = [random.random() for _ in range(0, n_points)]
    error = [random.random() for _ in range(0, n_points)]
    y = [round(grade[ii]*bumpy[ii]+0.3+0.1*error[ii]) for ii in range(0, n_points)]
    for ii in range(0, len(y)):
        if grade[ii] > 0.8 or bumpy[ii] > 0.8:
            y[ii] = 1.0

    # split into train/test sets
    x = [[gg, ss] for gg, ss in zip(grade, bumpy)]
    split: int = int(0.75*n_points)
    x_train = np.array(x[0:split])
    x_test = np.array(x[split:])
    y_train = np.array(y[0:split])
    y_test = np.array(y[split:])

    # return training_data, test_data
    return x_train, y_train, x_test, y_test

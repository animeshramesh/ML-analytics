from __future__ import division
import numpy as np


def get_y(slope, intercept, x):
    return x * slope + intercept


def get_error(test_data, computed_data):
    errors = []
    for a, b in zip(test_data, computed_data):
        diff = abs(a-b)
        error = diff/a
        errors.append(error)
    return sum(errors)/len(errors)


def normalize(x):
    x = np.array(x)
    cols = x.shape[1]
    rows = x.shape[0]

    for j in range(cols):
        column = x[:, j:j+1]
        for i in range(rows):
            min_a = get_min(column)
            max_a = get_max(column)
            den = max_a - min_a
            a = x[i][j]
            var = x[i][j] - min_a
            n = var/den
            x[i][j] = n
    return x


def normalize_matrix(matrix):
    least = matrix[0][0]
    greatest = matrix[0][0]
    matrix = np.array(matrix)
    rows = matrix.shape[0]
    cols = matrix.shape[1]
    for i in range(rows):
        for j in range(cols):
            if matrix[i][j] > greatest:
                greatest = matrix[i][j]
            elif matrix[i][j] < least and matrix[i][j] != 0:
                least = matrix[i][j]
    # print least, greatest
    for i in range(rows):
        for j in range(cols):
            matrix[i][j] = ((matrix[i][j]-least)/(greatest - least))

    return matrix

def get_min(x):
    f = x[0]
    for i in x:
        if i < f:
            f = i
    return f


def get_max(x):
    f = 0.0
    for i in x:
        if i > f:
            f = i
    return f
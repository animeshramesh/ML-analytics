from __future__ import division


def get_y(slope, intercept, x):
    return x * slope + intercept


def get_error(test_data, computed_data):
    errors = []
    for a, b in zip(test_data, computed_data):
        diff = abs(a-b)
        error = diff/a
        errors.append(error)
    return sum(errors)/len(errors)
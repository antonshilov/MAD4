from math import sqrt
from random import random

model_types = {0: "a1+a2*(u1-u_)"}


class Sample:
    input_values = [[]]
    true_values = []
    object_values = []


def calc(interval, iterations_amount, hidrance_disp, function, var_num):
    sample = generate_sample(interval, iterations_amount, hidrance_disp, function, var_num)
    model = build_model(sample, 0)
    return model


def generate_sample(interval, iterations_amount, hidrance_disp, function, var_num):
    step = interval / iterations_amount
    sample = Sample()
    param_value = 0
    input_values = []
    for i in range(iterations_amount):
        input_values.append([])
        params = []
        for j in range(var_num):
            input_values[i].append(param_value)
            params.append(param_value)
        sample.true_values.append(calc_function(input_values[i], function))
        sample.object_values.append(sample.true_values[i] + interference(hidrance_disp))
        param_value += step
    sample.input_values = input_values
    return sample


def build_model(sample, model_type):
    if model_type == 0:
        a1 = sum(sample.object_values) / len(sample.object_values)
        u_ = 0
        for val in sample.input_values:
            u_ += val[0]
        u_ /= len(sample.input_values)
        sm = 0
        for i in range(len(sample.input_values)):
            sm += (sample.input_values[i][0] - u_) * sample.object_values[i]
        smq = 0
        for i in range(len(sample.input_values)):
            smq += (sample.input_values[i][0] - u_) ** 2
        a2 = sm / smq
        model = "{0}+{1}*(u - {2})".format(a1, a2, u_)
        return model


def interference(d):
    val = 10
    hid = 0
    for i in range(val):
        hid += random() - 0.5
    hid *= sqrt(d) * sqrt(12 / val)
    return hid


def calc_function(vals, f):
    u1 = u2 = 0
    if len(vals) == 2:
        u1 = vals[0]
        u2 = vals[1]
    else:
        u1 = vals[0]
    return eval(f)


calc(10, 100, 8, '4+6*(u1-1)', 1)

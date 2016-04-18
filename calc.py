from math import sqrt
from random import random

model_types = {0: "a1+a2*(u1-u_)", 1: "a1+a2*u1", 2: "a"}


class Sample:
    input_values = [[]]
    true_values = []
    object_values = []
    disp = []


def calc(interval, iterations_amount, hidrance_disp, function, is_equally_accurate, var_num, model_type):
    sample = generate_sample(interval, iterations_amount, hidrance_disp, function, is_equally_accurate, var_num)
    model = build_model(sample, model_type)
    return {"model": model, "sample": sample}


def generate_disp(val):
    return random() * val


def generate_sample(interval, iterations_amount, hidrance_disp, function, is_equally_accurate, var_num):
    step = interval / iterations_amount
    sample = Sample()
    param_value = 0

    input_values = []
    for i in range(iterations_amount):
        params = []
        for j in range(var_num):
            input_values.append(param_value)
            params.append(param_value)
        sample.true_values.append(calc_function(input_values[i], function))
        if not is_equally_accurate:
            sample.disp.append(generate_disp(hidrance_disp))
        else:
            sample.disp.append(hidrance_disp)
        sample.object_values.append(sample.true_values[i] + interference(sample.disp[i]))
        param_value += step
    sample.input_values = input_values
    return sample


def build_model(sample, model_type):
    if model_type == 0:
        a1 = sum(sample.object_values) / len(sample.object_values)
        u_ = 0
        for val in sample.input_values:
            u_ += val
        u_ /= len(sample.input_values)
        sm = 0
        for i in range(len(sample.input_values)):
            sm += (sample.input_values[i] - u_) * sample.object_values[i]
        smq = 0
        for i in range(len(sample.input_values)):
            smq += (sample.input_values[i] - u_) ** 2
        a2 = sm / smq
        model = "{0}+{1}*(u1 - {2})".format(a1, a2, u_)
        return model
    elif model_type == 1:
        a1 = 0
        x1 = 0
        x2 = 0
        x3 = 0
        x4 = 0
        for i in range(len(sample.input_values)):
            for j in range(len(sample.input_values)):
                disp_i = sample.disp[i]
                disp_j = sample.disp[j]
                x1 += (sample.object_values[i] * sample.input_values[i] * sample.object_values[j]) / (
                    disp_i * disp_j)
                x2 += (sample.object_values[i] * sample.input_values[j] * sample.object_values[j]) / (
                    disp_i * disp_j)
                x3 += (sample.input_values[i] * sample.object_values[j]) / (disp_i * disp_j)
                x4 += (sample.input_values[i] * sample.object_values[i]) / (disp_i * disp_j)
        a1 = (x1 - x2) / (x3 - x4)
        x1 = 0
        x2 = 0
        x3 = 0
        for i in range(len(sample.input_values)):
            disp_i = sample.disp[i]
            x1 += sample.object_values[i] / disp_i
            x2 += 1 / disp_i
            x3 += sample.input_values[i] / disp_i
        a2 = (x1 - x2) / x3
        model = "{0}+{1}*u1".format(a1, a2)
        return model
    elif model_type == 2:
        x1 = 0
        x2 = 0
        for i in range(len(sample.input_values)):
            disp_i = sample.disp[i]
            x1 += sample.object_values[i] / disp_i
            x2 += 1 / disp_i
        a1 = x1 / x2
        model = "{0}".format(a1)
        return model


def interference(d):
    val = 10
    hid = 0
    for i in range(val):
        hid += random() - 0.5
    hid *= sqrt(d) * sqrt(12 / val)
    return hid


def calc_function(val, f):
    u1 = val
    return eval(f)

# calc(10, 100, 10, '4', False, 1, 2)

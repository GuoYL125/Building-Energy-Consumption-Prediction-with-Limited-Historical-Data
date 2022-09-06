import pandas as pd
import numpy as np
import json
import os

filePath = 'result_horizon_1_7'
fileList = os.listdir(filePath)

qw = 0
result_data = np.zeros((127, 7))

for file in fileList:
    path = os.path.join(filePath, file)

    # data_path = 'result_horizon_1_7/result1.csv'
    data_r = pd.read_csv(path, header=None, sep=',', low_memory=False)
    data = data_r.values  # 'dataframe' converted to 'matrix'

    with open('item.json', 'r') as f:
        item = json.load(f)
    item_dict = {}

    for i in item.keys():
        item_dict[int(i)] = item[i]
    f = {}

    a = np.array(data)
    for i in item_dict.keys():
        a = np.insert(a, i, [0], axis=0)
    a = np.maximum(a, 0)

    for i in item_dict.keys():
        f[i] = False
    item_dict.keys()


    def get_value(data, i):
        res = 0
        for x in item_dict[i]:
            if x == i:
                res = 0
            elif x not in item_dict.keys() or f[x]:
                res += data[x]
            else:
                res += get_value(data, x)
        data[i] = res
        f[i] = True
        return res


    f[1] = False
    if 0 not in [0, 2] or f[1]:
        res = 1
    else:
        res = 2

    for i in item_dict.keys():
        get_value(a, i)

    ###############################################
    with open('f_s_raw.json', 'r') as r:
        item_r = json.load(r)
    item_dict_r = {}

    for i in item_r.keys():
        item_dict_r[int(i)] = item_r[i]
    f = {}

    b = np.array(a)
    for i in item_dict_r.keys():
        b = np.insert(b, i, [0], axis=0)


    def get_value_final(data, i):
        res = 0
        for x in item_dict_r[i]:
            if x == i:
                res = 0
            elif x not in item_dict_r.keys() or f[x]:
                res += data[x]
            else:
                res += get_value(data, x)
        data[i] = res
        f[i] = True
        return res

    for i in item_dict_r.keys():
        get_value_final(b, i)

    b[22] = 21
    b[34] = 225
    b[50] = 21

    result_data[:, qw] = b[:, 0]
    qw += 1

dir_name = "../result switch code/result_switch"

if not os.path.isdir(dir_name):
    os.makedirs(dir_name)

np.savetxt("../result switch code/result_switch/result_value.csv", result_data, delimiter=",")

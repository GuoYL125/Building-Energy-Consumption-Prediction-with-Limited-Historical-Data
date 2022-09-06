import pandas as pd
import numpy as np
import json
import os

qw = 0
result_data = np.zeros((260, 625))

data_r = pd.read_csv('../dataset/all_meter_data.csv', header=None, sep=',', low_memory=False)
data = data_r.values  # 'dataframe' converted to 'matrix'
data = data.T
b = np.zeros(data.shape[0])

with open('624_78.json', 'r') as f:
    item = json.load(f)
item_dict = {}

for i in item.keys():
    item_dict[int(i)] = item[i]
f = {}


for lie in range(data.shape[1]):

    a = np.array(data[:, lie])

    def get_value(data, i):
        res = 0
        for x in item_dict[i]:
            res += data[x]
        b[i] = res
        return res

    for i in item_dict.keys():
        get_value(a, i)
        result_data[qw, :] = b

    qw += 1

dir_name = "../result switch code/result_switch"

if not os.path.isdir(dir_name):
    os.makedirs(dir_name)

np.savetxt("../result switch code/result_switch/data_new_5.11.csv", result_data, delimiter=",")

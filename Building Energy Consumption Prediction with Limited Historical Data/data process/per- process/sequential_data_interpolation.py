import numpy as np
import timesynth as ts
import pandas as pd
from scipy import interpolate
from scipy.interpolate import interp1d
import matplotlib.pyplot as plt

from pandas import read_csv
from pandas import datetime

data_path = 'ori_data_new_5.11.csv'

clterr_series = pd.read_csv(data_path, sep=',',low_memory=False)
clterr = clterr_series.values    # 'dataframe' converted to 'matrix'
x = [i for i in range(clterr.shape[0])]

a = clterr.shape[0]*7
b = clterr.shape[1]

clterr_inter = np.zeros((a, b))    # All interpolation output formats

# Interpolate
for i in range(clterr.shape[1]):
    if i==0:
        first_column = [i for i in range(a)]
        clterr_inter[:, i] = first_column
    else:
        samples = clterr[:, i]
        x_test = np.linspace(0, samples.size-1, a)
        fit_akima = interpolate.Akima1DInterpolator(x, samples)    # Akima interpolate
        y_test = fit_akima(x_test)                                 # Akima interpolate
        for c in range(clterr.shape[1]):
            clterr_inter[:, i] = y_test
np.savetxt("new_need_data_Akima-7.csv", clterr_inter, delimiter=",")
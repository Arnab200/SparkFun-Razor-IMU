from __future__ import division
import numpy as np
import csv
import pandas as pd


file = pd.read_csv("F:/IMU_data_log_dummy.csv")
accel_z = file.az
accel_z = float(accel_z)
accel_z = round(accel_z,3)


def ExpMovingAverage(values, window):
    weights = np.exp(np.linspace(-1., 0., window))
    weights /= weights.sum()
    a = np.convolve(values, weights, mode='full') [:len(values)]
    a[:window] = a[window]
    return a


for i in range(1, len(accel_z),6):
    try:
        dataset = [accel_z[i],accel_z[i+1],accel_z[i+2],accel_z[i+3],accel_z[i+4],accel_z[i+5]]
        print(dataset)
    except:
        pass



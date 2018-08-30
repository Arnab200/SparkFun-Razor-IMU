from __future__ import division
import numpy as py
from scipy import signal


def butter_highpass(cutoff, fs, order):
    nyq = 0.5 * fs
    normal_cutoff = cutoff / nyq
    b, a = signal.butter(order, normal_cutoff, btype='high', analog=False)
    return b, a


def butter_highpass_filter(data, cutoff, fs, order=1):
    b, a = butter_highpass(cutoff, fs, order=order)
    y = signal.filtfilt(b, a, data)
    return y


def butter_lowpass(cutoff, fs, order):
    nyq = 0.5 * fs
    normal_cutoff = cutoff / nyq
    b, a = signal.butter(order, normal_cutoff, btype='low', analog=False)
    return b, a

def butter_lowpass_filter(data, cutoff, fs, order=1):
    b, a = butter_lowpass(cutoff, fs, order=order)
    x = signal.filtfilt(b, a, data)
    return x

def calculation():
    data = 9.6
    hp_filtered_data = butter_highpass_filter(data, 0.5, 1/256, 1)                                #replace with actual values
    """
    hp_filtered_data = abs(hp_filtered_data)                                               #sample period is 1/256
    lp_filtered_data = butter_lowpass_filter(hp_filtered_data, cutoff, fs)              # replace with actual values
    
    if lp_filtered_data < 0.05:
        stationary = lp_filtered_data
        print("Values are stationary, no movement")
"""
    #take the values from gyro
    print(hp_filtered_data)


calculation()


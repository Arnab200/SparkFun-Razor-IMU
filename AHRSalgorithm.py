from __future__ import division
import datetime
import string

"""
class ahrs():
    samplePeriod = 0
    Quaternion = [1,0,0,0]
    Kp = 0
    Ki = 0
    KpInit = 0
    InitPeriod = 0

    def __init__(self):
        self.samplePeriod = 1/256
        self.Quaternion = [1, 0, 0, 0]
        self.Kp = 2
        self.Ki = 0
        self.KpInit = 200
        self.InitPeriod = 5
"""
x = str(datetime.datetime.now())
x = string.split(x,":")
print(int(x[1]) * 60 + float(x[2]))



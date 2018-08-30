########################################################import statements###############################################
from __future__ import division                                                                                        #
import serial                                                                                                          #
import itertools                                                                                                       #
import time                                                                                                            #
import timeit                                                                                                          #
import os                                                                                                              #
import string                                                                                                          #
import matplotlib.pyplot as plt                                                                                        #
import scipy
import math
from matplotlib import animation                                                                                       #
###################################################end of import statement##############################################
accel_factor = 9.806 / 256.0
imu_yaw_calibration = 0.0


ser = serial.Serial(port="COM8",baudrate=57600,bytesize=serial.EIGHTBITS,parity=serial.PARITY_NONE,stopbits=serial.STOPBITS_ONE, timeout=1)



def accel_offset(accel_sp_min, accel_sp_max):
    return (accel_sp_min + accel_sp_max ) / 2.0


def yprmain():
    while True:
        line = ser.readline()
        line = line.replace("!ANG:", "")
        line = line.replace("#YPR=","")
        words = string.split(line,",")
        if len(words) > 2:
            try:
                yaw = -float(words[0])
                yaw = yaw + imu_yaw_calibration
                if yaw > 180.0:
                    yaw = yaw - 360.0
                if yaw < -180.0:
                    yaw = yaw + 360.0
                pitch = -float(words[1])
                roll = float(words[2])
                print("roll = {0}, pitch = {1}, yaw = {2}".format(roll,pitch,yaw))

            except:
                pass


def accelmain():

    while True:
        millis1 = int(round(time.time() * 1000))
        ser.write('#oc')
        line = ser.readline()
        line = line.replace("accel x,y,z (min/max) = ","")
        parseline = string.split(line,"  ")
        try:
            accelx = parseline[0]
            accely = parseline[1]
            accelz = parseline[2]
            accelz = accelz.replace("\r\n","")

            accel_x = string.split(accelx, "/")
            accel_y = string.split(accely, "/")
            accel_z = string.split(accelz, "/")

            accel_x_min = float(accel_x[0])
            accel_x_max = float(accel_x[1])

            accel_y_min = float(accel_y[0])
            accel_y_max = float(accel_y[1])

            accel_z_min = float(accel_z[0])
            accel_z_max = float(accel_z[1])

            x = round((accel_offset(accel_x_min,accel_x_max) * accel_factor),3)
            y = round((accel_offset(accel_y_min, accel_y_max) * accel_factor),3)
            z = round((accel_offset(accel_z_min, accel_z_max) * accel_factor),3)
            millis2 = int(round(time.time() * 1000))

            print("ax = {0}    ay = {1}    az = {2}".format(x,y,z))
            #mag_accel = math.sqrt((pow(x,2) + pow(y,2) + pow(z,2)))
            #print(round(mag_accel, 3))


        except:
            pass


        ser.write('#on')
        line1 = ser.readline()
        print(line1)


if __name__ == '__main__':
    accelmain()
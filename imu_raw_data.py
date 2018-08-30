#############################################################import###############################################################
from __future__ import division                                                                                                  #
import csv                                                                                                                       #
import os                                                                                                                        #
import serial                                                                                                                    #
import string                                                                                                                    #
import time                                                                                                                      #
########################################################end of import#############################################################


########################################################global Variables#######################################################################
ser = serial.Serial(port="COM8",baudrate=57600,bytesize=serial.EIGHTBITS,parity=serial.PARITY_NONE,stopbits=serial.STOPBITS_ONE, timeout=1)   #                                                                                                      #                      #
fieldnames = ['Packet Number','ax','ay','az','gx','gy','gz']                                                                                  #
accel_factor = 9.806 / 256.0                                                                                                                  #
imu_yaw_calibration = 0.0                                                                                                                     #
gyro_average_offset_x = -42.05
gyro_average_offset_y = 96.20
gyro_average_offset_z = -18.36
gyro_gain = 0.06957                     #same for all axes                                                                                    #
###############################################################################################################################################



def accel_offset(accel_sp_min, accel_sp_max):
    return (accel_sp_min + accel_sp_max ) / 2.0

def magn_offset(magn_sp_min, magn_sp_max):
    return (magn_sp_min + magn_sp_max ) / 2.0

def to_rad(x):
    return x * 0.01745329252


def sensor_raw():
    i = -1
    with open('E:\IMU_data_log_falsetest.csv', 'wb') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()

        while True:
            
            ser.write('#oc')
            #time.sleep(0.02)                 #ideal reading 0.02
            line = ser.readline()
            ser.write('#on')
            line1 = ser.readline()
            
            
            try:
                if line1.startswith(('accel x,y,z (min/max)', 'magn x,y,z (min/max)', 'gyro x,y,z (current/average)')):
                    if line1.startswith('accel x,y,z (min/max)'):

                        line2 = line1.replace("accel x,y,z (min/max) = ", "")
                        parseline1 = string.split(line2, "  ")
                        accelx = parseline1[0]
                        accely = parseline1[1]
                        accelz = parseline1[2]
                        accelz = accelz.replace("\r\n", "")

                        accel_x = string.split(accelx, "/")
                        accel_y = string.split(accely, "/")
                        accel_z = string.split(accelz, "/")

                        accel_x_min = float(accel_x[0])
                        accel_x_max = float(accel_x[1])

                        accel_y_min = float(accel_y[0])
                        accel_y_max = float(accel_y[1])

                        accel_z_min = float(accel_z[0])
                        accel_z_max = float(accel_z[1])

                        x = round((accel_offset(accel_x_min, accel_x_max) * accel_factor), 3)
                        y = round((accel_offset(accel_y_min, accel_y_max) * accel_factor), 3)
                        z = round((accel_offset(accel_z_min, accel_z_max) * accel_factor), 3)

                        print "{0}, {1}, {2}".format(x, y, z),
                        

                    elif line1.startswith('magn x,y,z (min/max)'):
                        pass
                        """
                        line4 = line1.replace("magn x,y,z (min/max) = ","")
                        parseline2 = string.split(line4,"  ")
                        magnx = parseline2[0]
                        magny = parseline2[1]
                        magnz = parseline2[2]
                        magnz = magnz.replace("\r\n","")

                        magn_x = string.split(magnx,"/")
                        magn_y = string.split(magny, "/")
                        magn_z = string.split(magnz, "/")

                        magn_x_min = float(magn_x[0])
                        magn_x_max = float(magn_x[1])

                        magn_y_min = float(magn_y[0])
                        magn_y_max = float(magn_y[1])

                        magn_z_min = float(magn_z[0])
                        magn_z_max = float(magn_z[1])

                        magn_x_scld = (100 / (magn_x_max - magn_offset(magn_x_min, magn_x_max)))
                        magn_y_scld = (100 / (magn_y_max - magn_offset(magn_y_min, magn_y_max)))
                        magn_z_scld = (100 / (magn_z_max - magn_offset(magn_z_min, magn_z_max)))

                        act_magn_x = magn_x_scld * magn_offset(magn_x_min, magn_x_max)
                        act_magn_y = magn_y_scld * magn_offset(magn_y_min, magn_y_max)
                        act_magn_z = magn_z_scld * magn_offset(magn_z_min, magn_z_max)
                        print"{0}, {1}, {2}".format(round(act_magn_x, 2), round(act_magn_y, 2),round(act_magn_z, 2)) ,
                        """

                    elif line1.startswith('gyro x,y,z (current/average)'):

                        line3 = line1.replace("gyro x,y,z (current/average) = ","")
                        parseline3 = string.split(line3,"  ")
                        try:
                            gyrox = parseline3[0]
                            gyroy = parseline3[1]
                            gyroz = parseline3[2]
                            gyroz = gyroz.replace("\r\n","")

                            gyro_x = string.split(gyrox,"/")
                            gyro_y = string.split(gyroy,"/")
                            gyro_z = string.split(gyroz,"/")

                            gyro_x_avg = float(gyro_x[1])
                            gyro_y_avg = float(gyro_y[1])
                            gyro_z_avg = float(gyro_z[1])

                            scld_gyro_x = gyro_x_avg
                            scld_gyro_y = gyro_y_avg
                            scld_gyro_z = gyro_z_avg
                            print "{0}, {1}, {2}\n".format(scld_gyro_x,scld_gyro_y,scld_gyro_z)
                            i = i + 1
                            writer.writerow({'Packet Number':str(i),'ax':str(x),'ay':str(y),'az':str(z),'gx':str(scld_gyro_x),'gy':str(scld_gyro_y),'gz':str(scld_gyro_z)})


                        except:
                            pass


            except:
                pass


if __name__ == "__main__":
    sensor_raw()

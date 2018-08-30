from __future__ import division
import string
import csv


file = open("E:\imu_data_unparsed_square.txt","r")
fieldnames = ['Packet Number','ax','ay','az','gx','gy','gz'] 
accel_factor = 9.806 / 256.0
gyro_gain = 0.06957    
gyro_average_offset_x = float(-47.74)
gyro_average_offset_y = float(40.87)
gyro_average_offset_z = float(-9.05)



def accel_offset(accel_sp_min, accel_sp_max):
    return (accel_sp_min + accel_sp_max ) / 2.0

def magn_offset(magn_sp_min, magn_sp_max):
    return (magn_sp_min + magn_sp_max ) / 2.0

def to_rad(x):
    return x * 0.01745329252


def main():
    i = 0
    with open('F:\IMU_data_log_square.csv', 'wb') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()

        while True:
            line = file.readline()
            try:
                if line.startswith(('accel x,y,z (min/max)', 'magn x,y,z (min/max)', 'gyro x,y,z (current/average)')):
                    if line.startswith('accel x,y,z (min/max)'):
                        line1 = line.replace("accel x,y,z (min/max) = ", "")
                        parseline = string.split(line1, "  ")
                        accelx = parseline[0]
                        accely = parseline[1]
                        accelz = parseline[2]
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

                        print "{0}, {1}, {2}".format(x, y, z)

                    elif line1.startswith('magn x,y,z (min/max)'):
                        pass   

                    elif line.startswith('gyro x,y,z (current/average)'):
                        line2 = line.replace("gyro x,y,z (current/average) = ","")
                        parseline2 = string.split(line2,"  ")
                        try:
                            gyrox = parseline2[0]
                            gyroy = parseline2[1]
                            gyroz = parseline2[2]
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
               
                
            

if __name__ == '__main__':
    main()
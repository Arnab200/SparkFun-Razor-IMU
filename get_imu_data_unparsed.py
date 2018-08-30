import serial



ser = serial.Serial(port="COM8",baudrate=57600,bytesize=serial.EIGHTBITS,parity=serial.PARITY_NONE,stopbits=serial.STOPBITS_ONE, timeout=1)
file = open("E:\imu_data_unparsed_square.txt","wb")

def main():
    while True:
        ser.write('#oc')
        ser.write('#on')
        line = ser.readline()
        try:
            if line.startswith(('accel x,y,z (min/max)', 'magn x,y,z (min/max)', 'gyro x,y,z (current/average)')):
                file.write(str(line)+"\n")
                print(line)

        except:
            pass



if __name__ == '__main__':
    main()
# SparkFun Razor IMU
This repository contains code for extracting raw data from SparkFun Razor IMU into the serial monitor of the computer. The Razor IMU file has all the serial codes to get a specific data for example accelerometer, gyroscope and magnetometer. 

File razor_imu.py has the code to get the numerical values of all the 3 sensors into the serial monitor. It parses the serial string of sentences and presents only the numerical value of it and.

File get_imu_data_unparsed.py gets the data from the serial monitor and writes it into a txt file for later computation.

File parse_imu_data.py takes the imu data from the txt file and drops the unnecessary string part and puts only the actual sensor data in a CSV file for building data sets.

File exponential_imu_data.py takes the parsed data and applies exponential moving average to smooth out the output of gyroscope.

All the programs that are uploaded are purely for educational and research purposes and do not mean to to violate any copyright if any.

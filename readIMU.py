import re
import scipy.io
import numpy as np

# Read the data from the file
filepath  = "C:\\Users\\ezxtz6\\Downloads\\CoolTermWin\\static_drift.txt"
with open(filepath, 'r') as file:
    datas = file.readlines()
# Accel: -856.00,-350.00,8592.00; Gyro:122.00,29.00,-31.00; Compass:-114.00,99.00,82.00; 
# Split the data into individual readings
# # Initialize lists to store the parsed values

parsed_data = []

for (i, data) in enumerate(datas):
    data_list = []
    readings = data.split(';')
    data_list.append(i)
    # Parse each reading and extract the values
    for reading in readings:
        # Extract the values using regular expressions
        values = re.findall(r'[-+]?\d*\.\d+|\d+', reading)
    
        # Convert the values to floats
        values = [float(value) for value in values]
    
        # Append the values to the respective lists
        [data_list.append(value) for value in values]

    parsed_data.append(data_list)

mat_data = np.array(parsed_data)
# Save the parsed data to a MATLAB file
scipy.io.savemat('drift.mat', {'drift': mat_data})